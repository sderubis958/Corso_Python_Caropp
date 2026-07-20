"""_summary_

    Importare il file Esercizio2_Pulisci_Dataset.csv, 
    determinare e rappresentare le seguenti informazioni
******************************************************************************************
1. determinare se ci sono valori nan o righe duplicate
2. Riepilogo delle righe e colonne del file
3. Grafico ad istogrammi del totale di spesa di ogni persona
4. Grafico ad istogrammi del totale di spesa di ogni voce di costo (colonna tipo)
5. Diagramma a torta delle spese di Silvio confrontato con quello di Marisa
******************************************************************************************
"""

#importiamo le librerie
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os #per avere accesso alla console
import sys
import importlib.util
plt.ion()  # cosi i grafici non bloccano lo script

def print_dataset_info(file_path):
    """
    Stampa il nome del file e il percorso assoluto del dataset.
    """
    try:
        # Controllo se il file esiste
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Il file '{file_path}' non esiste.")

        # Nome del file
        file_name = os.path.basename(file_path)

        # Percorso assoluto
        absolute_path = os.path.abspath(file_path)

        print(f"Nome del dataset: {file_name}")
        print(f"Percorso completo: {absolute_path}")
        #input ("sto aspettando...")

    except Exception as e:
        print(f"Errore: {e}")

# Esempio di utilizzo
# dataset_path = "data/dataset.csv"  # Modifica con il tuo percorso
dataset_path = "C:/Data_Python/Source_Py/Dataset_DataFrame/Esercizio2_Pulisci_Dataset.csv"  # Modifica con il tuo percorso
print_dataset_info(dataset_path)
input ("sto aspettando...")
def pulisci_schermo():
    os.system('cls' if os.name == 'nt' else 'clear')
"""
    


"""
import pandas as pd
# try to import chardet for encoding detection; if unavailable, we'll fallback to common encodings
try:
    import chardet
    _HAS_CHARDET = True
except Exception:
    chardet = None
    _HAS_CHARDET = False

def smart_load(path):
    # 1️⃣ Rileva encoding automaticamente (usa chardet se disponibile, altrimenti prova encodings comuni)
    with open(path, "rb") as f:
        raw = f.read()

    enc = None
    if _HAS_CHARDET:
        try:
            enc = chardet.detect(raw).get("encoding")
        except Exception:
            enc = None

    if not enc:
        for e in ("utf-8", "cp1252", "latin1"):
            try:
                raw.decode(e)
                enc = e
                break
            except Exception:
                continue

    if not enc:
        enc = "utf-8"

    # 2️⃣ Prova a capire il separatore
    possible_separators = [",", ";", "\t", "|"]
    sep_found = None

    # Legge solo la prima riga per analizzare il separatore
    try:
        first_line = raw.splitlines()[0].decode(enc)
    except Exception:
        first_line = raw.splitlines()[0].decode("latin1", errors="ignore")

    for sep in possible_separators:
        if sep in first_line:
            sep_found = sep
            break

    # Se non trova nulla, assume CSV "strano"
    if sep_found is None:
        sep_found = ";"

    # 3️⃣ Carica il file
    try:
        df = pd.read_csv(path, sep=sep_found, encoding=enc)
    except Exception:
        # Se non è CSV, prova Excel
        df = pd.read_excel(path)

    # 4️⃣ Pulisce i nomi delle colonne
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace("\ufeff", "")  # BOM invisibile

    # 5️⃣ Converte automaticamente le colonne numeriche
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

    return df
sep_found = None
print("separatore trovato = ", sep_found)
df = None
##########################################
def cercanulli(dataset):
    brisultato= dataset.isna().any().any()   # per togliere i null
    return brisultato

pulisci_schermo ()
input("\nrilevamento dati nulli nel dataset csv...\n")
# passo 1: caricamento dati (csv)
percorso = r"C:\Data_Python\Source_Py\Dataset_DataFrame"
dataset = pd.read_csv(os.path.join(percorso, "Esercizio2_Pulisci_Dataset.csv"), sep=";")
print(dataset)
input ("sto aspettando...")
Nulli=cercanulli(dataset)
if  Nulli:
    print("Errore: presenza di dati nulli nel dataset: ", dataset_path)
    sys.exit(1)

num_nulli=dataset.isna().sum()
if num_nulli is False:
    print ("\nnum record nulli = 0\n", num_nulli)
else:
    print("\nesistono record nulli =", num_nulli)

print(dataset.isna().sum())
## input("\npremi un tastino piccolino...\n")
input("\nrilevamento numero righe duplicate...\n")

# rilevamento righe duplicate

numero_duplicati = dataset.duplicated().sum()

if numero_duplicati > 0:
    print(f"\nSono presenti {numero_duplicati} righe duplicate.")

    print("\nRighe duplicate:")
    print(dataset[dataset.duplicated(keep=False)])

    # Elimina le righe completamente duplicate
    df_ripulito = dataset.drop_duplicates()

    print("\nDataset ripulito:")
    print(df_ripulito)
else:
    print("\nIl dataset non contiene righe duplicate.")
    df_ripulito = dataset.copy()

input("\nriepilogo righe e colonne del dataset...\n")

# rilevamento righe e colonne del dataset 

df=dataset.describe()
print(df)
#input("\npremi un tastino piccolino...\n")

"""
Nel caso in cui desideriamo contare il numero di dati specifici all'interno di una colonna, 
possiamo usare il .value_counts () metodo. 
Ora vediamo un esempio dove contiamo quale tipi di metodi sono stati usati negli ordini.
"""
input("\nconta i valori specifici della colonna Nome ...\n")

pulisci_schermo()
count_nome = df["Nome"].value_counts()
count_tipo = df["Tipo"].value_counts()
print(dataset["Nome"].value_counts())

print(count_nome)
print(count_tipo)
print(dataset.columns)
input("\npremi un tastino piccolino...\n")
df = dataset
#print("media : " + str( df["Importo"].mean() ) )
#print("MAX : " + str( df["Importo"].max() ) )
#print("MIN : " + str( df["Importo"].min()) )
#print("COUNT : " + str( df["Nome"].count()) )
df['Importo'] = df['Importo'].str.replace('.', '').str.replace(',', '.').astype(float)

print(f"media : {df['Importo'].mean()}")
print(f"MAX : {df['Importo'].max()}")
print(f"MIN : {df['Importo'].min()}")
print(f"COUNT : {df['Nome'].count()}")

input("\npremi un tastino piccolino...\n")

"""
    inizio produzione grafici:
    3. Grafico ad istogrammi del totale di spesa di ogni persona
    4. Grafico ad istogrammi del totale di spesa di ogni voce di costo (colonna tipo)
    5. Diagramma a torta delle spese di Silvio confrontato con quello di Marisa

"""
# 3. Grafico ad istogrammi del totale di spesa di ogni persona
import matplotlib.pyplot as plt
import pandas as pd

# Raggruppa per persona e somma gli importi
totale_per_persona = dataset.groupby("Nome")["Importo"].sum()

# Grafico ad istogrammi
plt.figure(figsize=(10,6))
totale_per_persona.plot(kind="bar", color="skyblue")

plt.title("Totale di spesa per persona")
plt.xlabel("Persona")
plt.ylabel("Totale Spesa (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

input("\n Fermati ad ammirare il lavoro svolto ...\n")

# 4. Grafico ad istogrammi del totale di spesa di ogni voce di costo (colonna tipo)
##import matplotlib.pyplot as plt
##import pandas as pd

# Raggruppa per Tipo di voce e somma gli importi
totale_per_tipo = dataset.groupby("Tipo")["Importo"].sum()

# Grafico ad istogrammi
plt.figure(figsize=(10,6))
totale_per_tipo.plot(kind="bar", color="green")

plt.title("Totale di spesa per tipo (voce di costo)")
plt.xlabel("Tipo Costo")
plt.ylabel("Totale Spesa (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

input("\n Fermati ad ammirare il lavoro svolto ...\n")

#  5. Diagramma a torta delle spese di Silvio confrontato con quello di Marisa

## import matplotlib.pyplot as plt

# Filtra le spese di Silvio e Marisa
spesa_silvio = dataset[dataset["Nome"] == "Silvio"]["Importo"].sum()
spesa_marisa = dataset[dataset["Nome"] == "Marisa"]["Importo"].sum()

# Prepara i dati
valori = [spesa_silvio, spesa_marisa]
etichette = ["Silvio", "Marisa"]

# Grafico a torta
plt.figure(figsize=(8,8))
plt.pie(valori, labels=etichette, autopct="%1.1f%%", startangle=90, colors=["skyblue", "lightgreen"])
plt.title("Confronto spese: Silvio vs Marisa")
plt.show()

input("\n Fine lavoro svolto ...\n")

"""
    creazione di un grafico a torta contenente tutte le spese divise per nomi

"""
# Mantieni solo le prime 4 colonne
## df = df[['Data', 'Importo', 'Tipo', 'Nome']]

# Converti Importo da formato europeo
## df['Importo'] = df['Importo'].str.replace('.', '').str.replace(',', '.').astype(float)

# Somma delle spese per Nome
totali = df.groupby('Nome')['Importo'].sum()

# Identifica il massimo
max_nome = totali.idxmax()

# Prepara explode
explode = [0.1 if nome == max_nome else 0 for nome in totali.index]

# Grafico
plt.figure(figsize=(8,8))
plt.pie(totali, labels=list(totali.index), autopct='%1.1f%%', explode=explode, shadow=True)
plt.title("Spese totali per componente")
plt.show()

input("\n Fine lavoro svolto ...\n")
