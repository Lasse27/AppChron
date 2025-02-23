from flask import Flask, render_template
from flaskwebgui import FlaskUI

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    FlaskUI(
        app=app, port=80, fullscreen=False, width=800, height=600, server="flask"
    ).run()
