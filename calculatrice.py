#def additionner(x, y):
#    return x + y

#def soustraire(x, y):
#    return x - y

#def multiplier(x, y):
#    return x * y

#def diviser(x, y):
 #   if y != 0:
 #       return x / y
  #  else:
   #     return "Erreur : Division par zéro"

#print("Sélectionnez une opération :")
#print("1. Addition")
#print("2. Soustraction")
#print("3. Multiplication")
#print("4. Division")

#choix = input("Entrez le numéro de l'opération souhaitée (1/2/3/4) : ")

#nombre1 = float(input("Entrez le premier nombre : "))
#nombre2 = float(input("Entrez le deuxième nombre : "))

#if choix == '1':
 #   print(nombre1, "+", nombre2, "=", additionner(nombre1, nombre2))
#elif choix == '2':
 #   print(nombre1, "-", nombre2, "=", soustraire(nombre1, nombre2))
#elif choix == '3':
 #   print(nombre1, "*", nombre2, "=", multiplier(nombre1, nombre2))
#elif choix == '4':
 #   print(nombre1, "/", nombre2, "=", diviser(nombre1, nombre2))
#else:
 #   print("Opération invalide")


import argparse

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculatrice en ligne de commande.')
    parser.add_argument('choix', type=int, help='Numéro de l\'opération souhaitée (1/2/3/4)')
    parser.add_argument('nombre1', type=float, help='Premier nombre')
    parser.add_argument('nombre2', type=float, help='Deuxième nombre')

    args = parser.parse_args()

    if args.choix == 1:
        result = additionner(args.nombre1, args.nombre2)
    elif args.choix == 2:
        result = soustraire(args.nombre1, args.nombre2)
    elif args.choix == 3:
        result = multiplier(args.nombre1, args.nombre2)
    elif args.choix == 4:
        result = diviser(args.nombre1, args.nombre2)
    else:
        result = "Opération invalide"

    print(f"Résultat : {result}")
