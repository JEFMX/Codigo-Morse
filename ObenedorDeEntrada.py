class ObtenedorDeEntrada:
    def getEntrada(self):
        f = open ('Entrada.txt','r')
        entrada = f.read()
        print(entrada)
        f.close()
        return entrada
        #input("Introduce el texto\n")