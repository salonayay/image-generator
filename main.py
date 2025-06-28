from boltiotai import openai
import os
from flask import Flask, render_template_string, request

openai.api_key = os.environ['OPENAI_API_KEY']

def generate_tutorial(components):
    response = openai.Images.create(
        prompt=components,
        model="dall-e-3",
        size="1024x1024",
        response_format="url"
    )
    image_url = response['data'][0]['url']
    return image_url

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''<!DOCTYPE html>
<html>
<head>
    <title>Magic Image Maker</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container">
    <h1 class="my-4">Custom Image Generator</h1>
    <form id="tutorial-form" class="mb-3">
        <div class="mb-3">
            <label for="components" class="form-label">Textual Description of the Image:</label>
            <input type="text" class="form-control" id="components" name="components" placeholder="Ex: A lion in a cage" required>
        </div>
        <button type="submit" class="btn btn-primary">Generate Image</button>
    </form>
    <div class="card mt-3">
        <div class="card-header d-flex justify-content-between align-items-center">
            Output:
            <button class="btn btn-secondary btn-sm" onclick="copyToClipboard()">Copy</button>
        </div>
        <div class="card-body">
            <p id="output" style="white-space: pre-wrap;"></p>
            <img id="myImage" src="" style="width: auto; height: 300px;">
        </div>
    </div>
</div>

<script>
document.getElementById("tutorial-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/generate', {
        method: 'POST',
        body: formData
    });
    const imageUrl = await response.text();
    document.getElementById('myImage').src = imageUrl;
    document.getElementById('output').textContent = imageUrl;
});

function copyToClipboard() {
    const imageUrl = document.getElementById('myImage').src;
    const textarea = document.createElement('textarea');
    textarea.value = imageUrl;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    alert('Copied to clipboard!');
}
</script>
</body>
</html>
''')

@app.route('/generate', methods=['POST'])
def generate():
    components = request.form['components']
    image_url = generate_tutorial(components)
    return image_url, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
