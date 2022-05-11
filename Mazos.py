import random

class GeneradorAleatorios:
    def __init__(self):
        self.dados=list()
    
    def LanzarDados(self,n):
        
        i=0
        
        while i<n:
            dado=random.randint(1,6)
            self.dados.append(dado)
            i+=1
            
        return self.dados
miObjeto=GeneradorAleatorios()
print(miObjeto.LanzarDados(5))

def MezclarCartas(self):
        Mazo=[]
        Letras=['C','T','P','D']
        for letra in Letras:
            Cartas=[]
            i=1
            while i<=12:
                Cartas.append(letra+str(i))
                i+=1
            random.shuffle(Mazo)
            Mazo.append(Cartas)
        return Mazo
miObjeto=GeneradorAleatorios()

print(miObjeto.MezclarCartas())

class Ordenador(GeneradorAleatorios):
    def __init__(self) -> None:
        pass
    
    def OrdenarLista(self):
        #return sorted(Lista)
        pass
    
    def DesordenarLista(self):
        #return random.shuffle(Mazo)
        pass
    
class JugadorCartas(GeneradorAleatorios):
    def __init__(self) -> None:
        pass
    
    def RepartirCartas(self):
        miMazo=self.MezclarCartas()
        misCartas=[]
        for listas in miMazo:
            misCartas=misCartas+listas
        random.shuffle(misCartas)