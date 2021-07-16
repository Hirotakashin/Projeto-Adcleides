import math

#variáveis Globais
Num_Vertices = 0
Lista_X = []
Lista_Y = []

def Escolha_Parametros():
    #Garantia que a figura possa ser executada no programa
    while True:
        Tipo_Figura = input("A poligonal se encontra como um objeto Maciço ou Vazado? ")
        Tipo_Figura = Tipo_Figura.lower()
        # Verfica se é numérico
        while True:
            Num_Vertices = input("Defina o número de vértices a serem considerados: ")
            if Num_Vertices.isnumeric():
                Num_Vertices = int(Num_Vertices)
                break
            else:
                print("Não é numérico")
                continue
        #Verfica se a figura está dentro do escopo
        if Tipo_Figura == "maciço":
            Peca_Macica(Num_Vertices)
        elif Tipo_Figura == "vazado":
            Peca_Vazada(Num_Vertices)
        else:
            print("O tipo de figura não foi reconhecido")
            continue
        break


    return Num_Vertices


def Peca_Vazada(Numero_Vertices):
    Metade = Numero_Vertices // 2
    Metade_1 = Metade + 1
    for numero in range(1, Numero_Vertices + 1):
        #Laço de repetição para verificação se o Número é int ou float
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

        # Aqui repete nos locais que são necessários, após o final da primeira e depois da segunda metade
        if numero == Metade:
            Lista_X.append(Lista_X[0])
            Lista_Y.append(Lista_Y[0])

    Lista_X.append(Lista_X[Metade_1])
    Lista_Y.append(Lista_Y[Metade_1])

    Propriedades_Mecanicas(Numero_Vertices, Lista_X, Lista_Y)
    return Lista_X, Lista_Y

def Peca_Macica(Numero_Vertices):
    for n in range(1, Numero_Vertices + 1):
        # Laço de repetição para verificação se o Número é int ou float
        while True:
            X = input(f"Insira o valor do {n}° X: ")
            Y = input(f"Insira o valor do {n}° Y: ")
            if isnumber(X) and isnumber(Y):
                X = float(X)
                Y = float(Y)
                Lista_X.append(X)
                Lista_Y.append(Y)
                break
            else:
                print("Por favor, digite somente valores numéricos!")
                continue
        Lista_X.append(Lista_X[0])
        Lista_Y.append(Lista_Y[0])

    Propriedades_Mecanicas(Numero_Vertices, Lista_X, Lista_Y)
    return Lista_X, Lista_Y

def Propriedades_Mecanicas(Numero_Vertices, ListaX, ListaY):
    Area = 0
    PrimeiroMomAreaX = 0
    PrimeiroMomAreaY = 0
    SegundoMomAreaX = 0
    SegundoMomAreaY = 0
    ProdInerciaSecao = 0
    for i in range(1, Numero_Vertices + 1):
        #Calculo de Área
        iteravel = (ListaX[i - 1]*ListaY[i])-(ListaY[i - 1]*ListaX[i])
        Area = (1 / 2) * iteravel + Area

        # Momento de Primeira Ordem
        PrimeiroMomAreaY =(1 / 6) * iteravel * (ListaX[i - 1] + ListaX[i]) + PrimeiroMomAreaY
        PrimeiroMomAreaX = (1 / 6) * iteravel * (ListaY[i - 1] + ListaY[i]) + PrimeiroMomAreaX

        # Momento de Segunda Ordem
        SegundoMomAreaY = (1 / 12) * iteravel * ((ListaX[i - 1] ** 2) + (ListaX[i - 1] * ListaX[i])
                                                     + (ListaY[i] ** 2)) + SegundoMomAreaY
        SegundoMomAreaX =(1 / 12) * iteravel * ((ListaY[i - 1] ** 2) + (ListaY[i - 1] * ListaY[i])
                                                     + (ListaY[i] ** 2)) + SegundoMomAreaX

        # Produto de Inercia da Seção
        ProdInerciaSecao =(1 / 24) * iteravel * (2 * ListaX[i - 1] * ListaY[i - 1] + (ListaX[i - 1] * ListaY[i])
                                   + (ListaX[i] * ListaY[i - 1])
                                   + 2 * ListaX[i] * ListaY[i]) + ProdInerciaSecao
    Area = abs(Area)
    print(f"Área = {Area} u.a²")
    print(f"Momento de Primeira Ordem em X = {PrimeiroMomAreaX}")
    print(f"Momento de Primeira Ordem em Y = {PrimeiroMomAreaY}")
    print(f"Momento de Segunda Ordem em X = {SegundoMomAreaX}")
    print(f"Momento de Segunda Ordem em Y = {SegundoMomAreaY}")
    print(f"Produto de Inércia = {ProdInerciaSecao}")

    #Centro de Inércia e Raios de Giração
    Centro_Inercia_X = PrimeiroMomAreaY / Area

    Centro_Inercia_Y = PrimeiroMomAreaX / Area

    Raio_Giracao_X = math.sqrt(SegundoMomAreaX / Area)

    Raio_Giraaco_Y = math.sqrt(SegundoMomAreaY / Area)

    print(f"Centro de Inércia X = {Centro_Inercia_X}")
    print(f"Centro de Inércia Y = {Centro_Inercia_Y}")
    print(f"Centro de Raio de Giração X = {Raio_Giracao_X}")
    print(f"Centro de Raio de Giração Y = {Raio_Giraaco_Y}")

    #Transladar Propriedades para os Eixos Centroidais e Determinação da Seção Principal
    Inercia_Transladada_X = SegundoMomAreaX - Area * (Centro_Inercia_Y ** 2)

    Inercia_Transladada_Y = SegundoMomAreaY - Area * (Centro_Inercia_X ** 2)

    Inercia_Transladada_XY = ProdInerciaSecao - Area * Centro_Inercia_X * Centro_Inercia_Y

    print(f"Inercia Transladada para o eixo X:{Inercia_Transladada_X}")
    print(f"Inercia Transladada para o eixo Y:{Inercia_Transladada_Y}")
    print(f"Inercia Transladada para o eixo XY:{Inercia_Transladada_XY}")

    #Angulos

    Angulo_rad = (1/2) * math.atan(2*(Inercia_Transladada_XY/(Inercia_Transladada_Y-Inercia_Transladada_X)))

    Angulo_dg = Angulo_rad*(180/math.pi)

    print(f"Angulo:{Angulo_dg}°")

    #InerciasPrincipais

    Inercia_Principal_X = Inercia_Transladada_Y*(math.sin(Angulo_dg))**2 - 2*math.sin(Angulo_dg) * math.cos(Angulo_dg) \
                          + Inercia_Transladada_X*(math.cos(Angulo_dg))**2

    Inercia_Principal_Y = Inercia_Transladada_Y*(math.cos(Angulo_dg))**2 - 2*math.sin(Angulo_dg) * math.cos(Angulo_dg) \
                          + Inercia_Transladada_X*(math.sin(Angulo_dg))**2

    print(f"Inercia X no eixo Principal: {Inercia_Principal_X}")
    print(f"Inercia Y no eixo Principal: {Inercia_Principal_Y}")

    #Parâmetros do Circulo de Mohr

    Raio_Mohr = math.sqrt(Inercia_Transladada_XY**2 + ((Inercia_Transladada_Y - Inercia_Transladada_X)/2)**2)

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
