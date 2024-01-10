def additionner(x, y):
    return x + y

def soustraire(x, y):
    return x - y

def multiplier(x, y):
    return x * y

def diviser(x, y):
    if y != 0:
        return x / y
    else:
        return "Erreur : Division par zéro"

print("Sélectionnez une opération :")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

choix = input("Entrez le numéro de l'opération souhaitée (1/2/3/4) : ")

nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

if choix == '1':
    print(nombre1, "+", nombre2, "=", additionner(nombre1, nombre2))
elif choix == '2':
    print(nombre1, "-", nombre2, "=", soustraire(nombre1, nombre2))
elif choix == '3':
    print(nombre1, "*", nombre2, "=", multiplier(nombre1, nombre2))
elif choix == '4':
    print(nombre1, "/", nombre2, "=", diviser(nombre1, nombre2))
else:
    print("Opération invalide")
