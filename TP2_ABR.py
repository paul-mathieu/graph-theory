"""
TP2 : ABR
"""

#lien :
# http://ead-polytech.univ-savoie.fr/pluginfile.php/40002/mod_resource/content/2/Ennonce.pdf

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~ Recherche dans un ABR :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#noeud = (x, FilsGauche, FilsDroit)
recherche(noeud, valeur)
        
    #si la valeur cherchée n'existe pas    
    Si noeud est vide
        retourner 'erreur'
    
    #si le noeud contient la valeur
    Si noeud.valeur
        retourner Vrai
    
    #si le noeud a une valeur inférieure
    Sinon si valeur < noeud.valeur
        retourner Recherche(noeud.FilsGauche, valeur)
    
    #si le noeud a une valeur supérieure
    Sinon
        retourner Recherche(noeud.FilsDroit, valeur)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~ Insertion dans un ABR :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#noeud = (x, FilsGauche, FilsDroit)
insertion(noeud, valeur)
    Si noeud est vide
        retourner valeur
    Sinon Si valeur < noeud.valeur
        retourner (noeud.valeur, insertion(noeud.FilsGauche, valeur), noeud.FilsDroit)
    Sinon
        retourner (noeud.valeur, noeud.FilsGauche, insertion(noeud.FilsDroit, valeur))





    
"""

# =============================================================================
#  Classe 'Node'
# =============================================================================


class Node:

    def __init__(self, data):
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
    
    
    def search(self, data): 
          
        # Base Cases: root is null or key is present at root 
        if self is None or self.data == data: 
            return self 
      
        # Key is greater than root's key 
        if self.data < data: 
            return self.rightChild.search(data) 
        
        # Key is smaller than root's key 
        return self.leftChild.search(data) 

    def insert(self, node):
        #if tree is empty
        if self is None: 
            self = node
        
        #if tree exists
        else:
            
            #if the node's value is superior
            if self.data < node.data:
                #if rightChild is nothing
                if self.rightChild is None: 
                    self.rightChild = node
                #else récursivité
                else: 
                    self.rightChild.insert(node)
                    
            #if the node's value is inferior
            else: 
                #if rightChild is nothing
                if self.leftChild is None: 
                    self.leftChild = node 
                #else récursivité
                else: 
                    self.leftChild.insert(node) 


    def printABR(self): 
        if not self is None: 
            self.leftChild.printABR()
            print(self.data) 
            self.rightChild.printABR()

    
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
        


#CODE D'INSERTION


r = Node(50) 
r.insert(Node(30)) 
r.insert(Node(20)) 
r.insert(Node(40)) 
r.insert(Node(70)) 
r.insert(Node(60)) 
r.insert(Node(80))







#aide : https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/