import socket
import threading
import time
import platform

clean = ('clear', 'cls')[platform.system() == 'Windows']


def winner(tabuleiro):
    for i in ['X', 'O']:
        # horizontal
        if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == i: return i
        if tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == i: return i
        if tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == i: return i
        # vertical
        if tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == i: return i
        if tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == i: return i
        if tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == i: return i
        # diagonal
        if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == i: return i
        if tabuleiro[6] == tabuleiro[4] == tabuleiro[2] == i: return i
    return None


def salvaEstadoJogo(address1, address2, tabuleiro, numJogada, pontuacaoXis, pontuacaoBola):
    add1 = list(map(int, address1[0].split('.')))
    add2 = list(map(int, address2[0].split('.')))
    print(add1)
    if add1 < add2:
        nomeArq = "Estado_do_Jogo" + address1[0] + address2[0] + ".txt"
    else:
        nomeArq = "Estado_do_Jogo" + address2[0] + address1[0] + ".txt"

    print("Estado do jogo salvo em: " + nomeArq)

    try:
        file = open(nomeArq, "w+")
    except IOError:
        print("Nao foi possivel abrir o arquivo para escrita.")
        return None

    # salvar tabuleiro
    for i in tabuleiro:
        file.write(i)

    file.write("\n")
    # salvar numJogada
    file.write(str(numJogada) + "\n")

    # salvar pontuacao do Jogo
    file.write(str(pontuacaoBola) + "\n" + str(pontuacaoXis))

    file.close()


def recuperaEstadoJogo(address1, address2):
    add1 = list(map(int, address1[0].split('.')))
    add2 = list(map(int, address2[0].split('.')))

    # ler o arquivo
    if add1 < add2:
        nomeArq = "Estado_do_Jogo" + address1[0] + address2[0] + ".txt"
    else:
        nomeArq = "Estado_do_Jogo" + address2[0] + address1[0] + ".txt"

    try:
        file = open(nomeArq)
    except IOError:
        print("Nome de arquivo invalido, talvez esses dois jogadores nao tenham jogado um contra o outro.")
        print("Um novo jogo sera criado")
        return 0, 0, 0, "000000000"

    contents = file.read()
    file_as_list = contents.splitlines()
    print(file_as_list)

    tabString = file_as_list[0]
    numJogada = file_as_list[1]
    pontuacaoBola = file_as_list[2]
    pontuacaoXis = file_as_list[3]

    file.close()

    # atualizar o valor do numJogada
    # atualizar o valor da pontuacao do Jogo
    return int(numJogada), int(pontuacaoBola), int(pontuacaoXis), tabString


def arrumaTabuleiro(tabString):
    tabuleiro = []
    for i in tabString:
        tabuleiro.append(i)

    return tabuleiro

def inputOpcao():
    while True:
        try:
            valor = int(input("Digite 1 para novo jogo ou 2 para recuperar um jogo: "))
            return valor
        except:
            print("Caractere invalido, deve ser um inteiro!")

def inputIp():
    while True:
        try:
            ip = str(input("Digite o IP de quem era a bola: "))
            return ip
        except:
            print("IP invalido, deve ser uma string somente com numeros e pontos!")

def handleGame(conn1, conn2, address1, address2):
    opcao = 0
    ipBola = 0
    tabuleiro = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
    numJogada = 0
    pontuacaoXis = 0
    pontuacaoBola = 0
    while opcao != 1 and opcao != 2:
        opcao = inputOpcao()
        if opcao == 2:
            while ipBola != address1[0] and ipBola != address2[0]:
                ipBola = inputIp()
                if ipBola == address1[0]:
                    bola = conn1
                    xis = conn2
                elif ipBola == address2[0]:
                    xis = conn1
                    bola = conn2
                else:
                    print("IP invalido!!")
            bola.send('jo'.encode())
            xis.send('jx'.encode())
            time.sleep(1)
            numJogada, pontuacaoBola, pontuacaoXis, tabString = recuperaEstadoJogo(address1, address2)
            bola.send(("recuperaEstado" + tabString + str(pontuacaoBola)).encode())
            xis.send(("recuperaEstado" + tabString + str(pontuacaoXis)).encode())
            tabuleiro = arrumaTabuleiro(tabString)
        elif opcao == 1:
            bola = conn1
            xis = conn2
            bola.send('jo'.encode())
            xis.send('jx'.encode())
            time.sleep(1)
        else:
            print("Opcao invalida!!")

    while True:
        salvaEstadoJogo(address1, address2, tabuleiro, numJogada, pontuacaoXis, pontuacaoBola)
        if numJogada % 2 == 0:  # se for jogada par, a bola joga
            bola.send('suaVez'.encode())
            xis.send('aguardeSuaVez'.encode())
            message = bola.recv(1024).decode()
            xis.send(message.encode())
            time.sleep(1)  # tivemos que colocar, pois estava chegando juntando duas mensagens no linux
            tabuleiro[int(message) - 1] = 'O'
        else:  # se for impar, o xis joga
            xis.send('suaVez'.encode())
            bola.send('aguardeSuaVez'.encode())
            message = xis.recv(1024).decode()
            bola.send(message.encode())
            time.sleep(1)  # tivemos que colocar, pois estava chegando juntando duas mensagens no linux
            tabuleiro[int(message) - 1] = 'X'
        win = winner(tabuleiro)
        if win == 'X':
            pontuacaoXis += 1
            if pontuacaoXis > 1:
                xis.send('ganhouJogo'.encode())
                xis.close()
                bola.send('perdeuJogo'.encode())
                bola.close()
                print("Conexao finalizada com " + address1[0] + " e " + address2[0])
                return None
            else:
                xis.send('ganhouRodada'.encode())
                bola.send('perdeuRodada'.encode())
            tabuleiro = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
            numJogada = 0
        elif win == 'O':
            pontuacaoBola += 1
            if pontuacaoBola > 1:
                bola.send('ganhouJogo'.encode())
                bola.close()
                xis.send('perdeuJogo'.encode())
                xis.close()
                print("Conexao finalizada com " + address1[0] + " e " + address2[0])
                return None
            else:
                bola.send('ganhouRodada'.encode())
                xis.send('perdeuRodada'.encode())
            tabuleiro = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
            numJogada = -1
        numJogada += 1
        if numJogada == 9:
            bola.send('empate'.encode())
            xis.send('empate'.encode())
            tabuleiro = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
            numJogada = 0


def main():
    serverSocket = socket.socket()
    host = "localhost"  # alterar para ip local do computador
    port = 12348
    serverSocket.bind((host, port))
    serverSocket.listen(30)

    connection1 = None
    connection2 = None
    address1 = None
    address2 = None

    while True:
        connection, address = serverSocket.accept()
        print("Got connection from: " + str(address))
        if connection1 is None:
            connection1 = connection
            address1 = address
            connection1.send("aguardeRival".encode())
        else:
            connection2 = connection
            address2 = address
            connection2.send("aguardeRival".encode())
        if connection2 is not None:
            threading.Thread(target=handleGame, args=(connection1, connection2, address1, address2)).start()
            connection1 = None
            connection2 = None
            address1 = None
            address2 = None


if __name__ == "__main__":
    main()

'''
funcao pra pegar o ip local do servidor
mudar antes da apresentacao.
esta em localhost somente para testes

def get_my_ip_address(remote_server="google.com"):
    """
    Return the/a network-facing IP number for this system.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
        s.connect((remote_server, 80))
        return s.getsockname()[0]

print(get_my_ip_address())
'''