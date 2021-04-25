import db_utils
from signals import Communicate
from window import admin_window
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox


class AdminWindow(QtWidgets.QMainWindow, admin_window.Ui_AdminWindow):
    def __init__(self, patient_login):
        super().__init__()
        self.setupUi(self)
        self.back = Communicate()
        self.login = patient_login
        self.size_time = 0
        self.id_vectors = list()
        self.free_proc.setText("5")

        self.init_combo_boxes()
        self.init_tab_procedure()
        self.pushButton_logout.clicked.connect(self.clicked_back)
        self.pushButton_show.clicked.connect(self.clicked_show)
        self.comboBox_proc.currentIndexChanged.connect(self.change_proc_index)
        self.comboBox_cabinet.currentIndexChanged.connect(self.change_days_index)
        self.comboBox_day.currentIndexChanged.connect(self.change_day_index)
        self.pushButton_record.clicked.connect(self.clicked_record)
        self.pushButton_delete.clicked.connect(self.clicked_delete)

    def clear(self):
        self.comboBox_proc.setCurrentIndex(-1)
        self.comboBox_cabinet.setCurrentIndex(-1)
        self.comboBox_day.clear()
        for i in range(self.size_time):
            self.tabel_time.setItem(i, 2, QtWidgets.QTableWidgetItem())

    @pyqtSlot()
    def change_proc_index(self):
        val = self.comboBox_proc.currentIndex()
        self.comboBox_cabinet.setCurrentIndex(val)
        days = db_utils.get_days_for_procedure(val + 1, val + 1)
        self.init_days_box(days)
        for i in range(self.size_time):
            self.tabel_time.setItem(i, 2, QtWidgets.QTableWidgetItem())

    @pyqtSlot()
    def change_days_index(self):
        val = self.comboBox_cabinet.currentIndex()
        self.comboBox_proc.setCurrentIndex(val)
        days = db_utils.get_days_for_procedure(val + 1, val + 1)
        self.init_days_box(days)

    @pyqtSlot()
    def change_day_index(self):
        for i in range(self.size_time):
            self.tabel_time.setItem(i, 2, QtWidgets.QTableWidgetItem())

    @pyqtSlot()
    def clicked_back(self):
        self.back.close_signal.emit()
        self.clear()
        self.hide()

    @pyqtSlot()
    def clicked_show(self):
        if self.comboBox_proc.currentIndex() == -1 \
                or self.comboBox_cabinet.currentIndex() == -1 \
                or self.comboBox_day.currentIndex() == -1:
            QMessageBox.warning(self, 'Ошибка', f'Выберете параметры!', QMessageBox.Ok)
            return
        self.set_status_column()

    @pyqtSlot()
    def clicked_record(self):
        if self.comboBox_proc.currentIndex() == -1 \
                or self.comboBox_cabinet.currentIndex() == -1 \
                or self.comboBox_day.currentIndex() == -1:
            QMessageBox.warning(self, 'Ошибка', f'Выберете параметры!', QMessageBox.Ok)
            return

        indexes = self.tabel_time.selectionModel().selectedIndexes()
        row = indexes[0].row()

        if self.tabel_time.item(row, 2).text() == 'Занято':
            QMessageBox.warning(self, 'Ошибка', f'Выберете другое время!', QMessageBox.Ok)
        else:
            procedure = self.comboBox_proc.currentIndex() + 1
            id_day = db_utils.get_id_day(self.comboBox_day.currentText())
            id_patient = db_utils.get_id_patient(self.login)
            db_utils.add_entry_for_procedure(procedure, id_day, row + 8, id_patient)
            self.tabel_time.setItem(row, 2, QtWidgets.QTableWidgetItem('Занято'))
            self.update_procedure_table()
            count = int(self.free_proc.text()) - 1
            if count != 0:
                self.free_proc.setText(str(count))

    @pyqtSlot()
    def clicked_delete(self):
        indexes = self.table_activ_proc.selectionModel().selectedIndexes()
        row = indexes[0].row()
        db_utils.delete_procedure_entry(self.id_vectors[row])
        self.table_activ_proc.removeRow(row)
        self.clicked_show()

    def set_status_column(self):
        procedure = self.comboBox_proc.currentIndex() + 1
        day = self.comboBox_day.currentIndex() + 7
        result = db_utils.get_registration_for_procedures(procedure, day)
        for i in range(self.size_time):
            self.tabel_time.setItem(i, 2, QtWidgets.QTableWidgetItem('Свободно'))
        for i in range(len(result)):
            self.tabel_time.setItem(result[i], 2, QtWidgets.QTableWidgetItem('Занято'))

    def init_days_box(self, days):
        self.comboBox_day.clear()
        for i in range(len(days)):
            self.comboBox_day.addItem(str(days[i][0]))

    def init_combo_boxes(self):
        procedures = db_utils.get_procedures()
        for i in range(len(procedures)):
            self.comboBox_proc.addItem(procedures[i][0])
        self.comboBox_proc.setCurrentIndex(-1)

        cabinets = db_utils.get_procedures_cabinet()
        for i in range(len(cabinets)):
            self.comboBox_cabinet.addItem(str(cabinets[i][0]))
        self.comboBox_cabinet.setCurrentIndex(-1)

        labels = ['Начало', 'Окончание', 'Статус записи']
        self.tabel_time.setColumnCount(len(labels))
        self.tabel_time.setHorizontalHeaderLabels(labels)
        header = self.tabel_time.horizontalHeader()
        for i in range(len(labels)):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        time_intervals = db_utils.get_time_interval()
        self.size_time = len(time_intervals)
        for i in range(self.size_time):
            row = self.tabel_time.rowCount()
            self.tabel_time.setRowCount(row + 1)
            self.tabel_time.setItem(row, 0, QtWidgets.QTableWidgetItem(time_intervals[i][0]))
            self.tabel_time.setItem(row, 1, QtWidgets.QTableWidgetItem(time_intervals[i][1]))

    def init_tab_procedure(self):
        labels = ['Процедура', 'День записи', 'Начало', 'Конец']
        self.table_activ_proc.setColumnCount(len(labels))
        self.table_activ_proc.setHorizontalHeaderLabels(labels)
        header = self.table_activ_proc.horizontalHeader()
        for i in range(len(labels)):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.update_procedure_table()

    def update_procedure_table(self):
        self.clear_procedure_table()
        res = db_utils.get_unique_procedure(db_utils.get_id_patient(self.login))
        procedures = db_utils.get_procedures()
        days = db_utils.get_days()
        time_intervals = db_utils.get_time_interval()
        for j in range(len(res)):
            row = self.table_activ_proc.rowCount()
            self.table_activ_proc.setRowCount(row + 1)
            self.id_vectors.append(res[j][4])
            self.table_activ_proc.setItem(row, 0, QtWidgets.QTableWidgetItem(procedures[res[j][0] - 1][0]))
            self.table_activ_proc.setItem(row, 1, QtWidgets.QTableWidgetItem(days[res[j][1] - 7][0]))
            self.table_activ_proc.setItem(row, 2, QtWidgets.QTableWidgetItem(time_intervals[res[j][2] - 8][0]))
            self.table_activ_proc.setItem(row, 3, QtWidgets.QTableWidgetItem(time_intervals[res[j][2] - 8][1]))

    def clear_procedure_table(self):
        self.id_vectors.clear()
        size = self.table_activ_proc.rowCount()
        for j in range(size):
            row = self.table_activ_proc.rowCount()
            self.table_activ_proc.removeRow(row)
