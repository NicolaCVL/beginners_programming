#############################################
############## LES ASTUCES ##################
#############################################
# Lorsque vous souhaitez commenter plusieurs lignes : vous les 
# sélectionnez, et ensuite "ctrl + :"
# 
# Ceci ne marche que pour VSCODE :
# Vous pouvez accéder à tous les raccourcis en tapant "ctrl + k",
# suivi tout de suite par "ctrl + s"
# 
# LIEN EXERCICES
# https://github.com/kevinniel/Python-Lessons/wiki/1---variables


#############################################
########### LES COMMENTAIRES ################
#############################################
# ceci est un commentaire sur une ligne
"""
ceci est un commentaire sur plusieurs lignes
"""

#############################################
############# LES VARIABLES #################
#############################################
# déclaration d'une variable prennant comme valeur 123
# a = 10
# b = 3

# déclaration de texte dans une variable
# c = "texte 1"
# d = 'texte 2'

# utilisation de la fonction "print()" pour afficher les variables
# ci-dessus
# print(a, b, c, d)

#############################################
############ LES OPERATIONS #################
#############################################

# opérations sur les nombres
# addition
# print("a + b")
# print( a + b )
# # soustraction
# # le "\n" permet de faire un saut de ligne
# print( "\n a - b" )
# print( a - b )
# # multiplication
# print( "\n a * b" )
# print( a * b )
# # division
# print( "\n a / b" )
# print( a / b )
# # résultat ENTIER de la division
# print( "\n a // b" )
# print( a // b )
# # "modulo" => reste du résultat de la vision entière
# print( "\n a % b" )
# print( a % b )

# Opérations sur les chaines de caractères
# affichage des deux variables, l'une après l'autre
# print(c, d)
# affichage du résultat de la concaténation des deux variables
# concaténation = mise bout-à-bout de plusieurs chaines de caractères
# print(c + d)

#############################################
############# LES TABLEAUX ##################
#############################################

# Listes
# my_list = [0,4,8,9]

# Dictionnaires
# my_dict = {1: "a", 2: "b"}

# tuples
# my_tuple = (1,35,89)


#############################################
############### LES TESTS ###################
#############################################
# valeurs attendues : 
# - rouge
# - vert
# - orange
# feux = "rouge"

# Méthode 1
# if feux == "rouge":
#     print("je m'arrête")
# elif feux == "orange":
#     print("je m'arrête")
# else:
#     print("j'avance")

# Méthode 2
# if feux == "vert":
#     print("j'avance")
# else:
#     print("je m'arrête")

# Méthode 3
# if feux == "rouge" or feux == "orange":
#     print("je m'arrête")
# else:
#     print("j'avance")

#############################################
############## LES BOUCLES ##################
#############################################

# je déclare une liste
# my_tableau = [1,1,2,3,5,8,13,21]

# afficher tous les éléments de ma liste, dans l'ordre de lecture
# avec une boucle "pour"
# for element in my_tableau:
#     print(element)

# afficher tous les éléments de ma liste, dans l'ordre de lecture
# avec une boucle "tant que"
# i = 0
# while i < len(my_tableau):
#     print(my_tableau[i])
#     i += 1


#############################################
############# LES FONCTIONS #################
#############################################

def calculate_ttc(ht, tva):
    return ht * tva

a = calculate_ttc(10, 0.2)
print(a)


