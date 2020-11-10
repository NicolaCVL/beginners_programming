#############################################
######### PREMIER PAS SUR PYTHON ############
#############################################

#EXERCICE 8
# Définir 2 variables : 1 contenant un age en nombre et l'autre contenant votre prénom. 
# Créez une troisième variable qui devra contenir la phrase suivante : "Je suis [NOM] et j'ai [AGE] ans."
# Enfin, afficher cette dernière variable

# age = 22
# prenom = "nicola"
# t = "je suis", prenom, "et jai", age, "ans"
# print(t)

# c = "freddy"
# print(c)

#t = 1
#x = 2
#print(p * 4)
#print (p + 1)
#print (p + t)

#print (p - 1)
#print (p - t)
#p = 5

#print (p * 2)
#print (p * x)

#print (p / 2)
#print (p / x)

#EXERCICE 9

# a = 3
# b = 8
# c = a
# a = b
# b = c
# print(a, b, c)

#EXERCICE 11

# a = 10
# print(a)
# print(a / 2)
# print(a // 2)
# print(a % 2)
# print(a^3)

#EXERCICE 12 

#pht = int(input("Entrer le prix :"))
#art = int(input("Entrer le nombre d'article :"))
#tva = 1.2 
#Prixfinal = (pht * art) * tva
#print(Prixfinal)

#############################################
############### LES LISTES ##################
#############################################

#EXERCICE 13/14

# list = [4, 5, "fred"]
# list.append("yop")
# print(list[3])
# print(type(list[3]))

#EXERCICE 15

#list1 = [1,2,3,4]
#list2 = [5,7,8,9]
#list3 = list1 + list2
#print(list3)

#EXERCICE 16

# list = [0,1,2,3,4,5,6,7,8,9]
# mini = min(list)
# maxi = max(list)
# somme = sum(list)
# tot = 0
# longueur = len(list)
# print(list)

# Perso = {
#   "Vie" : 10,
#     "Mana" : 20,
#    "Attaque" : 100,
#    "Defense" : 50
# }
# print(Perso)
# def maximum(list):
#   max = list[0]
#   longueur = len(list)
#   for Compt in range (longueur):
#       if list[Compt] >= max:
#   maxi = list[Compt]
# return max

# for i in list:
#   tot = tot + i
#   tot

# del list[1]
# max(list)      
# min(list)
# print(Perso["Vie"])

# print(list[3])
# print(list[3:5])
# print(list[2:8:2])

# print(len(list))
# print(maxi)
# print(mini)
# print(somme)

# print("le total est", tot)
# print(list)

#list2 = ["ok", 4, 2,78, "bonjour"]
#list2[1] = "toto"
#print(list2)

# list3 = [0,1,2,3,4,5]
# V = (0,1,2,3,4,5)
# list4 = [V]
# print(list3,list4)

#EXERCICE 18 

# list5 = []
# for i in range (0, 6):
#   list5 += [i]
# print(list5)

#############################################
################LES DICTIONNAIRES############
#############################################

#EXERCICE 19 

#Dico = {
#    "key" : "valeur",
#    "key2": "valeur2"
#    }

#Dico["titi"] = "toto"
#Dico["tata"] = Dico["titi"]
#del Dico["titi"]
#V = Dico["key"]
#del Dico["key"]

#Dico2 = {
#    "Dico1" : Dico
#    }

#print(V)
#print(Dico)
#print(Dico2)

#############################################
######LISTES, DICTIONNAIRES, TUPLES##########
#############################################

#EXERCICE 20

# x = 1
# y = 2
# Tup = [("x", "y") , ("x", "y") ,("x","y"),("x", "y")]
# Tup.append("a")
# Tup.extend("b")

# Tup2 = [(1,2,3)]
# Tup.extend(Tup2)
# Tup3 = Tup + Tup2
# Tup[3] = 2
# Tup3 = Tup2
# print(Tup3)
# print(Tup)
# print(Tup3)
# del Tup2[:]
# print(Tup2)



#############################################
############### LES TESTS ###################
#############################################

#EXERCICE 1

#A = int(input("Entrer le premier nombre :"))
#B = int(input("Entrer le deuxieme nombre :"))
#C = A * B

#if C > 0:
  #  print("Positif")
#elif C < 0 :
   # print("Negatif")
#else :
   # print("Nul")


#EXERCICE 2

#Age = int(input("Entrer votre age :"))
#if Age >= 18:
#    print("Vous etes majeur !")

#elif Age < 18 :
#    print("Vous n'etes pas majeur...")


#A = int(input("Entrer un nombre :"))
#if A > 5 and A < 10 : # Si A est compris entre 5 et 10 (10 exclus)
  #  print(A > 5 and A < 10)
#else :
 #   print("False")


#if A > 5:
    ##if A < 10.5:
      ###  print("True")
   #### else:
        #####print("False")
#else:
  #  print("True")

#############################################
############## LES BOUCLES ##################
#############################################

# EXERCICE 1 
# créez une boucle for qui affiche les numéros de 0 à 5

# for compt in range(0, 6):
#    print(compt)


# for compt in (v):
#     print(compt + "*")

##EXERCICE 3
# Soit la variable x = "anticonstitutionnellement". 
# A l'aide d'une boucle for, afficher les lettres présentes dans x.

# for test in v:
#     print("longueur de la chaine", test, '=', len(test))

# list2 = "anitconstitutionnellement"
# index2 = 0
# AntiC = list2

# for compt2 in (AntiC):
#     print(compt2 + "*")

# EXERCICE 10 
#  Grâce à la liste suivante : ordi = ["apple", "asus", "dell", "samsung"], 
# utilisez la boucle While pour afficher toutes les marques d'ordinateur

# P = "Apple"
# F = "Asus"
# C = "Dell"
# S = "Samsung"
# index = 0
# list = [P,F,C,S]
# v = list

#EXERCICE 10

# while index < len(v):
#     print(list[index])
#     index += 1

#EXERCICE 11

# text = input("Ecrire un mot : ")
# while text != "exit":
#   text = input("Ecrire un mot : ")
# print(text)

#EXERCICE 12

# v = 0
# while v <= 100:
#   print(v)
#   v += 5

#############################################
############## LES FONCTIONS ################
#############################################

#EXERCICE 1

# def multi(x, ):
#   return x*5

# T = int(input("Donner un nombre : "))
# x = T
# a = multi(T,)
# print(a)

#EXERCICE 2

#list = [2,1,54,83,108,97,7]

# list2 = []
# a = 0
# max = 5

# print(list2)
# print(a)

# list2 = [max]

# while a < max :
#   b = int(input("Entrer un nombre : "))
#   list2.append(b)
#   a += 1

# print(list2)

# def nombres(list2):
#   for i in range (0, len(list2)):
#       if list2[i] % 2 == 0:
#           print(list2[i])
#       if list2[i] % 2 != 0:
#         list2.remove[i]
# nombres(list2)

# print(b)
# print(list2)
      
# def paires (list2):
#   paires (list2)


# print(a)
# print(v)
# print(list2)

# for i in range (0, len(list2):
#   if list2[i] % 2 == 0:
#     print (list2[i])

# nombre = [2, 5, 14, 16, 159, 198]
# def paires (nombre):
#     for i in range (0, len(nombre)):
#         if nombre[i] % 2 == 0:
#             print (nombre[i])
# paires (nombre)

#EXERCICE 3

# def fibo(x, n+x)
  
# import random

# list2 = []
# a = 0
# max = 25
# u = 0
# n = random.randint(1, 100)

# list2 = [n]

# while a < n :
#   b = random.randint(0, n+1)
#   list2.append(b)
#   a += 1


# def nombres(list2):

#   for i in range (0, len(list2)):

#     if list2[i] % 2 == 0:
#       print(list2[i])
#     else:
#       break
# nombres(list2)

# print(b)
# print(list2)
      
# def paires (list2):
#     paires (list2)


# def mult(nb):
#     print(nb*5)
# print("Quel est votre nombre?")
# a=int(input())
# mult(a)


# def nbp(nb):
#     if(nb%2==0):
#         print("pair")
#     else:
#         print("pas pair")
# nbp(8)


# s1=1
# s2=1
# s3=0
# while s3<50:
#     s3=s1+s2
#     s1=s2
#     s2=s3
#     print(s2)



# mot=input("Entrer un mot : ")
# liste_voyelles=["a","e","i","o","u","y"]
# nb_voyelles = 0  
# for lettre in mot : 
#         if lettre in liste_voyelles :
#             nb_voyelles+=1
# print(nb_voyelles)


# nbr = int(input('Entrez un nombre : '))
# fact = 1
# for i in range(1, nbr+1):
#   fact = fact * i
# print (nbr,'! = ',fact)


