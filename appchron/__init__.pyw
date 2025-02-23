import multiprocessing
import os
from argparse import ArgumentParser

from app import runGUI
from watcher import WatcherThread
from db_handler import DatabaseHandler



# Constant
_DATA_DIR: str = os.path.join(os.path.dirname(__file__), 'data')
_SQLITE_PATH: str = _DATA_DIR + "/appchron.sqlite3"



def recording():
    """
    Starts the recording of the active application.
    """
    # Create the sqlite if it doesn't exist
    handler: DatabaseHandler = create_sqlite_file()

    # Initialize the watcher to begin watching and logging the active application.
    watcherthread: WatcherThread = WatcherThread(handler)
    watcherthread.start()



def create_sqlite_file() -> DatabaseHandler:
    """
    This function creates a SQLite database file and returns a DatabaseHandler object.
    
    *Returns*: 
        The function `create_sqlite_file()` returns an instance of `DatabaseHandler`.
    """
    # Create data folder
    os.makedirs(_DATA_DIR, exist_ok=True)

    # Create DbHandler and database file
    handler: DatabaseHandler = DatabaseHandler(
        _SQLITE_PATH)
    handler.createTables()
    return handler



if __name__ == '__main__':
    multiprocessing.freeze_support()

    parser: ArgumentParser = ArgumentParser()
    parser.add_argument(
        '--mode', choices=['gui', 'recording', 'all'], required=True)

    args = parser.parse_args()

    processes = []
    if args.mode in ['gui', 'all']:
        processes.append(multiprocessing.Process(target=runGUI))

    if args.mode in ['recording', 'all']:
        processes.append(multiprocessing.Process(target=recording))

    for p in processes:
        p.start()
