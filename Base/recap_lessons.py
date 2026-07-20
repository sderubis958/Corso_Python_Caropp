"""
    +; -; *; /; //; %; **
"""

num1 = 12
num2 = 30

somma = num1 + num2

print(somma)

risultato_sott = num2 - num1
print(risultato_sott)

resto_mul = num1 * num2
print(resto_mul)

resto_div = num1 / num2
print(resto_div)

resto_modu = num1 % num2
print(resto_modu)

resto_nin = num1 // num2
print(resto_nin)

resto_pot = num1 ** num2
print(resto_pot)

# 2f (è usato per la formattare i numeri con la virgola mobile)
media = 23.456789

# ERRORE COMUNE
# print(media.2f) # attenzione a questo tipo di AttributeError: 'float' object has no attribute '2f
print(f"La media è: {media:.5f}") # 5 cifre dopo la virgola


# ****************
# formaggiare le stringhe ed i numeri
# ****************
# primo passo
"""
    I tipi di dati in python

    int => intero
    str => stringa
    float => decimali
    bool => boolean

    Dichiarazione di una variabile in python

    nome_variabile = ''
"""

# <class 'str'>
nome_variabile = 'Mattia'
# print(type(nome_variabile))

# <class 'int'>
numero_int = 15
# print(type(numero_int))

# <class 'float'>
numero_deci = 15.85694
# print(type(numero_deci))

# <class 'bool'
boolean_var = True
# print(type(boolean_var))


print("=" * 40)
print("       Concatenazione     ")
print("=" * 40, '\n')

nome = 'Roxana'
cognome = 'Otori'
eta = 35
stipendio = 23.456789

print('Nome ' + nome + ' Cognome ' + cognome + ' età ' + str(eta) + ' stipendio ' + str(stipendio) + '€ al mese')
print('\n') # vai alla riga

print('Nome', nome, 'Cognome', cognome, 'età', str(eta), 'stipendio', str(stipendio), '€ al mese')
print('\n') # vai alla riga

# formattazione
print(f'ciao mi chiamo {nome} - {cognome} ho {eta} anni, guadagno {stipendio}€ al mese\n')
print('\n') # vai alla riga


