from stand import Stand

class StandPremium(Stand):
    def __init__(self, codice, superificie, padiglione, prezzo, zona):
        prezzo = float(prezzo)
        super().__init__(codice, superificie, padiglione, prezzo)
        self.__zona=zona
        self.__prezzo=prezzo*1.30
        self._tipo="Premium"

    @property
    def prezzo(self):
        return self.__prezzo

    def __str__(self):

        if self.espositore_assegnato is None:
            return f"{super().__str__()} - Zona: {self.__zona} - Disponibile"
        else:
            return f"{super().__str__()} - Zona: {self.__zona}"


