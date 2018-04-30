# -*- coding: utf-8 -*-
import sys
from Controller.dbf2csv import Tocsv
from PyQt5 import QtCore
from View.FrmPrincipal import *

if len(sys.argv) > 1:
    print("Converting...")
    try:
        Tocsv(sys.argv[1])
        print("Done!")
    except Exception as e:
        print('Error: {}'.format(e))
    sys.exit(1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmPrincipal = QtWidgets.QMainWindow()
    ui = Ui_FrmPrincipal()
    ui.setupUi(FrmPrincipal)
    FrmPrincipal.show()
    sys.exit(app.exec_())
