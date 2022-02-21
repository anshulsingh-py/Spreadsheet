from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
import os
import pandas as pd


class Functions(QMainWindow):
    def __init__(self, tableWidget, Modulename):
        super().__init__()
        self.tableWidget = tableWidget
        self.data = []
        self.error_msg = []
        self.error = True
        self.flag = 0
        self.Modulename = Modulename

    def open(self):
        self.tableWidget.clearContents()
        path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV/XLSX(*.csv *.xlsx)')
        f = path[0]
        if f != '':
            try:
                dataset = pd.read_csv(f)
            except Exception:
                dataset = pd.read_excel(f)
            row = 0
            for i in range(len(dataset.axes[0])):
                col = 0
                for j in range(len(dataset.axes[1])):
                    if pd.isnull(dataset.iloc[i, j]):
                        break
                    else:
                        oneitem = QTableWidgetItem(str(dataset.iloc[i, j]))
                        self.tableWidget.setItem(row, col, oneitem)
                        col += 1
                row += 1

    def validate(self):
        self.error = True
        self.data.clear()
        row = 0
        while True:
            col = 0
            try:
                self.tableWidget.item(col, row).text()
            except Exception:
                break
            temp = []
            while True:
                try:
                    x = self.tableWidget.item(col, row).text()
                except Exception:
                    break
                try:
                    a = int(x)
                except Exception:
                    try:
                        a = float(x)
                    except Exception:
                        a = -1
                temp.append(a)
                col += 1
            self.data.append(temp)
            row += 1
        self.check()
        self.flag = 0
        if len(self.error_msg) == 0 and self.error is True:
            inf = QMessageBox.information(self, 'Next', 'You can submit now')
            self.flag = 1
        else:
            self.showMessage()

    def check(self):
        if len(self.data) == 0:
            not_filled = QMessageBox.critical(self, 'Error', 'Please fill the table or Load csv/xlxs File')
            self.error = False
        else:
            self.error_msg.clear()
            if len(set(self.data[0])) != len(self.data[0]):
                self.error_msg.append('ID coloum should be unique.')
            for rows in self.data:
                for value in rows:
                    if value == -1:
                        self.error_msg.append('All values should be Numerics.')
                        pass

    def showMessage(self):
        error = ""
        for text in self.error_msg:
            error += text
            error += '\n'
        if error != "":
            msg = QMessageBox.critical(self, 'error', error)

    def submit(self):
        if self.flag != 1:
            ms1 = QMessageBox.critical(self, 'error', 'Please! validate first')
        else:
            name = QFileDialog.getExistingDirectory(None, 'Choose the directory to save', os.getenv('HOME'))
            if name != '':
                for i in range(len(self.data[0])):
                    na = name
                    na += '/{0}_{1}.txt'.format(self.Modulename, i+1)
                    with open(na, "w") as file:
                        count = self.tableWidget.columnCount()
                        x = count
                        for j in range(count):
                            file.write("\"{0}\" : \"{1}\"".format(self.tableWidget.horizontalHeaderItem(j).text(), self.data[j][i]))
                            if x>1:
                                file.write(", ")
                                x -= 1
                        file.close()
        self.flag = 0
