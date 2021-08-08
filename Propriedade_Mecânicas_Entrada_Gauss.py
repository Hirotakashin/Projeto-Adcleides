import math
from matplotlib import pyplot

#variáveis Globais

Lista_X = []
Lista_Y = []

def Escolha_Parametros():
    #Garantia que a figura possa ser executada no programa
    while True:
        Num_Vertices = input("Defina o número de vértices a serem considerados: ")
        if Num_Vertices.isnumeric():
            Num_Vertices = int(Num_Vertices)
            break
        else:
            print("Não é um valor válido!")
            continue
    Calculo_Peca(Num_Vertices)



def Calculo_Peca(Numero_Vertices):
    Num_Vertices = Numero_Vertices
    for numero in range(1, Numero_Vertices + 1):
        #Laço de repetição para verificação se o Número é float
        while True:
            X = input(f"Insira o valor do {numero}° X: ")
            Y = input(f"Insira o valor do {numero}° Y: ")
            if isnumber(X) and isnumber(Y):
                X = float(X)
                Y = float(Y)
                Lista_X.append(X)
                Lista_Y.append(Y)
                break
            else:
                print("Por favor, digite somente valores numéricos!")
                continue
    Propriedades_Mecanicas(Num_Vertices, Lista_X, Lista_Y)


def Propriedades_Mecanicas(Numero_Vertices ,Lista_X, Lista_Y):
    Area = 0
    PrimeiroMomAreaX = 0
    PrimeiroMomAreaY = 0
    SegundoMomAreaX = 0
    SegundoMomAreaY = 0
    ProdInerciaSecao = 0
    for i in range(0, Numero_Vertices):
        #Calculo de Área
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
    print(f"Área = {round(Area, 4)} u.a²")
    print(f"Momento de Primeira Ordem em X = {round(PrimeiroMomAreaX, 4)}")
    print(f"Momento de Primeira Ordem em Y = {round(PrimeiroMomAreaY, 4)}")
    print(f"Momento de Segunda Ordem em X = {round(SegundoMomAreaX, 4)}")
    print(f"Momento de Segunda Ordem em Y = {round(SegundoMomAreaY, 4)}")
    print(f"Produto de Inércia = {ProdInerciaSecao}")

    #Centro de Inércia e Raios de Giração
    Centro_Inercia_X = PrimeiroMomAreaY / Area

    Centro_Inercia_Y = PrimeiroMomAreaX / Area

    Raio_Giracao_X = math.sqrt(abs(SegundoMomAreaX) / Area)

    Raio_Giraaco_Y = math.sqrt(abs(SegundoMomAreaY) / Area)

    print(f"Centro de Inércia X = {round(Centro_Inercia_X, 4)}")
    print(f"Centro de Inércia Y = {round(Centro_Inercia_Y, 4)}")
    print(f"Centro de Raio de Giração X = {round(Raio_Giracao_X, 4)}")
    print(f"Centro de Raio de Giração Y = {round(Raio_Giraaco_Y, 4)}")

    #Transladar Propriedades para os Eixos Centroidais e Determinação da Seção Principal
    Inercia_Transladada_X = SegundoMomAreaX - Area * (Centro_Inercia_Y ** 2)

    Inercia_Transladada_Y = SegundoMomAreaY - Area * (Centro_Inercia_X ** 2)

    Inercia_Transladada_XY = ProdInerciaSecao - Area * Centro_Inercia_X * Centro_Inercia_Y

    print(f"Inercia Transladada para o eixo X:{round(Inercia_Transladada_X, 4)}")
    print(f"Inercia Transladada para o eixo Y:{round(Inercia_Transladada_Y, 4)}")
    print(f"Inercia Transladada para o eixo XY:{round(Inercia_Transladada_XY, 4)}")

    #Angulos
    Angulo_rad = (1/2) * math.atan(2*(Inercia_Transladada_XY/(Inercia_Transladada_Y-Inercia_Transladada_X)))

    Angulo_dg = Angulo_rad*(180/math.pi)

    print(f"Angulo:{round(Angulo_dg, 4)}°")

    #InerciasPrincipais
    Inercia_Principal_X = Inercia_Transladada_Y*(math.sin(Angulo_rad))**2 - 2*math.sin(Angulo_rad) * math.cos(Angulo_rad) \
                          + Inercia_Transladada_X*(math.cos(Angulo_rad))**2

    Inercia_Principal_Y = Inercia_Transladada_Y*(math.cos(Angulo_rad))**2 - 2*math.sin(Angulo_rad) * math.cos(Angulo_rad) \
                          + Inercia_Transladada_X*(math.sin(Angulo_rad))**2

    print(f"Inercia X no eixo Principal: {round(Inercia_Principal_X, 4)}")
    print(f"Inercia Y no eixo Principal: {round(Inercia_Principal_Y, 4)}")

    #Parâmetros do Circulo de Mohr
    Raio_Mohr = math.sqrt(abs(Inercia_Transladada_XY**2 + ((Inercia_Transladada_Y - Inercia_Transladada_X)/2)**2))

    Centro_Circulo_Mohr = (Inercia_Transladada_Y + Inercia_Transladada_X)/2

    inercia_Maxima = Centro_Circulo_Mohr + Raio_Mohr
    Inercia_Minima = Centro_Circulo_Mohr - Raio_Mohr

def isnumber(value):#Verificador para as entradas na lista
    try:
         float(value)
    except ValueError:
         return False
    return True

if __name__ == '__main__':
    Escolha_Parametros()
