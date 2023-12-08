import sys
from PySide6 import QtCore, QtWidgets, QtGui
from windows import MainWindow
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
