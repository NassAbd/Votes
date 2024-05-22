import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import messagebox 
import numpy as np
import random
from projet_class import Votant, Candidat
from MethodesDeVote import Electorat_aléatoire, Electorat_gaussien, Electorat_gaussien_button, maj2tours, Borda, Copeland, Simpson, Approbation, Veto
import os

#sdv univ paris diderot tkinter


class Interface(tk.Tk):

    Liste_pt_candidat = []
    Liste_pt_votant = []
    Liste_nom = []
    Campagne = False

    sauvegarde = []
    sauvegarde_nom = []

    def __init__(self):
        tk.Tk.__init__(self)
        self.add_canvas() # Méthode auxiliaire qui ajoute un canvas qui nous sert 
        self.add_widget() # Méthode auxiliaire qui ajoute des widgets à l'interface
        self.attributes('-fullscreen', True)
        self.configure(bg="light gray")
    
    def add_widget(self):
        self.button = tk.Button(self, text="Exit program", bg="red", command=self.quit)
        self.button2 = tk.Button(self, text="Majorité à 2 tours",bg="white", command=self.M2T)
        self.button3 = tk.Button(self, text="Electorat aléatoire",bg="white", command=self.Elect_al)
        self.button4 = tk.Button(self, text="Réinitialiser éléctorat",bg="white", command=self.reinitialise_elec)
        self.button5 = tk.Button(self, text="Borda",bg="white", command=self.Borda)
        self.button6 = tk.Button(self, text="Réinitialiser Candidat",bg="white", command=self.reinitialise_candidats)
        self.button7 = tk.Button(self, text="Attaque",bg="white", command=self.attaque_interface)
        self.button8 = tk.Button(self, text="Defense",bg="white", command=self.defense_interface)
        self.button9 = tk.Button(self, text="Veto",bg="white", command=self.Veto)
        self.button10 = tk.Button(self, text="Approbation",bg="white", command=self.Approbation)
        self.button11 = tk.Button(self, text="Sauvegarde",bg="white", command=self.Sauvegarde)
        self.button12 = tk.Button(self, text="Charge",bg="white", command=self.Charge)
        self.button13 = tk.Button(self, text="Copeland",bg="white", command=self.Copeland)
        self.button14 = tk.Button(self, text="Electorat gaussien",bg="white", command=self.Elect_gauss_butt)
        self.button15 = tk.Button(self, text="Simpson",bg="white", command=self.Simpson)
        self.button17 = tk.Button(self, text="Info Vote",bg="white", command=self.Help)
        self.button16 = tk.Button(self, text="Présidentielle 2017",bg="white", command=self.Election_Presidentielle_2017)
        
        
        self.lbl = tk.Label(self , text = "Ajouter Candidat = Clic droit \nAjouter Votant = Clic Gauche \nElectorat Gaussien = Clic milieu", font=18, bg='yellow')
        self.lbl.place(x=1662, y=0)
        
        

        self.button.place(x=0,y=0)
        self.button2.place(x=1650,y=500)
        self.button3.place(x=100,y=500)
        self.button4.place(x=100,y=540)
        self.button5.place(x=1650,y=540)
        self.button6.place(x=100,y=580)
        self.button7.pack(side=tk.BOTTOM)
        self.button8.pack(side=tk.BOTTOM)
        self.button9.place(x=1650,y=580)
        self.button10.place(x=1650,y=620)
        self.button11.pack()
        self.button12.pack()
        self.button13.place(x=1650,y=460)
        self.button14.place(x=100,y=620)
        self.button15.place(x=1650,y=660)
        self.button16.place(x=100,y=460)
        self.button17.place(x=1650,y=420)
        


    def add_canvas(self):
        self.canvas = tk.Canvas(self, width=1000, height=1000, bg="white") #OPTION DE TKINTER QUI PERMET D'AVOIR UNE ZONE OU LONT PEUT AJOUTER DES FORMES
        self.canvas.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
        self.canvas.create_line(0,500,500,500, fill="black")
        self.canvas.create_line(500,500,1000,500, fill="black")
        self.canvas.create_line(500,0,500,500, fill="black")
        self.canvas.create_line(500,500,500,1000, fill="black")
    
    def add_point(self, dx, dy):
        self.canvas.create_oval(dx, dy, dx, dy, fill="black", width="10")

    def mouse_add_point_candidat(self, event):
        if Interface.Campagne :
            tk.messagebox.showerror(title=None,message="Campagne débuté, plus d'inscription possible !")
            return
        self.maj_pt_candidats()
        x = event.x
        y = event.y
        def get_entry(event):
            nom = ligne_texte.get()
            for c in Candidat.Liste_candidat:
                if (nom==c.nom):
                    tk.messagebox.showinfo(title=None,message="Ce nom existe déjà !")
                    root.destroy()
                    return
            Candidat(nom, x, y)
            self.maj_pt_candidats()
            root.destroy()
        root = tk.Tk()
        l = tk.Label( root, text = "Entrez le nom du candidat" )
        l.pack( side = tk.LEFT )
        ligne_texte = tk.Entry(root, width=30)
        ligne_texte.focus()
        ligne_texte.pack()
        root.bind('<Return>', get_entry)


    def mouse_add_point_votant(self, event):
        self.Liste_pt_votant.append(self.canvas.create_oval(event.x, event.y, event.x, event.y, fill='black', outline="orange",width="10"))
        new_votant = Votant(event.x, event.y)


    def Help(self):
        
        fichier = open("info_vote.txt", "r")
        info = fichier.read()

        fen=tk.Tk()
        fen.title("Méthode de vote")
        texteLabel = tk.Label(fen, text = info)
        texteLabel.pack(anchor='w')

    def Elect_al(self):
        Electorat_aléatoire(50,0,1000)
        for v in Votant.Electorat:
            self.Liste_pt_votant.append(self.canvas.create_oval(v.x, v.y, v.x, v.y, fill='black', outline="orange",width="10"))

    def Elect_gauss(self, event):
        Electorat_gaussien(event.x, event.y)
        for v in Votant.Electorat:
            self.Liste_pt_votant.append(self.canvas.create_oval(v.x, v.y, v.x, v.y, fill='black', outline="orange",width="10"))
            
    def Elect_gauss_butt(self):
        Electorat_gaussien_button()
        for v in Votant.Electorat:
            self.Liste_pt_votant.append(self.canvas.create_oval(v.x, v.y, v.x, v.y, fill='black', outline="orange",width="10"))
    
    def reinitialise_elec(self):
        '''Reinitialise l'éléctorat'''
        self.canvas.delete("all")
        Votant.Reinitialse()
        for c in Candidat.Liste_candidat:
            self.Liste_pt_candidat.append(self.canvas.create_rectangle(c.x, c.y, c.x, c.y, fill="", width="25"))
            self.Liste_nom.append(self.canvas.create_text(c.x, c.y-25, text=c.nom, fill="black", font=('Helvetica 10 bold')))
        self.canvas.create_line(0,500,500,500, fill="black")
        self.canvas.create_line(500,500,1000,500, fill="black")
        self.canvas.create_line(500,0,500,500, fill="black")
        self.canvas.create_line(500,500,500,1000, fill="black")
        

    def reinitialise_candidats(self):
        '''Reinitialise les candidats'''
        Interface.Campagne = False
        for p in self.Liste_pt_candidat:
            self.canvas.delete(p)
        for n in self.Liste_nom:
            self.canvas.delete(n)
        Candidat.Reinitialse()



    def maj_pt_candidats(self):
        '''maj des candidats'''
        for p in self.Liste_pt_candidat:
            self.canvas.delete(p)
        for n in self.Liste_nom:
            self.canvas.delete(n)
        for c in Candidat.Liste_candidat:
            self.Liste_pt_candidat.append(self.canvas.create_rectangle(c.x, c.y, c.x, c.y, fill="", width="25"))
            self.Liste_nom.append(self.canvas.create_text(c.x, c.y-25, text=c.nom, fill="black", font=('Helvetica 10 bold')))
        
        Candidat.maj_util(Votant.Electorat,len(Votant.Electorat))


    def maj_pt_votants(self):
        for p in self.Liste_pt_votant:
            self.canvas.delete(p)
        for v in Votant.Electorat:
            self.canvas.create_oval(v.x, v.y, v.x, v.y, fill='black', outline="orange",width="10")  


    def Sauvegarde(self):
        def get_entry(event):
            nom_sauvegarde = ligne_texte.get()
            file_save =  open(nom_sauvegarde+".txt","w+")
            file_save.write("Candidats:\n")
            for c in Candidat.Liste_candidat:
                file_save.write(c.nom+":"+str(c.x)+":"+str(c.y)+"\n")
            file_save.write("Votants:\n")
            for v in Votant.Electorat:
                file_save.write(str(v.x)+":"+str(v.y)+"\n")
            root.destroy()
        root = tk.Tk()
        l = tk.Label( root, text = "Entrez le nom de votre fichier à sauvegarder")
        l.pack( side = tk.LEFT )
        ligne_texte = tk.Entry(root, width=30)
        ligne_texte.focus()
        ligne_texte.pack()
        root.bind('<Return>', get_entry)

    def Charge(self):
        self.reinitialise_candidats()
        self.reinitialise_elec()
        def get_entry(event):
            nom = ligne_texte.get()+".txt"
            if(not (os.path.exists(nom))):
                tk.messagebox.showerror(title=None,message="Ce fichier n'existe pas!")
                root.destroy()
                return
            file_charge = open(nom,"r")
            mode = 0
            file_charge_iterate = file_charge.readlines()
            for line in file_charge_iterate:
                if(line == "Candidats:\n"):
                    mode = 0
                    continue
                if(line == "Votants:\n"):
                    mode = 1
                    continue
                if(mode == 0):
                    data = line.split(':')
                    Candidat(data[0], float(data[1]), float(data[2]))
                if(mode ==1):
                    data = line.split(':')
                    Votant(float(data[0]), float(data[1])) 
            self.maj_pt_candidats()
            self.maj_pt_votants()
            root.destroy()
        root = tk.Tk()
        l = tk.Label( root, text = "Entrez le nom du fichier à charger")
        l.pack( side = tk.LEFT )
        ligne_texte = tk.Entry(root, width=30)
        ligne_texte.focus()
        ligne_texte.pack()
        root.bind('<Return>', get_entry)
        
        




    def attaque_interface(self):
        Interface.Campagne = True
        d,a=self.budget_non_nul()
        if(a==0):
            tk.messagebox.showinfo(title=None,message="Tous les budgets attaque de tous les Candidats ont été dépensé")
            return
        def get_entry(event):
            atta = ligne_texte.get()
            attaquant = None
            for c in Candidat.Liste_candidat:
                if (c.nom == atta):
                    attaquant = c
            if (attaquant == None):
                tk.messagebox.showerror(title=None,message="Ce Candidat n'existe pas!")
                root.destroy()
                return
            victime = None
            u_min = 10000000
            for c in Candidat.Liste_candidat:
                if (c.nom==attaquant.nom):
                    continue
                if (c.util<u_min):
                    u_min=c.util
                    victime = c

            att = attaquant.attaque_candidat(victime)
            if (att==0) :
                res = attaquant.nom + " n'a plus de budget"
            else : 
                res = attaquant.nom + " a attaqué " + victime.nom
            tk.messagebox.showinfo(title=None,message=res)
            self.maj_pt_candidats()
            root.destroy
        root = tk.Tk()
        l = tk.Label( root, text = "Entrez le nom de l'attaquant")
        l.pack( side = tk.LEFT )
        ligne_texte = tk.Entry(root, width=30)
        ligne_texte.focus()
        ligne_texte.pack()
        root.bind('<Return>', get_entry)

    def defense_interface (self): 
        Interface.Campagne = True
        d,a=self.budget_non_nul()
        if(d==0):
            tk.messagebox.showinfo(title=None,message="Tous les budgets défense de tous les Candidats ont été dépensé")
            return
        defenseur = random.choice(Candidat.Liste_candidat)
        df = defenseur.Defense_candidat(Votant.Electorat)
        if df == 0 : 
            res = defenseur.nom + " n'a plus de budget"
        else : 
            res = defenseur.nom + " s'est défendu"

        tk.messagebox.showinfo(title=None,message=res)
        self.maj_pt_candidats()
      
    def budget_non_nul(self):
        d = 0
        a = 0
        for c in Candidat.Liste_candidat:
            if (c.budget_defense != 0):
                d=d+1
            if (c.budget_attaque != 0):
                a=a+1
        return d,a
    
    def M2T(self):
        if (Votant.nbv == 0) and (len(Candidat.Liste_candidat) == 0):
            messagebox.showerror("Erreur", "Pas de candidat ni de votant")
            return
        elif Votant.nbv == 0:
            messagebox.showerror("Erreur", "Pas de votant")
            return
        elif len(Candidat.Liste_candidat) == 0:
            messagebox.showerror("Erreur", "Pas de candidat")
            return
        

        res1,res2 = maj2tours(Candidat.Liste_candidat, Votant.Electorat)
        liste1 = []
        for c,s in res1 :
            for i in range (s) : 
                liste1.append(c)

        fig,(ax1, ax2) = plt.subplots(1,2, constrained_layout=True)
        fig.suptitle("Vainqueur : "+ res2[0][0])

        ax1.hist(liste1, color= "blue", edgecolor = 'black')
        ax1.set_title("Résultat du premier tour")
        ax1.set(xlabel="Candidats", ylabel="Nombre de voix")
        ax1.tick_params(axis='x', rotation=45)
        
        liste2 = []
        for c,s in res2 : 
            for i in range (s) :
                liste2.append(c)

        
        ax2.hist(liste2, color= "blue", edgecolor = 'black')
        ax2.set_title("Résultat du deuxième tour")
        ax2.set(xlabel="Candidats", ylabel="Nombre de voix")
        ax2.tick_params(axis='x', rotation=45)

        fig.tight_layout()

        plt.show()



    
    def Borda(self):
        if (Votant.nbv == 0) and (len(Candidat.Liste_candidat) == 0):
            messagebox.showerror("Erreur", "Pas de candidat ni de votant")
            return
        elif Votant.nbv == 0:
            messagebox.showerror("Erreur", "Pas de votant")
            return
        elif len(Candidat.Liste_candidat) == 0:
            messagebox.showerror("Erreur", "Pas de candidat")
            return

        res = Borda(Candidat.Liste_candidat,Votant.Electorat)
        x = []
        y = []
        tot = 0
        for c,s in res:
            x.append(s)
            y.append(c)
            tot += s
        plt.figure("Borda")
        plt.pie(x, labels = y, normalize = True, autopct = lambda x : str(round(x*tot/100)))
        k,v = res[len(res)-1]
        print (res)
        plt.title("Vainqueur :"+k)

        plt.show()


    def Veto(self):
        if (Votant.nbv == 0) and (len(Candidat.Liste_candidat) == 0):
            messagebox.showerror("Erreur", "Pas de candidat ni de votant")
            return
        elif Votant.nbv == 0:
            messagebox.showerror("Erreur", "Pas de votant")
            return
        elif len(Candidat.Liste_candidat) == 0:
            messagebox.showerror("Erreur", "Pas de candidat")
            return

        res = Veto(Candidat.Liste_candidat,Votant.Electorat)
        x = []
        y = []
        tot = 0
        for c,s in res:
            x.append(s)
            y.append(c)
            tot += s
        plt.figure("Veto")
        plt.pie(x, labels = y, normalize = True, autopct = lambda x : str(round(x*tot/100)))
        k,v = res[len(res)-1]
        print (res)
        plt.title("Vainqueur :"+k)

        plt.show()
        
        
    def Approbation(self):
        if (Votant.nbv == 0) and (len(Candidat.Liste_candidat) == 0):
            messagebox.showerror("Erreur", "Pas de candidat ni de votant")
            return
        elif Votant.nbv == 0:
            messagebox.showerror("Erreur", "Pas de votant")
            return
        elif len(Candidat.Liste_candidat) == 0:
            messagebox.showerror("Erreur", "Pas de candidat")
            return

        res = Approbation(Candidat.Liste_candidat,Votant.Electorat)
        x = []
        y = []
        tot = 0
        for c,s in res:
            x.append(s)
            y.append(c)
            tot += s
        plt.figure("Approbation")
        plt.pie(x, labels = y, normalize = True, autopct = lambda x : str(round(x*tot/100)))
        k,v = res[len(res)-1]
        print (res)
        plt.title("Vainqueur :"+k)

        plt.show()

    def Copeland(self):
        if (Votant.nbv == 0) and (len(Candidat.Liste_candidat) == 0):
            messagebox.showerror("Erreur", "Pas de candidat ni de votant")
            return
        elif Votant.nbv == 0:
            messagebox.showerror("Erreur", "Pas de votant")
            return
        elif len(Candidat.Liste_candidat) == 0:
            messagebox.showerror("Erreur", "Pas de candidat")
            return

        tab_score,tab_nom,vainq = Copeland(Candidat.Liste_candidat,Votant.Electorat)
        labels_x = tab_nom.copy()
        labels_x.append("score")


        fig, ax = plt.subplots()
        hm = ax.imshow(tab_score, cmap='copper')
        ax.set_xticks(np.arange(len(labels_x)), labels=labels_x, rotation = 45)
        ax.set_yticks(np.arange(len(tab_nom)), labels=tab_nom)
        for i in range(len(tab_nom)):
            for j in range(len(labels_x)):
                text = ax.text(j, i, tab_score[i, j],ha="center", va="center", color="w")
        fig.tight_layout()
        ax.set_title("Vainqueur : "+ vainq[0])
        plt.show()
    
    def Simpson(self):
        if (Votant.nbv == 0) and (len(Candidat.Liste_candidat) == 0):
            messagebox.showerror("Erreur", "Pas de candidat ni de votant")
            return
        elif Votant.nbv == 0:
            messagebox.showerror("Erreur", "Pas de votant")
            return
        elif len(Candidat.Liste_candidat) == 0:
            messagebox.showerror("Erreur", "Pas de candidat")
            return

        tab_score,tab_nom,vainq = Simpson(Candidat.Liste_candidat,Votant.Electorat)
        labels_x = tab_nom.copy()
        labels_x.append("score")

        fig, ax = plt.subplots()
        hm = ax.imshow(tab_score, cmap='copper')
        ax.set_xticks(np.arange(len(labels_x)), labels=labels_x, rotation = 45)
        ax.set_yticks(np.arange(len(tab_nom)), labels=tab_nom)
        for i in range(len(tab_nom)):
            for j in range(len(labels_x)):
                text = ax.text(j, i, tab_score[i, j],ha="center", va="center", color="w")
        fig.tight_layout()
        plt.title("Vainqueur :" + vainq[0])

        plt.show()


    def Electorat_2017(self, a, b, nb,r):
        mu, sigma = (a,b), r
        x = np.random.normal(mu[0], sigma, nb)
        y = np.random.normal(mu[1], sigma, nb)

        x = list(map(lambda x: min(max(int(x), 0), 1000), x))
        y = list(map(lambda y: min(max(int(y), 0), 1000), y))
        
        pairs = list(zip(x, y))
        for x, y in pairs : 
            Votant (x, y)


    def Election_Presidentielle_2017(self):
        self.reinitialise_candidats()
        self.reinitialise_elec()
        liste_votants_2017 = [2401,2130,1958,2001,470,92,18,121,64,109,636]
        liste_rayons = [20,20,60,60,5,5,5,5,5,5,20]
        C1 = Candidat("Macron",753,250)
        C2 = Candidat("Lepen",430,803)
        C3 = Candidat("Mélenchon",115,445)
        C4 = Candidat("Fillon",899,612)
        C5 = Candidat("Aignan",496,849)
        C6 = Candidat("Asselineau",311,747)
        C7 = Candidat("Cheminade",341,702)
        C8 = Candidat("Lassalle",270,695)
        C9 = Candidat("Arthaud",106,317)
        C10 = Candidat("Poutou",82,185)
        C11 = Candidat("Hamon",283,88)
        C4m = Candidat("Fillon",900, 450) #centre de gaussienne modifiée
        C3m = Candidat("Mélenchon",400, 400) #centre de gaussienne modifiée
        C11m = Candidat("Hamon",183,128)
        liste_candidats_2017 = [C1,C2,C3m,C4m,C5,C6,C7,C8,C9,C10,C11m]
        for i in range (len(liste_votants_2017)) : 
            self.Electorat_2017(liste_candidats_2017[i].x, liste_candidats_2017[i].y, liste_votants_2017[i], liste_rayons[i])

        for v in Votant.Electorat:
            self.canvas.create_oval(v.x, v.y, v.x, v.y, fill='black', outline="orange",width="10")

        Candidat.Liste_candidat.pop()
        Candidat.Liste_candidat.pop()
        Candidat.Liste_candidat.pop()

        self.maj_pt_candidats()