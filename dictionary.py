# Definizione della classe. In Python, i nomi delle classi iniziano con la lettera Maiuscola (CamelCase).
# Una classe è come il "progetto" o lo "stampo" per creare oggetti.
class Dictionary:
    # Metodo costruttore: __init__ viene chiamato automaticamente ogni volta che creiamo un NUOVO oggetto di questa classe.
    # 'self' è obbligatorio come primo parametro in tutti i metodi di istanza.
    # Rappresenta l'oggetto stesso che stiamo creando/usando (equivale a 'this' in Java).

    def __init__(self):
        # self.dizionario = {} crea un ATTRIBUTO DI ISTANZA.
        # Significa che ogni oggetto 'Dictionary' che creeremo avrà il SUO dizionario personale e vuoto.
        # Usiamo un dizionario Python (dict) in cui:
        # CHIAVE = la parola aliena (stringa)
        # VALORE = una lista di traduzioni (lista di stringhe)
        self.dizionario = {}

    # Metodo per aggiungere una parola e le sue traduzioni.
    # Riceve 'self' (l'oggetto corrente), 'parola_aliena' (una stringa) e 'traduzioni' (una lista di stringhe).
    def addWord(self,parola_aliena: str, traduzioni: list):
        # Prima di tutto, controlliamo se la parola aliena NON è ancora presente nelle chiavi del nostro dizionario.
        if parola_aliena not in self.dizionario:
            # Se non esiste, creiamo la "voce" nel dizionario e le assegniamo una lista vuota [].
            # Questo prepara il terreno per potervi inserire le traduzioni.
            self.dizionario[parola_aliena] = []
        # Ora iteriamo (cicliamo) su ogni singola traduzione presente nella lista in arrivo.
        for trad in traduzioni:
             # Controlliamo se questa specifica traduzione NON è già presente nella lista di traduzioni
            # associata a quella parola aliena (per evitare doppioni come "cane cane").
            if trad not in self.dizionario[parola_aliena]:
                # Se è una traduzione nuova, la "appendiamo" (aggiungiamo alla fine) della lista.
                # self.dizionario[parola_aliena] accede alla lista, .append(trad) inserisce l'elemento.
                self.dizionario[parola_aliena].append(trad)


    # Metodo per cercare la traduzione esatta di una singola parola aliena.
    def translate(self,parola_aliena: str):
        # I dizionari Python hanno un metodo comodissimo chiamato .get(chiave, valore_di_default).
        # Cerca la 'parola_aliena' nel dizionario:
        # - Se la trova, restituisce il suo valore (ovvero la lista delle traduzioni).
        # - Se NON la trova, non va in errore (KeyError), ma restituisce il valore di default, ovvero una lista vuota [].
        return self.dizionario.get(parola_aliena, [])

    # Metodo per gestire la ricerca con il carattere jolly (wildcard '?').
    def translateWordWildCard(self,wildcard_query: str):
        # Creiamo un nuovo dizionario vuoto locale (non ha 'self.' perché serve solo dentro questa funzione, non è dell'oggetto).
        # Conterrà tutti i "match" (le corrispondenze) che troviamo.
        risultati = {}

        # Il metodo .items() del dizionario ci permette di scorrere sia le chiavi (parola) che i valori (traduzioni) contemporaneamente.
        for parola, traduzioni in self.dizionario.items():
            # Condizione base: se la lunghezza della parola aliena nel dizionario è diversa dalla query (es. "ali?no" = 6 lettere),
            # è inutile fare il controllo carattere per carattere. Controlliamo solo quelle lunghe uguali.
            if len(parola) == len(wildcard_query):
                # Usiamo una variabile "bandiera" (flag) impostata a True.
                # Assumiamo che le due parole siano identiche finché non troviamo prove del contrario.
                match = True

                # Usiamo zip() per accoppiare carattere per carattere la 'parola' del dizionario e la 'wildcard_query'.
                # Esempio: zip("koira", "k?ira") -> coppie: (k,k), (o,?), (i,i), (r,r), (a,a).
                for char_alieno, char_query in zip(parola, wildcard_query):
                    # Se il carattere della query NON è il jolly '?' E INOLTRE i due caratteri sono diversi...
                    if char_query != '?' and char_alieno != char_query:
                        # ...allora le due parole non corrispondono! Abbassiamo la bandiera a False.
                        match = False
                        # Usiamo 'break' per interrompere subito questo ciclo for interno: inutile controllare le altre lettere.
                        break

                        # Una volta finito di controllare tutte le lettere, se la bandiera è rimasta True...
                if match:
                    # ...abbiamo trovato una parola aliena compatibile! La salviamo nei risultati.
                    risultati[parola] = traduzioni

        # Alla fine del ciclo su tutto il dizionario, restituiamo i risultati trovati al programma chiamante.
        return risultati

        # Metodo per recuperare l'intero dizionario.
    def getAll(self):
        # Restituisce semplicemente l'attributo di istanza intero.
        return self.dizionario

