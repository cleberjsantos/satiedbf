# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/UI/FrmPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from View.FrmInformation import Ui_FrmInformation
from Controller.Utils import _fromUtf8, _translate, resolve
from Controller.Utils import _get_icon, _get_img
from Controller.Utils import DBFRead
from Controller.dbf2csv import Tocsv
from Controller.Utils import pyqt_pdb
from Controller.config import ENCODING_SUPPORT
from Controller.dbfread.exceptions import MissingMemoFile
from datetime import date
import webbrowser


class Ui_FrmPrincipal(object):
    def __init__(self):
        super(Ui_FrmPrincipal, self).__init__()
        self.isChanged = False
        self.fileName = ""
        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None

    def dialog_msg(self, text='', icon='Information'):
        """ NoIcon, Question, Information, Warning, Critical """
        dlg = QtWidgets.QMessageBox()
        dlg.setText(text)
        dlg.setWindowTitle(icon)
        dlg.setIcon(resolve('PyQt5.QtWidgets.QMessageBox.{}'.format(icon)))
        dlg.exec_()

    def question_url(self):
        webbrowser.open_new_tab('http://www.dbase.com/KnowledgeBase/int/db7_file_fmt.htm')

    def FrmImport_Click(self):
        """ """
        if not self.groupBoxExport.isHidden():
            self.groupBoxExport.hide()

        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

        self.path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Import file", "", "DBF files (*.dbf)", options=options)

        if self.path:
            self.fileName = str(self.path.split('/')[-1])

            try:
                self.read_dbf = DBFRead(self.path,
                                        encoding=_fromUtf8(self.comboBoxEncoding.currentText()),
                                        ignore_missing_memofile=self.checkBoxMemofile.isChecked(),
                                        char_decode_errors='ignore')

                self.dbf = self.read_dbf.parseDBF()

                # todo load dbf to table grid
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

                for row_number, row_data in enumerate(self.dbf):
                    r_number = int(row_number)
                    self.tableWidget.insertRow(r_number)

                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setColumnCount(len(row_data))

                        # Header
                        self.tableWidget.setHorizontalHeaderItem(column_number,
                                                  QtWidgets.QTableWidgetItem(data))

                        rData = row_data[data]
                        if isinstance(row_data[data], date):
                            rData = str(row_data[data])

                        self.tableWidget.setItem(r_number, column_number,
                                                     QtWidgets.QTableWidgetItem(rData))
                # Do the resize of the columns by content
                self.tableWidget.resizeColumnsToContents()

                # Total entries
                totalEntries = str(self.read_dbf.meta_data['numrecords'])
                self.labelTotalDataValue.setText(totalEntries)
            except MissingMemoFile as e:
                self.dialog_msg(text=_fromUtf8('Missing memo file'),
                                icon='Critical')
            except Exception as e:
                self.dialog_msg(text=_fromUtf8(str(e)),
                                icon='Critical')

    def Show_ExpOpt(self):
        """ """
        self.groupBoxExport.show()

    def Convert_Csv(self):
        """ """
        if self.tableWidget.rowCount() < 1:
            self.dialog_msg(text=_fromUtf8('Missing Data'),
                            icon='Critical')
        else:
            if self.fileName.endswith('.dbf'):
                self.fileName = self.fileName.replace('.dbf',
                                                      '.csv')

            filePath, _ = QtWidgets.QFileDialog.getSaveFileName(None,
                                                                "Save File",
                                                                self.fileName,
                                                                "CSV Files (*.csv)")
            if filePath:
                self.header = []
                self.data = []
                columncount = range(self.tableWidget.columnCount())
                rowcount = range(self.tableWidget.rowCount())

                for c_item in columncount:
                    self.header.append(self.tableWidget.horizontalHeaderItem(c_item).text())

                for r_item in rowcount:
                    rowdata = []
                    for column in columncount:
                        item = self.tableWidget.item(r_item, column)
                        if item is not None:
                            rowdata.append(
                                _fromUtf8(item.text()))
                        else:
                            rowdata.append('')
                    self.data.append(rowdata)

                Tocsv(filePath, header=self.header, data=self.data)
                self.dialog_msg(text=_fromUtf8('CSV exported!'))

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
        iconCsv = _get_icon("Images/csv.png")
        iconPdf = _get_icon("Images/pdf.png")
        iconInfo = _get_icon("Images/info.png")
        iconQuestion = _get_icon("Images/question.png")

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

        # Default Font conf
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
        self.btnImport.setIconSize(QtCore.QSize(40, 40))
        self.btnImport.setObjectName(_fromUtf8("btnImport"))
        # Btn Import Click Event
        self.btnImport.clicked.connect(self.FrmImport_Click)

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
        self.btnExport.setIconSize(QtCore.QSize(40, 40))
        self.btnExport.setShortcut("")
        self.btnExport.setObjectName(_fromUtf8("btnExport"))
        # Btn Export Click Event
        self.btnExport.clicked.connect(self.Show_ExpOpt)

        font.setPointSize(10)
        # Export Actions
        self.groupBoxExport = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxExport.setEnabled(True)
        self.groupBoxExport.setFont(font)
        self.groupBoxExport.setGeometry(QtCore.QRect(370, 20, 221, 81))
        self.groupBoxExport.setStyleSheet("QGroupBox{\n"
                                          "  background-color: transparent;\n"
                                          "  background-clip: margin;\n"
                                          "  border: 1px solid #777;\n"
                                          "  border-radius: 4px;\n"
                                          "  margin-top: 10px;\n"
                                          "  padding-top: 4px;}\n"
                                          "QGroupBox::title{\n"
                                          "  padding: 2px 8px;\n"
                                          "  subcontrol-origin: margin;\n"
                                          "  subcontrol-position: top center;\n"
                                          "  color: #555;}\n")
        self.groupBoxExport.setObjectName(_fromUtf8("groupBoxExport"))

        # Default is Hide
        if not self.groupBoxExport.isHidden():
            self.groupBoxExport.hide()

        # Bnt CSV
        self.btnExpCSV = QtWidgets.QPushButton(self.groupBoxExport)
        self.btnExpCSV.setGeometry(QtCore.QRect(20, 20, 82, 51))
        self.btnExpCSV.setStyleSheet("border: 1px solid #8f8f91;\n"
                                     "border-radius: 6px;\n"
                                     "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                     "min-width: 80px;\n")
        self.btnExpCSV.setText("")
        self.btnExpCSV.setIcon(iconCsv)
        self.btnExpCSV.setIconSize(QtCore.QSize(40, 40))
        self.btnExpCSV.setObjectName(_fromUtf8("btnExpCSV"))
        # Btn Export CSV Click Event
        self.btnExpCSV.clicked.connect(self.Convert_Csv)

        # Bnt PDF
        self.btnExpPDF = QtWidgets.QPushButton(self.groupBoxExport)
        self.btnExpPDF.setGeometry(QtCore.QRect(120, 20, 82, 51))
        self.btnExpPDF.setStyleSheet("border: 1px solid #8f8f91;\n"
                                     "border-radius: 6px;\n"
                                     "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                     "min-width: 80px;")
        self.btnExpPDF.setText("")
        self.btnExpPDF.setIcon(iconPdf)
        self.btnExpPDF.setIconSize(QtCore.QSize(40, 40))
        self.btnExpPDF.setObjectName(_fromUtf8("btnExpPDF"))

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
        self.btnInfo.setObjectName(_fromUtf8("btnInfo"))
        # Btn Info Click Event
        self.btnInfo.clicked.connect(self.FrmInformation_Click)

        # Column for Import/Export and Information Bnts
        font.setPointSize(12)
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(10, 10, 779, 101))
        self.columnView.setStyleSheet("background:#fff")
        self.columnView.setObjectName(_fromUtf8("columnView"))

        # Dbf Text
        self.labelDbfText = QtWidgets.QLabel(self.centralwidget)
        self.labelDbfText.setGeometry(QtCore.QRect(10, 190, 200, 19))
        self.labelDbfText.setFont(font)
        self.labelDbfText.setStyleSheet("")
        self.labelDbfText.setObjectName(_fromUtf8("labelDbfText"))

        font.setPointSize(10)

        # GroupBox import options
        self.groupBoxImport = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxImport.setGeometry(QtCore.QRect(230, 130, 561, 80))
        self.groupBoxImport.setFont(font)
        self.groupBoxImport.setStyleSheet("QGroupBox {\n"
                                          "  background-color: transparent;\n"
                                          "  background-clip: margin;\n"
                                          "  border: 1px solid #777;\n"
                                          "  border-radius: 4px;\n"
                                          "  margin-top: 10px;\n"
                                          "  padding-top: 4px; }\n\n"
                                          "QGroupBox::title {\n"
                                          "  padding: 2px 8px;\n"
                                          "  subcontrol-origin: margin;\n"
                                          "  subcontrol-position: top center;\n"
                                          "  color: #555;}\n\n"
                                          "")
        self.groupBoxImport.setObjectName(_fromUtf8("groupBoxImport"))

        self.checkBoxMemofile = QtWidgets.QCheckBox(self.groupBoxImport)
        self.checkBoxMemofile.setGeometry(QtCore.QRect(20, 40, 181, 20))
        self.checkBoxMemofile.setFont(font)
        self.checkBoxMemofile.setStyleSheet("")
        self.checkBoxMemofile.setChecked(True)
        self.checkBoxMemofile.setObjectName(_fromUtf8("checkBoxMemofile"))

        self.labelQuestionMemofile = QtWidgets.QPushButton(self.groupBoxImport)
        self.labelQuestionMemofile.setGeometry(QtCore.QRect(190, 43, 16, 16))
        self.labelQuestionMemofile.setFont(font)
        self.labelQuestionMemofile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.labelQuestionMemofile.setWhatsThis("")
        self.labelQuestionMemofile.setAccessibleDescription("")
        self.labelQuestionMemofile.setText("")
        self.labelQuestionMemofile.setIcon(iconQuestion)
        self.labelQuestionMemofile.setIconSize(QtCore.QSize(16, 16))
        self.labelQuestionMemofile.setStyleSheet("QPushButton {   background-color: transparent; border: none; }")
        self.labelQuestionMemofile.setObjectName(_fromUtf8("labelQuestionMemofile"))
        # Action to Label Questin clickable
        self.labelQuestionMemofile.clicked.connect(self.question_url)

        self.labelEncoding = QtWidgets.QLabel(self.groupBoxImport)
        self.labelEncoding.setGeometry(QtCore.QRect(290, 30, 71, 16))
        self.labelEncoding.setFont(font)
        self.labelEncoding.setObjectName(_fromUtf8("labelEncoding"))

        self.comboBoxEncoding = QtWidgets.QComboBox(self.groupBoxImport)
        self.comboBoxEncoding.setGeometry(QtCore.QRect(290, 50, 101, 22))
        self.comboBoxEncoding.setFont(font)
        self.comboBoxEncoding.setObjectName("comboBoxEncoding")
        self.comboBoxEncoding.setStyleSheet("QComboBox {\n"
                                            "    border: 1px solid #8f8f91;\n"
                                            "    border-radius: 3px;\n"
                                            "    padding: 1px 18px 1px 3px;\n"
                                            "    min-width: 6em;}\n"
                                            "QComboBox:editable {\n"
                                            "    background: white;}\n"
                                            "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                            "     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                            "                                 stop: 0 #f6f7fa, \n"
                                            "                                 stop: 1 #dadbde);\n"
                                            "     color: #000;}\n"
                                            "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
                                            "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                            "                                stop: 0 #E1F5A9,\n"
                                            "                                stop: 1 #cedf9a);}\n"
                                            "QComboBox:on {\n"
                                            "    padding-top: 3px;\n"
                                            "    padding-left: 4px;}\n"
                                            "QComboBox::drop-down {\n"
                                            "    subcontrol-origin: padding;\n"
                                            "    subcontrol-position: top right;\n"
                                            "    width: 15px;\n"
                                            "    border-left-width: 1px;\n"
                                            "    border-left-color: darkgray;\n"
                                            "    border-left-style: solid;\n"
                                            "    border-top-right-radius: 3px;\n"
                                            "    border-bottom-right-radius: 3px;}\n"
                                            "QComboBox::down-arrow {\n"
                                            "    image: url(Images/downarrow.png);}\n"
                                            "QComboBox::down-arrow:on {\n"
                                            "    top: 1px;\n"
                                            "    left: 1px;}\n")
        for cb_i, cb_v in enumerate(ENCODING_SUPPORT):
            self.comboBoxEncoding.addItem("")
            self.comboBoxEncoding.setItemText(cb_i, _fromUtf8(cb_v))

        # Table GridView for DBF load
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
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))

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
        self.labelTotalData.setObjectName(_fromUtf8("labelTotalData"))
        self.labelTotalDataValue = QtWidgets.QLabel(self.centralwidget)
        self.labelTotalDataValue.setGeometry(QtCore.QRect(120, 560, 80, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTotalDataValue.sizePolicy().hasHeightForWidth())
        self.labelTotalDataValue.setSizePolicy(sizePolicy)
        self.labelTotalDataValue.setObjectName(_fromUtf8("labelTotalDataValue"))

        self.columnView.raise_()
        self.btnImport.raise_()
        self.btnExport.raise_()
        self.groupBoxExport.raise_()
        self.btnInfo.raise_()
        self.labelDbfText.raise_()
        self.groupBoxImport.raise_()
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
        self.groupBoxImport.setTitle(_translate("FrmPrincipal", "Import options"))
        self.checkBoxMemofile.setText(_translate("FrmPrincipal", "ignore missing memofile"))
        self.labelEncoding.setText(_translate("FrmPrincipal", "Encoding"))
        self.groupBoxExport.setTitle(_translate("FrmPrincipal", "Export To"))
        self.tableWidget.setSortingEnabled(True)
        self.labelTotalData.setText(_translate("FrmPrincipal", "Total data"))
        self.labelTotalDataValue.setText(_translate("FrmPrincipal", "0"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    FrmPrincipal = QtWidgets.QMainWindow()
#    ui = Ui_FrmPrincipal()
#    ui.setupUi(FrmPrincipal)
#    FrmPrincipal.show()
#    sys.exit(app.exec_())
