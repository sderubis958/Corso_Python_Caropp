import os

def clear_console():
    """
    Clears the console screen.
    Works on Windows, macOS, and Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')    

# esempio con le function
# questo programma calcola la somma tra 2 numeri

def pulisci_console():
    # 'nt' indica Windows, 'posix' indica macOS e Linux
    os.system('cls' if os.name == 'nt' else 'clear')
  ##os.system('cls')

#definire la mia function
def Somma(x,y):
    c=x+y
    return c

def Stampa_In_Console(messaggio):
    #cancello la finstra
    #cls
    pulisci_console()
    print(messaggio) 

pulisci_console()
A= input("Inserisci il primo numero")
B=  input("Inserisci il secondo numero")
a=int(A)
b=int(B)

C=Somma(a,b)
Stampa_In_Console("Risultato-->  "+str(C))
Stampa_In_Console(f'La somma è-->  {C}')

#stampare un messaggio a video
"""

    testo=
    Oggi è la prima lezione di python
facciamo un ripasso.

Domani, anzi mercoledi riprndiamo!   
"""


