class Stand:

    def __init__(self, codice, superficie, padiglione, prezzo):
        self.__codice=codice
        self.__superficie=superficie
        self.__padiglione=padiglione
        self.__prezzo=float(prezzo)
        self._tipo= "Standard"
        self.__espositore_assegnato=None

    def __str__(self):
        if self.__espositore_assegnato is None:
            return f"{self.__codice}: {self._tipo} | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.__prezzo}€ - Disponibile"
        else:
            return f"{self.__codice}: {self._tipo} | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.__prezzo}€"

    @property
    def codice(self):
        return self.__codice

    @property
    def prezzo(self):
        return self.__prezzo

    @property
    def espositore_assegnato(self):
        return self.__espositore_assegnato

    @property
    def disponibile(self):
        return self.__espositore_assegnato is None

    def __lt__(self, other):
        return self.__prezzo < other.prezzo

    def assegna_espositore(self, espositore):
        self.__espositore_assegnato=espositore


    #ST2: Prese Extra | 12 mq - Padiglione 2 - Prezzo 266.20€ - Prese aggiuntive: 3 - Disponibile