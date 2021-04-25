from PyQt5.QtCore import QObject, pyqtSignal


class Communicate(QObject):
    close_signal = pyqtSignal()
