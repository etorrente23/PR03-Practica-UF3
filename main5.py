import os
#Exercici 10
with open('quixot.txt', 'w') as f:
    f.write("En un lugar de La Mancha de cuyo nombre no quiero acordarme...")

#Exercici 11
with open('quixot.txt', 'r') as f:
    contingut = f.read()
    print(contingut)

#Exercici 13
with open('quixot.txt', 'r') as f:
    contingut = f.read()
    print(contingut)

#Exercici 14
with open('quixot.txt', 'r') as f:
    contingut = f.read(11)
    print(contingut)

#Exercici 16
with open('prova.txt', 'w') as f:
    f.write("Un altre inici")

#Exerxici 17
with open('quixot_extended.txt', 'w') as f:
    f.write("capitol1\n")
    with open('quixot.txt', 'r') as f_quixot:
        for linia in f_quixot:
            f.write(linia)
    f.write("capítol 2\n")
    f.write("Al capítol 2 tenim més aventures\n")

with open('quixot_extended.txt', 'r') as f:
    primera_linia = f.readline()
    segona_linia = f.readline()
print(primera_linia, end="")
print(segona_linia, end="")
