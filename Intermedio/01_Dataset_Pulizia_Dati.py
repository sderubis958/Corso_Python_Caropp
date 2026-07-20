#Pulizia deei daati

import pandas as pd
import os

def pulisci_console():
    # 'nt' indica Windows, 'posix' indica macOS e Linux
    os.system('cls' if os.name == 'nt' else 'clear')


# Creazione da un dizionario
dati = {
    'Nome': ['Alice', 'Bob', 'Charlie','Nome1','Nome2','Nome3','Cognome','Cognome2','Cognome3'],
    'Età': [25, 30, 35,20,21,22,50,51,52],
    'Città': ['Roma', 'Milano', 'Napoli','Catania','Catania','Catania','Salerno','Salerno','Salerno']
}
df = pd.DataFrame(dati)

#1. rimuovere i duplicati in un DataFrame di Pandas
df.drop_duplicates(inplace=False)# conservo la prima occorrenza
print(df)

df_ripulito=df.drop_duplicates(subset=['Città'], keep='first', inplace=False)#inplacee=True modifica il dataframe di partenza
print(df_ripulito)
#df.drop_duplicates(keep=False, inplace=True) ELIMINA TUTTI I DUPLICATI

#Trovare i Nan
print(df.isna().sum()) # NUMERO ESATTO DI DUPLICATI