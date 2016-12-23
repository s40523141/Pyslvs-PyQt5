from .modules import *

class WorkerThread(QThread):
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.stoped = False
        self.mutex = QMutex()
        self.progress = 0
    
    def setPath(self, data):
        self.path = data
    
    def run(self):
        ''''''
    
    def progress_going(self):
        self.progress = self.progress+1
    
    def stop(self):
        with QMutexLocker(self.mutex): self.stoped = True