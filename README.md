LU2IN013 – Groupe 1
Nom du groupe : GLAN
Membres : Guillaume LEBRETON / Luka BALY / Abdallah NASSUR / Nabil BATTATA


## Objectif :

L’objectif du projet est de simuler et visualiser certains processus électoraux. 
Plusieurs règles de votes doivent être comparées. Les électeurs et les candidats sont plongés dans le plan (on peut voir cela comme leurs positions selon deux axes). La proximité entre un votant et un candidat représente l’intensité de la préférence du votant pour ce candidat.

## Structure du Projet :

Le projet est structuré en 4 programmes : 

- projet_class.py : défini les classes Candidat et Votant qui vont nous permettre de créer un panel de candidat et un électorat. Ces classes vont également nous permettre  d’appliquer toutes sortes de fonctions sur nos échantillons.

- MethodesDeVote.py : défini les différentes méthodes de vote étudiées dans l’UE (Majorité à 2 tours, Borda, Copeland, Simpson, Approbation, Veto)

- interface.py : Défini la classe interface qui présente un graphique tkinter avec toutes les fonctions qui seront mis à disposition de l’utilisateur

- main.py : Qui permet de lancer l’interface pour tester les modalités du projet










## Fonctionnalités :


Notre interface graphique est composé d’un plan pour situer les candidats et les votants et de boutons reparti en 4 groupe




A gauche : disposition et suppression des votants et candidats

A droite : Les méthodes de votes, résultats affichés avec des graphes pyplot

En haut : pour sauvegarder et charger des situations à partir de fichier txt

En bas : méthode d’influence sur les candidats










Paramètres des classes Votant et Candidat : 

- Votant :
  
  - Nom prédéfini 
  - Coordonnées x et y
  - Dictionnaire de la distance entre ce votant et tous les candidats

- Candidat :

  - Nom choisi par le client
  - Coordonnées x et y
  - L’utilité (Score de chaque candidat par rapport à leurs distances entre chaque votant)
  - Pourcentage d’attaque choisi aléatoirement (ce pourcentage va nous permettre de définir le budget à dépenser pour l’attaque et la défense)
  - Un budget attaque pour attaquer un autre candidat (déplace aléatoirement le candidat  qui a le plus d’utilité sur le graphe)
  -  Un budget  défense pour se défendre face aux autres candidats (le candidat se déplace de telle sorte qu’il obtienne plus de voix à partir d’un rayon prédéfini) 




