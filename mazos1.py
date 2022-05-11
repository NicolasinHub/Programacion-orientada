
import random


class GenerarAleatorios:
    
    def __init__(self):
        self.Dados=[]
        
    def LanzarDados(self):
        self.Dados=[]
        for i in range(0,2):
            a=random.randint(1,6)
            self.Dados.append(a)
        return self.Dados
    
    def MezclarCartas(self):
        Mazo=[]
        Letras=['C','T','P','D']
        for letra in Letras:
            Cartas=[]
            i=1
            while i<=12:
                Mazo.append(letra+str(i))
                i+=1
            random.shuffle(Mazo)
        return Mazo
    
Generar=GenerarAleatorios()
Repartir=GenerarAleatorios()
for i in range(1,8):
    print(Generar.LanzarDados()) 

print(Repartir.MezclarCartas())

class Ordenar(GenerarAleatorios):
    def DesordenarLista(self):
        Lista=[]
        Lista.append(Generar.MezclarCartas())
        print(random.shuffle(Lista))
        return Lista
    
    def OrdenarLista(self):
        Lista=[]
        Lista.append(Generar.MezclarCartas())
        print(sorted(Lista))
        return Lista

Ordenada=Ordenar()
Desordenada=Ordenar()

Desordenada.DesordenarLista()
Ordenada.OrdenarLista()