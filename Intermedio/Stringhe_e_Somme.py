"""
    Scrivere un programma ch prseenta un mnu di scelta come di seguito riportato

    1. Somma tra 2 numeri
    2. Concatenare 2 stringhe date in input
    3. Pulire la console di debug
    4. Terminare il programma
Il menu di scelta deve essere presentato a video fin quando l'utente non decide di terminare il programma    
"""
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear') 

def somma(A,B):
    somma_num=A+B
    return somma_num

def concat_stringa(C,D):
    concatenazione = C + " " + D
    return concatenazione


clear_console()

while True:
    print("\n--- Funzioni miste ---\n")
    print("1. Somma tra 2 numeri")
    print("2. Concatenare 2 stringhe")
    print("3. Pulire la console")
    print("4. Terminare il programma")
    print("0. Scelta non valida!")

    scelta = int(input("\nInserisci la tua scelta: "))

    if scelta == 1:
        num1 = int(input("Inserisci il primo numero: "))
        num2 = int(input("Inserisci il secondo numero: "))
        y = somma (num1,num2)
        print('la somma di ', num1, ' e ', num2, ' è: ', y)
        print(y)
    elif scelta == 2:   
        clear_console()
        stringa1 = input("Inserisci la prima stringa: ")
        stringa2 = input("Inserisci la seconda stringa: ")
      #  concat_stringa(C,D)
        print('La concatenazione delle due stringhe è: ', concat_stringa(stringa1, stringa2)) 
    elif scelta == 3:
        clear_console()
        print("Console pulita!")
    elif scelta == 4:  
        clear_console()
        print("Fine del programma...")
        break
    else:
        print("Scelta non valida!")