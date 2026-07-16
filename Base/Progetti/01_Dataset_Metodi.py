# esempio sui dataset e dataframe

#1.	Importazione e Creazione 
import pandas as pd
# Creazione da un dizionario
dati = {
    'Nome': ['Alice', 'Bob', 'Charlie','Everardo','Abelardo','Tantalio','Colonnello','AntonGiulio','Mariano'],
    'Età': [25, 30, 35,20,21,22,50,51,52],
    'Città': ['Roma', 'Milano', 'Napoli','Catania','Catania','Catania','Salerno','Salerno','Salerno']
}
df = pd.DataFrame(dati)
# Caricamento da fonti esterne (es. CSV o Excel)
#risultato=df.to_csv ('./dataset_dataframe/file.csv')
#risultato = df.to_excel('./dataset_dataframe/file.xlsx')

#2. ISPEZIONE DEL DATAFRAME
#peer default prende le prime 5
print(df.head())
#prendo le prime 7
print (df.head(7))

#tipo delle colonne
print(df.info())

#rstituisce alcune statistiche sui dati
# 
print(df.describe())

print(df.shape)
print(df.tail(3))