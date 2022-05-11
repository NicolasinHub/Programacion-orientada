import random
    def RepartirCartas(self):
        Mazo=self.MezclarCartas
        print(Mazo)
        misCartas=[]
        Jugadores=[]
        
        for i in range(0,4):
            mano=[]
            for i in range(1,12):
                mano.append(Mazo[0])
                Mazo.pop(0)
            Jugadores.append(mano)
        for jugador in range(0,len(Jugadores)):
            print('Mano del jugador' + str(jugador))
            print(Jugadores[jugador])