from time import sleep
import psutil.tests
import win32gui  # type: ignore
import win32process  # type: ignore
import psutil
import threading

from db_handler import DatabaseHandler


class WatcherThread(threading.Thread):

    #
    #

    def __init__(self, databaseHandler: DatabaseHandler):
        super(WatcherThread, self).__init__()
        self.databaseHandler = databaseHandler

    #
    #

    def run(self) -> None:
        """
        Runs on start of watcher thread, general procedure.
        """
        durationSeconds: int = 0
        process: psutil.Process = self.getActiveProcess()
        while True:
            sleep(5)
            durationSeconds += 5
            nextProcess: psutil.Process = self.getActiveProcess()
            if process.pid == nextProcess.pid:
                pass
            else:
                self.on_active_changed(process, durationSeconds)
                process = nextProcess
                durationSeconds = 0

    #
    #

    def on_active_changed(self, process: psutil.Process, durationSeconds: int) -> None:
        """
        Ereignis bei Wechsel des aktiven Prozesses

        *Args*:
            process (psutil.Process): Der Prozess der vorher aktiv war und nun geloggt wird.
        """
        try:
            self.databaseHandler.connect()
            
            _INSERT_PROCESS: str = f"INSERT OR REPLACE INTO PROCESS (name) SELECT '{process.name()}' WHERE NOT EXISTS (SELECT 1 FROM PROCESS WHERE name = '{process.name()}')"
            _MID_PROCESS: str = f"SELECT (id) FROM PROCESS WHERE name = '{process.name()}'"

            self.databaseHandler.runQuery(_INSERT_PROCESS)
            mid = self.databaseHandler.runQuery(_MID_PROCESS)
            print(mid)
            _INSERT_ENTRY: str = f"INSERT INTO ENTRY('pid', 'mid', 'name', 'durationSec') VALUES('{process.pid}', '{mid[0][0]}', '{process.name()}', '{durationSeconds}')"
            self.databaseHandler.runQuery(_INSERT_ENTRY)
            
        except Exception as e:
            print(f"Something went wrong: {e}")

        finally:
            self.databaseHandler.disconnect()

    #
    #

    def getActiveProcess(self) -> psutil.Process:
        """
        Collects the currently active process from the win32 api.

        *Returns*:
            psutil.Process: The currently active process as psutil.Process instance.
        """
        windowHandle = win32gui.GetForegroundWindow()
        _, process_id = win32process.GetWindowThreadProcessId(windowHandle)
        return psutil.Process(process_id)
