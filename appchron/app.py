from flask import Flask, jsonify, render_template
from flaskwebgui import FlaskUI
from db_handler import DatabaseHandler
from pathlib import Path
from calculator import calculate_duration, TimeFormat

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
        data : list[tuple] = get_usage_data()
        
        # Daten in JSON-Format für D3.js konvertieren
        return jsonify([{'id': row[0], 'name': row[1]} for row in data])
    
    except Exception as e:
        app.logger.error(f"Datenbankfehler: {str(e)}")
        return jsonify({'error': 'Datenbankzugriff fehlgeschlagen'}), 500
       
#
#

def get_usage_data() -> list[tuple]:
    # Daten aus SQLite-Datenbank laden
    handler = DatabaseHandler(str(SQL_PATH))
    handler.connect()
    process_names = handler.runQuery('Select id, name FROM PROCESS')
    handler.disconnect()
    
    result : list = []
    for (id, name) in process_names:
        handler.connect()
        process_durations = handler.runQuery(f"""Select "durationSec" FROM "ENTRY" WHERE "mid" = "{id}" """)
        duration_minutes = calculate_duration(process_durations, TimeFormat.Minute)
        handler.disconnect()
        result.append((name, duration_minutes))
    
    print(result)
    return result
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