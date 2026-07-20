# spezzata
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [0, 2, 4, 6]
y = [1, 5, 2, 7]

plt.ion()  # Enable interactive mode
# Personalizzazione: linea continua con cerchietti ai vertici
plt.plot(x, y, color='red', linestyle='solid', marker='o')

plt.xlabel('Asse X')
plt.ylabel('Asse Y')
plt.title('Grafico a spezzata')
plt.grid(True)
plt.show()
key=input("premi un tasto")
plt.savefig("./Dataset_DataFrame/spezzata.jpg")