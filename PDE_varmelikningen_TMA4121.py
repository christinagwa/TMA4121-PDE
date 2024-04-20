import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# har en kvadratisk plate med konstant temperatur langs kantene, der én av de fire kantene er varmere enn de tre andre (som har samme temperatur)
# ser på hvordan temperaturen endrer seg over tid ved å bruke eulers eksplisitte metode


L = 1  # platens lengde
N = 50  # Antall rutenettspunkter i hver retning
alpha = 0.01  # termisk diffusivitet
T_0 = 100  # initialtemperatur
T_h = 200  # temperatur på den varme siden
timesteps = 1000  # tidssteg
dt = 0.01  

x = np.linspace(0, L, N) # N punkter mellom 0 og L
y = np.linspace(0, L, N)
X, Y = np.meshgrid(x, y) # "setter sammen" x og y verdiene til punkter, 2D
T = np.ones((N, N)) * T_0 # temperaturmatrise, setter temp i hele platen lik T_0


fig, ax = plt.subplots()
heatmap = ax.contourf(X, Y, T, cmap='hot_r', levels=np.linspace(T_0, T_h, 100)) #temperaturskalaen

def varmeutvikling(tidssteg):
    global T
    if tidssteg == 0:
        T[:, 0] = T_h  # setter temperaturen ved den varme platen lik T_h ved tiden 0
    Tn = T.copy() # for å unngå at endringene i temperaturene påvirker beregningene for neste tidssteg lages det en kopi Tn av temperaturmatrisen T
    for i in range(1, N-1): # går gjennom hver rad (utenom kantene)
        for j in range(1, N-1): # går gjennom hver kolonne (utenom kantene)
            T[i, j] = Tn[i, j] + alpha * dt * ((Tn[i+1, j] - 2*Tn[i, j] + Tn[i-1, j]) / (L/N)**2 + (Tn[i, j+1] - 2*Tn[i, j] + Tn[i, j-1]) / (L/N)**2)
    heatmap = ax.contourf(X, Y, T, cmap='hot_r', levels=np.linspace(T_0, T_h, 100)) # oppdaterer heatmap-plottet med de nye temperaturene etter at de er beregnet for det gjeldende tidsskrittet
    return heatmap,

ani = FuncAnimation(fig, varmeutvikling, frames=timesteps, interval=20, blit=True)
plt.colorbar(heatmap, label='Temperatur (°C)')
plt.title('Temperaturfordeling over platen')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
