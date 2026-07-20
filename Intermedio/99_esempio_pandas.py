# esempio presoo da
#https://www.intelligenzaartificialeitalia.net/post/una-guida-semplice-e-completa-per-passare-da-excel-a-python-usando-le-librerie-pandas-e-numpy

#importiamo le librerie
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os #per avere accesso alla consolle

plt.interactive(True)# cosi i graaafici non bloccano lo script

def pulisci_schermo():
    os.system('cls' if os.name == 'nt' else 'clear')

#passo 1: leggiamo i dati dal csv
path=f"C:\sviluppo\data analist\esempio pandas"
dataset = pd.read_csv(f"{path}\EsempioPython.csv")
print(dataset)

#passo 2: SOMMA, MEDIA, MAX, MIN e COUNT
#per fare queste funzini ci occorre prima il metodo describe
"""
genera un riepilogo statistico dei dati. Di base, analizza le colonne numeriche 
calcolando: conteggio dei valori validi, media, deviazione standard, valore minimo, massimo e i quartili (25%, 50% o mediana, 75%).
Esclude in automatico i valori mancanti (NaN)
"""
df=dataset.describe()
print(df)

#passo3
#esempi pratici:
"""
#Vogliamo calcolare le vendite totali dei negozi 
vendite_totali = dataset["Quantity"].sum()
print(vendite_totali)
"""
pulisci_schermo()
vendite_totali = dataset["Quantity"].sum()
print(f"vendite tootali-->{vendite_totali}")

#passo 4
"""
Quindi, se vogliamo selezionare una colonna specifica, selezioniamo prima con parentesi quadre ["colonna"]
e poi usa il metodo di cui abbiamo bisogno (.sum (), .mean (), .count (), ecc.). 
Ad esempio, calcoliamo la media, il max e il min delle quantità vendute dei negozi.
"""
print("media : " + str( dataset["Quantity"].mean() ) )
print("MAX : " + str( dataset["Quantity"].max() ) )
print("MIN : " + str( dataset["Quantity"].min()) )

#passo 5
"""
Nel caso in cui desideriamo contare il numero di dati specifici all'interno di una colonna, 
possiamo usare il .value_counts () metodo. 
Ora vediamo un esempio dove contiamo quale tipi di metodi sono stati usati negli ordini.
"""
print(dataset["Order_method_type"].value_counts())

#passo 6
"""
Possiamo facilmente sostituire la funzione IF di Excel utilizzando Numpy.
Immaginiamo di voler sapere quali vendite sono superiori ad una quantità di 500 pezzi
 e creare quindi un nuovo attributo per ogni riga la dove la vendita risulta maggiore o minore di questa quantità.
"""
dataset["Vendite_all_ingrosso"] = np.where(dataset['Quantity'] >500,  'vendita ad un negozio', 'vendita per privato')
print(dataset)

#passo7
"""
    Supponiamo ora di avere una condizione più complessa, la quale richiede di classificare nello specifico a che tipo di struttura è stato l'acquisto basandosi sulle quantità. In questo
    case, abbiamo più di 2 valori, quindi usiamo np.select () necessita di argomenti: 

    un elenco di condizioni 

    un elenco di valori

    Un elenco in Python è rappresentato dalle parentesi quadre [].
"""

condizioni = [(dataset['Quantity']>=900),
            (dataset['Quantity']>=800)&(dataset['Quantity']<900),
            (dataset['Quantity']>=700)&(dataset['Quantity']<800),
            (dataset['Quantity']>=600)&(dataset['Quantity']<700),
            (dataset['Quantity']>=500)&(dataset['Quantity']<600),
            (dataset['Quantity']<500) ]

valori= ['Negozio vendita ingrosso',
 'Centro commerciale',
 'Catena di negozi',
 'Negozio Grande',
 'Negozio medio-piccolo',
 'Ptivato-Retailer']

"""
valori= ['A',
 'B',
 'C',
 'D',
 'E',
 'F']
"""

dataset["Acquirente"] = np.select(condizioni, valori,default="?")
pulisci_schermo()

print(dataset)

#passo 8
"""
Immaginiamo di voler le vendite di prodotti solo di uno specifico Paese. 
Per farlo, in primo luogo, scrivi la condizione dataset ["Retailer_country"] == "Italy" e poi selezioniamo 
quella condizione all'interno del frame dataset utilizzando parentesi quadre []
"""
dataset_italia = dataset[dataset["Retailer_country"]=="Italy"]
dataset_italia

#passo9 
# facciaamo delle stitistiche
dataset_italia_2014 = dataset[(dataset["Retailer_country"]=="Italy") & (dataset["Year"]==2014)]
print("SOLO ITALIA")
print(dataset_italia_2014)

#PASSO 10 
#mettiamo dei grafici
pulisci_schermo()

mio_df=pd.DataFrame(dataset)
print(mio_df)

#raggruppo per paes e per anno e ne calcolo i totali
df2=pd.DataFrame(dataset)
print(df2)

pulisci_schermo()
#estraggo paese anno quantita
df4=df2[['Retailer_country','Year','Quantity']]
print (df4)
#lo slvo in un foglio eexceel

df4.to_excel('output.xlsx', index=False)

#studi solo l italia
#df_italia=df2.groupby(['Retailer_country','Year']) .filter(lamba x: x['Retailer_country']=='Italy')
df_italia=df2[df2['Retailer_country'] =='Italy']
df_italia.to_excel("solo_italia.xlsx",index=False)

pulisci_schermo()
df3=df_italia.groupby(['Retailer_country','Year'])['Quantity'].sum()
print(df3)
#df5=df3[['Retailer_country','Year','Quantity']]
#print(df5)
#PER FAR VEDERE UN ERRORE
#df[['Retailer_country', 'Costi']].plot(kind='line')
#plt.show()


grouped = df2.groupby(['Retailer_country','Year']).agg({
    'Quantity': 'sum'
}).reset_index()
print(grouped)

s=input("press key")
grouped.to_excel("totali.xlsx")
#grafici

grouped.plot.hist(alpha=0.5, bins=5)
plt.show()

# 2. Riorganizzare i dati con una Pivot Table
# Sposta la seconda categoria nelle colonne per permettere a pandas di creare il gruppo
df_pivot = grouped.pivot(index='Retailer_country', columns='Year', values='Quantity')

# 3. Disegnare il grafico a barre affiancate
df_pivot.plot(kind='bar', figsize=(10, 6), edgecolor='black')

# Personalizzazione
plt.title('Totale per Nazione e Anno')
plt.xlabel('Nazione')
plt.ylabel('Totale (Valori)')
plt.xticks(rotation=0) # Mantiene i nomi sull'asse X orizzontali
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

# Usando lo stesso df_pivot dell'esempio precedente
df_pivot.plot(kind='bar', stacked=True, figsize=(10, 6), edgecolor='black')

# Personalizzazione
plt.title('Totale Complessivo per Nazione (Suddiviso per Anno)')
plt.xlabel('Nazione')
plt.ylabel('Totale Cumulativo')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

#AGGIUNGIAMO LA LINEEA X IL VALORE MEDIO
# 2. Calcolo della media complessiva della colonna dei totali
valore_medio = df['Quantity'].mean()
valore_medio = grouped['Quantity'].mean()
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
s=input("premi un tasto")

#diaagraamma a torta dll italia
# uso df_italia
pulisci_schermo()
df_italia_totali=grouped[(grouped["Retailer_country"]=="Italy")]
print(df_italia_totali)

df_italia_totali.set_index('Year').plot.pie(y='Quantity', autopct='%1.1f%%', figsize=(6, 6))

#plt.ylabel('') # Rimuove l'etichetta dell'asse y, che di solito non serve
plt.title('Grafico a Torta di Esempio')
