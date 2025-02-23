import multiprocessing
import os
from argparse import ArgumentParser

import app
import db_handler
import watcher

_DATA_DIR: str = "appchron/data"
_SQLITE_PATH: str = _DATA_DIR + "/appchron.sqlite3"


def gui():
    app.runGUI()
    pass


def recording():
    # Create the sqlite if it doesn't exist
    dbHandler: db_handler.DatabaseHandler = createSQLiteFile()

    # Initialize the watcher to begin watching and logging the active application.
    watcherthread: watcher.WatcherThread = watcher.WatcherThread(dbHandler)
    watcherthread.start()


def createSQLiteFile() -> db_handler.DatabaseHandler:
    # Create data folder
    try:
        os.makedirs(_DATA_DIR)
    except FileExistsError:
        pass

    # Create DbHandler and database file
    dbHandler: db_handler.DatabaseHandler = db_handler.DatabaseHandler(
        _SQLITE_PATH)
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
