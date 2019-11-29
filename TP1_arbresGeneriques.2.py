"""
TP1 : Arbres Génériques
"""


#==============================================================================        
#==============================================================================        
#   Classe 'Node'
#==============================================================================        
#==============================================================================        

class Node :
    
    """
    Node class that represent nodes in rooted tree
    A node is composed of:
    ● A label or list of labels of any type
    ● A list of nodes, its children
    """
    
    def __init__(self, labels, children=[]):
        
        #étiquette du noeud
        self.labels = labels
        
        #enfants du noeud
        self.children = children
        
        #enfants du noeud sous forme de liste avec le nom des variables
        self.lChildren = [var_name(a) for a in children]

        #enfants du noeud sous forme de dictionnaire
        #avec le nom et l'étiquette de chaque enfant
        # => {'node4': '3', 'node5': '3', 'node6': '9'}
        self.dChildren = dict([(var_name(a), a.labels) for a in children])



#==============================================================================        
#    Q 2.1 - la liste des etiquettes d'un noeud binaire
#                 (Primitive Content)
#==============================================================================        

   
    def content(self): 
        
        """
        
        Cette fonction retourne le contenu d'un noeud avec 
        les informations suivantes :
            - l'étiquette
            - les enfants (sous forme de liste)
            
        """
        
        return {'Etiquette' : self.labels, 'Enfants' : self.children}




#==============================================================================        
#    Q 4.1 - children
#==============================================================================        

    def children(self):
        """
        getter des children d'un noeud
        """
        return self.children
    
    

  
#==============================================================================        
#    Q 4.3 - descending
#==============================================================================        
    
    
    def descending(self):
        
        """
        fonction qui renvoie tous les descendants d'un noeud
        """
        
        #initialisation de la liste à vide
        listeEnfants = []
        
        #pour tous les enfants du noeud
        for enfant in self.children:
            
            #ajout des ses enfants
            listeEnfants.append(enfant)
            
            #ajouts des enfants de ses efants
            listeEnfants += enfant.descending()
        
        return listeEnfants
 
    

    
#==============================================================================        
#    Q 4.5 - is_leaf
#==============================================================================        

    
    def is_leaf(self):
        
        """
        Retourne un booléen qui vérifie si le noeud est une feuille
        """
        
        return len(self.children) == 0
    
    
    
    
#==============================================================================        
#    Q 4.6 - degree
#==============================================================================        
    
    def degreeN(self):
        """
        le degré d'un noeud est son nombre de fils
        """
        return len(self.children)
    
        
    


    











#==============================================================================        
#==============================================================================        
#   Classe 'RTree'
#==============================================================================        
#==============================================================================        




class RTree(Node):
    
    """
    A rooted tree is represented by its root node
    """
    
    def __init__(self, labels, children = []):
        
        super().__init__(labels, children)




#==============================================================================        
#    Q 3.1 - la primitive « root »
#==============================================================================        

    #méthode prof
    def root(self):
        return self
        
        

#==============================================================================        
#    Q 3.2 - la primitive « sub_tree »
#==============================================================================        


    def sub_tree(self):
        """
        all the sub tree are defined by the children of the root of the tree
        """
        return self.children



    
#==============================================================================        
#    Q 3.3 - la méthode « display_depth »
#            (affichage des étiquettes de l’arborescence avec un parcours 
#            en profondeur)
#==============================================================================        
    
    
    def display_depth(self):
        
        """
        parcours de l'arbre en profondeur
        """
        
#        listeLabels.append(self.labels)
        
#        print(str(listeLabels))
        
        listeLabels = [self.labels]
        
        for child in self.children:
                        
            if not child.is_leaf():
                
                listeLabels += child.display_depth()
            
            else:
                
                listeLabels.append(child.labels)
                
        
        return listeLabels


        

            
    def display_depthOL(self):
          
        return [self.labels] + [child.display_depthOL2() if not child.is_leaf() else child.labels for child in self.children]
        


#==============================================================================        
#    Q 3.4 - la méthode « display_width »
#            (affichage des étiquettes de l’arborescence avec un parcours en largeur)
#==============================================================================        
    

    #fonctionne
    def display_width(self, listeLabels = []):
        
        """"
        parcours de l'arbre en largeur
        """"

        for child in self.children: 
            
            listeLabels.append(child.labels) 
            
        for child in self.children:   
            
            child.display_width(listeLabels)
            
        return [self.labels] + listeLabels  



    #python est étrange 
    def display_width2(self, listeLabels = []):
        """
        
        """
        listeLabels += [child.labels for child in self.children]
#        print(str(listeLabels))
        
        for child in self.children:
                
            listeLabels.append(child.display_width2(listeLabels))
       
#        listeLabels = [self.labels] + listeLabels
        
        return listeLabels

#print (a)
#a=node0.display_width2([])
#print (a[7])
#print (a[10])
#print (len(a))
#print (a[13])
#print (len(a[13][13][13]))

#Vous aviez dit qu'il s'agit d'une liste récursive



#==============================================================================        
#    Q 4.2 - father
#==============================================================================        

    def father(self, node):
        
        """
        Le père d'un noeud est le noeud l'ayant pour enfant
        """
        
        #pour tous les noeuds de l'arbre self
        for parent in self.root().descending():
            
            #pour tous les enfants du noeud
            for child in parent.children:
                
                #si l'enfant est égal au neaud cherché
                if child == node:
                    
                    return parent
        
        return None


#==============================================================================        
#    Q 4.4 - ascending
#==============================================================================        
     
        
    def ascending(self, tree):

        """
        fonction qui regarde tous les ancetres
        on a besoin du tree pour connaitre la root de l'arbre (le plus lointain parent)
        """    
        
        #initialisation de la liste à vide
        listeParents = [tree]
        
        #pour tous les element de la liste E de l'arbre
        for parent in tree.root().descending():
            
            #si c'est le parent
            for child in parent.children:
                
                if child == self:
                    
                    #ajout du noeud
                    listeParents.append(parent)
                    
                    #ajout de son parent
#                    listeParents += parent[0].ascending(tree)
        
        #retour de la liste des parents
        return listeParents
    
    

#==============================================================================        
#    Q 4.6 - degree
#==============================================================================        
    
    def degreeT(self, maximum = 0):
        
        """
        le degré d'un arbre est son nombre maximal de fils
        """
                
        if not len(self.children) == 0:
            
            for child in self.children:
            
                maximum = child.degreeT(maximum)
        
        #si le noeud principal est supérieur au maximum calculé
        if len(self.children) > maximum:
            
            maximum = len(self.children) 
        
        
        return maximum
    
    
    
#==============================================================================        
#    Q 4.6 - depth
#==============================================================================        
    
    def depth(self, taille = 0):
        
        """
        la pronfondeur d'un noeud est nombre maximal de déscendants de la racine
        """
        
        for child in self.children:
            
            taille += 1
            
            child.depth(taille)
            
        return taille
    
    
    
    
#==============================================================================        
#    Q 4.6 - width
#==============================================================================        
    
    def width(self, tree, taille = 0):
        
        """
        la largeur d'un arbre est son nombre maximal de fils sur un même niveau
        """
        
        #pour tous les noeuds
        for noeud in self.sub_tree():
            
            #si la taille est inf à la taille du nombre de fils d'un noeud
            if len(noeud.children) > taille:
                
                taille = len(noeud.children)
            
            #récursivité
            noeud.width(tree, taille)
            
        return taille    
    
    
    
    
    
    
    
    
   
    
#==============================================================================        

#   AUTRES FONCTIONS

#==============================================================================        


#fonction qui renvoie le nom d'une variable
def var_name(var):
    for name, value in globals().items():
        if value is var:
            return name
    return 'inconnu'




#fonction qui vérifie si un element à la forme ('node0', 'z')
def isTupleNode(vTuple):
    return type(vTuple) is tuple and len(vTuple) == 2 and type(vTuple[0]) is str
#isTupleNode = lambda vTuple : type(vTuple) is tuple and len(vTuple) == 2 and type(vTuple[0]) is str







#~~~~~~~~~~~~~~~~~~~~~~
# Création de l'arbre
#~~~~~~~~~~~~~~~~~~~~~~




# Question 1 : implémentation de l'arborescence

#node6 = Node("9")
#node5 = Node("3")
#node4 = Node("3")
#node3 = Node("m")
#node2 = Node("a")
#node1 = Node("2", [node4, node5, node6])
#node0 = Node("z", [node1, node2, node3])



node7 = RTree("v")
node6 = RTree("9")
node5 = RTree("3")
node4 = RTree("3")
node3 = RTree("m")
node2 = RTree("a")
node1 = RTree("2", [node4, node5, node6, node7])
node0 = RTree("z", [node1, node2, node3])


















