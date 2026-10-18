from stand import Stand

class StandPrese(Stand):
    def __init__(self, codice, superificie, padiglione, prezzo, prese):
        prezzo=float(prezzo)
        super().__init__(codice, superificie, padiglione, prezzo)
        self.__prese=int(prese)
        self.__prezzo=prezzo*(1 + 0.07*self.__prese)
        self._tipo="Prese extra"

    @property
    def prese(self):
        return self.__prese

    @property
    def prezzo(self):
        return self.__prezzo

    def __str__(self):
        if self.espositore_assegnato is None:
            return f"{super().__str__()} - Prese aggiuntive: {self.__prese} - Disponibile"
        else:
            return f"{super().__str__()} - Prese aggiuntive: {self.__prese}"



