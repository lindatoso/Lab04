class Stand:

    def __init__(self, codice, superficie, padiglione, prezzo):
        self.__codice=codice
        self.__superficie=superficie
        self.__padiglione=padiglione
        self._prezzo=float(prezzo) # inizializzo come float
        self._tipo= "Standard" # inizializzo tipo per stampa - single underscore per ereditarietà
        self.__espositore_assegnato=None # inizializzo l'espositore associato a nessuno

    def __str__(self):
        if self.__espositore_assegnato is None: # se non ci sono espositori associati stampo anche disponibile
            return f"{self.__codice}: {self._tipo} | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {round(self._prezzo,2)}€ - Disponibile"
        else: # altrimenti stampo i campi normalmente
            return f"{self.__codice}: {self._tipo} | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self._prezzo}€"

    def __repr__(self):
        return f"{self.__class__.__name__}codice='{self.__codice}', tipo='{self._tipo}', superficie='{self.__superficie}', padiglione='{self.__padiglione}', prezzo='{self._prezzo}'"

    @property # definisco getter per codice (assegna_stand_a_espositore)
    def codice(self):
        return self.__codice

    @property # definisco getter per prezzo (stand_ordinati_per_prezzo)
    def prezzo(self):
        return self._prezzo

    @property # definisco getter per espositore associato (assegna_stand_a_espositore, elenca_espositori)
    def espositore_assegnato(self):
        return self.__espositore_assegnato

    @property # definisco una proprietà associata a espositore_assegnato per segnalarne la disponibilità
    def disponibile(self):
        return self.__espositore_assegnato is None # uno stand è disponibile se non ha un espositore associato

    def __lt__(self, other): # definisco una funzione di ordinamento per prezzo crescente
        return self._prezzo < other.prezzo

    def assegna_espositore(self, espositore): # definisco una funzione per assegnare un espositore all'attributo espositore_assegnato
        self.__espositore_assegnato=espositore
