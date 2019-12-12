"""
TP2 : ABR
"""

#lien :
# http://ead-polytech.univ-savoie.fr/pluginfile.php/40002/mod_resource/content/2/Ennonce.pdf


from random import randint
import numpy as np


#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~ Recherche dans un ABR :
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
##noeud = (x, FilsGauche, FilsDroit)
#recherche(noeud, valeur)
#        
#    #si la valeur cherchée n'existe pas    
#    Si noeud est vide
#        retourner 'erreur'
#    
#    #si le noeud contient la valeur
#    Si noeud.valeur
#        retourner Vrai
#    
#    #si le noeud a une valeur inférieure
#    Sinon si valeur < noeud.valeur
#        retourner Recherche(noeud.FilsGauche, valeur)
#    
#    #si le noeud a une valeur supérieure
#    Sinon
#        retourner Recherche(noeud.FilsDroit, valeur)
#
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~ Insertion dans un ABR :
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
##noeud = (x, FilsGauche, FilsDroit)
#insertion(noeud, valeur)
#    Si noeud est vide
#        retourner valeur
#    Sinon Si valeur < noeud.valeur
#        retourner (noeud.valeur, insertion(noeud.FilsGauche, valeur), noeud.FilsDroit)
#    Sinon
#        retourner (noeud.valeur, noeud.FilsGauche, insertion(noeud.FilsDroit, valeur))
#    


# =============================================================================
#  Question 1 : Classe 'Node'
# =============================================================================


class Node:
    """
    Un noeud est composé de deux fils et d'une valeur
    """

    def __init__(self, data):
        """
        Initialisation de la classe Node
        """
        self.data = data
        self.leftChild = None
        self.rightChild = None



    def __list__(self):
        return [self.leftChild, self.rightChild]
    
    def get(self, data):
        if data < self.data:
            return self.leftChild.get(data) if self.leftChild else None
        elif data > self.data:
            return self.rightChild.get(data) if self.rightChild else None
        return self
    
    def getParent(self, tree):
        pass
    
    
# =============================================================================
# Question 3 : Recherche de l'existance d'une valeur
# =============================================================================
   
    def existe(self, data, compteur = 1): 
        """
        Parcours de l'arbre pour vérifier si une valeur existe
        Retourne de booleen de verification et le compteur d'itérations
        """
        
        if self.data == data:
            return {"Existe" : True, "NbIterations" : compteur}
      
        # si data sup 
        if self.data < data:
            
            #si le noeud droit est nul
            if self.rightChild is None:
                return {"Existe" : False, "NbIterations" : compteur}
            
            #sinon recursivité
            return self.rightChild.existe(data, compteur + 1) 
        
        # si data inf
        if self.data > data: 
            
            #si le noeud gauche est nul
            if self.rightChild is None:
                return {"Existe" : False, "NbIterations" : compteur}
            
            #sinon recursivité
            return self.leftChild.existe(data, compteur + 1)
        
        #sinon retourner False
        return {"Existe" : False, "NbIterations" : compteur}
    
    

    def insert(self, node):
        """
        Parcours tout l'arbre et ajoute une feuille Node avec la valeur
        """
        
        #si l'arbre est vide
        if self is None: 
            self = node
        
        #sinon si l'arbre existe
        else:
            
            #si la valeur du noeud est sup
            if self.data < node.data:
                
                #si le rightChild est nul
                if self.rightChild is None: 
                    self.rightChild = node
                    
                #else récursivité
                else: 
                    self.rightChild.insert(node)
                    
            #si la valeur du noeud est inf
            elif self.data > node.data: 
                
                #si le rightChild est nul
                if self.leftChild is None: 
                    self.leftChild = node 
                    
                #else récursivité
                else: 
                    self.leftChild.insert(node) 


    def printABR(self, niveau = 0): 
        
        if not self is None:
            
            if not self.leftChild is None:
                self.leftChild.printABR(niveau + 1)
                
            print(self.data) 
            
            if not self.rightChild is None:
                self.rightChild.printABR(niveau + 1)
            
            
    
    #return the level of a node
    def level(self, root):
        level = 0
        while root != self:
            #si la valeur du noeud recherchée est inférieure
            if self.data > root.data:
                root = root.rightChild 
            #sinon si elle est sup
            else:
                root = root.leftChild
            
            print(root.data)
            
            #on augmente le niveau
            level += 1
            
        return level
        


# =============================================================================
# Question 3&4 : Recherche de l'existance d'une valeur
# =============================================================================

def existe(liste, valeur):
    
    """
    pour la méthode existe de node et pour la fonction existe, on a respectivement:
        - n/2 recherche en moyenne dans la liste
        - log2(n) recherche en moyenne dans la méthode
    """
    
    return liste.index(valeur) if valeur in liste else len(liste)




# =============================================================================
# Question 5 : la classe ABR
# =============================================================================

class ABR:
    """
    Un ABR est un Arbre Bianire de Recherche
    """
    
    def __init__(self, listeData):
        """
        Initialisattion de l'abr avec une liste de variables
        """
        
        
        #si il 
        if listeData == []:
            
            self.value = None
            
        else:
            
            self.isListEven = len(listeData) % 2 == 0
            
            #si liste pair on enleve le dernier element de la lise pour trouver la médiane
            self.value = np.median(listeData[:len(listeData) - 1]) if self.isListEven else np.median(listeData)
            
#            self.leftChild = ABR([[element for element in listeData if element < self.value] if not len(listeData) == 0 else None][0])
#            self.rightChild = ABR([[element for element in listeData if element > self.value] if not len(listeData) == 0 else None][0]) 
            
            self.leftChild = ABR([element for element in listeData if element < self.value])
            self.rightChild = ABR([element for element in listeData if element > self.value])    

        
   
    def afficherValeurs(self, niveau = 0): 
        """
        affiche dans la console toutes les valeurs de l'arbre dans un ordre trié
        """
        
        if not self is None:
            
            if not self.leftChild.value == None:
                self.leftChild.afficherValeurs(niveau + 1)
                
            print(self.value) 
            
            if not self.rightChild.value == None:
                self.rightChild.afficherValeurs(niveau + 1)

                     
        
    def diviserListeTo2ABR(self):
        """
        inutilisé
        """
        
        listLeft, listRight = [], []
        
        for element in self.listeData:
            
            if element < self.value:
                
                listLeft.append(element)
                
            elif element > self.value:
                
                listRight.append(element)
        
        return ABR(listLeft), ABR(listRight)


    
# =============================================================================
#     Question 6 :Insertion de valeurs numériques
# =============================================================================
    
    def add_node(self, abr):
        """
        Parcours tout l'arbre et ajoute une feuille avec la valeur
        """
        
        #si l'arbre est vide
        if self.value is None: 
            self = abr.value
        
        #sinon si l'arbre existe
        else:
            
            #si la valeur du noeud est sup
            if self.value < abr.value:
                
                #si le rightChild est nul
                if self.rightChild is None: 
                    self.rightChild = abr
                    
                #else récursivité
                else: 
                    self.rightChild.add_node(abr)
                    
            #si la valeur du noeud est inf
            elif self.value > abr.value: 
                
                #si le rightChild est nul
                if self.leftChild is None: 
                    self.leftChild = abr 
                    
                #else récursivité
                else: 
                    self.leftChild.add_node(abr) 



# =============================================================================
# Question 7 : Liste des valeurs de l'abr triées
# =============================================================================
                    

    def listeValeurs(self, niveau = 0, liste = []):       
        
        """
        Retourne la liste des valeurs triées en parcourant l'arbre en profondeur
        Chaque tuple de la liste contient :
            - element 1 : valeur
            - element 2 : position
        """
        
        if not self.leftChild.value == None:
            self.leftChild.listeValeurs(niveau + 1)
            
        liste.append((self.value, niveau))
        
        if not self.rightChild.value == None:
            self.rightChild.listeValeurs(niveau + 1)
        
        return(liste)
        
        
    def balance(self):
        
        """
        Prend la liste de valeurs triées et en fait un abr
        """
        
        return ABR([element[0] for element in self.listeValeurs()])
        
        
        
# =============================================================================
# Question 8 : Manipulation de listes d'étiquettes        
# =============================================================================
        
        
    def __eq__(self, other):
        """
        Retourne un booléen qui permet de savoir si deux valeurs de noeuds sont égales
        """
        return self.value == other.value
        
    def __lt__(self, other):
        """
        Retourne un booléen qui permet de savoir si deux valeurs de noeuds sont égales
        """
        return self.value < other.value




# =============================================================================
# Question 8 : Rotation de noeud
# =============================================================================

    def leftFlip(self): 
        """
        un left flip retourne un nouvel arbre avec un changement de noeud
        """
          
        if self.value is None: 
            return self.value  
          
        if self.leftChild is None and self.rightChild is None: 
            return self 
      
        flippedRoot = self.leftFlip() 
      
        self.leftChild.leftChild = self.rightChild 
        self.leftChild.rightChild = self 
        self.leftChild = None 
        self.rightChild = None
      
        return flippedRoot 
    

# =============================================================================
# Question 2 : Implémentation de valeurs numériques
# =============================================================================


t = Node(5) 
t.insert(Node(3)) 
t.insert(Node(2)) 
t.insert(Node(4)) 
t.insert(Node(7)) 
t.insert(Node(6)) 
t.insert(Node(8))



abr = Node(randint(0, 100)) 

#abr.insert(Node(2)) 
#abr.insert(Node(5)) 
#abr.insert(Node(5)) 
#abr.insert(Node(6)) 
#abr.insert(Node(7))
#abr.insert(Node(8))
#abr.insert(Node(9))


for index in range(50):
    abr.insert( Node(randint(0, 100)) )



#aide : https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/





# =============================================================================
# Affichage
# =============================================================================
print("======================================================================")

#recherche d'une valeur
print(t.existe(10))

#print de l'abr avec les valeurs aléatoires
print("=======")
#print(abr.printABR())



#moyenne de comparaiseon des listes
result = []
for a in range(50):
    result.append(existe([randint(0, 100) for index in range(50)], 10))
    
print(result)
print([element for element in result if element < len(result)])

print("nb iterations moyen avec la liste :", end = " ")
print(np.mean([element for element in result if element < len(result)]))




abrEq = ABR([randint(0, 100) for index in range(50)])

print(abrEq.value)

#abrEq.afficherValeurs()
print(abrEq.listeValeurs())

abrEq.add_node(ABR([5]))
help(ABR([]).add_node)








