# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/UI/FrmInformation.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.Utils import _fromUtf8, _translate, _get_icon, _get_img
from Controller.config import VERSION, ABOUT_TEXT


class Ui_FrmInformation(QtCore.QObject):
    def setupUi(self, FrmInformation):
        # Icons
        icon = _get_icon("Images/satiedbfIcon.png")
        logo = _get_img("Images/logo.png")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FrmInformation.sizePolicy().hasHeightForWidth())

        FrmInformation.setWindowIcon(icon)
        FrmInformation.setIconSize(QtCore.QSize(40, 40))
        FrmInformation.setObjectName(_fromUtf8("FrmInformation"))
        FrmInformation.setFixedSize(660, 489)
        FrmInformation.setSizePolicy(sizePolicy)
        FrmInformation.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))

        # Deault Font conf
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        FrmInformation.setFont(font)
        FrmInformation.setStyleSheet("background:#eee;")

        # Logo
        self.labelImageLogo = QtWidgets.QLabel(FrmInformation)
        self.labelImageLogo.setGeometry(QtCore.QRect(10, 20, 135, 135))
        self.labelImageLogo.setStyleSheet("")
        self.labelImageLogo.setObjectName(_fromUtf8("labelImageLogo"))
        self.labelImageLogo.setPixmap(logo)
        self.labelImageLogo.show()

        # Title Of Page
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle = QtWidgets.QLabel(FrmInformation)
        self.labelTitle.setGeometry(QtCore.QRect(160, 20, 211, 21))
        self.labelTitle = QtWidgets.QLabel(FrmInformation)
        self.labelTitle.setGeometry(QtCore.QRect(160, 20, 211, 21))
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName(_fromUtf8("labelTitle"))

        # Version
        font.setPointSize(9)
        font.setBold(False)
        self.labelVersion = QtWidgets.QLabel(FrmInformation)
        self.labelVersion.setGeometry(QtCore.QRect(290, 40, 81, 16))
        self.labelVersion.setFont(font)
        self.labelVersion.setObjectName(_fromUtf8("labelVersion"))

        # Body License
        font.setPointSize(10)
        self.textBrowser = QtWidgets.QTextBrowser(FrmInformation)
        self.textBrowser.setGeometry(QtCore.QRect(160, 60, 491, 421))
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setStyleSheet("font-weight:400")
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(FrmInformation)
        QtCore.QMetaObject.connectSlotsByName(FrmInformation)

    def retranslateUi(self, FrmInformation):
        _translate = QtCore.QCoreApplication.translate
        FrmInformation.setWindowTitle(_translate("FrmInformation", "About"))
        self.labelTitle.setText(_translate("FrmInformation", "About Satie DBF Convert"))
        self.labelVersion.setText(_translate("FrmInformation", "Version {}".format(VERSION)))
        self.textBrowser.setHtml(_translate("FrmInformation", "{}".format(ABOUT_TEXT)))

#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    FrmInformation = QtWidgets.QDialog()
#    ui = Ui_FrmInformation()
#    ui.setupUi(FrmInformation)
#    FrmInformation.show()
#    sys.exit(app.exec_())
