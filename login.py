import db_utils
from admin import AdminWindow
from signals import Communicate
from window import login_window
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox


class LoginWindow(QtWidgets.QMainWindow, login_window.Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.admin_window = None
        self.login = "none"

        self.back = Communicate()
        self.pushButton_back.clicked.connect(self.clicked_back)
        self.pushButton_login.clicked.connect(self.open_admin_window)

    def clear(self):
        self.lineEdit_login.clear()
        self.lineEdit_pass.clear()

    @pyqtSlot()
    def clicked_back(self):
        self.back.close_signal.emit()
        self.clear()
        self.hide()

    @pyqtSlot()
    def open_admin_window(self):
        if not self.check_credentials():
            QMessageBox.warning(self, 'Ошибка', f'Введены некорректные данные\n'
                                                f'или пациента не существует', QMessageBox.Ok)
            return
        self.hide()
        self.clear()
        self.admin_window = AdminWindow(self.login)
        self.admin_window.back.close_signal.connect(self.clicked_back)
        self.admin_window.patient_name.setText(db_utils.give_name_by_login(self.login))
        self.admin_window.show()

    def check_credentials(self):
        if not self.lineEdit_login.text() or not self.lineEdit_pass.text():
            return False
        login_data = self.lineEdit_login.text()
        passwd_data = self.lineEdit_pass.text()
        self.login = login_data
        return db_utils.check_credentials(login_data, passwd_data)