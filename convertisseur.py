"""
Pour cet exercice, vous allez créer un programme de conversion d'unités, qui sera capable de convertir des pouces (inch) en centimètres (cm), et vice-versa.


1 pouce = 2.54 cm

1 cm = 0.394 pouces


Exemple :

Un écran de 17 pouces de diagonale, correspond à 43,18 cm (=17*2.54)


Voici comment votre programme doit se comporter :

1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"

2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)

3 - Afficher la valeur convertie (et l'unité : cm ou pouces)

- fin du programme.


Nombres à virgule :

Nous avons vu comment manipuler des données numériques avec Python, notamment avec le type "int" qui concerne les nombres entiers (sans virgules).

Pour cet exercice, vous allez être amené à manipuler des nombres à virgule. Il s'agit du type "float".

Le principe du float est similaire à celui du int.

Pour utiliser un nombre à virgule, il faut utiliser le point (et non une virgule).

Exemples :

a = 5  # int

b = 5.2 # float

c = 5,2 # erreur : ne pas utiliser de virgule, mais le point


Optionnel :

Boucler pour convertir plusieurs valeurs (en conservant toujours le même sens de conversion), et proposer une option pour sortir du programme.
"""

"""
effectuer_conversion : Cette fonction convertit une valeur d'une unité à une autre, en fonction du facteur de conversion fourni.
Return: 
True: l'utilisateur ne veut plus convertir
False: l'utilisateur a donné une valeur a convertir
"""

# Conversion unit1 vers unit2
def effectuer_conversion(unit1: str, unit2: str, facteur: float):
    valeur_str = input(f"Conversion {unit1} vers {unit2}. Entrez la valeur en {unit1}: (ou 'q' pour quitter) : ")
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERREUR: vous devez entrer un nombre")
        print("utiliser le point pour les nombres à virgule")
        return effectuer_conversion(unit1, unit2, facteur)
    
    valeur_convertie = round(valeur_float * facteur, 2)
    print(f"Résultat de conversion : {valeur_float} {unit1} = {valeur_convertie} {unit2}")
    return False
    
    
while True:
    print("Ce programme permet de convertir des pouces en centimètres et vice-versa.")
    print("1 - Convertir des pouces en centimètres")
    print("2 - Convertir des centimètres en pouces")
    choix = input("Votre choix (1 ou 2) : ")
    if (choix == "1" or choix == "2"):
        break
    print("ERREUR: vous devez choisir 1 ou 2")
      

while True:
    if choix == "1":
        if effectuer_conversion("pouces", "cm", 2.54):
            break
    if choix == "2":
        if effectuer_conversion("cm", "pouces", 0.394):
            break