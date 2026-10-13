from stand import Stand

class StandPremium(Stand):
    def __init__(self, codice, superificie, padiglione, prezzo, zona):
        super().__init__(codice, superificie, padiglione, prezzo)
        self.__zona=zona

    def __str__(self):
        return f"{super().__str__()} {self.__zona}"