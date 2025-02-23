from flask import Flask, render_template
from flaskwebgui import FlaskUI

_APP: Flask = Flask(__name__)


@_APP.route("/")
def index():
    return render_template("index.html")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Main-Process >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #


def runGUI() -> None:

    # Starts the UI
    FlaskUI(
        app=_APP, port=80, fullscreen=False, width=800, height=600, server="flask"
    ).run()
