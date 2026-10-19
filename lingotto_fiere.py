import csv
from stand import Stand
from stand_prese import StandPrese
from stand_premium import StandPremium
from espositori import Espositori

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome=nome
        self.__bancarelle=[] # inizializzo lista di oggetti stand e lista di oggetti espositori
        self.__espositors=[]


    @property # definisco getter e setter per cambiare nome del centro fieristico
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome=nome

    @property # definisco getter e setter per modificare entrambe le liste di oggetti
    def bancarelle(self):
        return self.__bancarelle

    @bancarelle.setter
    def bancarelle(self, bancarelle):
        self.__bancarelle = bancarelle

    @property
    def espositors(self):
        return self.__espositors

    @espositors.setter
    def espositors(self, espositors):
        self.__espositors = espositors

    def __str__(self): # definisco funzione per stampa
        return f"{self.__nome}"

    def __repr__(self): # definisco funzione per stampare attributi e i loro valori
        return f"{self.__class__.__name__}(nome='{self.__nome}', stand='{self.__bancarelle}', espositori='{self.__espositors}')"

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        try:
            infile=open(file_path, 'r', encoding='utf-8')
            file=csv.reader(infile)
            lista_stand=[] # creo due liste vuote per contenere stand ed espositori
            lista_espositori=[]
            standard=[] # creo liste per dividere gli stand in sottocategorie
            presa=[]
            premium=[]
            for line in file:

                if line[0][0]=='S': # se il primo elemento inizia con S è uno stand
                    if len(line)==4: # se ha solo 4 campi allora è standard
                        bancarella=Stand(line[0],line[1], line[2], line[3]) # creo oggetto Stand
                        standard.append(bancarella) # aggiungo stand a standard
                    else:
                        if line[4].isnumeric(): # se l'ultimo campo è un numero, lo stand ha prese extra
                            bancarella=StandPrese(line[0],line[1], line[2], line[3], line[4]) # creo oggetto Stand prese extra
                            presa.append(bancarella) # aggiungo stand a prese extra
                        else: # altrimenti lo stand è premium
                            bancarella = StandPremium(line[0], line[1], line[2], line[3], line[4]) # creo oggetto Stand premium
                            premium.append(bancarella) # aggiungo stand a premium
                    lista_stand.append(bancarella) # qualsiasi sia il tipo di stand, lo aggiungo alla lista di stand

                elif line[0][0]=='E': # se il primo elemento inizia con E è un espositore
                    expo=Espositori(line[0], line[1], line[2]) # creo oggetto Espositore
                    lista_espositori.append(expo) # aggiungo oggetto alla lista di espositori
                else:
                    raise Exception('Impossibile registrare linea') # altrimenti formato non riconosciuto

            self.__bancarelle=lista_stand # assegno le due liste agli attributi di classe
            self.__espositors=lista_espositori

            '''for i in lista_stand:
                print(i)
            for i in lista_espositori:
                print(i)'''

            infile.close() # chiudo file
        except FileNotFoundError: # scateno errore file
            print('File non trovato')

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

        stand_trovato = None # variabile per verificare esistenza codice stand
        for i in self.__bancarelle: # per ogni stand
            if i.codice==codice_stand: # se il codice inserito corrisponde con il codice dello stand
                stand_trovato=i # il codice dello stand diventa lo stand trovato
                break # esco
        if stand_trovato is None: # se non trovo corrispondenza sollevo errore
            raise Exception("Lo stand non esiste")

        esp_trovato = None # ripeto per il codice espositore
        for i in self.__espositors:
            if i.codice == codice_espositore:
                esp_trovato = i
                break
        if esp_trovato is None:
            raise Exception("L'espositore non esiste")

        if not stand_trovato.disponibile: # richiamo funzione 'disponibile' definita in Stand
            raise Exception("Lo stand non è disponibile")

        for stand in self.__bancarelle: # per ogni stand
            if stand.espositore_assegnato==esp_trovato: # se l'espositore associato allo stand corrisponde con l'espositore inserito
                raise Exception("L'espositore non è disponibile") # l'espositore è già associato a un altro stand

        stand_trovato.assegna_espositore(esp_trovato) # richiamo funzione in Stand per creare associazione



    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for esp in self.__espositors: # per ogni espositore
            for stand in self.__bancarelle: # per ogni stand
                if esp==stand.espositore_assegnato: # se l'espositore corrisponde con l'espositore associato allo stand (definisco __eq__())
                    print(f"{esp} - Stand associato: {stand.codice}") # stampo anche il codice dello stand
                    break # esco dal ciclo
            else:
                print(f"{esp}") # altrimenti stampo solo le informazioni dell'espositore


    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        l=sorted(self.__bancarelle) # creo una lista ordinata per prezzo
        return l
