# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(789, 509)
        self.tab = QtWidgets.QTabWidget(AdminWindow)
        self.tab.setGeometry(QtCore.QRect(10, 10, 771, 431))
        self.tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab.setObjectName("tab")
        self.tab_record = QtWidgets.QWidget()
        self.tab_record.setObjectName("tab_record")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_record)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 746, 58))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_proc = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_proc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_proc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_proc.setObjectName("label_proc")
        self.verticalLayout.addWidget(self.label_proc)
        self.comboBox_proc = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_proc.setMinimumSize(QtCore.QSize(340, 25))
        self.comboBox_proc.setObjectName("comboBox_proc")
        self.verticalLayout.addWidget(self.comboBox_proc)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_cab = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_cab.setMinimumSize(QtCore.QSize(100, 0))
        self.label_cab.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_cab.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cab.setObjectName("label_cab")
        self.verticalLayout_2.addWidget(self.label_cab)
        self.comboBox_cabinet = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_cabinet.setMinimumSize(QtCore.QSize(100, 25))
        self.comboBox_cabinet.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_cabinet.setObjectName("comboBox_cabinet")
        self.verticalLayout_2.addWidget(self.comboBox_cabinet)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_day = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_day.setAlignment(QtCore.Qt.AlignCenter)
        self.label_day.setObjectName("label_day")
        self.verticalLayout_3.addWidget(self.label_day)
        self.comboBox_day = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_day.setEnabled(True)
        self.comboBox_day.setMinimumSize(QtCore.QSize(160, 25))
        self.comboBox_day.setObjectName("comboBox_day")
        self.verticalLayout_3.addWidget(self.comboBox_day)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.pushButton_show = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_show.setMinimumSize(QtCore.QSize(115, 0))
        self.pushButton_show.setObjectName("pushButton_show")
        self.verticalLayout_4.addWidget(self.pushButton_show)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.tabel_time = QtWidgets.QTableWidget(self.tab_record)
        self.tabel_time.setGeometry(QtCore.QRect(10, 80, 741, 281))
        self.tabel_time.setObjectName("tabel_time")
        self.tabel_time.setColumnCount(0)
        self.tabel_time.setRowCount(0)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_record)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 360, 741, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_record = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_record.setObjectName("pushButton_record")
        self.horizontalLayout_3.addWidget(self.pushButton_record)
        self.tab.addTab(self.tab_record, "")
        self.tab_show_record = QtWidgets.QWidget()
        self.tab_show_record.setObjectName("tab_show_record")
        self.table_activ_proc = QtWidgets.QTableWidget(self.tab_show_record)
        self.table_activ_proc.setGeometry(QtCore.QRect(10, 10, 741, 341))
        self.table_activ_proc.setObjectName("table_activ_proc")
        self.table_activ_proc.setColumnCount(0)
        self.table_activ_proc.setRowCount(0)
        self.pushButton_delete = QtWidgets.QPushButton(self.tab_show_record)
        self.pushButton_delete.setGeometry(QtCore.QRect(640, 360, 111, 31))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.tab.addTab(self.tab_show_record, "")
        self.tab_reselt = QtWidgets.QWidget()
        self.tab_reselt.setObjectName("tab_reselt")
        self.label_2 = QtWidgets.QLabel(self.tab_reselt)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 711, 41))
        self.label_2.setObjectName("label_2")
        self.tab.addTab(self.tab_reselt, "")
        self.pushButton_logout = QtWidgets.QPushButton(AdminWindow)
        self.pushButton_logout.setGeometry(QtCore.QRect(660, 470, 111, 31))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.verticalLayoutWidget = QtWidgets.QWidget(AdminWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 450, 371, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_patient = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_patient.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_patient.setObjectName("label_patient")
        self.horizontalLayout.addWidget(self.label_patient)
        self.patient_name = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.patient_name.setObjectName("patient_name")
        self.horizontalLayout.addWidget(self.patient_name)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.free_proc = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.free_proc.setObjectName("free_proc")
        self.horizontalLayout_4.addWidget(self.free_proc)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.retranslateUi(AdminWindow)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "ИС Поликлиниа"))
        self.label_proc.setText(_translate("AdminWindow", "Процедура"))
        self.label_cab.setText(_translate("AdminWindow", "Кабинет"))
        self.label_day.setText(_translate("AdminWindow", "День"))
        self.pushButton_show.setText(_translate("AdminWindow", "Просмотр"))
        self.pushButton_record.setText(_translate("AdminWindow", "Записаться"))
        self.tab.setTabText(self.tab.indexOf(self.tab_record), _translate("AdminWindow", "Запись на процедуры"))
        self.pushButton_delete.setText(_translate("AdminWindow", "Удалить"))
        self.tab.setTabText(self.tab.indexOf(self.tab_show_record), _translate("AdminWindow", "Активные записи"))
        self.label_2.setText(_translate("AdminWindow", "Тут можно отображать результаты уже выполненных анализов, в варианте не прописано"))
        self.tab.setTabText(self.tab.indexOf(self.tab_reselt), _translate("AdminWindow", "Результат процедур"))
        self.pushButton_logout.setText(_translate("AdminWindow", "Выход"))
        self.label_patient.setText(_translate("AdminWindow", "Пациент:"))
        self.patient_name.setText(_translate("AdminWindow", "TextLabel"))
        self.label_3.setText(_translate("AdminWindow", "Бесплатные процедуры:"))
        self.free_proc.setText(_translate("AdminWindow", "TextLabel"))
