import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


# Array für die Speicherung der Population
pop_num = 102
population = np.empty((pop_num, pop_num))


# Anzahl Tage, die Simuliert werden sollen
tage = int(input("Wie lange soll die Simulation dauern? "))
anz_krank = int(input("Wie viele Personen werden zu Beginn der Simulation krank? "))
ansteckungsrat = int(input("Wie hoch ist die Ansteckungsrate der Krankheit? [0%-50%] "))

kranke = np.empty((tage-1, tage))
kranke_counter = 0


# notwendig für die Darstellung der Grafik
fig = plt.figure()
cmap = plt.get_cmap('brg', 8)
mat = plt.imshow(population, cmap=cmap, animated=True)
cax = plt.colorbar(mat, ticks=np.arange(0, 8))
plt.clim(0, 8)
plt.grid(True)
# Ende der Grafik Optionen


def update(tag):
  global kranke_counter
  mat.set_data(population)
  plt.title("Tag: " + str(tag))

  for i in range(tag, tage):
    kranke[i-1 , tag] = kranke_counter



# initialer Zustand der Simulation
def setup():
  for i, j in np.ndindex(population.shape):
    population[i, j] = 0

  for i, j in np.ndindex(kranke.shape):
    kranke[i, j] = 0

  for i in range(0, anz_krank):
      pop1 = random.randint(0, pop_num - 1)
      pop2 = random.randint(0, pop_num - 1)

      # wenn die zufällige Person bereits erkrankt ist, wird eine andere Person angesteckt.
      while (population[pop1, pop2] == 1):
          pop1 = random.randint(0, pop_num - 1)
          pop2 = random.randint(0, pop_num - 1)
          print("nochmal")

      population[pop1, pop2] = 1

  update(0)
  return mat


# gibt einen zufälligen wert zurück
def get_zufall():
  anst_zahl = int(100 / ansteckungsrat)
  zufall = random.randint(0, anst_zahl - 1)
  return zufall


# bestimmt ob die betreffende Person infektioes ist oder nicht
def infektioes(x, y):
    if population[x, y] > 0 and population[x, y] < 8:
        angesteckt = True
    else:
        angesteckt = False

    return angesteckt


# berechnet, ob die getestete Person angesteckt wurde oder nicht
# der Krankheitsgrad wird um 1 erhöht und nach 8 Tagen ist die Person wieder gesund
def ansteckung(x, y):
  global kranke_counter
  if population[x, y] == 0:
    if infektioes(x - 1, y) or infektioes(x + 1, y) or infektioes(x, y - 1)or infektioes(x, y + 1):
      if get_zufall() == 0:
        population[x, y] = 1
        kranke_counter += 1
  elif population[x, y] < 8:
      population[x, y] = population[x, y] + 1
      kranke_counter += 1


# aktualisiert die Animation
def animate(t):
  global kranke_counter
  kranke_counter = 0

  for i, j in np.ndindex(population.shape):
    if 0 < i < pop_num - 1 and 0 < j < pop_num - 1:
      # Berechnung der Ansteckung
      ansteckung(i, j)
  # Aktualisierung der Darstellung mit den neuen Werten
  update(t)
  return mat





# Animiert die Darstellung
ani = animation.FuncAnimation(fig, animate, range(1, tage), repeat=False, interval=300, blit=False, init_func=setup)
writer = animation.PillowWriter(fps=5)
ani.save("D:\Simons Bilder\karank.gif", writer=writer)

# kranke:
for i in kranke:
    print(i)

plt.clf()
plt.plot(kranke[tage-2])
plt.xlabel("Zeit")
plt.ylabel("Kranke")
plt.show()
