from EmitidorDeSonido import EmitidorDeSonido
from Diccionario import Diccionario
import time
class ProcesadorDeEntrada:
    def procesarEntrada(self, entrada):
        miDiccionario = Diccionario()
        sonido = EmitidorDeSonido()
        f = open ('Salida.txt','w')
        for i in entrada.upper():
            if i == " ":
                time.sleep(2)
                f.write("|")
                continue
            claveMorse = miDiccionario.getMorse(i)
            print(i," "+claveMorse)
            f.write(claveMorse)
            #f.write("|")

            for j in claveMorse:
                if j == ".":
                    sonido.SonidoCorto()
                else:
                    sonido.SonidoLargo()
                #time.sleep(0.5)
        f.close()