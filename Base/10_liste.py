"""
    la lista é un insieme  di valori e di oggetti, che possono essere 
    di qualsiasi tipo, e possono essere modificati, aggiunti o rimossi.
    Le liste sono definite tra parentesi quadre [] e gli elementi
    sono separati da virgole.
"""
# Creazione della lista
            # 0      1        2         3          4    
mia_lista= ["Mela", "Banana", "Pera", "Arancia", "Kiwi"] # definizione di una lista

# Creazione della lista
            # 0      1        2         3          4 
colori = ['Rosso', 'Verde', 'Blu', 'Giallo', 'Viola'] # definizione di una lista    
# Stampa della lista
print(mia_lista, '\n\n')

# Accedere ad un elemento della lista
print(colori[1]) # select nome from colori where id = 1

# Modificare un elemento della lista
mia_lista[1] = 'Kiwi' # UPDATE ... set nome = ..
print(mia_lista)


print('=' * 40, '\n')

print(mia_lista, '\n\n') # stampa la lista
print(colori) # stampa la lista

print(colori[1]) # stampa la lista

# Modificare un elemento della lista
colori[1] = 'Nero' # modifica il secondo elemento della lista   
print(colori) # stampa la lista


# Lunghezza della lista 
studenti = ['Massa', 'Antonella', 'Luigi', 'Eduardo', 'Matteo', 'Stefano', 'Lucia', 'Annaritantonia', 'Paolo']
print('=' * 30, '\n') # genera 70 ================================================
print(f"Numero di studenti: {len(studenti)}")
print('=' * 30, '\n') # genera 70

# aggiungere uno o più elementi alla lista
voti = []

voti.append(10) # aggiunge un elemento alla lista # INSERT INTO tabella (ore) values (10)
voti.extend([20, 30, 40, 50]) # aggiunge più elementi alla lista # INSERT INTO tabella (ore) values (10) (20), (30), (40), (50)

print ('lista dei voti:', voti, '\n') # stampa la lista

frutti = ['Mela', 'Banana', 'Pera', 'Arancia', 'Kiwi'] # definizione di una lista
frutti.insert(1, 'Fragola') # inserisce un elemento alla lista in una posizione specifica
print(frutti) # stampa la lista

# eliminare uno o più elementi dalla lista
frutti.remove('Pera') # DELETE FROM frutti WHERE nome = 'Pera';     
print(frutti) # stampa la lista

print(studenti) # stampa la lista
studenti.pop(4) # elimina l'elemento in posizione 4
print(studenti) # stampa la lista

# svuotare la lista
utenti = ['Massa', 'Anntonella', 'Luigi', 'Eduardo', 'Matteo', 'Stefano', 'Lucia', 'Annaritantonia', 'Paolo']
print(utenti,'\n', 'Prima della cancellazione') # stampa la lista
utenti.clear() # elimina tutti gli elementi della lista - DELETE utenti (elimina lista)

print('***Lista vuota ***', utenti) # stampa la lista

for i in range(len(studenti)):
    print(f"Studente {i+1}: {studenti[i]}") # stampa la lista
   # print('studeinti in ordine alfabetico:', sorted(studenti)) # stampa la lista in ordine alfabetico   
    #print('studente, i, studenti(i):', studenti[i]) # stampa la lista
print('=' * 40, '\n')
for i in range(len(studenti)):
    print('Nome ', i, studenti[i])


print('=' * 40, '\n')
