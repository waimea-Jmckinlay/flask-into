from flask import Flask
from flask import render_template
from random import randint
#create the app 
app = Flask(__name__)



@app.get("/")
def home():
    return render_template('pages/home.jinja')

@app.get("/random/")
def random():
    randNum = randint(1,9999)
    return render_template('pages/random.jinja', number=randNum)


@app.get("/about/")
def about():
    return render_template('pages/about.jinja')
