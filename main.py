from mainwindow import *
from functions import *
import sys


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.Fun_FinPlate = Functions(self.ui.tableWidget_FinPlate, 'FinPlate')
        self.ui.pushButton_1.clicked.connect(self.Fun_FinPlate.open)
        self.Fun_TensionMember = Functions(self.ui.tableWidget_TensionMember, 'TensionMember')
        self.ui.pushButton_4.clicked.connect(self.Fun_TensionMember.open)
        self.Fun_BCEndPlate = Functions(self.ui.tableWidget_BCEndPlate, 'BCEndPlate')
        self.ui.pushButton_7.clicked.connect(self.Fun_BCEndPlate.open)
        self.Fun_CleatAngle = Functions(self.ui.tableWidget_CleatAngle, 'CleatAngle')
        self.ui.pushButton_10.clicked.connect(self.Fun_CleatAngle.open)
        self.ui.pushButton_2.clicked.connect(self.Fun_FinPlate.validate)
        self.ui.pushButton_5.clicked.connect(self.Fun_TensionMember.validate)
        self.ui.pushButton_8.clicked.connect(self.Fun_BCEndPlate.validate)
        self.ui.pushButton_11.clicked.connect(self.Fun_CleatAngle.validate)
        self.ui.pushButton_3.clicked.connect(self.Fun_FinPlate.submit)
        self.ui.pushButton_6.clicked.connect(self.Fun_TensionMember.submit)
        self.ui.pushButton_9.clicked.connect(self.Fun_BCEndPlate.submit)
        self.ui.pushButton_12.clicked.connect(self.Fun_CleatAngle.submit)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MyForm()
    sys.exit(app.exec_())
