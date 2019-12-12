# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:59:27 2019

@author: mathieu9
"""


class Etape:
    """
    
    """
    
    def __init__(self, number, au_plus_tot, au_plus_tard, taches = []):
        """
        Constructeur de la classe Etape
        """
        
        self.number = number
        self.au_plus_tot = au_plus_tot
        self.au_plus_tard = au_plus_tard
        
        self.taches = taches
        

# =============================================================================
# Question 2.1) Getter pour les etapes
# =============================================================================
        
    def get_au_plus_tot(self):
        return self.au_plus_tot
    
    def get_au_plus_tard(self):
        return self.au_plus_tard
    
    def get_number(self):
        return self.number
    
    def get_next_steps(self):
        return [tache.next_step for tache in self.taches]
    
    def get_previous_steps(self):
        pass
    

# =============================================================================
# Tests
# =============================================================================
    
    def parcourir(self, liste_passage = [], liste_numbers = []):
        
        liste_numbers = [self.get_number()]
        
        for etape in self.get_next_steps():
            
            if not etape in liste_passage:
#            if True:
            
                liste_passage.append(etape)
                
                liste_numbers += etape.parcourir(liste_passage)
                
        return liste_numbers
            


class Tache:
    """
    
    """
    
    def __init__(self, name, duration, next_step = None):
        """
        Constructeur de la classe Tache
        """
        self.name = name
        self.duration = duration
        
        self.next_step = next_step

# =============================================================================
# Question 2.2) Getter pour les taches
# =============================================================================

    def get_name(self):
        return self.name
    
    def get_duration(self):
        pass
    
    def get_begin_step(self):
        pass
    
    def get_end_step(self):
        pass
    



# =============================================================================
# Question 4) Chemin Critique
# =============================================================================

def critique():
    """
    Prend en parametre un diagramme pert
    Retourne le chemin critique (Djikstra)
    """
    pass

# =============================================================================
# Question 5.1) compute_au_plus_tot
# =============================================================================

def compute_au_plus_tot():
    """
    Prend en parametre un diagramme pert
    Retourne le chemin critique (Djikstra)
    """
    pass


# =============================================================================
# Question 5.2) compute_au_plus_tard
# =============================================================================

def compute_au_plus_tard():
    """
    Prend en parametre un diagramme pert
    Retourne le chemin critique (Djikstra)
    """
    pass





etape8 = Etape('8', 220, 220) 
tacheH = Tache('H', 10, etape8)
etape7 = Etape('7', 210, 210, [tacheH]) 
tacheG = Tache('G', 60, etape7)
tacheT = Tache('T', 0, etape7)   
etape5 = Etape('5', 50, 210, [tacheT]) 
etape6 = Etape('6', 150, 150, [tacheG])    
etape3 = Etape('3', 150, 210, [tacheT])   
tacheE = Tache('E', 10, etape5)
tacheF = Tache('F', 30, etape6)
tacheC = Tache('C', 30, etape3)
etape4 = Etape('4', 40, 200, [tacheE])
etape2 = Etape('2', 120, 120, [tacheC,tacheF])
tacheD = Tache('D', 10, etape4)
tacheB = Tache('B', 90, etape2)
etape1 = Etape('1', 30, 30, [tacheB,tacheD])
tacheA = Tache('A', 30, etape1)
etape0 = Etape('0', 0, 0, [tacheA])






#Etape0 = Etape(0, 0, 0)
#Etape1 = Etape(1, 30, 30)
#Etape2 = Etape(2, 120, 120)
#Etape3 = Etape(3, 150, 210)
#Etape4 = Etape(4, 40, 200)
#Etape5 = Etape(5, 50, 210)
#Etape6 = Etape(6, 150, 150)
#Etape7 = Etape(7, 210, 210)
#Etape8 = Etape(8, 220, 220)
#
#
#TacheA = Tache('A', 30)
#TacheB = Tache('B', 90)
#TacheC = Tache('C', 30)
#TacheD = Tache('D', 10)
#TacheE = Tache('E', 10)
#TacheF = Tache('F', 30)
#TacheG = Tache('G', 60)
#TacheH = Tache('H', 10)








