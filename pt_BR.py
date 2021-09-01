
def ptBrTraduction(self):
    # wdw_Main_Window
    self.lbl_Entrace.setText("Entrada de Dados:")
    self.Cbx_Entrace.setItemText(0, "Seções Convencionais")
    self.Cbx_Entrace.setItemText(1, "Seções por Pontos")

    # menubar
    self.Mnb_Manual.setTitle("Manual de Utilização")
    self.Mnb_Configs.setTitle("Configurações")
    self.Qmn_language.setTitle("Idioma")
    self.Qac_ptBR.setText("Português Brasileiro")
    self.Qac_enUS.setText("English")
    self.Qac_esES.setText("Español")
    self.Qmn_Theme.setTitle("Tema")
    self.Qac_light_theme.setText("Tema Claro")
    self.Qac_dark_theme.setText("Tema Escuro")

    # gbr_SectionPoints
    self.gbr_SectionPoints.setTitle("Seção por pontos")
    # Labels
    self.lbl_PointX.setText("Coordenada X:")
    self.lbl_PointY.setText("Coordenada Y:")
    # Buttons
    self.btn_AddItem.setText("Add Item")
    self.btn_DeleteItem.setText("Delete Item")
    self.btn_ClearItem.setText("Limpar lista")
    self.btn_Finalized.setText("Finalizado")

    # gbr_View_Section
    self.gbr_View_Section.setTitle("Seção Visualizada")
    # labels

    # gbr_ConventionalSections
    self.gbr_ConventionalSections.setTitle("Seções Convencionais")
    # labels
    self.lbl_SectionDetermination.setText("Defina o formato da Seção:")
    self.lbl_bf.setText("bf:")
    self.lbl_hf.setText("hf:")
    self.lbl_bw.setText("bw:")
    self.lbl_hw.setText("hw:")
    # buttons
    self.btn_Conventional.setText("Prosseguir!")

    # gbr_Geometrics_Properties
    self.gbr_Geometrics_Properties.setTitle("Propriedades Geométricas")
    # labels
    self.lbl_Area.setText("Área:")
    self.lbl_FirstOrderMomentX.setText("Primeiro Momento de X:")
    self.lbl_FirstOrderMomentY.setText("Primeiro Momento de Y:")
    self.lbl_SecondOrderMomentX.setText("Segundo Momento de X:")
    self.lbl_SecondOrderMomentY.setText("Segundo Momento de Y:")
    self.lbl_InertiaProduct.setText("Produto de Inércia XY:")
    self.lbl_InertiaCenterX.setText("Centro de Inércia X:")
    self.lbl_InertiaCenterY.setText("Centro de Inércia Y:")
    self.lbl_RotationRadiusCenterX.setText("Raio de giração X:")
    self.lbl_RotationRadiusCenterY.setText("Raio de Giração Y:")
    self.lbl_TranslatedInertiaX.setText("Inércia Transladada em X:")
    self.lbl_TranslatedInertiaY.setText("Inércia Transladada em Y:")
    self.lbl_TranslatedInertiaXY.setText("Inércia Transladada em XY:")
    self.lbl_AngleDg.setText("Ângulo de rotação (°):")
    self.lbl_MainInertiaX.setText("Inércia Principal em X:")
    self.lbl_MainInertiaY.setText("Inércia Principal em Y:")

    with open('GPY.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    linhas[0] = "language = pt_BR\n"
    with open('GPY.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
    arquivo.close()