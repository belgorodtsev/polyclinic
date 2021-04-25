import db_utils
from signals import Communicate
from window import registration_window
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox


class RegistrationWindow(QtWidgets.QMainWindow, registration_window.Ui_Registration):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back = Communicate()
        self.pushButton_back.clicked.connect(self.clicked_back)
        self.pushButton_registr.clicked.connect(self.registration)

    def clear(self):
        self.lineEdit_login.clear()
        self.lineEdit_passwd.clear()
        self.lineEdit_passwd2.clear()
        self.lineEdit_name.clear()
        self.checkBox_insurance.setChecked(False)

    @pyqtSlot()
    def clicked_back(self):
        self.back.close_signal.emit()
        self.hide()

    @pyqtSlot()
    def registration(self):
        login_data = self.lineEdit_login.text()
        passwd_data = self.lineEdit_passwd.text()
        passwd_data2 = self.lineEdit_passwd2.text()
        name = self.lineEdit_name.text()
        insurance = int(self.checkBox_insurance.isChecked())
        if passwd_data != passwd_data2:
            QMessageBox.warning(self, 'Ошибка', f'Пароли не совпадают, повторите ввод', QMessageBox.Ok)
            self.lineEdit_passwd.clear()
            self.lineEdit_passwd2.clear()
            return
        if db_utils.check_login_exists(login_data):
            QMessageBox.warning(self, 'Ошибка', f'Пользователь с таким логином существует', QMessageBox.Ok)
            self.lineEdit_login.clear()
            return
        db_utils.add_patient(login_data, passwd_data, name, insurance)
        QMessageBox.information(self, 'Успешно',
                                f'Пациент {name} успешно зарегистрировался, выполните вход', QMessageBox.Ok)
        self.clear()
        self.clicked_back()