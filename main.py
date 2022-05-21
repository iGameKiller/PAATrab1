class Pedra:
    def __init__(self, tamanho, distancia):
        self.tamanho = tamanho
        self.distancia = distancia


def subCaminho(vetor):
    distMaxLocal = 0
    sapo1 = 0
    sapo2 = 0

    posIni = 0
    posFim = len(vetor) - 1

    distIni = vetor[posIni].distancia
    distFim = vetor[posFim].distancia

    print('')
    print('-----------------Vetor Auxiliar--------------------')
    for i in range(posIni, posFim + 1):
        pedraDistPrint = str(vetor[i].distancia)
        pedraTamPrint = str(vetor[i].tamanho)
        print(pedraTamPrint + '-' + pedraDistPrint)
    print('')

    sapo1 = distIni
    sapo2 = distIni

    print('Sapo 1: Tam ' + str(vetor[posIni].tamanho) + ' Dist-' + str(vetor[posIni].distancia) + ' Salto-' + str(0))
    print('Sapo 2: Tam ' + str(vetor[posIni].tamanho) + ' Dist-' + str(vetor[posIni].distancia) + ' Salto-' + str(0))

    i = 1
    while not ((sapo1 == distFim) and (sapo2 == distFim)):
        if i < posFim:
            if sapo1 < sapo2:
                distLocalAux = vetor[i].distancia - sapo1
                sapo1 = vetor[i].distancia
                print('Sapo 1: Tam-' + str(vetor[i].tamanho) + ' Dist-' + str(vetor[i].distancia) + ' Salto-' + str(
                    distLocalAux))
            elif sapo2 < sapo1:
                distLocalAux = vetor[i].distancia - sapo2
                sapo2 = vetor[i].distancia
                print('Sapo 2: Tam-' + str(vetor[i].tamanho) + ' Dist-' + str(vetor[i].distancia) + ' Salto-' + str(
                    distLocalAux))
            else:
                distLocalAux = vetor[i].distancia - sapo1
                sapo1 = vetor[i].distancia
                print('Sapo 1: Tam ' + str(vetor[i].tamanho) + ' Dist-' + str(vetor[i].distancia) + ' Salto-' + str(
                    distLocalAux))

            i += 1
        else:
            if sapo1 < sapo2:
                distLocalAux = vetor[posFim].distancia - sapo1
                sapo1 = vetor[posFim].distancia
                print('Sapo 1: Tam ' + str(vetor[posFim].tamanho) + ' Dist-' + str(
                    vetor[posFim].distancia) + ' Salto-' + str(distLocalAux))
            elif sapo2 < sapo1:
                distLocalAux = vetor[posFim].distancia - sapo2
                sapo2 = vetor[posFim].distancia
                print('Sapo 2: Tam ' + str(vetor[posFim].tamanho) + ' Dist-' + str(
                    vetor[posFim].distancia) + ' Salto-' + str(distLocalAux))
            else:

                distLocalAux = vetor[posFim].distancia - sapo1
                sapo1 = vetor[posFim].distancia
                print('Sapo 1: Tam ' + str(vetor[i].tamanho) + ' Dist-' + str(vetor[i].distancia) + ' Salto-' + str(
                    distLocalAux))

        if distLocalAux > distMaxLocal:
            distMaxLocal = distLocalAux

    print('-------------------------------------------------')

    return distMaxLocal


def caminho(vetor):
    distMaxGlobal = 0
    # Esvazia a lista auxiliar.
    vetorAux = []
    # Seta para primeira posição.
    j = 0

    for i in range(0, len(vetor)):
        if (vetor[i].tamanho == 'ME'):
            # Pega a primeira posição da "Lista Principal" de pedra, que seria a margem esquerda.
            # Incrementando na "Lista Auxiliar".
            vetorAux.append(vetor[i])
            # Seta para a proxima posição da "Lista Auxiliar".
            j += 1

        elif (vetor[i].tamanho == 'MD'):
            # Pega a ultima posição da Lista Principal" de pedra, que seria a margem direita.
            # Incrementando na "Lista Auxiliar".
            vetorAux.append(vetor[i])
            # Função gerada quando o sapo encontra uma pedra grande ou a margem direita.
            # Retorna salto maximo minimizado na subLista representado na "Lista Auxiliar".
            distMaxLocal = subCaminho(vetorAux)
            # Verifica se o otimo local retornado da função será o otimo global da "Lista Principal".
            if distMaxLocal > distMaxGlobal:
                distMaxGlobal = distMaxLocal

        elif (vetor[i].tamanho == 'B'):
            # Pega a posição da pedra grande referente a "Lista Principal" de pedra.
            # Incrementando na "Lista Auxiliar".
            vetorAux.append(vetor[i])
            distMaxLocal = subCaminho(vetorAux)
            # Verifica se o otimo local retornado da função será o otimo global da "Lista Principal".
            if distMaxLocal > distMaxGlobal:
                distMaxGlobal = distMaxLocal
                # Esvazia a lista auxiliar.
            vetorAux = []
            # Seta para primeira posição.
            j = 0
            # Pega novamente a posição da pedra grande referente a "Lista Principal" de pedra.
            # Incrementando na "Lista Auxiliar".
            vetorAux.append(vetor[i])
            # Seta para a proxima posição da "Lista Auxiliar".
            j += 1

        else:
            # Pega a posição da pedra pequena referente a "Lista Principal" de pedra.
            # Incrementando na "Lista Auxiliar".        
            vetorAux.append(vetor[i])
            # Seta para a proxima posição da "Lista Auxiliar".
            j += 1

    print('')
    print('Maior salto minimizado: ', distMaxGlobal)
    print('')


def main():
    with open("arq.txt", "r") as arq:
        # Leitura do arquivo de entrada.
        # Primeira linha do arquivo contem o numero de casos.
        numCasos = int(arq.readline())

        while numCasos > 0:
            # Zera a lista de pedras para cada caso.
            vetorPedras = []

            # Pega a proxima linha contendo o "Numero de Pedras" e "Distancia entre as Margens", inserindo numa lista
            # "contLinha".
            contLinha = arq.readline().split()
            # Pega a posição da lista "contLinha" referente ao "Numero de Pedras".
            numPedra = int(contLinha[0])

            # Pega a posição da lista "contLinha" referente ao "Distancia entre as Margens".
            # Defino meu ponto de partida, referente a ME - Margem Esquerda
            distIni = 0
            # Defino meu ponto de chegada, referente a  MD - Margem Direita
            distFim = int(contLinha[1])

            # Pega a proxima linha que representa as pedras, inserindo numa lista.
            vetorPedrasAux = arq.readline().split()

            # Inseri uma pedra denominada de ME - Margem Esquerda
            objPedra = Pedra('ME', distIni)
            vetorPedras.append(objPedra)

            # Inseri as pedras como objeto que esta na "vetorPedrasAux"
            for i in range(0, numPedra):
                aux = vetorPedrasAux[i].split("-")
                tam = aux[0]
                distPedra = int(aux[1])

                objPedra = Pedra(tam, distPedra)
                vetorPedras.append(objPedra)

            # Inseri uma pedra denominada de MD - Margem Direita
            objPedra = Pedra('MD', distFim)
            vetorPedras.append(objPedra)

            print('')
            print('--------------Vetor Principal--------------------')
            for i in range(0, len(vetorPedras)):
                pedraDistPrint = str(vetorPedras[i].distancia)
                pedraTamPrint = str(vetorPedras[i].tamanho)
                print(pedraTamPrint + '-' + pedraDistPrint)

            caminho(vetorPedras)
            numCasos -= 1


if __name__ == "__main__":
    main()
