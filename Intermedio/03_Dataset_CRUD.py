#Pulizia dei dati

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
print(df.isna().sum()) # NUMEERO ESATTO DI Nan

import numpy as np

# 1. Creiamo un DataFrame di esempio con alcuni valori NaN
dati = {
    "Nome": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Età": [25, np.nan, 30, np.nan, 22],
    "Stipendio": [50000, 60000, np.nan, 45000, np.nan],
    "Città": ["Roma", "Milano", "Napoli", None, "Torino"],
}

df = pd.DataFrame(dati)
print("--- DataFrame Originale ---")
print(df)
print("\nConteggio NaN per colonna:")
print(df.isna().sum())

#Controllare se c'è almeno un NaN nell'intero DataFrame 
print(df.isna().any().any())

# 2. Esempio di ELIMINAZIONE (dropna)
# Eliminiamo le righe dove la Città è mancante
df_drop_citta = df.dropna(subset=["Città"])
print("\n--- DataFrame dopo dropna (rimossa riga 3 senza Città) ---")
print(df_drop_citta)

# 3. Esempio di SOSTITUZIONE (fillna) con la MEDIANA
# Calcoliamo la media dell'età (escludendo i NaN in automatico)
mediana_eta = df["Età"].mean()  # Risultato: 25.0

# Sostituiamo i NaN nella colonna Età
df["Età"] = df["Età"].fillna(mediana_eta)

# 4. Esempio di SOSTITUZIONE con un valore fisso o testuale
df["Stipendio"] = df["Stipendio"].fillna(0)
df["Città"] = df["Città"].fillna("Non specificata")

print("\n--- DataFrame Finale Pulito ---")
print(df)

#Sostituire con dizionario (valori diversi per colonne diverse)
valori_personalizzati = {'Age': 30, 'City': 'Sconosciuto'}
df_sostituito=df.fillna(value=valori_personalizzati)

print("\n--- DataFrame Finale Sostiutuzini ---")
print(df_sostituito)
input("premi un tasto")