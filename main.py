from PyQt5 import QtCore, QtGui, QtWidgets
from convertiseur import Ui_MainWindow


def convertir():
    devisereup = ui.devise.text()
    montantrecup = int(ui.montant.text())
    facteur_euro = 655
    if devisereup.upper() == 'E':
        ui.resultat.setText("%f Cfa" %(montantrecup * facteur_euro))
    elif devisereup.upper() == 'CFA':
        ui.resultat.setText("%f Euros"% (montantrecup / facteur_euro))
    else:
        ui.resultat.setText("Il faut entrer Cfa ou E")        







import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ui.btn_convertir.clicked.connect(convertir)
sys.exit(app.exec_())
