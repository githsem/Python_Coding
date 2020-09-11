import sys
import sqlite3
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.echoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giris")
        self.yazi_alani = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Kullanici Girisi")

        self.show()


app = QtWidgets.QApplication()
pencere = Pencere()
sys.exit(app.exec_())