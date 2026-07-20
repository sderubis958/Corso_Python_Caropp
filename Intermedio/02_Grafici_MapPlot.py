#Three lines to make our compiler able to draw:
import sys
import matplotlib
# matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
 
#plt.ion() # enable interactive mode

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

#Two  lines to make our compiler able to draw:
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()

#barre
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
plt.title('Grafico a barre')
plt.grid(True)
plt.show()
key=input("premi un tasto")
plt.savefig("./Dataset_DataFrame/bar.jpg")
