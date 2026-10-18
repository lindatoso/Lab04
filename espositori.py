class Espositori:

    def __init__(self, codice, nome, cognome):
        self.__codice=codice
        self.__nome=nome
        self.__cognome=cognome

    def __str__(self):
        return f"{self.__codice} {self.__nome} {self.__cognome}"

    @property
    def codice(self):
        return self.__codice

    def __eq__(self,other):
        if other is None:
            return False
        else:
            return self.__codice==other.codice