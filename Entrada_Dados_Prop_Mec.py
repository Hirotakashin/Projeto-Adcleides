import math
import matplotlib.pyplot as plt

Lista_X = []
Lista_Y = []

Area = 0
PrimeiroMomAreaX = 0
PrimeiroMomAreaY = 0
SegundoMomAreaY = 0
SegundoMomAreaX = 0
ProdInerciaSecao = 0
Centro_Inercia_X = 0
Centro_Inercia_Y = 0
Raio_Giracao_X = 0
Raio_Giracao_Y = 0
Inercia_Transladada_X = 0
Inercia_Transladada_Y = 0
Inercia_Transladada_XY = 0
Angulo_dg = 0
Inercia_Principal_X = 0
Inercia_Principal_Y = 0


def Calculo_Peca(DadoX, DadoY):
    if isnumber(DadoX) and isnumber(DadoY):
        X = float(DadoX)
        Y = float(DadoY)
        Lista_X.append(X)
        Lista_Y.append(Y)
        print("add")
        print(Lista_X)
        print(Lista_Y)
        return Lista_X, Lista_Y


def remove_element():
    Lista_X.pop()
    Lista_Y.pop()
    print("rem")
    print(Lista_X)
    print(Lista_Y)
    return Lista_X, Lista_Y


def Clear_list():
    Lista_X = []
    Lista_Y = []
    print("clr")
    print(Lista_X)
    print(Lista_Y)
    return Lista_X, Lista_Y


def Calculos_Points(self, Num_Vertices, Lista_X, Lista_Y):
    global Area, PrimeiroMomAreaX, PrimeiroMomAreaY, SegundoMomAreaY, SegundoMomAreaX, ProdInerciaSecao, \
        Raio_Giracao_X, Raio_Giracao_Y, Centro_Inercia_X, Centro_Inercia_Y, Inercia_Transladada_X, Inercia_Transladada_Y, \
        Inercia_Transladada_XY, Angulo_dg, Inercia_Principal_X, Inercia_Principal_Y

    for i in range(0, Num_Vertices):
        # Calculo de Área
        iteravel = (Lista_X[i - 1] * Lista_Y[i]) - (Lista_Y[i - 1] * Lista_X[i])
        Area = (1 / 2) * iteravel + Area

        # Momento de Primeira Ordem
        PrimeiroMomAreaY = (1 / 6) * iteravel * (Lista_X[i - 1] + Lista_X[i]) + PrimeiroMomAreaY
        PrimeiroMomAreaX = (1 / 6) * iteravel * (Lista_Y[i - 1] + Lista_Y[i]) + PrimeiroMomAreaX

        # Momento de Segunda Ordem
        SegundoMomAreaY = (1 / 12) * iteravel * ((Lista_X[i - 1] ** 2) + (Lista_X[i - 1] * Lista_X[i])
                                                 + (Lista_X[i] ** 2)) + SegundoMomAreaY
        SegundoMomAreaX = (1 / 12) * iteravel * ((Lista_Y[i - 1] ** 2) + (Lista_Y[i - 1] * Lista_Y[i])
                                                 + (Lista_Y[i] ** 2)) + SegundoMomAreaX

        # Produto de Inercia da Seção
        ProdInerciaSecao = (1 / 24) * iteravel * (2 * Lista_X[i - 1] * Lista_Y[i - 1] + (Lista_X[i - 1] * Lista_Y[i])
                                                  + (Lista_X[i] * Lista_Y[i - 1])
                                                  + 2 * Lista_X[i] * Lista_Y[i]) + ProdInerciaSecao
    Area = abs(Area)

    Centro_Inercia_X = PrimeiroMomAreaY / Area

    Centro_Inercia_Y = PrimeiroMomAreaX / Area

    Raio_Giracao_X = math.sqrt(abs(SegundoMomAreaX) / Area)

    Raio_Giracao_Y = math.sqrt(abs(SegundoMomAreaY) / Area)

    # Transladar Propriedades para os Eixos Centroidais e Determinação da Seção Principal
    Inercia_Transladada_X = SegundoMomAreaX - Area * (Centro_Inercia_Y ** 2)

    Inercia_Transladada_Y = SegundoMomAreaY - Area * (Centro_Inercia_X ** 2)

    Inercia_Transladada_XY = ProdInerciaSecao - Area * Centro_Inercia_X * Centro_Inercia_Y

    # Angulos
    try:
        Angulo_rad = (1 / 2) * math.atan(2 * (Inercia_Transladada_XY / (Inercia_Transladada_Y - Inercia_Transladada_X)))
    except:
        if Inercia_Transladada_XY == 0:
            Angulo_rad = 0
        else:
            Angulo_rad = math.pi / 2

    Angulo_dg = Angulo_rad * (180 / math.pi)

    # InerciasPrincipais
    Inercia_Principal_X = Inercia_Transladada_Y * (math.sin(Angulo_rad)) ** 2 - 2 * math.sin(Angulo_rad) * math.cos(
        Angulo_rad) \
                          + Inercia_Transladada_X * (math.cos(Angulo_rad)) ** 2

    Inercia_Principal_Y = Inercia_Transladada_Y * (math.cos(Angulo_rad)) ** 2 - 2 * math.sin(Angulo_rad) * math.cos(
        Angulo_rad) \
                          + Inercia_Transladada_X * (math.sin(Angulo_rad)) ** 2

    self.let_area.setText(str(Area.__round__(4)))
    self.let_FirstOrderMomentX.setText(str(PrimeiroMomAreaX.__round__(4)))
    self.let_FirstOrderMomentY.setText(str(PrimeiroMomAreaY.__round__(4)))
    self.let_SecondOrderMomentX.setText(str(SegundoMomAreaX.__round__(4)))
    self.let_SecondOrderMomentY.setText(str(SegundoMomAreaY.__round__(4)))
    self.let_InertiaProduct.setText(str(ProdInerciaSecao.__round__(4)))
    self.let_InertiaCenterX.setText(str(Centro_Inercia_X.__round__(4)))
    self.let_InertiaCenterY.setText(str(Centro_Inercia_Y.__round__(4)))
    self.let_RotationRadiusCenterX.setText(str(Raio_Giracao_X.__round__(4)))
    self.let_RotationRadiusCenterY.setText(str(Raio_Giracao_Y.__round__(4)))
    self.let_TranslatedIertiaX.setText(str(Inercia_Transladada_X.__round__(4)))
    self.let_TranslatedIertiaY.setText(str(Inercia_Transladada_Y.__round__(4)))
    self.let_TranslatedIertiaXY.setText(str(Inercia_Transladada_XY.__round__(4)))
    self.let_AngleDg.setText(str(Angulo_dg.__round__(4)))
    self.let_MainInertiaX.setText(str(Inercia_Principal_X.__round__(4)))
    self.let_MainInertiaY.setText(str(Inercia_Principal_Y.__round__(4)))

    return Area, PrimeiroMomAreaX, PrimeiroMomAreaY, SegundoMomAreaY, SegundoMomAreaX, ProdInerciaSecao, \
           Centro_Inercia_X, Centro_Inercia_Y, Raio_Giracao_X, Raio_Giracao_Y, Inercia_Transladada_X, \
           Inercia_Transladada_Y, Inercia_Transladada_XY, Angulo_dg, Inercia_Principal_X, Inercia_Principal_Y


def Show_Image(ListaX, ListaY):
    plt.figure()
    plt.plot(ListaX, ListaY, '-.', color='gray')
    plt.scatter(ListaX, ListaY, color='red', marker='x')
    plt.axis("off")
    plt.savefig("section.png")


def isnumber(value):  # Verificador para as entradas na lista
    try:
        float(value)
    except ValueError:
        return False
    return True
