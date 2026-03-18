# Importiamo il file translator.py e per comodità gli diamo il soprannome 'tr'
import translator as tr

# ISTANZIAZIONE: Creiamo un OGGETTO della classe Translator e lo assegniamo alla variabile 't'.
# Da questo momento, 't' è un traduttore vivo e funzionante, con il suo dizionario interno vuoto.
t = tr.Translator()

# Usiamo l'oggetto 't' per chiamare il suo metodo di caricamento file.
# Lo facciamo QUI (fuori dal ciclo while), così il file viene letto una volta sola all'avvio.
# (Se lo mettessimo nel while, lo rileggerebbe ogni secondo azzerando le modifiche dell'utente!)
t.loadDictionary("dictionary.txt")

# Creiamo un ciclo infinito. Il programma rimarrà intrappolato qui finché non useremo 'break' (opzione 5).
while(True):

    # Chiediamo all'oggetto traduttore di mostrarci il menù.
    t.printMenu()

    # Mettiamo in pausa il programma e aspettiamo che l'utente scriva qualcosa sulla console.
    txtIn = input("\nScegli un'opzione:")

    # Add input control here!

    # .isdigit() è un metodo delle stringhe che restituisce True solo se la stringa contiene SOLO numeri (es "3").
    if not txtIn.isdigit():
        # Se l'utente ha scritto "ciao" o lasciato vuoto, diamo errore...
        print("Errore: devi inserire un numero!")
        # ...e usiamo 'continue' per saltare il resto del codice sottostante e ricominciare il ciclo while da capo.
        continue

    # Ora siamo sicuri che l'input sia un numero, quindi lo convertiamo da testo (stringa) a intero (int)
    scelta = int(txtIn)

    # A seconda del numero scelto, chiediamo all'utente i dati necessari
    # e poi li passiamo all'oggetto Translator ('t') che sa come gestirli.
    if scelta == 1:
        entry = input("Ok, quale parola devo aggiungere? (es. 'aliena ita1 ita2'):\n")
        # Chiamata di metodo sull'oggetto
        t.handleAdd(entry)

    elif scelta == 2:
        query = input("Ok, quale parola aliena devo cercare?\n")
        t.handleTranslate(query)

    elif scelta == 3:
        query = input("Ok, quale parola devo cercare con wildcard? (es. 'ko?ra'):\n")
        t.handleWildCard(query)

    elif scelta == 4:
        print("\n--- CONTENUTO DEL DIZIONARIO ---")
        t.printAll()

    elif scelta == 5:
        # Se l'utente sceglie 5, stampiamo i saluti
        print("Chiusura in corso. Arrivederci!")
        # 'break' distrugge il ciclo while infinito. Il programma arriva alla fine del file e si spegne.
        break

    else:
        # Questo caso copre numeri come 6, 7, 0, ecc. che non sono previsti dal menù.
        print("Opzione non valida. Seleziona un numero da 1 a 5.")