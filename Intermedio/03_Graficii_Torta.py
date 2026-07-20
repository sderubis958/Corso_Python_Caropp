# Grafici a Torta

import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.ion() # enable interactive mode

# Dati da rappresentare e relative etichette
fette = [15, 30, 45, 10]
attivita = ['Lavoro', 'Studio', 'Riposo', 'Altro']
fette.sort()
# Creazione del grafico a torta
plt.pie(fette, labels=attivita, autopct='%1.1f%%')

# Titolo del grafico
plt.title("Distribuzione delle mie attività")

# Mostra il grafico
plt.show()
s=input("premi un tasto x chiudere")
plt.savefig('./Dataset_DataFrame/grafico_x_torta.png', dpi=300, bbox_inches='tight') #bbox_inches='tight' assicura di nn tagliare i margini

#s=input("premi un tasto x chiudere")

#secondo esempio
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

#ruoto la torta di 24 gradi in enso antiorario
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=24)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show() 
s=input("premi un tasto x chiudere")
plt.savefig('./Dataset_DataFrame/grafico_a_torta.png', dpi=300, bbox_inches='tight') #bbox_inches='tight' assicura di nn tagliare i margini

#s=input("premi un tasto x chiudere")