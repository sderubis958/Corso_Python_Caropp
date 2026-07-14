#esempio con le function

# questo programma calcola la somma tra 2 numeri

# definire la mia function
def Somma(x,y):
    c=x+y
    return c

def Stampa_In_Console(messaggio):
    #cancello la finstra
    #cls
    print(messaggio) 

A= input("Inserisci il primo numero:  ")
B=  input("Inserisci il secondo numero:  ")
a=int(A)
b=int(B)

C=Somma(a,b)

print("Risultato-->  "+str(C))
print(f'La somma è   {C}')

## definizione di una function con parametri di default per pulire console

