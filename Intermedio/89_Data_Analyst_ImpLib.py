#importiamo le librerie
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os #per avere accesso alla console
import sys

plt.ion()  # cosi i graafici non bloccano lo script

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

    except Exception as e:
        print(f"Errore: {e}")

# Esempio di utilizzo
# dataset_path = "data/dataset.csv"  # Modifica con il tuo percorso
dataset_path = "C:/Data_Python/Source_Py/Dataset_DataFrame/EsempioPython.csv"  # Modifica con il tuo percorso
print_dataset_info(dataset_path)

def pulisci_schermo():
    os.system('cls' if os.name == 'nt' else 'clear')

def cercanulli(dataset):
    brisultato= dataset.isna().any().any()   # per togliere i null
    return brisultato

# passo 1: caricamento dati (csv)
percorso = r"C:\Data_Python\Source_Py\Dataset_DataFrame"
dataset = pd.read_csv(os.path.join(percorso, "EsempioPython.csv"))
print(dataset)

Nulli=cercanulli(dataset)
if  not Nulli:
    print("Errore: presenza di dati nulli nel dataset: ", dataset_path)
    sys.exit(1)

print(dataset.isna().sum())
input("\npremi un tastino piccolino...\n")
#passo 2: SOMMA, MEDIA, MAX, MIN e COUNT
#per fare queste funzioni ci occorre prima il metodo describe
"""
genera un riepilogo statistico dei dati. Di base, analizza le colonne numeriche 
calcolando: conteggio dei valori validi, media, deviazione standard, valore minimo, massimo e i quartili (25%, 50% o mediana, 75%).
Esclude in automatico i valori mancanti (NaN)
"""
df=dataset.describe()
print(df)
input("\npremi un tastino piccolino...\n")

#passo3
#esempi pratici:
"""
#Vogliamo calcolare le vendite totali dei negozi 
vendite_totali = dataset["Quantity"].sum()
print(vendite_totali)
"""
pulisci_schermo()
vendite_totali = dataset["Quantity"].sum()
print(f"vendite totali-->{vendite_totali}")
input("\npremi un tastino piccolino...\n")
#passo 4
"""
Quindi, se vogliamo selezionare una colonna specifica, selezioniamo prima con parentesi quadre ["colonna"]
e poi usa il metodo di cui abbiamo bisogno (.sum (), .mean (), .count (), ecc.). 
Ad esempio, calcoliamo la media, il max e il min delle quantità vendute dei negozi.
"""
pulisci_schermo()
print("media : " + str( dataset["Quantity"].mean() ) )
print("MAX : " + str( dataset["Quantity"].max() ) )
print("MIN : " + str( dataset["Quantity"].min()) )
input("\npremi un tastino piccolino...\n")
#passo 5
"""
Nel caso in cui desideriamo contare il numero di dati specifici all'interno di una colonna, 
possiamo usare il .value_counts () metodo. 
Ora vediamo un esempio dove contiamo quale tipi di metodi sono stati usati negli ordini.
"""
pulisci_schermo()
print(dataset["Order_method_type"].value_counts())
input("\npremi un tastino piccolino...\n")
#passo 6
"""
Possiamo facilmente sostituire la funzione IF di Excel utilizzando Numpy.
Immaginiamo di voler sapere quali vendite sono superiori ad una quantità di 500 pezzi
 e creare quindi un nuovo attributo per ogni riga la dove la vendita risulta maggiore o minore di questa quantità.
"""
pulisci_schermo()
dataset["Vendite_all_ingrosso"] = np.where(dataset['Quantity'] >500,  'vendita ad un negozio', 'vendita per privato')
print(dataset)
input("\npremi un tastino piccolino...\n")

#passo 5
"""
Nel caso in cui desideriamo contare il numero di dati specifici all'interno di una colonna, 
possiamo usare il .value_counts () metodo. 
Ora vediamo un esempio dove contiamo quale tipi di metodi sono stati usati negli ordini.

"""
print(dataset["Order_method_type"].value_counts())
input("premi un tasto")

#STUDIAMO SOLO L ITALIA
dataset_italia = dataset[dataset["Retailer_country"]=="Italy"]
print(dataset_italia)
input("premi un tasto")

#STUDIAMO SOLO L ITALIA
dataframe_italia = dataset[dataset["Retailer_country"]=="Italy"]
print(dataframe_italia)
input("\npremi un tastino piccolino...\n")

# passo 6
#lo salvo in un foglio excel
"""#passo 6
#STUDIAMO SOLO L ITALIA
dataframe_italia = dataset[dataset["Retailer_country"]=="Italy"]
print(dataframe_italia)  
#lo slvo in un foglio eexceel

path_excel=f"C:\\analisi\\cliente1\\dati_xcel"
dataframe_italia.to_excel("italia.xlsx", index=False)# con True creo anche una colonna con l indice
"""

dataframe_italia.to_excel('italia.xlsx', index=False)
dataframe_italia.to_excel(os.path.join(percorso, "DS_ITALIA.xlsx"), index=False) 

# passo 7
# 
dataframe=pd.DataFrame(dataset)
dataframe_grouped = dataframe.groupby(['Retailer_country','Year']).agg({
    'Quantity': 'sum'
}).reset_index()
print(dataframe_grouped)

s=input("press key")
dataframe_grouped.to_excel(os.path.join(percorso, "totali.xlsx"),index=False)
#grafici

dataframe_grouped.plot.hist(alpha=0.5, bins=5)
plt.show()
input("\n Fermati ad ammirare il lavoro svolto questa mattina...\n")

# 2. Riorganizzare i dati con una Pivot Table
# Sposta la seconda categoria nelle colonne per permettere a pandas di creare il gruppo
df_pivot = dataframe_grouped.pivot(index='Retailer_country', columns='Year', values='Quantity')
print (df_pivot)
plt.show()
input("\n Fermati ad ammirare il lavoro svolto questa mattina...\n")

#df_pivot2=dataframe.pivot(index='Retailer_country', columns='Year', values='Quantity')
#print (df_pivot2)

# 3. Disegnare il grafico a barre affiancate
df_pivot.plot(kind='bar', figsize=(10, 6), edgecolor='black')

# Personalizzazione
plt.title('Totale per Nazione e Anno')
plt.xlabel('Nazione')
plt.ylabel('Totale (Valori)')
plt.xticks(rotation=0) # Mantiene i nomi sull'asse X orizzontali
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
input("\npremi un tastino piccolino...\n")

# Usando lo stesso df_pivot dell'esempio precedente
df_pivot.plot(kind='bar', stacked=True, figsize=(10, 6), edgecolor='black')

# Personalizzazione
plt.title('Totale Complessivo per Nazione (Suddiviso per Anno)')
plt.xlabel('Nazione')
plt.ylabel('Totale Cumulativo')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
input("\npremi un tastino piccolino...\n")

#AGGIUNGIAMO LA LINEEA X IL VALORE MEDIO
# 2. Calcolo della media complessiva della colonna dei totali
valore_medio = dataframe_grouped['Quantity'].mean()
# 3. Riorganizzazione dei dati con la Pivot Table
#df_pivot = df.pivot(index='Retailer_country', columns='Year', values='Quantity')

# 4. Creazione del grafico (puoi cambiare in stacked=True se preferisci)
ax = df_pivot.plot(kind='bar', figsize=(10, 6), edgecolor='black', alpha=0.8)

# 5. Aggiunta della linea orizzontale per il valore medio
plt.axhline(y=valore_medio, color='red', linestyle='--', linewidth=2, 
            label=f'Media Totale ({valore_medio:.1f})')

# Personalizzazione del grafico
plt.title('Totale per Nazione e Anno con Linea del Valore Medio')
plt.xlabel('Nazione')
plt.ylabel('Totale (Valori)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Aggiorna la legenda per includere sia le barre sia la linea della media
plt.legend(title='Legenda')

plt.show()
s=input("premi un tasto prima della torta")

#diaagraamma a torta dell' italia
# uso df_italia
pulisci_schermo()
df_italia_totali=dataframe_grouped[(dataframe_grouped["Retailer_country"]=="Italy")]
print(df_italia_totali)

df_italia_totali.set_index('Year').plot.pie(y='Quantity', autopct='%1.1f%%', figsize=(6, 6), startangle=0, explode=[0.2, 0, 0])

#plt.ylabel('') # Rimuove l'etichetta dell'asse y, che di solito non serve
plt.title('Grafico a Torta di Esempio')

plt.show()
s=input("premi un tastuccio")

# ruoto la torta di 24 gradi in enso antiorario
sizes = df_italia_totali['Quantity'].to_numpy(dtype=float)
labels = df_italia_totali['Year'].astype(str).to_numpy(dtype=str)

y = np.array([2012, 2013, 2014, 2015])
mylabels = ["A", "B", "C", "D"]
myexplode = [0.2, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, startangle=float)
plt.show() 
#explode = [0.05] * len(sizes)
#myexplode = [0.2, 0, 0, 0]
#explode = myexplode

# Inserendo myexplode con i mei parametri riesco a graficare a torata con uno solo degli spicchi sollevato
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#ax1.pie(sizes, explode=[0.2], autopct='%1.1f%%',
#        shadow=True, startangle=24)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show() 
#s=input("premi un tasto x chiudere")
plt.savefig('./Dataset_DataFrame/grafico_bullish.png', dpi=300, bbox_inches='tight') #bbox_inches='tight' assicura di nn tagliare i margini

s=input("premi un tasto x chiudere")
