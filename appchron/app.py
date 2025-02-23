from flask import Flask, render_template
from flaskwebgui import FlaskUI

from watcher import WatcherThread


app: Flask = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Main-Process >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

if __name__ == "__main__":
    # Initialize the watcher to begin watching and logging the active application.
    watcherthread: WatcherThread = WatcherThread()
    watcherthread.start()

    # Starts the UI
    FlaskUI(
        app=app, port=80, fullscreen=False, width=800, height=600, server="flask"
    ).run()
