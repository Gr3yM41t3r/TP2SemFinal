import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from graphTools.GraphTools import Graphtools


class Ui_MainWindow(object):
    def __init__(self):
        self.checkBoxList = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(403, 735)
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 401, 5))
        self.line.setMouseTracking(False)
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("border-color: rgb(20, 55, 255);\n"
                                "background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 640, 381, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 125, 58, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.targetEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.targetEdit.setGeometry(QtCore.QRect(80, 220, 201, 32))
        self.targetEdit.setObjectName("targetEdit")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 170, 401, 5))
        self.line_2.setMouseTracking(False)
        self.line_2.setAutoFillBackground(False)
        self.line_2.setStyleSheet("border-color: rgb(20, 55, 255);\n"
                                  "background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.selectSource = QtWidgets.QPushButton(self.centralwidget)
        self.selectSource.setGeometry(QtCore.QRect(310, 120, 88, 32))
        self.selectSource.setObjectName("selectSource")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 225, 58, 18))
        self.label_5.setObjectName("label_5")
        self.sourceEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sourceEdit.setGeometry(QtCore.QRect(80, 120, 201, 32))
        self.sourceEdit.setObjectName("sourceEdit")
        self.selectTarget = QtWidgets.QPushButton(self.centralwidget)
        self.selectTarget.setGeometry(QtCore.QRect(310, 220, 88, 32))
        self.selectTarget.setObjectName("selectTarget")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 270, 401, 5))
        self.line_3.setMouseTracking(False)
        self.line_3.setAutoFillBackground(False)
        self.line_3.setStyleSheet("border-color: rgb(20, 55, 255);\n"
                                  "background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 280, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.threshold = QtWidgets.QLabel(self.centralwidget)
        self.threshold.setGeometry(QtCore.QRect(10, 360, 111, 18))
        self.threshold.setObjectName("threshold")
        self.levenshteinSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.levenshteinSpinBox.setGeometry(QtCore.QRect(110, 395, 71, 32))
        self.levenshteinSpinBox.setMaximum(10.0)
        self.levenshteinSpinBox.setSingleStep(0.1)
        self.levenshteinSpinBox.setObjectName("levenshteinSpinBox")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 320, 131, 18))
        self.label_9.setObjectName("label_9")
        self.property = QtWidgets.QComboBox(self.centralwidget)
        self.property.setGeometry(QtCore.QRect(170, 315, 141, 32))
        self.property.setObjectName("property")
        self.property.addItem("")
        self.property.addItem("")
        self.property.addItem("")
        self.property.addItem("")
        self.property.addItem("")
        self.property.addItem("")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 530, 401, 5))
        self.line_4.setMouseTracking(False)
        self.line_4.setAutoFillBackground(False)
        self.line_4.setStyleSheet("border-color: rgb(20, 55, 255);\n"
                                  "background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(120, 550, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 600, 81, 18))
        self.label_11.setObjectName("label_11")
        self.outputFileEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.outputFileEdit.setGeometry(QtCore.QRect(100, 595, 201, 32))
        self.outputFileEdit.setObjectName("outputFileEdit")
        self.selectOutput = QtWidgets.QPushButton(self.centralwidget)
        self.selectOutput.setGeometry(QtCore.QRect(310, 595, 88, 32))
        self.selectOutput.setObjectName("selectOutput")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(160, 680, 88, 32))
        self.start.setObjectName("start")
        self.levenshteinCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.levenshteinCheckBox.setGeometry(QtCore.QRect(10, 400, 101, 22))
        self.levenshteinCheckBox.setObjectName("levenshteinCheckBox")
        self.jaccardSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.jaccardSpinBox.setGeometry(QtCore.QRect(330, 395, 71, 32))
        self.jaccardSpinBox.setMaximum(10.0)
        self.jaccardSpinBox.setSingleStep(0.1)
        self.jaccardSpinBox.setObjectName("jaccardSpinBox")
        self.jaroCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.jaroCheckBox.setGeometry(QtCore.QRect(10, 460, 101, 22))
        self.jaroCheckBox.setObjectName("jaroCheckBox")
        self.jaccardheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.jaccardheckBox.setGeometry(QtCore.QRect(220, 400, 101, 22))
        self.jaccardheckBox.setObjectName("jaccardheckBox")
        self.jaroSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.jaroSpinBox.setGeometry(QtCore.QRect(110, 455, 71, 32))
        self.jaroSpinBox.setMaximum(10.0)
        self.jaroSpinBox.setSingleStep(0.1)
        self.jaroSpinBox.setObjectName("jaroSpinBox")
        self.jarowinklerCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.jarowinklerCheckbox.setGeometry(QtCore.QRect(220, 460, 101, 22))
        self.jarowinklerCheckbox.setObjectName("jarowinklerCheckbox")
        self.jaroWinklerSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.jaroWinklerSpinBox.setGeometry(QtCore.QRect(330, 455, 71, 32))
        self.jaroWinklerSpinBox.setMaximum(10.0)
        self.jaroWinklerSpinBox.setSingleStep(0.1)
        self.jaroWinklerSpinBox.setObjectName("jaroWinklerSpinBox")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(170, 355, 71, 32))
        self.doubleSpinBox_5.setMaximum(1.0)
        self.doubleSpinBox_5.setSingleStep(0.1)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TP2"))
        self.label_2.setText(_translate("MainWindow", "File input:"))
        self.label_3.setText(_translate("MainWindow", "Source "))
        self.selectSource.setText(_translate("MainWindow", "sélectionner"))
        self.label_4.setText(_translate("MainWindow", "Target"))
        self.label_5.setText(_translate("MainWindow", "File input:"))
        self.selectTarget.setText(_translate("MainWindow", "sélectionner"))
        self.label_6.setText(_translate("MainWindow", "Similarity Measure"))
        self.threshold.setText(_translate("MainWindow", "threshold:"))
        self.label_9.setText(_translate("MainWindow", "property to compare:"))
        self.property.setItemText(0, _translate("MainWindow", "P102_has_title"))
        self.property.setItemText(1, _translate("MainWindow", "U13_has_casting"))
        self.property.setItemText(2, _translate("MainWindow", "P3_has_note"))
        self.property.setItemText(3, _translate("MainWindow", "U12_has_genre"))
        self.property.setItemText(4, _translate("MainWindow", "U11_has_key"))
        self.property.setItemText(5, _translate("MainWindow", "U16_has_catalogue_statement"))
        self.label_10.setText(_translate("MainWindow", "OutPut File"))
        self.label_11.setText(_translate("MainWindow", "File output:"))
        self.selectOutput.setText(_translate("MainWindow", "sélectionner"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.jaroWinklerSpinBox.setValue(1)
        self.jaroSpinBox.setValue(1)
        self.levenshteinSpinBox.setValue(1)
        self.jaccardSpinBox.setValue(1)
        self.checkBoxList = []
        self.levenshteinCheckBox.setText(_translate("MainWindow", "Levenshtein"))
        self.jaroCheckBox.setText(_translate("MainWindow", "Jaro"))
        self.jaccardheckBox.setText(_translate("MainWindow", "Jaccard"))
        self.jarowinklerCheckbox.setText(_translate("MainWindow", "Jaro Winkler"))
        self.checkBoxList.append(self.levenshteinCheckBox)
        self.checkBoxList.append(self.jaroCheckBox)
        self.checkBoxList.append(self.jaccardheckBox)
        self.checkBoxList.append(self.jarowinklerCheckbox)
        self.start.clicked.connect(self.startProgram)
        self.selectSource.clicked.connect(self.selectSourceFile)
        self.selectTarget.clicked.connect(self.selectTargetFile)
        self.selectOutput.clicked.connect(self.selectOutputFile)

    def selectSourceFile(self):
        filepath = QFileDialog.getOpenFileName()[0]
        filepath = os.path.normpath(filepath)
        self.sourceEdit.setText(filepath)

    def selectTargetFile(self):
        filepath = QFileDialog.getOpenFileName()[0]
        filepath = os.path.normpath(filepath)
        self.targetEdit.setText(filepath)

    def selectOutputFile(self):
        filepath = QFileDialog.getOpenFileName()[0]
        filepath = os.path.normpath(filepath)
        self.outputFileEdit.setText(filepath)

    def getSelectedThreshold(self):
        return float(self.threshold.text())

    def getSelectedProperty(self):
        return str(self.property.currentText())

    def getAppropriateSimilarityMeasure(self):
        measure_array = []
        measure_array.clear()
        for i in self.checkBoxList:
            self.levenshteinCheckBox.text()
            if i.isChecked():
                measure_array.append("{}{}{}".format(i.text(), ':', round(self.getPonderation(i.text()),3)))
        return measure_array

    def getPonderation(self, measure):
        if measure == "Jaro":
            return self.jaroSpinBox.value()
        elif measure == "Levenshtein":
            return self.levenshteinSpinBox.value()
        elif measure == "Jaccard":
            return self.jaccardSpinBox.value()
        elif measure == "Jaro Winkler":
            return self.jaroWinklerSpinBox.value()

    def startProgram(self):

        one = Graphtools(self.sourceEdit.text(), self.targetEdit.text(), self.outputFileEdit.text())
        one.setup()
        selectedProperty = str(self.property.currentText())
        selectedMeasure = self.getAppropriateSimilarityMeasure()
        print(selectedProperty)
        print(selectedMeasure)
        threshold = round(self.doubleSpinBox_5.value(),2)
        print(threshold)
        if selectedProperty == "P102_has_title":
            one.function_comp_title(selectedMeasure, threshold, self.progressBar)
        elif selectedProperty == "P3_has_note":
            one.function_comp_note(selectedMeasure, threshold, self.progressBar)
        elif selectedProperty == "U12_has_genre":
            one.function_comp_genre(selectedMeasure, threshold, self.progressBar)
        elif selectedProperty == "U11_has_key":
            one.function_comp_key(selectedMeasure, threshold, self.progressBar)
        elif selectedProperty == "U13_has_casting":
            one.function_comp_casting(selectedMeasure, threshold, self.progressBar)
        elif selectedProperty == "U16_has_catalogue_statement":
            one.request_by_catalogue(selectedMeasure, threshold, self.progressBar)
        else:
            print("property selected unknown")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
