class Pedra:
    def __init__(self, tam, dist):
        self.tam = tam
        self.dist = dist


def subRotina(vetor):
    distMaxLocal = 0

    posIni = 0
    posFim = len(vetor) - 1

    distIni = vetor[posIni].dist
    distFim = vetor[posFim].dist

    sapo1 = distIni
    sapo2 = distIni

    i = 1
    while sapo1 < distFim and sapo2 < distFim:
        if i < posFim:
            if sapo1 < sapo2:
                distLocalAux = vetor[i].dist - sapo1
                sapo1 = vetor[i].dist

            elif sapo2 < sapo1:
                distLocalAux = vetor[i].dist - sapo2
                sapo2 = vetor[i].dist

            else:
                distLocalAux = vetor[i].dist - sapo1
                sapo1 = vetor[i].dist

            i += 1
        else:
            if sapo1 < sapo2:
                distLocalAux = vetor[posFim].dist - sapo1
                sapo1 = vetor[posFim].dist

            elif sapo2 < sapo1: #
                distLocalAux = vetor[posFim].dist - sapo2
                sapo2 = vetor[posFim].dist

            else:
                distLocalAux = vetor[posFim].dist - sapo1
                sapo1 = vetor[posFim].dist

        if distLocalAux > distMaxLocal:
            distMaxLocal = distLocalAux

    return distMaxLocal



def caminho(vetor):
    distMaxGlobal = 0
    # Esvazia a lista auxiliar.
    vetorAux = []
    # Seta para primeira posição.
    j = 0

    for i in range(0, len(vetor)):
        if vetor[i].tam == 'Margem Esquerda':
            # Pega a primeira posição da "Lista Principal" de pedra, que seria a margem esquerda.
            # Incrementando na "Lista Auxiliar".
            vetorAux.append(vetor[i])
            # Seta para a proxima posição da "Lista Auxiliar".
            j += 1

        elif vetor[i].tam == 'Margem Direita':
            # Pega a ultima posição da Lista Principal" de pedra, que seria a margem direita.
            # Incrementando na "Lista Auxiliar".
            vetorAux.append(vetor[i])
            # Função gerada quando o sapo encontra uma pedra grande ou a margem direita.
            # Retorna salto maximo minimizado na subLista representado na "Lista Auxiliar".
            distMaxLocal = subRotina(vetorAux)
            # Verifica se o otimo local retornado da função será o otimo global da "Lista Principal".
            if distMaxLocal > distMaxGlobal:
                distMaxGlobal = distMaxLocal

        elif vetor[i].tam == 'B':
            # Pega a posição da pedra grande referente a "Lista Principal" de pedra.
            # Incrementando na "Lista Auxiliar".
            vetorAux.append(vetor[i])
            distMaxLocal = subRotina(vetorAux)
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

if __name__ == "__main__":

    with open("arq.txt", "r") as entrada:

        casosdeteste = int(entrada.readline())

        it = 0
        for i in range(casosdeteste):
            pedras = []  # Pedras do turno

            linha = entrada.readline().split()  # info do rio
            qtdPedras = int(linha[0])  # info da qtd de pedras

            rioMargemEsq = 0  # rioMargemDir = 0 |------------------------------------| rioMargemDir = int(linha[1])
            rioMargemDir = int(linha[1])

            infoPedras = entrada.readline().split()
            newPedra = Pedra("Margem Esquerda", rioMargemEsq)  # inserindo pedra marcando a margem esquerda do rio,
            pedras.append(newPedra)  # considera-se que a margem esquerda é uma "pedra grande também"

            j = 0
            while qtdPedras > 0:  # loop que mapeia o restante das pedras
                linhaTratada = infoPedras[j].split("-")  # trata linha
                bigORsmall = linhaTratada[0]  # especificação da pedra ( big(G) ou small(S) )
                distMargemEsq = int(linhaTratada[1])  # distância da pedra até a margem esquerda
                newPedra = Pedra(bigORsmall, distMargemEsq)  # create it!
                pedras.append(newPedra)  # add it!

                j += 1
                qtdPedras -= 1

            newPedra = Pedra('Margem Direita', rioMargemDir)  # inserindo pedra marcando a margem direita do rio,
            pedras.append(newPedra)  # considera-se que a margem direita é uma "pedra grande também"

            caminho(pedras)
