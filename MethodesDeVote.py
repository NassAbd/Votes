from math import sqrt
from collections import OrderedDict
import random
from projet_class import Votant, Candidat
import numpy as np

def Electorat_aléatoire(nbv,min,max):
    for i in range(nbv):
        Votant(random.randint(min,max),random.randint(min,max))
        
def Electorat_gaussien(a,b) : 
    mu, sigma = (a,b), 100

    x = np.random.normal(mu[0], sigma, 50)
    y = np.random.normal(mu[1], sigma, 50)

    x = list(map(lambda x: min(max(int(x), 0), 1000), x))
    y = list(map(lambda y: min(max(int(y), 0), 1000), y))
        
    pairs = list(zip(x, y))
        
    for x, y in pairs : 
        Votant (x, y)
        
def Electorat_gaussien_button() : 
    mu, sigma = 500, 100

    x = np.random.normal(mu, sigma, 50)
    y = np.random.normal(mu, sigma, 50)

    x = list(map(lambda x: min(max(int(x), 0), 1000), x))
    y = list(map(lambda y: min(max(int(y), 0), 1000), y))
        
    pairs = list(zip(x, y))
        
    for x, y in pairs : 
        Votant (x, y)
        
def countX(lst, x): #pour compter le nombre d'occurences d'un élément dans une liste
    count = 0
    for ele in lst:
        if (ele == x):
             count = count + 1
    return count

def Borda(Liste_candidat,Electorat):
    
    print('---Méthode de Borda----')
    Liste = []
    Score = len(Liste_candidat)
    Resultat = dict()

    for k in Liste_candidat:
        Resultat[k.nom]=0

    
    for l in Electorat :
        for k in l.Distance(Liste_candidat):
            Resultat[k]+=Score
            Score=Score-1
        Score = len(Liste_candidat)

    Resultat = OrderedDict(sorted(Resultat.items(), key=lambda t: t[1]))
    res = list(Resultat.items())
    print("Résultat :",res)
    k,v = res[len(res)-1]
    print("Vainqueur :",k)
    print('---------------------------')

    return res

def Copeland(listeC, listeV):

    t = len(listeC)
    tableau_score = np.zeros((t,t+1))
    tableau_nom = []

    print('----Méthode de Copeland----')
    Score = {}  #initialisation des scores
    for c in listeC:
        Score[c.nom] = 0
    
    for v in listeV:
        v.Distance(listeC)

    DejaVu = set() #duels déjà faits

    x=0
    y=0

    for c1 in listeC:
        y=0
        tableau_nom.append(c1.nom)
        for c2 in listeC:
            if c1 != c2 and (c1,c2) not in DejaVu:
                #print("Duel", c1.nom , c2.nom)
                pref1 = 0
                pref2 = 0
                for v in listeV:
                    if v.distance[c1.nom] < v.distance[c2.nom]:
                        pref1 += 1
                    elif v.distance[c1.nom] > v.distance[c2.nom]:
                        pref2 += 1
                    else:
                        pref1 += 0.5
                        pref2 += 0.5
                tableau_score[x][y]=pref1
                tableau_score[y][x]=pref2
                if pref1 > pref2:
                    Score[c1.nom] = Score[c1.nom] + 1
                    tableau_score[x][t] += 1
                    #print(c1.nom, "gagne")
                    
                elif pref1 < pref2:
                    Score[c2.nom] = Score[c2.nom] + 1
                    tableau_score[y][t] += 1
                    #print(c2.nom, "gagne")
                else:
                    Score[c2.nom] = Score[c2.nom] + 0.5
                    Score[c1.nom] = Score[c1.nom] + 0.5
                    tableau_score[x][t] += 0.5
                    tableau_score[y][t] += 0.5
                    #print("égalité")
                #print("----------------")
            DejaVu.add((c2,c1))
            y+=1
        x+=1

    
    Score = OrderedDict(sorted(Score.items(), key=lambda t: t[1]))
    res = list(Score.items())

    print('Resultat :' , res)
    print('Vainqueur : ',res[len(Score)-1][0])
    print('---------------------------')
    vainqueur = res[len(Score)-1]
    print(tableau_score)
    print(tableau_nom)
    return tableau_score, tableau_nom, vainqueur
    
def maj2tours (listeC, listeV) : 

    print('----Majorité à 2 tours----')

    #Tour 1
    lresT1 = []
    for v in listeV : 
        lresT1.append(next(iter(v.Distance(listeC))))  #pour obtenir le candidat selectionné pour chaque votant parmi tous les candidats(le candidat le plus proche)
    dicres = {}
    for c in listeC : 
        dicres[c.nom] = countX(lresT1, c.nom)  #initialisation des resultats de chaque candidat à zero
    dicres = OrderedDict(sorted(dicres.items(), key=lambda t: t[1], reverse=True)) #dictionnaire trié dans l'ordre décroissant du nombre de voix
    ResTour1 = list(dicres.items())

    print('Résultats 1er tour :', ResTour1)

    #Tour2

    lresT2 = []
    listeC2 = []
    for k,v in list(dicres.items())[:2]: 
        for c in listeC : 
                if k == c.nom : 
                    listeC2.append(c) #liste des candidats au 2eme tour
    for v in listeV : 
        v.Réinitialiser_Distance()
        lresT2.append(next(iter(v.Distance(listeC2))))  #pour obtenir le candidat selectionné pour chaque votant parmi tous les candidats(le candidat le plus proche)

    dicres2 = {}
    for c in listeC2 : 
        dicres2[c.nom] = countX(lresT2, c.nom)  #initialisation des resultats de chaque candidat à zero
    dicres2 = OrderedDict(sorted(dicres2.items(), key=lambda t: t[1], reverse=True)) #dictionnaire trié dans l'ordre décroissant du nombre de voix
    ResTour2 = list(dicres2.items())

    print('Résultats 2eme tour :', ResTour2)

    print('Vainqueur : ', ResTour2[0][0])
    print('---------------------------')
    return ResTour1, ResTour2
    
def Simpson(listeC, listeV):
    print('----Méthode de Simpson----')

    t = len(listeC)
    tableau_score = np.zeros((t,t+1))
    tableau_nom = []
    Score = {}  #initialisation des scores

    for c in listeC:
        Score[c.nom] = len(listeV)
    
    for v in listeV:
        v.Distance(listeC)

    DejaVu = set() #duels déjà faits

    x=0
    y=0

    for c1 in listeC:
        y=0
        tableau_nom.append(c1.nom)
        for c2 in listeC:
            if c1 != c2 and (c1,c2) not in DejaVu:
                #print("Duel", c1.nom , c2.nom)
                pref1 = 0
                pref2 = 0
                for v in listeV:
                    if v.distance[c1.nom] < v.distance[c2.nom]:
                        pref1 += 1
                    elif v.distance[c1.nom] > v.distance[c2.nom]:
                        pref2 += 1
                    else:
                        pref1 += 0.5
                        pref2 += 0.5
                
                tableau_score[x][y]=pref1
                tableau_score[y][x]=pref2

                #print(pref1, pref2)
                #print("---------------------")
                if pref1 < Score[c1.nom]:
                    Score[c1.nom] = pref1
                if pref2 < Score[c2.nom]:
                    Score[c2.nom] = pref2

            DejaVu.add((c2,c1))
            y+=1
        tableau_score[x][t] = Score[c1.nom]
        x+=1

    Score = OrderedDict(sorted(Score.items(), key=lambda t: t[1]))
    res = list(Score.items())
    
    print('Resultat :', res)
    print('Vainqueur :', res[len(Score)-1][0])
    print('---------------------------')

    vainqueur = res[len(Score)-1]
    print(tableau_score)
    print(tableau_nom)
    return tableau_score, tableau_nom, vainqueur
    
def Veto(Liste_candidat,Electorat):
    
    print('---Méthode de Veto----')
    Liste = []
    Resultat = dict()

    for k in Liste_candidat:
        Resultat[k.nom]=0

    for votant in Electorat :
        votant.distance = votant.Distance(Liste_candidat)

        for candidat, position in votant.distance.items():
            candidat_elem = next(reversed(votant.distance)) #on recupere la cle du candidat a eliminer , clé du dernier element de l'ordered dict
            if candidat != candidat_elem:
                Resultat[candidat]+= 1

    


    Resultat = OrderedDict(sorted(Resultat.items(), key=lambda t: t[1]))

    res = list(Resultat.items())
    print("Résultat :",res)
    k,v = res[len(res)-1]
    print("Vainqueur :",k)
    print('---------------------------')
    
    #return list(Resultat.items())[len(Resultat)-1]
    return res 


def Approbation(Liste_candidat,Electorat):

    print("---Méthode d'Approbation---")

    rayon = 500#Arbitraire
    Resultat = dict()

    for candidat in Liste_candidat:
        Resultat[candidat.nom]=0

    for votant in Electorat:
        votant.distance = votant.Distance(Liste_candidat)

        for candidat, position in votant.distance.items():
            if position <= rayon:
                Resultat[candidat]+=1
    
    Resultat = OrderedDict(sorted(Resultat.items(), key=lambda t: t[1]))

    res = list(Resultat.items())
    print("Résultat :",res)
    k,v = res[len(res)-1]
    print("Vainqueur :",k)
    print('---------------------------')

    
    #return list(Resultat.items())[len(Resultat)-1]
    return res
