from flask import Flask , render_template

app = Flask(__name__)

#Global Variables. 
Notes = {"Hi", "MyName is ","<h1>Jaibeer</h1>"}

@app.route("/") #This is default rout 
def index():
    note = "Why?"
    return render_template('index.html', Notes=Notes)

@app.route("/<string:name>")
def hello(name):
    name.capitalize()
    return f"Hello, {name}"