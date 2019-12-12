# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:59:27 2019

@author: Paul MATHIEU
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
        """
        getter de l'attirbut au_plus_tot
        """
        return self.au_plus_tot
    
    def get_au_plus_tard(self):
        """
        getter de l'attirbut au plus_tard
        """
        return self.au_plus_tard
    
    def get_number(self):
        """
        getter de l'attirbut number
        """
        return self.number
    
    def get_next_steps(self):
        """
        getter qui permet d'obtenir toutes les etapes suivantes
        """
        return [tache.next_step for tache in self.taches]
    
    def get_previous_steps(self, etape_recherche, liste_passage = [], liste_previous_steps = []):
        """
        getter qui permet d'obtenir toutes les etapes precedentes
        """ 
        if etape_recherche in self.get_next_steps():
            liste_previous_steps.append(self)

        for etape in self.get_next_steps():
            
            if not etape in liste_passage:
            
                liste_passage.append(etape)
                
                liste_previous_steps += etape.get_previous_steps(etape_recherche, 
                                                                 liste_passage, 
                                                                 liste_previous_steps)
                
        return list(set(liste_previous_steps))

    def get_previous_taches(self, etape_recherche):
        liste_retourne = []
        for etape in self.get_previous_steps(etape_recherche):
            for tache in etape.taches:
                if tache.get_end_step() == etape_recherche:
                    liste_retourne.append(tache)
        return liste_retourne
            
    def get_last_tache(self, liste_passage = [], etape_retourner = []):
        
        etape_retourner = self
        
        for etape in self.get_next_steps():
            
            if not etape in liste_passage:
#            if True:
            
                liste_passage.append(etape)
                
                return etape.get_last_tache(liste_passage)
                
        return etape_retourner


# =============================================================================
# Setters
# =============================================================================

    def set_au_plus_tot(self, value):
        self.au_plus_tot = value

    def set_au_plus_tard(self, value):
        self.au_plus_tard = value

# =============================================================================
# Question 3) Chemin Critique
# =============================================================================

    def critique(self):
        """
        Prend en parametre un diagramme pert
        Retourne le chemin critique
        """
        chemin_critique = [self.get_number()]
        
        for etape in self.get_next_steps():
            if not etape == None:
                if etape.get_au_plus_tot() == etape.get_au_plus_tard():
                    chemin_critique += etape.critique()
                    break
        return chemin_critique
        

# =============================================================================
# Question 4.1) compute_au_plus_tot
# =============================================================================

    def compute_au_plus_tot(self, compteur_au_plus_tot = 0):
        """
        Prend en parametre la racine diagramme pert
        Calcul toutes les valeurs au_plus_tot
        
        Algo recursif qui parcours tous les arcs avec un compteur qui ajoute
        leur valeur (depart du noeud racine)
        
        La valeur gardee est la plus grande
        """
                
            
        if self.get_au_plus_tot() in [0, None] or self.get_au_plus_tot() < compteur_au_plus_tot:
            
            self.set_au_plus_tot(compteur_au_plus_tot)
#                print(compteur_au_plus_tot)
                
                    
        for tache in self.taches:
            
            compteur_au_plus_tot += tache.duration
            
            etape_suivante = tache.get_end_step()
            etape_suivante.compute_au_plus_tot(compteur_au_plus_tot)
            
            compteur_au_plus_tot -= tache.duration

            


# =============================================================================
# Question 4.2) compute_au_plus_tard
# =============================================================================

    def compute_au_plus_tard():
        """
        Prend en parametre la racine diagramme pert
        Calcul toutes les valeurs au_plus_tart
        
        Algo recursif qui parcours tous les arcs avec un compteur qui enleve
        leur valeur (depart de la derniere etape)
        
        La valeur gardee est la plus petite
        """
        pass


# =============================================================================
# Tests
# =============================================================================
    
    def parcourir(self, liste_passage = [], liste_numbers = []):
        
        liste_numbers = [self]
        
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
        """
        getter de l'attirbut name
        """
        return self.name
    
    def get_duration(self):
        """
        getter de l'attirbut duration
        """
        return self.duration
    
    def get_begin_step(self, etape0):
        """
        getter de l'etape precedente
        """
        
        end_step = self.get_end_step()
        
        liste_parent_etape_of_end_step = etape0.get_previous_steps(end_step)
        
        for etape in liste_parent_etape_of_end_step:
            
            for tache in etape.taches:
                
                if tache == self:
                    
                    return etape
        

    def get_end_step(self):
        """
        getter de l'etape suivante
        """
        return self.next_step
    










# =============================================================================
# Tests
# =============================================================================
    
    def parcourir(self, liste_passage = [], liste_return = []):
        
        liste_return = [self]
        
        for etape in self.get_next_steps():
            
            if not etape in liste_passage:
#            if True:
            
                liste_passage.append(etape)
                
                liste_return += etape.parcourir(liste_passage)
                
        return liste_return
            



#etape8 = Etape('8', 220, 220) 
#tacheH = Tache('H', 10, etape8)
#etape7 = Etape('7', 210, 210, [tacheH]) 
#tacheG = Tache('G', 60, etape7)
#tacheT = Tache('T', 0, etape7)   
#etape5 = Etape('5', 50, 210, [tacheT]) 
#etape6 = Etape('6', 150, 150, [tacheG])    
#etape3 = Etape('3', 150, 210, [tacheT])   
#tacheE = Tache('E', 10, etape5)
#tacheF = Tache('F', 30, etape6)
#tacheC = Tache('C', 30, etape3)
#etape4 = Etape('4', 40, 200, [tacheE])
#etape2 = Etape('2', 120, 120, [tacheC,tacheF])
#tacheD = Tache('D', 10, etape4)
#tacheB = Tache('B', 90, etape2)
#etape1 = Etape('1', 30, 30, [tacheB,tacheD])
#tacheA = Tache('A', 30, etape1)
#etape0 = Etape('0', 0, 0, [tacheA])

etape8 = Etape('8', None, None) 
tacheH = Tache('H', 10, etape8)
etape7 = Etape('7', None, None, [tacheH]) 
tacheG = Tache('G', 60, etape7)
tacheT = Tache('T', 0, etape7)   
etape5 = Etape('5', None, None, [tacheT]) 
etape6 = Etape('6', None, None, [tacheG])    
etape3 = Etape('3', None, None, [tacheT])   
tacheE = Tache('E', 10, etape5)
tacheF = Tache('F', 30, etape6)
tacheC = Tache('C', 30, etape3)
etape4 = Etape('4', None, None, [tacheE])
etape2 = Etape('2', None, None, [tacheC,tacheF])
tacheD = Tache('D', 10, etape4)
tacheB = Tache('B', 90, etape2)
etape1 = Etape('1', None, None, [tacheB,tacheD])
tacheA = Tache('A', 30, etape1)
etape0 = Etape('0', None, None, [tacheA])






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


# =============================================================================
# Tests des fonctions :
# =============================================================================

#etape0.parcourir()

#print(etape0.get_previous_steps(etape7))
#print([etape.number for etape in etape0.get_previous_steps(etape7)])

#etape0.critique()

#print(etape7.au_plus_tot)
etape0.compute_au_plus_tot()
#print(etape7.au_plus_tot)

#etape0.get_previous_taches(etape7)












#print(tacheD.get_begin_step(etape0).number)

