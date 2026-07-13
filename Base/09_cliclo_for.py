"""
    Il ciclo for in python
    
    il ciclo "for" è una struttura di iterazione 
    che permette di ripetere un blocco di codice
    un numero definito di volte oppure di scorrere 
    gli elementi di una sequenza (Lista, stringa, tuple, dizionario, inseme, ecc...) 
    
    
    Perché usare il ciclo "for"?
    
    immaginate di voler stampare 10 volte Ciao😅 
    esempio senza for:
        Ciaooooo 😅
        Ciaooooo 😅
        Ciaooooo 😅
        Ciaooooo 😅
        Ciaooooo 😅
        Ciaooooo 😅
        Ciaooooo 😅
        Ciaooooo 😅
        Ciaooooo 😅
        Ciaooooo 😅
    è lungo, ripetitivo e difficile da modificare🤨
    
    Con il ciclo for basta scrivere:
    
    for i in range(numero desiderato):
        stampa Ciaooooo 😅       
"""

# (variable) i: int
for i in range(10):
    print( 'sono Roxana N°', i, '😅')


"""
    for     -> parola chiave che avvia il ciclo
    i = 0   -> variabile del ciclo
    in      -> significa "dentro"
    range() -> genera un sequenza di numeri passato nel parametro
    :       -> indica l'inizio del blocco
    indentazione importente ricordatevi 🤣🤣🤣🤣🤣🤣🤣
"""

# Esempio 2: Range(inizio, fine)
# for i in range(3, 9):
#     print('numero =>', i)


# Esempio 2: Range(inizio, fine, passo)
for i in range(0, 11, 2):
    print('numero =>', i)


# (variable) i: int
for i in range(10):
    print( 'sono Massa N°', i, '😅')
    

"""
    for     -> parola chiave che avvia il ciclo
    i       -> variabile del ciclo
    in      -> significa "dentro"
    range() -> genera un sequenza di numeri passato nel parametro
    :       -> indica l'inizio del blocco
    indentazione importente ricordatevi 🤣🤣🤣🤣🤣🤣🤣
"""

# Esempio 2: Range(inizio, fine)
# for i in range(3, 9):
#     print('numero =>', i)


# Esempio 2: Range(inizio, fine, passo)
for i in range(0, 11, 2):
    print('numero =>', i)
    



# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# .........
# 5 x 10 = 50

p = range(0, 11)

for i in range(0, 55, 5):
    print('numero=>', i )
    print('5 x', p[i//5], '=', i)

numero = int(input('Inserisci un numer maggiore di 0:'))

for i in range(1,11):
       print(numero, 'x', i, '=', numero * i )

      