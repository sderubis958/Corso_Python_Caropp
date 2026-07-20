# esempio sui dataset e dataframe

#1.	Importazione e Creazione 
import pandas as pd
import os
pd.options.display.float_format = '${:,.2f}'.format

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
# Caricamento da fonti esterne (es. CSV o Excel)
#risultato=df.to_csv ('./dataset_dataframe/file.csv')
#risultato = df.to_excel('./dataset_dataframe/file.xlsx')

#2. ISPEZINE DEL DATAFRAME
#peer default prende le prime 5
print(df.head())

#prendo le prime 7
print (df.head(7))

#tipo delle colonne
print(df.info())

#rstituisce alcune statistichee sui dati
# 
print(df.describe())

print(df.shape)

#leggo dalla fine
print (df.tail(3))

pulisci_console()

#Selezione e Indicizzazione
print("Selezione e Indicizzazione")
Nomi=df['Nome'] # tutti i valori della colonna Nome e quindi è unaa SERIE
print(Nomi)

Nomi_Citta=df[['Nome', 'Città']]
print("questo è un datafram di 2 clonne")
print(Nomi_Citta)

#loc e iloc pr selezionare la "cella"

#selezionare in base al nome della cella
valore1=df.loc[0, 'Nome'] 
valore2=df.loc[1, 'Nome'] 
print(f"{valore1}----{valore2}")
 

#selezionare in base ALLA POSIZIONE della cella
valore1=df.iloc[0, 0] 
valore2=df.iloc[0, 1] 

valore3=df.iloc[1, 0] 
valore4=df.iloc[1, 1] 

#print (format(valore1, "----", valore2, "-----", valore3, "-----", valore4))
def pulisci_console():
    """
    Clears the console screen.
    Works on Windows, macOS , and Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')    
input("premi un tasto per continuare")
pulisci_console()

#Filtro dei Dati (Filtro Booleano)

# Seleziona solo le righe dove l'Età è maggiore di 28
df_risultato=df[df['Età'] > 28]
print (df_risultato)
#Seleziona solo le righe dove la citta è salerno
df_risultato=df[df['Città'] =="Salerno"]
print (df_risultato)

pulisci_console()
#Manipolazione e Modifica
#•	Aggiungere una colonna

df['Stipendio'] = [2000, 2500, 3000,1000,1000,1000,1000,1000,-1]


#df['Stipendio'] = [2000, 2500, 3000] QUSTA DA ERRORE PERCHE DEVE AVERE LA STESSA DIMENSIONE DELLE ALTRE COLONNE
print(df)
"""
#RIMUOVERE una colonna
df_modificato=df.drop(columns=['Stipendio'])
pulisci_console()
print(f"dataframe modificato {df_modificato}")
print(f"dataframe originario {df}")

print(df_modificato)
"""  

#RIMUOVERE una colonna
df_modificato=df.drop(columns=['Stipendio'])
pulisci_console()
print("dataframe modificato ")
print(df_modificato)
print("-------------------------------------------------------------------------------")
print("dataframe modioriginario")
print(df)