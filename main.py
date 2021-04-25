import sys
from start import StartWindow
from PyQt5 import QtWidgets, QtGui


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('src/icon.ico'))
    window = StartWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
