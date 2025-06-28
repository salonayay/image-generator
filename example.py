from flask import Flask, render_template #flask is needed even tho u r not running any html page here, it is needed to keep your app awake and respond to basic requests like "hey are you alive"
from threading import Thread #helps u run two things at the same time - "run the flask server in background while my bot does other stuff"
app = Flask(__name__) #makes a flask app just llike openeing a restaurant
@app.route('/') #this is the home page of our website, it is like the entrance of your restaurant 
def index(): 
     return "example" #this is what it returns when u go to the home page of your website, it is like the receptionist welcoming u to your restaurant 
def run():
     app.run(host='0.0.0.0',port=8080) #this is the port number of your website, it is like the room number of your restaurant
def example():
 t = Thread(target=run) #this is the thread that runs the flask server in background
 t.start() #it is like the manager of your restaurant who is always there to welcome u and show u around - starts running the flask in the bg while your main code keeps going
#this prevents your bot from stopping and freezing due to inactivity especially on platforms like repl.it

