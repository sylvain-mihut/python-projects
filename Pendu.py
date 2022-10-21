import random


f = open ('dico_france.txt', encoding="ISO-8859-1")
word = f.read()
liste = word.split()

difficulte = (input("choisissez un niveau de difficulté :  \n\ndebutant \n\nintermediaire \n\nexpert \n\n>>> "))

if difficulte == "debutant":
    nombre_de_vies = 10

elif difficulte == "intermediaire":
    nombre_de_vies = 7

elif difficulte == "expert":
    nombre_de_vies = 4


lettres_trouvees = set()
mot = random.choice(liste)


def afficher_mot(mot,lettres_trouvees):
    print("Mot : ", end= '')
    for i in range(len(mot)):
        if mot [i] in lettres_trouvees:
            print(mot[i], end='')

        else:
            print(" _", end='')


def main():
    mot = random.choice(liste)
    print(mot)
    

def mot_trouve(mot,lettres_trouvees):
    for i in range (len(mot)):
        if mot [i] not in lettres_trouvees:
            return False

    return True


while nombre_de_vies > 0:
    afficher_mot(mot,lettres_trouvees)
    print("\nNombre de vies restant", nombre_de_vies)
    lettre = input("Entrez une lettre : ")
    if lettre not in mot:
        nombre_de_vies -= 1
    
    if lettre in mot and lettre not in lettres_trouvees:
        lettres_trouvees.add(lettre)
    
    print(lettre)

    if mot_trouve(mot, lettres_trouvees):
        print("le mot a été trouvé ! ! \nGG")
        print(mot)
        break

    if nombre_de_vies == 0:
        print("tu es pendu x( ")
        break

# main()
