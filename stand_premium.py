from stand import Stand # come per stand_prese

class StandPremium(Stand):
    def __init__(self, codice, superificie, padiglione, prezzo, zona):
        super().__init__(codice, superificie, padiglione, prezzo)
        self.__zona=zona
        self._prezzo=float(prezzo)*1.30
        self._tipo="Premium"

    @property
    def prezzo(self):
        return self._prezzo

    def __str__(self):
        if self.espositore_assegnato is None:
            return f"{super().__str__()} - Zona: {self.__zona} - Disponibile"
        else:
            return f"{super().__str__()} - Zona: {self.__zona}"

    def __repr__(self):
        return f"{super().__repr__()}, {self.__class__.__name__}zona='{self.__zona}'"


