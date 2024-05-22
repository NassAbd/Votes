from projet_class import Votant, Candidat
from MethodesDeVote import Electorat_aléatoire, maj2tours, Borda, Copeland, Simpson, Approbation, Veto
from interface import Interface

if __name__ == "__main__":
    interface = Interface()
    interface.title("Political Compass - LU2IN013 ")

    interface.canvas.bind('<Button-1>', interface.mouse_add_point_votant)
    interface.canvas.bind('<Button-3>', interface.mouse_add_point_candidat)
    interface.canvas.bind('<Button-2>', interface.Elect_gauss)
    interface.mainloop()

    print("Nombre de Votant :",Votant.nbv)
    print("Nombre de Candidat :",len(Candidat.Liste_candidat))

    '''
    Approbation(Candidat.Liste_candidat, Votant.Electorat)
    Simpson(Candidat.Liste_candidat, Votant.Electorat)
    Copeland(Candidat.Liste_candidat, Votant.Electorat)
    Veto(Candidat.Liste_candidat, Votant.Electorat)
    Borda(Candidat.Liste_candidat, Votant.Electorat)
    maj2tours(Candidat.Liste_candidat, Votant.Electorat)
    '''

