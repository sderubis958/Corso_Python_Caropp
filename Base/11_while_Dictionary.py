"""
    Dictionary in Python
    Cos'è un dictionary?
    ----------------------

    Un dizionario è una struttura cha salva dati in questo modo
    chiave -> valore
"""

# Esempio reale:
# nome = 'mario'
# eta = 20
# citta = 'Roma'

studente = {
    'nome': 'Mario',
    'cognome': 'Rossi',
    'eta': 25,
    'citta': 'Bologna',
    'corsi': [
        'Python', 'SQL Server', 'Pandas', 'MatplotLib', 'FastApi'
    ],
    'telefono': '+39-333-1234567'
}
# Accedere ai valori
print(studente['corsi'])
print(studente.get('telefono'))

# Modificare un volore
studente['eta'] = 26
print(studente['eta'])

print(studente) # stampa il dizionario
print(studente['nome']) # stampa il valore della chiave 'nome'
print(studente['corsi']) # stampa il valore della chiave 'corsi'

# Ciclo su dictionary
# Esempio 1: Solo valori
for key in studente:
    print(key)

#  Esempio 2: Solo valori
for value in studente.values():
    print(value)

# Esempio 3: Chiavi e valori
for key, value in studente.items():
 #   print('Chiave => ', key, '\nValore => ', value)
    print('Chiave => ', key, ' e valore => ', value)

for key, value in studente.items():
    print(key, value)

# Dictionry con Liste (Avanzato)
utenti = {
    "name": "Mario",
    "age": 30,
    "isStudent": False,
    "courses": {
        "Math": ["Algebra", "Geometry", "Trigonometry","Analysis"],
        "Science": ["Biology", "Chemistry", "Physics", "Astronomy"],
    },
    "address": {
        "city": ["Ferrara", "Bologna", "Roma", "Milano", "Napoli", "Torino", "Genova", "Venezia", "Verona", "Padova"],
        "country": ["Italy", "France", "Cameroun", "Germany", "Spain", "Portugal", "Greece", "Netherlands", "Belgium", "Switzerland", "Austria"]
    }
}

for key, value in utenti.items():
    print(key, value)


studenti = {
    'Stefano': [5, 10, 28, 30, 26, 7],
    'Massa': [10, 3, 18, 25, 30,],
    'Lucia': [50, 40, 30, 20, 10]
}

for nome, voti in studenti.items():
    media = sum(voti) / len(voti)
    print(f"Nome: {nome} - Voti: {voti} - Media: {media:.2f}")
    print(f"Nome: {nome} - Voti: {voti}")

# Ciclo while con dictionary
# Esempio 1: Solo valori
numero = 10
while True:
    numero = numero - 1
    if numero == 0:
        print('Numero è uguale a zero, esco dal ciclo while')
        break
    else:
        print('Numero è uguale a ', numero, ' e continuo il ciclo while')   
    print('Ciaoooooo :) :) ')
    
