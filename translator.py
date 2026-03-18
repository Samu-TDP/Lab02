# Importiamo la classe Dictionary dal file dictionary.py
from dictionary import Dictionary

class Translator:

    def __init__(self):
        # COMPOSIZIONE: Appena creiamo un oggetto Translator, lui crea automaticamente al suo interno
        # un oggetto Dictionary e lo salva nel suo attributo 'self.diz'.
        # In questo modo, il Translator può usare tutte le funzioni di Dictionary.
        self.diz = Dictionary()

    def printMenu(self):
        # Metodo semplicissimo che esegue solo delle stampe a schermo.
        print("\n--- Translator Alien-Italian ---")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il Dizionario")
        print("5. Exit")

    def loadDictionary(self, filename: str):
        # Usiamo un blocco try-except. Serve a "catturare" gli errori in modo elegante.
        # Se il file non esiste, il programma non andrà in crash, ma eseguirà l'except.
        try:
            # Apriamo il file in lettura ('r'). Il costrutto 'with' è fantastico perché chiude
            # automaticamente il file alla fine del blocco, anche se ci sono errori.
            with open(filename, 'r', encoding='utf-8') as file:
                # Iteriamo direttamente sul file: ad ogni giro, 'line' è una riga del testo.
                for line in file:
                    # Puliamo la stringa:
                    # .strip() toglie gli spazi e il carattere di 'a capo' (\n) all'inizio e alla fine.
                    # .lower() trasforma tutto in minuscolo per rendere la ricerca Case Insensitive.
                    # .split() taglia la frase ovunque ci sia uno spazio, creando una lista di parole.
                    # Esempio: "Koira cane cagnolino" diventa ["koira", "cane", "cagnolino"]
                    elementi = line.strip().lower().split()

                    # Controlliamo che la riga avesse almeno 2 parole (l'aliena e almeno una traduzione).
                    if len(elementi) >= 2:
                        # La parola aliena è sempre la prima (indice 0 della lista).
                        parola_aliena = elementi[0]
                        # Le traduzioni sono tutte le parole restanti.
                        # elementi[1:] usa lo "slicing": prende la lista dall'elemento di indice 1 fino alla fine.
                        traduzioni = elementi[1:]

                        # Validazione: .isalpha() controlla che una stringa contenga SOLO lettere dell'alfabeto (niente numeri o punteggiatura).
                        # all(...) controlla che questa condizione sia vera per TUTTE le traduzioni della lista.
                        if parola_aliena.isalpha() and all(t.isalpha() for t in traduzioni):
                            # DELEGAZIONE: Il Translator non inserisce i dati da solo.
                            # Chiama il metodo addWord dell'oggetto Dictionary (self.diz) passandogli i dati puliti.
                            self.diz.addWord(parola_aliena, traduzioni)

        # Se il file non si chiama "dictionary.txt" o non c'è, Python lancia un FileNotFoundError. Lo gestiamo qui:
        except FileNotFoundError:
            print(f"Attenzione: Il file '{filename}' non è stato trovato.")

    def handleAdd(self, entry: str):
        # Questo metodo elabora l'input digitato dall'utente per aggiungere una parola (es. "kissa gatto micio")
        elementi = entry.strip().lower().split()

        # Se l'utente ha scritto solo una parola (es. "kissa") o ha premuto invio a vuoto, c'è un errore.
        if len(elementi) < 2:
            print("Errore: Inserisci la parola aliena seguita da almeno una traduzione.")
            return  # 'return' a vuoto interrompe immediatamente l'esecuzione del metodo.

        parola_aliena = elementi[0]
        traduzioni = elementi[1:]

        # Stesso controllo sulle lettere dell'alfabeto fatto durante la lettura del file.
        if not parola_aliena.isalpha() or not all(t.isalpha() for t in traduzioni):
            print("Errore: Sono ammessi solo caratteri alfabetici [a-zA-Z].")
            return

        # Se i controlli sono passati, deleghiamo al dizionario l'aggiunta in memoria.
        self.diz.addWord(parola_aliena, traduzioni)
        print("Aggiunta con successo!")

    def handleTranslate(self, query:str):
        # Pulizia dell'input utente
        query = query.strip().lower()

        # Se ci sono numeri o spazi, rifiutiamo.
        if not query.isalpha():
            print("Errore: Inserire solo caratteri alfabetici.")
            return

        # Chiediamo al dizionario di cercare la parola. Ci tornerà una lista (piena o vuota).
        risultati = self.diz.translate(query)

        # In Python, le liste vuote [] sono considerate "False". Le liste con elementi sono "True".
        if risultati:
            # Se la lista ha roba dentro, la stampiamo.
            print(f"Traduzioni: {risultati}")
        else:
            # Se la lista è vuota
            print("Nessuna traduzione trovata per questa parola.")

    def handleWildCard(self,query:str):
        query = query.strip().lower()

        # Dobbiamo assicurarci che l'utente abbia inserito ESATTAMENTE un solo "?" (.count('?') != 1)
        # e che, se togliamo il "?", tutto il resto sia composto da lettere alfabetiche.
        if query.count('?') != 1 or not query.replace('?', '').isalpha():
            print("Errore: Formato non valido. Usa un solo '?' e caratteri alfabetici.")
            return

        # Deleghiamo la ricerca complessa al Dictionary
        risultati = self.diz.translateWordWildCard(query)

        if risultati:
            # Iteriamo sul dizionario dei risultati
            for aliena, traduzioni in risultati.items():
                # Stampiamo ogni singola traduzione per quella parola aliena
                for t in traduzioni:
                    print(t)
        else:
            print("Nessuna corrispondenza trovata.")

    def printAll(self):
        # Chiediamo al Dictionary di restituirci tutto quello che ha in pancia
        tutto = self.diz.getAll()
        # Per ogni chiave (aliena) e valore (traduzioni)...
        for aliena, traduzioni in tutto.items():
            # ...stampiamo in modo ordinato
            print(f"{aliena} : {traduzioni}")