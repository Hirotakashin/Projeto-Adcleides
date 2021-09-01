def enUSTraduction(self):
    # wdw_Main_Window
    self.lbl_Entrace.setText("Data Input:")
    self.Cbx_Entrace.setItemText(0, "Conventional Sections")
    self.Cbx_Entrace.setItemText(1, "Sections by Points")

    # menubar
    self.Mnb_Manual.setTitle("User's Manual")
    self.Mnb_Configs.setTitle("Configurations")
    self.Qmn_language.setTitle("Language")
    self.Qac_ptBR.setText("Português Brasileiro")
    self.Qac_enUS.setText("English")
    self.Qac_esES.setText("Español")
    self.Qmn_Theme.setTitle("Theme")
    self.Qac_light_theme.setText("Light Theme")
    self.Qac_dark_theme.setText("Dark Theme")

    # gbr_SectionPoints
    self.gbr_SectionPoints.setTitle("Section by Points")
    # Labels
    self.lbl_PointX.setText("X coordinate:")
    self.lbl_PointY.setText("Y coordinate:")
    # Buttons
    self.btn_AddItem.setText("Add Item")
    self.btn_DeleteItem.setText("Delete Item")
    self.btn_ClearItem.setText("Clear")
    self.btn_Finalized.setText("Finished")

    # gbr_View_Section
    self.gbr_View_Section.setTitle("Section Viewed")
    # labels

    # gbr_ConventionalSections
    self.gbr_ConventionalSections.setTitle("Convencionail Sections")
    # labels
    self.lbl_SectionDetermination.setText("Define Section Format:")
    self.lbl_bf.setText("bf:")
    self.lbl_hf.setText("hf:")
    self.lbl_bw.setText("bw:")
    self.lbl_hw.setText("hw:")
    # buttons
    self.btn_Conventional.setText("Proceed!")

    # gbr_Geometrics_Properties
    self.gbr_Geometrics_Properties.setTitle("Geometric Properties")
    # labels
    self.lbl_Area.setText("Area:")
    self.lbl_FirstOrderMomentX.setText("First X-Axis Moment:")
    self.lbl_FirstOrderMomentY.setText("First Y-Axis Moment:")
    self.lbl_SecondOrderMomentX.setText("Second X-Axis Moment:")
    self.lbl_SecondOrderMomentY.setText("Second Y-Axis Moment:")
    self.lbl_InertiaProduct.setText("XY Inertia Product:")
    self.lbl_InertiaCenterX.setText("Inertia Center X-Axis:")
    self.lbl_InertiaCenterY.setText("Inertia Center Y-Axis:")
    self.lbl_RotationRadiusCenterX.setText("X-axis radius of rotation:")
    self.lbl_RotationRadiusCenterY.setText("Y-axis radius of rotation:")
    self.lbl_TranslatedInertiaX.setText("Translated Inertia X-axis:")
    self.lbl_TranslatedInertiaY.setText("Translated Inertia Y-axis:")
    self.lbl_TranslatedInertiaXY.setText("Translated Inertia XY-axis:")
    self.lbl_AngleDg.setText("Rotation Angle (°):")
    self.lbl_MainInertiaX.setText("Main inertia X axis:")
    self.lbl_MainInertiaY.setText("Main inertia Y axis:")

    with open('GPY.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    linhas[0] = "language = en_US\n"
    with open('GPY.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
    arquivo.close()