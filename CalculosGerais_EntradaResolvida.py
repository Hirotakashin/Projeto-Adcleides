import math


def pg2():
    nvar = int(
        input(
            "Insira a quantidade de coordenadas (maior ou igual a 3), de forma que a figura fique sempre à esquerda: "))
    listax = []
    listay = []
    metade = nvar // 2
    metade_1 = metade + 1
    for n in range(1, nvar + 1):
        x = float(input(f"Insira o valor do {n}° X: "))
        y = float(input(f"Insira o valor do {n}° Y: "))
        listax.append(x)
        listay.append(y)
    #Aqui repete nos locais que são necessários, após o final da primeira e depois da segunda metade
        if n == metade:
            listax.append(listax[0])
            listay.append(listay[0])

    listax.append(listax[metade_1])
    listay.append(listay[metade_1])
    area = 0
    PrimeiroMomAreaX = 0
    PrimeiroMomAreaY = 0
    SegundoMomAreaX = 0
    SegundoMomAreaY = 0
    ProdInerciaSecao = 0
    for i in range(1, nvar + 1):
        #Calculo de Área
        iteravel = (listax[i - 1]*listay[i])-(listay[i - 1]*listax[i])
        area = (1/2)*iteravel + area

        # Momento de Primeira Ordem
        PrimeiroMomAreaY =(1 / 6) * iteravel * (listax[i - 1] + listax[i]) + PrimeiroMomAreaY
        PrimeiroMomAreaX = (1 / 6) * iteravel * (listay[i - 1] + listay[i]) + PrimeiroMomAreaX

        # Momento de Segunda Ordem
        SegundoMomAreaY = (1 / 12) * iteravel * ((listax[i - 1] ** 2) + (listax[i - 1] * listax[i])
                                                     + (listax[i] ** 2)) + SegundoMomAreaY
        SegundoMomAreaX =(1 / 12) * iteravel * ((listay[i - 1] ** 2) + (listay[i - 1] * listay[i])
                                                     + (listay[i] ** 2)) + SegundoMomAreaX

        # Produto de Inercia da Seção
        ProdInerciaSecao =(1 / 24) * iteravel * (2 * listax[i - 1] * listay[i - 1] + (listax[i - 1] * listay[i])
                                   + (listax[i] * listay[i - 1])
                                   + 2 * listax[i] * listay[i]) + ProdInerciaSecao
    area = abs(area)
    print(f"Área = {area} u.a²")
    print(f"Momento de Primeira Ordem em X = {PrimeiroMomAreaX}")
    print(f"Momento de Primeira Ordem em Y = {PrimeiroMomAreaY}")
    print(f"Momento de Segunda Ordem em X = {SegundoMomAreaX}")
    print(f"Momento de Segunda Ordem em Y = {SegundoMomAreaY}")
    print(f"Produto de Inércia = {ProdInerciaSecao}")

    #Centro de Inércia e Raios de Giração
    Centro_Inercia_X = PrimeiroMomAreaY / area

    Centro_Inercia_Y = PrimeiroMomAreaX/area

    Raio_Giracao_X = math.sqrt(SegundoMomAreaX / area)

    Raio_Giraaco_Y = math.sqrt(SegundoMomAreaY / area)

    print(f"Centro de Inércia X = {Centro_Inercia_X}")
    print(f"Centro de Inércia Y = {Centro_Inercia_Y}")
    print(f"Centro de Raio de Giração X = {Raio_Giracao_X}")
    print(f"Centro de Raio de Giração Y = {Raio_Giraaco_Y}")

    #Transladar Propriedades para os Eixos Centroidais e Determinação da Seção Principal
    Inercia_Transladada_X = SegundoMomAreaX - area*(Centro_Inercia_Y**2)

    Inercia_Transladada_Y = SegundoMomAreaY - area*(Centro_Inercia_X**2)

    Inercia_Transladada_XY = ProdInerciaSecao - area*Centro_Inercia_X*Centro_Inercia_Y

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




pg2()