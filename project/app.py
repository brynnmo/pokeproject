from flask import Flask, render_template

app = Flask(__name__)

#@app.route("/")
#def index():
    #return "<p>Hello, World!</p>"

@app.route('/')
def about():
    return render_template('index.html')