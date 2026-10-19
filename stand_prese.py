from stand import Stand # importo classe padre

class StandPrese(Stand):
    def __init__(self, codice, superificie, padiglione, prezzo, prese):
        super().__init__(codice, superificie, padiglione, prezzo) # attributi ereditati
        self.__prese=int(prese) # definisco prese come intero
        self._prezzo=float(prezzo)*(1 + 0.07*self.__prese) # ridefinisco il prezzo con il sovrapprezzo
        self._tipo="Prese extra" # definisco il tipo

    @property # getter per prese
    def prese(self):
        return self.__prese

    @property # getter per prezzo
    def prezzo(self):
        return self._prezzo

    def __str__(self): # overriding del metodo ereditato, con aggiunta di informazione su prese
        if self.espositore_assegnato is None:
            return f"{super().__str__()} - Prese aggiuntive: {self.__prese} - Disponibile"
        else:
            return f"{super().__str__()} - Prese aggiuntive: {self.__prese}"

    def __repr__(self): # overriding del metodo ereditato
        return f"{super().__repr__()}, {self.__class__.__name__}prese='{self.__prese}'"


