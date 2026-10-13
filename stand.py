class Stand:

    def __init__(self, codice, superficie, padiglione, prezzo):
        self.__codice=codice
        self.__superficie=superficie
        self.__padiglione=padiglione
        self.__prezzo=prezzo

    def __str__(self):
        return f"{self.__codice} {self.__superficie} {self.__padiglione} {self.__prezzo}€"

    #ST2: Prese Extra | 12 mq - Padiglione 2 - Prezzo 266.20€ - Prese aggiuntive: 3 - Disponibile