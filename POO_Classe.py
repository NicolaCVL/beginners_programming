#############################################
############## LES CLASSES ##################
#############################################

class Carre:
  count = 0
    def __init__(self, nb_cote, taille_cote):
        self.nb_cote = nb_cote
        self.taille_cote = taille_cote

    def calculate_perimeter(self):
      return self.nb_cote * self.taille_cote
    
    def calculate_area(self):
      return self.taille_cote * self.taille_cote

    def factor(self):
      return (self.nb_cote * self.taille_cote) * multi

    def count(self):
      return type(self)ct = count
        count += 1
    
"""
    def int(self):
      return (self.nb_cote)

    def Comp(self):
      if self.taille_cote > C2.taille_cote2:
        print("True")
      else:
        print("False")
"""

if __name__ == "__main__":

    a = int(input("Entrer Nombre de coter : "))
    b = int(input("Entrer Tailler des coter : "))
    d = int(input("Entrer Tailler des coter : "))

    C = Carre(a, b)
    C2 = Carre(a, d) 

    multi = int(input("Entrer : "))
#   multi2 = int(input("Entrer : "))

    print(C.nb_cote)
    print(C.taille_cote)
    print(C.calculate_perimeter())
    print(C.calculate_area())

    print(C2.nb_cote)
    print(C2.taille_cote)
    print(C2.calculate_perimeter())
    print(C2.calculate_area())
    print(C.count())

    print("Le carré n°1 est", multi, "fois plus grand, soit", C.factor(), "cm")
    print("Les cotés du carré ont une longueur de", C.taille_cote,"cm, une aire de", C.calculate_area(),"cm², et un périmètre de", C.calculate_perimeter(),"cm.")

"""
class Carre2:
   
  def __init__(self, nb_cote2, taille_cote2):
    self.nb_cote2 = nb_cote2
    self.taille_cote2 = taille_cote2

  def calculate_perimeter2(self):
    return self.nb_cote2 * self.taille_cote2
  
  def calculate_area2(self):
    return self.taille_cote2 * self.taille_cote2

  def factor2(self):
    return (self.nb_cote2 * self.taille_cote2) * multi2
  print(C2.nb_cote2)
  print(C2.taille_cote2)
  print(C2.calculate_perimeter2())
  print(C2.calculate_area2())
  print(C.int())
  print(C.Comp())


  print("Le carré n°2 est", multi2, "fois plus grand, soit", C2.factor2(), "cm")
  print("Les cotés du carré ont une longueur de", C2.taille_cote2,"cm, une aire de", C2.calculate_area2(),"cm², et un périmètre de", C2.calculate_perimeter2(),"cm.")
  

  print("Les deux carré additionnés ont un périmètre de", C.calculate_perimeter() + C2.calculate_perimeter2(),"cm")
  print("Les deux carré soustrait ont un périmètre de", C.calculate_perimeter() - C2.calculate_perimeter2(),"cm")
"""
