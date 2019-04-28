from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    headLine = "You all got something new"
    return render_template("index.html",headLine=headLine)
