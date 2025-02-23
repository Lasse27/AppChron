from flask import Flask, jsonify, render_template
from flaskwebgui import FlaskUI
from db_handler import DatabaseHandler
from pathlib import Path

#
#

# Constant
BASE_DIR : Path = Path(__file__).parent.resolve()
DATA_DIR : Path = BASE_DIR / 'data'
SQL_PATH : Path = DATA_DIR / 'appchron.sqlite3'

#
#

# Erstellen der Flask-App
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#
#

@app.route("/")
def index():
    """Zeigt die Hauptseite der Anwendung."""
    return render_template("index.html")

#
#

@app.route('/refresh-data')
def refresh_data():
    """
    Liefert Prozessdaten im JSON-Format für D3.js.
    
    Returns:
        JSON-Response mit Prozessdaten oder Fehlermeldung
    """
    try:
        # Daten aus SQLite-Datenbank laden
        handler = DatabaseHandler(str(SQL_PATH))
        handler.connect()
        query_result = handler.runQuery('Select id, name FROM PROCESS')
        handler.disconnect()
        
        # Daten in JSON-Format für D3.js konvertieren
        return jsonify([{'id': row[1], 'name': row[0]} for row in query_result])
    
    except Exception as e:
        app.logger.error(f"Datenbankfehler: {str(e)}")
        return jsonify({'error': 'Datenbankzugriff fehlgeschlagen'}), 500

#
#

def run_gui() -> None:
    """Startet die GUI-Anwendung."""
    FlaskUI(
        app=app, port=80, fullscreen=False, width=800, height=600, server="flask"
    ).run()

#
#

if __name__ == "__main__":
    run_gui()