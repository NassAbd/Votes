from math import sqrt
from math import radians
from math import cos
from math import sin
from collections import OrderedDict
import random



class Candidat:
    #Variables associées au calcul du budget de référence
    budget = 0
    distance_relative_max = 0
    Liste_candidat = []
    def __init__(self, nom, dx, dy):
        self.nom = nom
        self.x = dx
        self.y = dy
        self.util = 0
        self.pourc_attaque = (random.randint(0,10)/10)
        self.budget_attaque = 0
        self.budget_defense =  0

        (Candidat.Liste_candidat).append(self) #avec self seul on a la liste des adresses memoire des candidats

        #Calcul du budget de référence:
        if( len(Candidat.Liste_candidat)>= 2):
            for candidat1 in Candidat.Liste_candidat:
                for candidat2 in Candidat.Liste_candidat:
                    distance_temporaire = sqrt( ( (candidat1.x)-(candidat2.x) )**2+( (candidat1.y)-(candidat2).y)**2)
                    if Candidat.distance_relative_max<=distance_temporaire:
                        Candidat.distance_relative_max = distance_temporaire

                
        Candidat.budget=1/3*Candidat.distance_relative_max
        #Fin de calcul du budget de référence

        #recalcul le bugdet de tout les candidats
        for c in Candidat.Liste_candidat :
            c.budget_attaque = c.pourc_attaque*Candidat.budget
            c.budget_defense = (1-c.pourc_attaque)*Candidat.budget


    def attaque_candidat(self,c) : 
        if self.budget_attaque == 0:
            return 0
            
        if c.nom == self.nom :
            return 1
        direction = random.uniform(0,360)
        norme = self.budget_attaque
        angle = radians(direction)
        compx = norme*cos(angle)
        compy = norme*sin(angle)
        c.x += compx
        c.y += compy
        self.budget_attaque = 0

    def Distance_indiv(self, v) : 
        return sqrt(((v.x)-(self.x))**2+((v.y)-(self.y))**2)

    def Defense_candidat(self, Electorat) : 
        if self.budget_defense == 0:
            return 0
        x_init = self.x
        y_init = self.y
        direction = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360]
        rayon_votants = self.budget_defense
        entourage_init = 0
        for v in Electorat : 
            if self.Distance_indiv(v) < rayon_votants : 
                entourage_init += 1
        for d in direction : 
            entourage_res = 0
            angle = radians(d)
            compx = rayon_votants * cos (angle)
            compy = rayon_votants * sin (angle)
            self.x += compx 
            self.y += compy 
            for v in Electorat : 
                if self.Distance_indiv(v) < rayon_votants : 
                    entourage_res += 1
            if entourage_res > entourage_init : 
                entourage_init = entourage_res
                x_init = self.x 
                y_init = self.y
        self.x = x_init
        self.y = y_init
        self.budget_defense = 0

    
  



 
    def utilite(self,Electorat,nbv):
        if (nbv == 0):
            return
        u = 0
        for v in Electorat:
            u += ((v.x)-(self.x))**2+((v.y)-(self.y))**2
        u = u/(nbv)**2
        self.util = u
        return u

    @staticmethod 
    def maj_util(Electorat,nbv):
        for c in Candidat.Liste_candidat:
            c.utilite(Electorat,nbv)


    def label(self):
        print("Nom:", self.nom ,"Coordonée:", self.x, ",", self.y)

    @staticmethod 
    def supp_candidat(C):
        del Candidat.Liste_candidat[C]
        print("Candidat ", C.nom, "supprimé de la liste des candidats")
    
    @staticmethod 
    def Reinitialse():
        Candidat.Liste_candidat = []



class Votant:
    nbv = 0
    Electorat = []
    distance = {}

    @staticmethod 
    def Compteur() :
        Votant.nbv+=1

    @staticmethod 
    def Reinitialse():
        Votant.nbv = 0
        Votant.Electorat = []
    
    def __init__(self,dx,dy):
        self.Compteur()
        self.nom = "Ano"+str(Votant.nbv)
        self.x = dx
        self.y = dy
        self.distance = {}
        (Votant.Electorat).append(self)

    def label(self):
        print("Nom:", self.nom ,"Coordonées:", self.x, ",", self.y)

    @staticmethod 
    def Nbv():
        print("Nombre de votant: ", str(Votant.nbv))

    @staticmethod 
    def Liste_votant():
        return Votant.Electorat

    @staticmethod 
    def Affiche_electorat():
        for i in Votant.Electorat:
            i.label()

    def Distance(self, Liste_c):
        for c in Liste_c:
            d = sqrt(((c.x)-(self.x))**2+((c.y)-(self.y))**2)
            self.distance[c.nom]=d
        self.distance = OrderedDict(sorted(self.distance.items(), key=lambda t: t[1]))
        return self.distance

    def Réinitialiser_Distance(self):
        self.distance = {}


def Electorat_aléatoire(nbv,min,max):
    for i in range(nbv):
        Votant(random.randint(min,max),random.randint(min,max))
