from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from qdarkstyle import *

import Entrada_Dados_Prop_Mec as epp
import en_US
import pt_BR


class UIteste(QMainWindow):
    def __init__(self):
        super(UIteste, self).__init__()
        uic.loadUi("UIteste.ui", self)

        self.initLanguage()

        self.Qac_enUS.triggered.connect(lambda: en_US.enUSTraduction(self))
        self.Qac_ptBR.triggered.connect(lambda: pt_BR.ptBrTraduction(self))

        # Active e inative in __init__()
        self.gbr_ConventionalSections.setEnabled(False)
        self.gbr_SectionPoints.setEnabled(False)

        self.Cbx_Entrace.currentIndexChanged.connect(self.cbx_Entrace_Change)

        # gbr_SectionPoints buttons
        self.btn_AddItem.clicked.connect(self.Add_elements)

        self.btn_DeleteItem.clicked.connect(self.Remove_element)

        self.btn_ClearItem.clicked.connect(self.Clear_list)

        self.btn_Finalized.clicked.connect(self.Finalized)

    # Funções para Os botões de gbr_sectionPoints
    row_count = 0

    def Add_elements(self):
        DadoX = self.let_PointX.text()
        DadoY = self.let_PointY.text()
        self.row_count += 1

        epp.Calculo_Peca(DadoX, DadoY)
        self.ltw_Points.addItem(f"Ponto {self.row_count}: ({DadoX}, {DadoY})")

        self.let_PointX.setText("")
        self.let_PointY.setText("")

    def Remove_element(self):
        self.ltw_Points.takeItem(self.ltw_Points.currentRow())
        self.row_count -= 1
        epp.remove_element()

    def Clear_list(self):
        self.ltw_Points.clear()
        self.row_count = 0
        epp.Clear_list()

    def Finalized(self):
        print(self.row_count)

        epp.Calculos_Points(self, self.row_count, epp.Lista_X, epp.Lista_Y)
        epp.Show_Image(epp.Lista_X, epp.Lista_Y)

        pixmap = QPixmap("section.png")
        self.lbl_image_viewSection.setPixmap(pixmap)

    def initLanguage(self):
        with open('GPY.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        print(linhas)
        if linhas[0] == "language = pt_BR\n":
            pt_BR.ptBrTraduction(self)
        elif linhas[0] == "language = en_US\n":
            en_US.enUSTraduction(self)

    # Cbx_Entrace
    def cbx_Entrace_Change(self):
        if self.Cbx_Entrace.currentIndex() == 0:
            self.gbr_ConventionalSections.setEnabled(True)
            self.gbr_SectionPoints.setEnabled(False)
        elif self.Cbx_Entrace.currentIndex() == 1:
            self.gbr_SectionPoints.setEnabled(True)
            self.gbr_ConventionalSections.setEnabled(False)


# main
app = QApplication(sys.argv)
welcome = UIteste()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setWindowTitle("Propriedades Geométricas - Alpha 1")
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("")
