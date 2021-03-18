#enconding: utf-8
from ObenedorDeEntrada import ObtenedorDeEntrada
from ProcesadorDeEntrada import ProcesadorDeEntrada
if __name__== "__main__":
    entrada = ObtenedorDeEntrada()
    procesador = ProcesadorDeEntrada()
    procesador.procesarEntrada(entrada.getEntrada())