from flask import Flask, render_template
from flaskwebgui import FlaskUI

from db_handler import DatabaseHandler
from watcher import WatcherThread
import os

# CONST
_DATA_DIR: str = "appchron/data"
_SQLITE_PATH: str = _DATA_DIR + "/appchron.sqlite3"
_APP: Flask = Flask(__name__)


@_APP.route("/")
def index():
    return render_template("index.html")


def createSQLiteFile() -> DatabaseHandler:
    # Create data folder
    try:
        os.makedirs(_DATA_DIR)
    except FileExistsError:
        pass

    # Create DbHandler and database file
    dbHandler: DatabaseHandler = DatabaseHandler(_SQLITE_PATH)
    dbHandler.createTables()
    return dbHandler


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Main-Process >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #


if __name__ == "__main__":

    # Create the sqlite if it doesn't exist
    dbHandler: DatabaseHandler = createSQLiteFile()

    # Initialize the watcher to begin watching and logging the active application.
    watcherthread: WatcherThread = WatcherThread(dbHandler)
    watcherthread.start()

    # Starts the UI
    FlaskUI(
        app=_APP, port=80, fullscreen=False, width=800, height=600, server="flask"
    ).run()
