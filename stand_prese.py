from stand import Stand

class StandPrese(Stand):
    def __init__(self, codice, superificie, padiglione, prezzo, prese):
        super().__init__(codice, superificie, padiglione, prezzo)
        self.__prese=prese

    def __str__(self):
        return f"{super().__str__()} {self.__prese}"

