from time import sleep
import psutil.tests
import win32gui  # type: ignore
import win32process  # type: ignore
import psutil
import threading


class WatcherThread(threading.Thread):

    def __init__(self):
        super(WatcherThread, self).__init__()

    def run(self) -> None:
        """
        ### Summary
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
                self.on_active_changed(process)
                process = nextProcess

    def on_active_changed(self, process: psutil.Process) -> None:
        """
        ### Summary:
            Ereignis bei Wechsel des aktiven Prozesses

        ### Args:
            process (psutil.Process): Der Prozess der vorher aktiv war und nun geloggt wird.
        """
        print(process.pid)
        print(process.name())
        pass

    def getActiveProcess(self) -> psutil.Process:
        """
        ### Summary:
            Collects the currently active process from the win32 api.
        ### Returns:
            psutil.Process: The currently active process as psutil.Process instance.
        """
        windowHandle = win32gui.GetForegroundWindow()
        _, process_id = win32process.GetWindowThreadProcessId(windowHandle)
        return psutil.Process(process_id)
