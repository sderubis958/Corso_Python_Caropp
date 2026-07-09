"""
    IF (secondo la condizione) allora f (THEN) ai questo, 
    (ELSE) altrimenti fai quest'altro;
    ELIF (seconda condizione) allora fai questo,
    (ELSE) altrimenti fai quest'altro;

"""
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
