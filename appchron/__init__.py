import multiprocessing
import os
from argparse import ArgumentParser

import app
from db_handler import DatabaseHandler
from watcher import WatcherThread

_DATA_DIR: str = "appchron/data"
_SQLITE_PATH: str = _DATA_DIR + "/appchron.sqlite3"


def gui():
    app.runGUI()
    pass
    # Code für Modul 1


def recording():
    # Create the sqlite if it doesn't exist
    dbHandler: DatabaseHandler = createSQLiteFile()

    # Initialize the watcher to begin watching and logging the active application.
    watcherthread: WatcherThread = WatcherThread(dbHandler)
    watcherthread.start()


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


if __name__ == '__main__':
    multiprocessing.freeze_support()  # Wichtig für PyInstaller

    parser: ArgumentParser = ArgumentParser()
    parser.add_argument(
        '--modus', choices=['gui', 'recording', 'all'], required=True)

    args = parser.parse_args()

    prozesse = []
    if args.modus in ['gui', 'all']:
        prozesse.append(multiprocessing.Process(target=gui))

    if args.modus in ['recording', 'all']:
        prozesse.append(multiprocessing.Process(target=recording))

    for p in prozesse:
        p.start()
