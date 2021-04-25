import db_utils
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from signals import Communicate
from window import schedule_window


class ScheduleWindow(QtWidgets.QMainWindow, schedule_window.Ui_Schedule):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back = Communicate()
        self.pushButton_back.clicked.connect(self.clicked_back)
        self.pushButton_show.clicked.connect(self.clicked_show_schedule)
        self.doctors = list()

    @pyqtSlot()
    def clicked_back(self):
        self.back.close_signal.emit()
        self.clear_schedule_table()
        self.comboBox_doctor.setCurrentIndex(-1)
        self.hide()

    @pyqtSlot()
    def clicked_show_schedule(self):
        self.clear_schedule_table()
        doctor_id = self.comboBox_doctor.currentIndex() + 1
        cabinet = db_utils.get_doctor_cabinet(doctor_id)
        worked_days = db_utils.get_worked_days_doctor(doctor_id)
        start_time, end_time = db_utils.get_time_work(doctor_id)
        for i in range(len(worked_days)):
            self.tableWidget_shedule.setItem(worked_days[i], 2, QtWidgets.QTableWidgetItem(f"{cabinet[0]}"))

        print(start_time, end_time)
        for i in range(len(worked_days)):
            self.tableWidget_shedule.setItem(worked_days[i], 0, QtWidgets.QTableWidgetItem(f"{start_time}"))
            self.tableWidget_shedule.setItem(worked_days[i], 1, QtWidgets.QTableWidgetItem(f"{end_time}"))

    def clear_schedule_table(self):
        row = self.tableWidget_shedule.rowCount()
        col = self.tableWidget_shedule.columnCount()
        for i in range(row):
            for j in range(col):
                self.tableWidget_shedule.setItem(i, j, QtWidgets.QTableWidgetItem())

    def init_doctors(self):
        self.doctors = db_utils.get_doctors()
        for i in range(len(self.doctors)):
            self.comboBox_doctor.addItem(self.doctors[i][1])
        self.comboBox_doctor.setCurrentIndex(-1)
        header = self.tableWidget_shedule.horizontalHeader()
        for i in range(3):  # выравниваем столбцы
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)