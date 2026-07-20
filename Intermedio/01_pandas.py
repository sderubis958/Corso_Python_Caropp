# Pandas èn una libreria di python:
# Legge dati (CSV, Excel, Text)
# Analizza dati
# Filtrare, modificare, aggregare

# Quindi è lo strumento principale per un Data Analyst
# Installazione di PANDAS: pip install pandas

"""
    .env ==> salvare pacchetti installati    
        ==> riutilizzare pacchetti installati in altri progetti
        ==> esempio: import pandas as pd

"""
#  1. Creare un ambiente virtuale: python -m venv .env
#  2. Attivare l'ambiente virtuale:  .env\Scripts\activate 
#  3. Per disattivare l'ambiente virtuale: deactivate
#
# PIP install MATPLOTLIB
# in caso non permettesse di installare pacchetti, eseguire il prompt dei comandi come amministratore   :
#  (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) 
# (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& .venv\Scripts\Activate.ps1)
#
import pandas as pd

#Creazioen della lista 
studenti = {
    'nomi': ['Massa', 'Antonella', 'Luigi', 'Eduardo', 'Matteo', 'Stefano', 'Lucia', 'Annaritantonia', 'Paolo', "Gesualdo"],
    'voti': [10, 8, 9, 7, 10, 6, 5, 4, 10, 8]
}

# Creazione del DataFrame(Foglio excel, Tabella, Entità)
df = pd.DataFrame(studenti)

print(df) # stampa il DataFrame

