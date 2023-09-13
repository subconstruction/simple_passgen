import random
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def generate_password(self):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        special_alphabet = ['!', '@', '#', '$', '%', '^', '&', '*', '№']
        output_string = ''
        output_value = ''

        pass_len = self.horizontalSlider.value()

        for i in range(pass_len):
                char_case = 'lower'

                if self.lowercase.isChecked() and self.uppercase.isChecked():
                     char_case = 'lower' if random.random()*10 > 5 else 'upper'
                elif not self.lowercase.isChecked() and self.uppercase.isChecked():
                     char_case = 'upper'

                number = random.randint(0, 9)
                char = alphabet[round(random.random()*(len(alphabet) - 1))].lower() if char_case == 'lower' else alphabet[round(random.random()*(len(alphabet) - 1))].upper()

                check = random.randint(0, 2)
                if check == 2:
                     output_value = str(number) if self.numbers.isChecked() and i %2 == 1 else char
                elif check == 1:
                     output_value = char
                elif check == 0:
                     output_value = special_alphabet[round(random.random()*(len(special_alphabet) - 1))] if self.symbols.isChecked() and i%2 == 0 else char
                     
                output_string = output_string + str(output_value)

        self.output_text.setText(output_string)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(479, 246)
        Dialog.setStyleSheet("background-color: rgb(70, 70, 106);")
        self.output_text = QtWidgets.QLabel(Dialog)
        self.output_text.setGeometry(QtCore.QRect(10, 10, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Museo Sans Cyrl 500")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.output_text.setFont(font)
        self.output_text.setStyleSheet("border-radius: 4px;\n"
"background-color:  rgb(45, 45, 68);\n"
"color: rgb(226, 226, 226);")
        self.output_text.setText("")
        self.output_text.setObjectName("output_text")
        self.customize = QtWidgets.QLabel(Dialog)
        self.customize.setGeometry(QtCore.QRect(10, 92, 461, 141))
        font = QtGui.QFont()
        font.setFamily("Museo Sans Cyrl 900")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.customize.setFont(font)
        self.customize.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.customize.setAcceptDrops(False)
        self.customize.setStatusTip("")
        self.customize.setWhatsThis("")
        self.customize.setAccessibleName("")
        self.customize.setStyleSheet("border-radius: 4px;\n"
"color: rgb(235, 235, 235);")
        self.customize.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.customize.setIndent(0)
        self.customize.setObjectName("customize")
        self.uppercase = QtWidgets.QCheckBox(Dialog)
        self.uppercase.setGeometry(QtCore.QRect(330, 130, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Museo Sans Cyrl 700")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.uppercase.setFont(font)
        self.uppercase.setStyleSheet("QCheckBox {\n"
"    padding: 2px;\n"
"    color: rgb(235, 235, 235);\n"
"    \n"
"    font: 63 12pt \"Museo Sans Cyrl 700\";\n"
"}\n"
"QCheckBox:disabled, QRadioButton:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/object-select-symbolic.symbolic.png);\n"
"    height: 15px;\n"
"    width: 15px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #48a5fd;\n"
"    color: #ffffff;\n"
"    border-radius: 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #48a5fd, stop:0.5 #329cfb, stop:1 #48a5fd);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    \n"
"    height: 15px;\n"
"    width: 15px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #48a5fd;\n"
"    border-radius: 3px;\n"
"    background-color: #fbfdfa;\n"
"}\n"
"\n"
"")
        self.uppercase.setObjectName("uppercase")
        self.generate_btn = QtWidgets.QPushButton(Dialog)
        self.generate_btn.setGeometry(QtCore.QRect(30, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Museo Sans Cyrl 700")
        font.setPointSize(10)
        self.generate_btn.setFont(font)
        self.generate_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    border-color: #39305f;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #39305f;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-color: #39305f;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    background-color: #39305f;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-width: 2px;\n"
"    border-radius: 1px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-width: 2px;\n"
"    border-radius: 1px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"}")
        self.generate_btn.setObjectName("generate_btn")
        self.export_btn = QtWidgets.QPushButton(Dialog)
        self.export_btn.setGeometry(QtCore.QRect(120, 190, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Museo Sans Cyrl 700")
        font.setPointSize(10)
        self.export_btn.setFont(font)
        self.export_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    border-color: #39305f;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #39305f;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-color: #39305f;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    background-color: #39305f;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-width: 2px;\n"
"    border-radius: 1px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-width: 2px;\n"
"    border-radius: 1px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"}")
        self.export_btn.setObjectName("export_btn")
        self.lowercase = QtWidgets.QCheckBox(Dialog)
        self.lowercase.setGeometry(QtCore.QRect(330, 150, 131, 21))
        self.lowercase.setStyleSheet("QCheckBox {\n"
"    padding: 2px;\n"
"    color: rgb(235, 235, 235);\n"
"    \n"
"    font: 63 12pt \"Museo Sans Cyrl 700\";\n"
"}\n"
"QCheckBox:disabled, QRadioButton:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/object-select-symbolic.symbolic.png);\n"
"    height: 15px;\n"
"    width: 15px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #48a5fd;\n"
"    color: #ffffff;\n"
"    border-radius: 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #48a5fd, stop:0.5 #329cfb, stop:1 #48a5fd);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    \n"
"    height: 15px;\n"
"    width: 15px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #48a5fd;\n"
"    border-radius: 3px;\n"
"    background-color: #fbfdfa;\n"
"}\n"
"\n"
"")
        self.lowercase.setObjectName("lowercase")
        self.numbers = QtWidgets.QCheckBox(Dialog)
        self.numbers.setGeometry(QtCore.QRect(330, 170, 131, 21))
        self.numbers.setStyleSheet("QCheckBox {\n"
"    padding: 2px;\n"
"    color: rgb(235, 235, 235);\n"
"    \n"
"    font: 63 12pt \"Museo Sans Cyrl 700\";\n"
"}\n"
"QCheckBox:disabled, QRadioButton:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/object-select-symbolic.symbolic.png);\n"
"    height: 15px;\n"
"    width: 15px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #48a5fd;\n"
"    color: #ffffff;\n"
"    border-radius: 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #48a5fd, stop:0.5 #329cfb, stop:1 #48a5fd);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    \n"
"    height: 15px;\n"
"    width: 15px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #48a5fd;\n"
"    border-radius: 3px;\n"
"    background-color: #fbfdfa;\n"
"}\n"
"\n"
"")
        self.numbers.setObjectName("numbers")
        self.symbols = QtWidgets.QCheckBox(Dialog)
        self.symbols.setGeometry(QtCore.QRect(330, 190, 131, 21))
        self.symbols.setStyleSheet("QCheckBox {\n"
"    padding: 2px;\n"
"    color: rgb(235, 235, 235);\n"
"    \n"
"    font: 63 12pt \"Museo Sans Cyrl 700\";\n"
"}\n"
"QCheckBox:disabled, QRadioButton:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/object-select-symbolic.symbolic.png);\n"
"    height: 15px;\n"
"    width: 15px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #48a5fd;\n"
"    color: #ffffff;\n"
"    border-radius: 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #48a5fd, stop:0.5 #329cfb, stop:1 #48a5fd);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    \n"
"    height: 15px;\n"
"    width: 15px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #48a5fd;\n"
"    border-radius: 3px;\n"
"    background-color: #fbfdfa;\n"
"}\n"
"\n"
"")
        self.symbols.setObjectName("symbols")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 150, 201, 22))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setMouseTracking(False)
        self.horizontalSlider.setTabletTracking(False)
        self.horizontalSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalSlider.setStyleSheet("QSlider::groove {\n"
"    background-color: rgb(255, 170, 0);\n"
"    border: 1px solid #bbbbbb;\n"
"    background-color: #52595d;\n"
"    border-radius: 4px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 6px;\n"
"    \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    max-height: 10px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled, QSlider::sub-page:horizontal:disabled, QSlider::add-page:vertical:disabled, QSlider::sub-page:vertical:disabled {\n"
"    background: #b9b9b9;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover, QScrollBar::handle:vertical:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);\n"
"}\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    border: 2px transparent grey;\n"
"    border-radius: 4px;\n"
"    subcontrol-origin: margin;\n"
"    background: #b9b9b9;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"    image: url(QSS_IMG/go-next-symbolic.symbolic.png);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-next-symbolic.symbolic.png);\n"
"}\n"
"")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.slider_value = QtWidgets.QLabel(Dialog)
        self.slider_value.setGeometry(QtCore.QRect(30, 150, 31, 21))
        self.slider_value.setStyleSheet("color: rgb(235, 235, 235);\n"
"border-radius: 4px;\n"
"background-color: rgb(45, 45, 68);\n"
"font: 63 11pt \"Museo Sans Cyrl 700\";")
        self.slider_value.setAlignment(QtCore.Qt.AlignCenter)
        self.slider_value.setObjectName("slider_value")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.uppercase.setChecked(True)
        self.lowercase.setChecked(True)
        self.numbers.setChecked(True)
        self.horizontalSlider.setValue(12)
        self.generate_password()
        
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password Generator"))
        self.customize.setText(_translate("Dialog", "Customize your password"))
        self.uppercase.setText(_translate("Dialog", "Uppercase"))
        self.generate_btn.setText(_translate("Dialog", "Generate"))
        self.export_btn.setText(_translate("Dialog", "Export"))
        self.lowercase.setText(_translate("Dialog", "Lowercase"))
        self.numbers.setText(_translate("Dialog", "Numbers"))
        self.symbols.setText(_translate("Dialog", "Symbols"))
        self.slider_value.setText(_translate("Dialog", "12"))
        self.export_btn.clicked.connect(lambda: pyperclip.copy(self.output_text.text()))
        self.generate_btn.clicked.connect(lambda: self.generate_password())
        self.horizontalSlider.valueChanged.connect(lambda: self.generate_password())
        self.horizontalSlider.valueChanged.connect(lambda: self.slider_value.setText(str(
             self.horizontalSlider.value()
        )))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
