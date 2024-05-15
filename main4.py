#Exercici 8
import sys
print(sys.builtin_module_names)

#Pregunta 19

# La lletra que identifica els modes d'escriptura es la w
# Diferència entre obrir i crear un fitxer es que si l'obrim amb l'w i no exsisteix es creara un nou fitxer buit i si existeix el contigut es sobrescribira 

#Exercici 20
import shutil
shutil.copyfile('quixot_extended.txt', 'quixot_extended2.txt')
with open('quixot_extended2.txt', 'a') as f:
    f.write("capítol 3\n")
    f.write("Aquest capítol ha estat generat per un programa\n")

#Exercici 21
f.close()
with open('quixot_extended2.txt', 'r') as f:
    contingut = f.read()
    print(contingut)

#Exercici 22
with open('new_quixot.txt', 'w') as f:
    f.write("capitol 1\n")
    f.write("In a place of the stain...\n")




