class Espositori:

    def __init__(self, codice, nome, cognome):
        self.__codice=codice
        self.__nome=nome
        self.__cognome=cognome

    def __str__(self):
        return f"{self.__codice} {self.__nome} {self.__cognome}"

    def __repr__(self):
        return f"{self.__class__.__name__}(codice='{self.__codice}', nome='{self.__nome}', cognome='{self.__cognome}')"

    @property # getter per codice (assegna_stand_a_espositore)
    def codice(self):
        return self.__codice

    def __eq__(self,other): # definisco metodo di uguaglianza
        if other is None: # se viene confrontato con un oggetto vuoto restituisce falso
            return False
        else: # altrimenti confronta il codice
            return self.__codice==other.codice