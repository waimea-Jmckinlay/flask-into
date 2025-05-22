from flask import Flask
from flask import render_template
from random import randint
from flask import redirect
#create the app 
app = Flask(__name__)



@app.get("/")
def home():
    return render_template('pages/home.jinja')

@app.get("/random/")
def random():
    randNum = randint(1,999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    return render_template('pages/random.jinja', number=randNum)


@app.get("/about/")
def about():
    return render_template('pages/about.jinja')



@app.get("/number/<int:num>")
def analyesNumber(num):
    print(f"you entered : {num}")
    return  render_template('pages/number.jinja', number=num)



@app.get("/form/")
def form():
    return  render_template('pages/form.jinja')


@app.errorhandler(404)
def notfound(e):
     return  render_template('pages/404.jinja')

