# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/UI/FrmPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.Utils import _fromUtf8, _translate, _get_icon
from View.FrmInformation import Ui_FrmInformation


class Ui_FrmPrincipal(object):
    def FrmInformation_Click(self):
        """ """
        self.frmInformation = QtWidgets.QMainWindow()
        self.ui = Ui_FrmInformation()
        self.ui.setupUi(self.frmInformation)
        self.frmInformation.show()

    def setupUi(self, FrmPrincipal):
        # Icons
        icon = _get_icon("Images/satiedbfIcon.png")
        iconImport = _get_icon("Images/import.png")
        iconExport = _get_icon("Images/export.png")
        iconInfo = _get_icon("Images/info.png")

        # Initial Window config
        FrmPrincipal.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        FrmPrincipal.setWindowIcon(icon)
        FrmPrincipal.setIconSize(QtCore.QSize(40, 40))
        FrmPrincipal.setObjectName(_fromUtf8("FrmPrincipal"))
        FrmPrincipal.setWindowModality(QtCore.Qt.NonModal)
        FrmPrincipal.setFixedSize(801, 592)  # No resize Window
        FrmPrincipal.setAutoFillBackground(True)
        FrmPrincipal.setAcceptDrops(False)
        FrmPrincipal.setStyleSheet("background-color: #eee;")

        # Deault Font conf
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)

        self.centralwidget = QtWidgets.QWidget(FrmPrincipal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        # Bnt Import
        self.btnImport = QtWidgets.QPushButton(self.centralwidget)
        self.btnImport.setGeometry(QtCore.QRect(20, 20, 131, 81))
        self.btnImport.setFont(font)
        self.btnImport.setStyleSheet("border: 1px solid #8f8f91;\n"
                                     "border-radius: 6px;\n"
                                     "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                     "min-width: 80px;\n"
                                     "")
        self.btnImport.setIcon(iconImport)
        self.btnImport.setIconSize(QtCore.QSize(30, 30))
        self.btnImport.setObjectName("btnImport")

        # Btn Export
        self.btnExport = QtWidgets.QPushButton(self.centralwidget)
        self.btnExport.setGeometry(QtCore.QRect(170, 20, 131, 81))
        self.btnExport.setFont(font)
        self.btnExport.setStyleSheet("border: 1px solid #8f8f91;\n"
                                     "border-radius: 6px;\n"
                                     "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                     "min-width: 80px;\n"
                                     "")
        self.btnExport.setIcon(iconExport)
        self.btnExport.setIconSize(QtCore.QSize(30, 30))
        self.btnExport.setShortcut("")
        self.btnExport.setObjectName("btnExport")

        # Bnt Information
        self.btnInfo = QtWidgets.QPushButton(self.centralwidget)
        self.btnInfo.setGeometry(QtCore.QRect(650, 20, 131, 81))
        self.btnInfo.setFont(font)
        self.btnInfo.setStyleSheet("border: 1px solid #73AD21;\n"
                                   "border-radius: 6px;\n"
                                   "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1F5A9, stop: 1 #cedf9a);\n"
                                   "min-width: 80px;\n"
                                   "")
        self.btnInfo.setIcon(iconInfo)
        self.btnInfo.setIconSize(QtCore.QSize(30, 30))
        self.btnInfo.setShortcut("")
        self.btnInfo.setObjectName("btnInfo")
        # Btn Info Click Event
        self.btnInfo.clicked.connect(self.FrmInformation_Click)

        # Column for Import/Export and Information Bnts
        font.setPointSize(12)
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(10, 10, 779, 101))
        self.columnView.setStyleSheet("background:#fff")
        self.columnView.setObjectName("columnView")

        self.labelDbfText = QtWidgets.QLabel(self.centralwidget)
        self.labelDbfText.setGeometry(QtCore.QRect(10, 190, 779, 19))
        self.labelDbfText.setFont(font)
        self.labelDbfText.setStyleSheet("")
        self.labelDbfText.setObjectName("labelDbfText")


        # Table GridView for DBF load
        font.setPointSize(10)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 220, 779, 334))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: #E1F5A9;\n"
                                       "selection-color: #ccc;\n"
                                       "")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")

        self.labelTotalData = QtWidgets.QLabel(self.centralwidget)
        self.labelTotalData.setGeometry(QtCore.QRect(10, 560, 89, 14))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTotalData.sizePolicy().hasHeightForWidth())
        self.labelTotalData.setSizePolicy(sizePolicy)
        self.labelTotalData.setFont(font)
        self.labelTotalData.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelTotalData.setTextFormat(QtCore.Qt.RichText)
        self.labelTotalData.setScaledContents(False)
        self.labelTotalData.setObjectName("labelTotalData")
        self.labelTotalDataValue = QtWidgets.QLabel(self.centralwidget)
        self.labelTotalDataValue.setGeometry(QtCore.QRect(120, 560, 41, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTotalDataValue.sizePolicy().hasHeightForWidth())
        self.labelTotalDataValue.setSizePolicy(sizePolicy)
        self.labelTotalDataValue.setObjectName("labelTotalDataValue")

        self.columnView.raise_()
        self.btnImport.raise_()
        self.btnExport.raise_()
        self.btnInfo.raise_()
        self.labelDbfText.raise_()
        self.tableWidget.raise_()
        self.labelTotalData.raise_()
        self.labelTotalDataValue.raise_()
        FrmPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmPrincipal)
        QtCore.QMetaObject.connectSlotsByName(FrmPrincipal)

    def retranslateUi(self, FrmPrincipal):
        _translate = QtCore.QCoreApplication.translate
        FrmPrincipal.setWindowTitle(_translate("FrmPrincipal", "Satie DBF Convert"))
        self.btnImport.setText(_translate("FrmPrincipal", "Import"))
        self.btnExport.setText(_translate("FrmPrincipal", "Export"))
        self.btnInfo.setText(_translate("FrmPrincipal", "About"))
        self.labelDbfText.setText(_translate("FrmPrincipal", "DBF Visualization"))
        self.tableWidget.setSortingEnabled(True)
        self.labelTotalData.setText(_translate("FrmPrincipal", "Total data"))
        self.labelTotalDataValue.setText(_translate("FrmPrincipal", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmPrincipal = QtWidgets.QMainWindow()
    ui = Ui_FrmPrincipal()
    ui.setupUi(FrmPrincipal)
    FrmPrincipal.show()
    sys.exit(app.exec_())
