import db_utils
from login import LoginWindow
from registration import RegistrationWindow
from schedule import ScheduleWindow
from window import start_window
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox


class StartWindow(QtWidgets.QMainWindow, start_window.Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.image.setPixmap(QPixmap("src/image.png"))

        res = db_utils.check_connection()
        if not res[0]:
            QMessageBox.warning(self, 'Ошибка', f'Ошибка подключения к БД: {res[1]}', QMessageBox.Ok)
            self.hide()

        self.login_window = LoginWindow()
        self.schedule_window = ScheduleWindow()
        self.registration_window = RegistrationWindow()

        self.pushButton_autorization.clicked.connect(self.open_login_window)
        self.pushButton_registration.clicked.connect(self.open_registration_window)
        self.pushButton_schedule.clicked.connect(self.open_schedule_window)

        self.login_window.back.close_signal.connect(self.show)
        self.schedule_window.back.close_signal.connect(self.show)
        self.registration_window.back.close_signal.connect(self.show)

    @pyqtSlot()
    def open_login_window(self):
        self.hide()
        self.login_window.show()

    @pyqtSlot()
    def open_registration_window(self):
        self.hide()
        self.registration_window.show()

    @pyqtSlot()
    def open_schedule_window(self):
        self.hide()
        self.schedule_window.show()
        self.schedule_window.init_doctors()