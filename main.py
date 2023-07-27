import client
import server

def Menu():
    teste = {"1": client.main, "2": server.main}

    while True:
        print(" 1. Client\n 2. Server\n 3. Sair")
        op = input("\n>>> ")
        
        teste.get(op, lambda: print(" *** Opção inválida ***\n"))()

if __name__ == "__main__":
    Menu()