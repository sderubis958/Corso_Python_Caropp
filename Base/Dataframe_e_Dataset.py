# esempio sui dataset e dataframe

#1.	Importazione e Creazione 
import pandas as pd
# Creazione da un dizionario
dati = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Età': [25, 30, 35],
    'Città': ['Roma', 'Milano', 'Napoli']
}
df = pd.DataFrame(dati)
# Caricamento su fonti esterne (es. CSV o Excel)
risultato = df.to_csv ('./Dataset_DataFrame/01file.csv')
risultato = df.to_excel('./Dataset_DataFrame/01file.xlsx')