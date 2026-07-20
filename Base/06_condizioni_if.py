"""
    IF (secondo la condizione) allora f (THEN) ai questo, 
    (ELSE) altrimenti fai quest'altro;
    ELIF (seconda condizione) allora fai questo,
    (ELSE) altrimenti fai quest'altro;

"""
"""

    Servono a prendere decizioni al programma
    if(SE) else(altrimenti)
    if condizione:
        codie
    else:
        codice


    if(SE) elif(altrimenti sé) else(altrimenti)
    if condizione:
        codie
    elif condizione:
        codice
    elif condizione:
        codice
    elif condizione:
        codice
    else:
        codice
"""

"""
    Gli operatori di confronso sono
    <; >; ==; <=; >=; !=;
    
    Gli operatori logici
    AND(&&) OR(||) NOT(!)
"""
""" 
   If Annidato in python

    Sintassi base:
    if condizione:
        codice eseguito se la condizione è vera

        if altra_condizione:
            codice eseguito se anche seconda la condizione è vera
        else:
            codice eseguito se la seconda condizione è falsa
    else:
        codice eseguito se la prima condizione è falsa
"""
# Esempio 1 Maggiore età
eta = int(input('Inserisci la tua età: '))
patente = True

if eta >= 18:
    print('Sei maggiorenne.')

    if patente:
        print('Poi guidare...🚗')
    else:
        print('Non poi guidare perché non hai la patente...')
else:
    print('Sei minorenne!')

# esempio 2 Voto scolastico

voto = 85

if voto >= 90:
    print("Voto: A - Eccellente!")
elif voto >= 80:
    print("Voto: B - Molto buono.")
elif voto >= 70:
    print("Voto: C - Buono.")
else:
    print("Voto: F \n- Hai bisogno di studiare di più.")
# Usa il codice con cautela.
voto: int = int(input('inserisci il voto: '))

if voto >= 18:
    print('hai superato l\'esame ')
    if voto >= 30:
        print('Complimenti! Hai superato l\'esame con il massimo dei voti')
    else :
        print('Promosso! con un voto', voto)
else :
    print('Non ammesso! perché hai ottenuto un punteggio di', voto)


# esempio di login
input_email = input("Inserisci la tua email: ")
input_password = input("Inserisci la tua password: ")

email = "antonella.r@gmail.com"
password = "Antonella@2026"

if email == "antonella.r@gmail.com" and password == "Antonella@2026":
    print("Accesso consentito. Benvenuto!")
elif email == "carotone.c@libero.it" and password == "PrimoAccesso.2026":    
    print("Accesso consentito. Benvenuto!")

if email == input_email and password == input_password:
    print("Accesso consentito. Benvenuto!")
elif email == "carotone.c@libero.it" and password == "PrimoAccesso.2026":    
    print("Accesso consentito. Benvenuto!")

# ----------------------------------
# Esempio di login
email = 'antonella.r@gmail.com'
password = 'Antonella@2026'

utente = input("📧 Inserisci la mail: ")
password_utente = input('🔐 Inserisci la password: ')

if email == utente and password == password_utente:
    print('Benvenuto nel sistema')
elif email != utente:
    print('📧 Verifica la mail') 
elif password_utente != password:
    print('⚠️ Password errato.\n Riprova')
else:
    print('Accesso negato')
