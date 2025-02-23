from flask import Flask, jsonify, render_template
from flaskwebgui import FlaskUI
from db_handler import DatabaseHandler
import os



# Constant
_DATA_DIR: str = os.path.join(os.path.dirname(__file__), 'data')
_SQLITE_PATH: str = _DATA_DIR + "/appchron.sqlite3"
_APP: Flask = Flask(__name__)



@_APP.route("/")
def index():
    return render_template("index.html")



# Route für Datenabfrage (wird via AJAX aufgerufen)
@_APP.route('/refresh-data')
def refresh_data():
    handler : DatabaseHandler = DatabaseHandler(_SQLITE_PATH)
    handler.connect()
    query_result = handler.runQuery('Select * FROM PROCESS')
    handler.disconnect()
    
    # Daten in JSON-Format für D3.js konvertieren
    return jsonify([{'id': row[1], 'name': row[0]} for row in query_result])



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Main-Process >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #


def runGUI() -> None:

    # Starts the UI
    FlaskUI(
        app=_APP, port=80, fullscreen=False, width=800, height=600, server="flask"
    ).run()

if __name__ == "__main__":
    runGUI()