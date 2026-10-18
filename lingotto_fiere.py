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
        self.__bancarelle=[]
        self.__espositors=[]


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome=nome

    @property
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

    '''@property
    def assegnato(self):
        return self.__assegnato

    @assegnato.setter
    def assegnato(self, assegnato):
        self.__assegnato = assegnato'''

    def __str__(self):
        return f"{self.__nome}"

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        try:
            infile=open(file_path, 'r', encoding='utf-8')
            file=csv.reader(infile)
            lista_stand=[]
            lista_espositori=[]
            standard=[]
            presa=[]
            premium=[]
            for line in file:
                if line[0][0]=='S':
                    if len(line)==4:
                        bancarella=Stand(line[0],line[1], line[2], line[3])
                        standard.append(bancarella)
                    else:
                        if line[4].isnumeric():
                            bancarella=StandPrese(line[0],line[1], line[2], line[3], line[4])
                            presa.append(bancarella)
                        else:
                            bancarella = StandPremium(line[0], line[1], line[2], line[3], line[4])
                            premium.append(bancarella)
                    lista_stand.append(bancarella)

                elif line[0][0]=='E':
                    expo=Espositori(line[0], line[1], line[2])
                    lista_espositori.append(expo)
                else:
                    raise Exception('Impossibile registrare linea')

            self.__bancarelle=lista_stand
            self.__espositors=lista_espositori

            '''for i in lista_stand:
                print(i)
            for i in lista_espositori:
                print(i)'''

            infile.close()
        except FileNotFoundError:
            print('File non trovato')

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

        stand_trovato = None
        for i in self.__bancarelle:
            if i.codice==codice_stand:
                stand_trovato=i
                break
        if stand_trovato is None:
            raise Exception("Lo stand non esiste")

        esp_trovato = None
        for i in self.__espositors:
            if i.codice == codice_espositore:
                esp_trovato = i
                break
        if esp_trovato is None:
            raise Exception("L'espositore non esiste")

        if not stand_trovato.disponibile:
            raise Exception("Lo stand non è disponibile")

        for stand in self.__bancarelle:
            if stand.espositore_assegnato==esp_trovato:
                raise Exception("L'espositore non è disponibile")

        stand_trovato.assegna_espositore(esp_trovato)



    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for esp in self.__espositors:
            for stand in self.__bancarelle:
                if esp==stand.espositore_assegnato:
                    print(f"{esp} - Stand associato: {stand.codice}")
                    break
            else:
                print(f"{esp}")


    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        l=sorted(self.__bancarelle)
        return l
