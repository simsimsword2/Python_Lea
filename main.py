# 23.03.2021
#
# Schreiben Sie den Bubble-Sort-Algorithmus aus dem letzten Modul mit zwei Funktionen z.B. bubblesort() und swap().

import Modules
import random
import time

'#---------------------------------------------------------------------------------------------------------------------'
# testing:

a = [5, 1, 3, 2, 4]
random_list = []

print(a)
Modules.bubblesort(a)
print(a)

start = time.time()

for i in range(0, 1000):
    n = random.randint(1, 1000)
    random_list.append(n)

print(random_list)
Modules.bubblesort(random_list)
print(random_list)

end = time.time()
print("Das Sortieren der zufaelligen Liste dauerte", end-start, "s""")