studenti = {}

while True:
    print("\n--- Registro Studenti ---\n")
    print("1. AGGIUNGI STUDENTE:")
    print("2. MOSTRA REGISTRO")
    print("3. CALCOLA LA MEDIA")
    print("4. PROMOSSI/BOCCIATI")
    print("0. USCIRE")

    scelta = int(input("\nInserisci la tua scelta: 1"))

    if scelta == 1:
        nome = input("Nome: ")

        voti = []

        for i in range(3):
            while True:
                try:
                    voto = int(input(f"Voto {i+1}: "))
                    voti.append(voto)

                    # Salvataggio nel file (csv e excel)
                    break
                except:
                    print("\n Inserisci un numero valido!")

        studenti[nome] = voti
    elif scelta == 2:
        if not studenti:
            print("\nRegistro vuoto\n")
        else:
            for nome, voti in studenti.items():
                print(nome, voti)
    elif scelta == 3:
        if not studenti:
            print("\nNessuno studente inserito\n")
        else:
            for nome, voti in studenti.items():
                media = sum(voti) / len(voti)
                print(f"{nome} - media: {media:2f}")

    elif scelta == 4:
        if not studenti:
            print("\nNessuno studente inserito\n")
        else:
            for nome, voti in studenti.items():
                media = sum(voti) / len(voti)
                if media >= 18:
                    print(f"{nome} - media: {media:.2f} - PROMOSSO")
                else:
                    print(f"{nome} - media: {media:.2f} - BOCCIATO")
    elif scelta == 0:
        print("\nUscita dal programma...\n")
        break
    else:
        print("\nScelta non valida!\n")

