"""
   Obiettivo del progetto:
   il computer scgeglie un numero casuale tra 1 e 10, 
   l'utente deve indovinare il numero scelto dal computer 
   in un massimo di 5 tentativi 

   Ad ogni tentativo il computer deve dire se il numero scelto 
   è più alto o più basso del numero scelto dall'utente 

"""
import random

# il computer scgeglie un numero casuale tra 1 e 10, 
numero_segreto = random.randint(1, 10)

print('=' * 70) # genera 70 ================================================
print("🎮 INDOVINA IL NUMERO 🎮")
print('=' * 40)

print("il computer ssceglie un numero tra 1 e 10.")
print("Hai a disposizione 5 tentativi.\n")

# il ciclo for permette al gioccatore(utente) di fare 5 tentativi.
for tentativo in range(1, 6):
    print(f"\nTentativo {tentativo} di 5")
    
    # inserimento dell'utente
    numero = int(input("Inserisci il tuo numero: "))
    
    # Verifica se il numero dell'utente è uguale al numero generato del computer
    if numero == numero_segreto:
        print("🎉 Complimenti! Hai indovinato! Hai Vinto !!")
        break
#else:
 #   print(f"Mi dispiace, non hai indovinato. Il numero era {numero_segreto}.
 
  
    if numero < numero_segreto:
        print("📈 Il numero segreto è più grande!")

    if numero > numero_segreto:
        print('📉 Il numero segreto è più piccolo')
            
    # Se il ciclo termina seza break
if numero != numero_segreto:
    print('\n😭 Hai terminato i tentativi.')
    print('Il numero era', numero_segreto)    