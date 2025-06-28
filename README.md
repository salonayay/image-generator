Custom AI Image Generator
A Flask web app that generates images using OpenAI's DALL·E 3 model based on user-provided text prompts.
---

Features
- Generate AI images from natural language prompts
- Instantly view and copy image URLs
- Powered by OpenAI's DALL·E 3
- User-friendly interface with Bootstrap styling
---

Tech Stack

- Backend: Python, Flask
- Frontend: HTML, Bootstrap 5, JavaScript
- AI API: OpenAI DALL·E 3 via `boltiotai` wrapper
- Hosting: Replit or any Python-supported cloud provider

---

Setup Instructions
1. Clone this repository
git clone https://github.com/salonayay/image-generator.git
cd image-generator

2. Install the dependencies
pip install flask openai

3. Set your OpenAI API key
Create a .env file or set it in your environment:
export OPENAI_API_KEY='your_openai_key_here'

4. Run the app
python main.py

Example Prompts
"A robot painting a sunset on Mars"
"A neon cyberpunk city at night"
"A cat wearing sunglasses and drinking coffee"

Author:Saloni Verma
