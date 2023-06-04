"""utilisation des heritages afin de reduire le code"""
#version 2
class EtreVivant:
    ESPECE_ETRE_VIVANT = "(etre vivant non identifier)"
    def AfficherInfoEtreVivant(self):
        print("Info etre vivant : " + self.ESPECE_ETRE_VIVANT)

class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT = "Chat (mamifére felin)"
    #def AfficherInfoEtreVivant(self):
    #    print("Info etre vivant : " + self.ESPECE_ETRE_VIVANT)
           
class Personne(EtreVivant):
    ESPECE_ETRE_VIVANT = "humain (mamifére homo sapiens)"
    def __init__(self , nom: str= "" ,age: int = 0):
        self.nom = nom
        self.age = age
        
        if self.nom == "":
            self.DemanderNom()
        print("constructeur personne " + str(self.nom))
     
    def EstMajeur (self):
        return self.age >= 18
    
    def DemanderNom(self):
            self.nom = input("entrer votre nom : ")      
              
    #def AfficherInfoEtreVivant(self):
     #   print("Info etre vivant : " + self.ESPECE_ETRE_VIVANT)
           
    def se_presenter (self):
            #self.nom = input("entrer un nom : ")
        info_personne = " bonjour je m'appele " + str(self.nom) 
        if self.age !=0 :
            info_personne += " et j'ai " + str(self.age) + " ans "

        print(info_personne)
        if self.age !=0 :
            print("je suis majeur ") if self.EstMajeur() else print(" je suis mineur" )
    
class Etudiant(Personne):
    def __init__(self, nom: str, age: int ,etudes: str):
        self.nom = nom
        self.age = age
        self.etudes = etudes
    def se_presenter(self):
        super().se_presenter()
        print("je suis etudiant en " + self.etudes)
                
    
listePersonnes = [Personne("tom",30) ,
                  Personne("donald", 15) ,
                  Personne("zoe" , 20) ]

#for personne in listePersonnes:
 #   personne.se_presenter()
  #  personne.AfficherInfoEtreVivant()

#chat = Chat()    
#chat.AfficherInfoEtreVivant()
etudiant = Etudiant("toma", 23 , "ecole ingenieur de polytechnique")
etudiant.se_presenter()