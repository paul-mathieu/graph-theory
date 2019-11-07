"""
TP1 : Arbres Génériques
"""


"""
~~~~~~~~~~~~~~~~~~~~~~
 Classe 'Node'
~~~~~~~~~~~~~~~~~~~~~~
"""

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
    
    def tuple(self):
        return self, var_name(self), self.labels
    
    #renvoie V et E à partir d'un noeud défini comme une racine
    def makeItATree(self):
        return self.listV(), self.listE()
    
    #fonction qui renvoie tous les noeuds
    def listV(self):
        #liste sans doublons de tous les noeuds de .listE()
        return list(set([b for a in self.listE() for b in a]))
    
    #fonction qui renvoie tous les arcs
    def listE(self):
        
        #tuple entre le noeud et ses enfants
        tempListe = [(self, enfant) for enfant in self.children]
        
        #tuple entre les enfants et les enfants de ses enfants
        for enfant in self.children:
            for tupleEnfant in enfant.listE():
                tempListe.append(tupleEnfant)
        
        return tempListe
    
    #fonction qui renvoie tous les déscendants d'un noeud
    def descendants(self):
        
        #initialisation de la liste à vide
        listeEnfants = []
        
        #pour tous les enfants du noeud
        for enfant in self.children:
            
            #ajout des ses enfants
            listeEnfants.append(enfant)
            
            #ajouts des enfants de ses efants
            listeEnfants += enfant.descendants()
        
        return listeEnfants
    
    #fonction qui regarde tous les ancetres
    #on a besoin du tree pour connaitre la root de l'arbre (le plus lointain parent)
    def ascendants(self, tree):
        
        #initialisation de la liste à vide
        listeParents = []
        
        #pour tous les element de la liste E de l'arbre
        for parent in tree.root().listE():
            
            #si c'est le parent
            if parent[1] == self:
                
                #ajout du noeud
                listeParents.append(parent[0])
                
                #ajout de son parent
                listeParents += parent[0].ascendants(tree)
        
        #retour de la liste des parents
        return listeParents
    
    def is_leaf(self):
        return len(node4.children) == 0
        
    
    """
    Début de la partie de test
    """


    #fonction privee qui renvoie tous les déscendants et lui meme  
    def makeItATreePrivate(self):
        #si le noeud n'a pas d'enfants = si c'est une feuille
        if self.get_content()['Enfants'] == []:
            return (var_name(self), self.labels)
        
        #sinon retourne la liste des ses enfants
        return (var_name(self), self.labels), [a.makeItATreePrivate() for a in self.children]


    #fonction qui renvoie les feuilles de l'arbre
    def leafIfTree(self):
        
        #si le noeud n'a pas d'enfants = si c'est une feuille
        if self.get_content()['Enfants'] == []:
            return (var_name(self), self.labels)
        
        #sinon retourne la liste des ses enfants
        return [a.leafIfTree() for a in self.children]
    
    #fonction qui renvoie tous les noeuds nommés
    def listVn(self):
        
        #on prend l'arbre en carton
        tempTree = self.makeItATreePrivate()
        
        #on transforme l'arbre en carton pour ne récupérer que les éléments
        
        V = self.makeItATreePrivate()
        tempList=[]
        while sum(list(map(lambda x : not isTupleNode(x), V))) != 0:
            for sublist in V:
                if isTupleNode(sublist):
                    tempList.append(sublist)
                else:
                    for item in sublist:
                        tempList.append(item)
                        
            V, tempList = tempList, []
                
        return V

    
    """
    Fin de la partie de test
    """


    

        
    """    
    Q 1.1 - la liste des etiquettes d'un noeud binaire
                 (Primitive Content)
    """
    
    def content(self): #accesseur
        return dict((('Etiquette',self.labels), ('Enfants',self.children)))



"""
~~~~~~~~~~~~~~~~~~~~~~
 Classe 'RTree'
~
~~~~~~~~~~~~~~~~~
"""

class RTree:
    
    """
    A rooted tree is represented by
    A set of vertices
    A set of edges
    """
    
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges


    
    """
    Q 3.1 - la primitive « root »
    """
    
    #méthode prof
    def root(self):
        """
        Return the root of rooted tree
        root : Rtree → Node
        """
        # Extract all father nodes and remove double
        f = set([e[0] for e in self.edges])
        
        # Extract all children nodes and remove double
        c = set([e[1] for e in self.edges])
        
        # remove children nodes from father list: compute r = f - c 
        r = [e for e in f if e not in c]
        
        return r[0]
    
    #méthode moi
    def root2(self):        
        #liste des ascendents d'un noeud
        tempList = self.vertices[0].ascendants(self)       
        #dernier element de cette liste = plus root
        return tempList[len(tempList) - 1]

    """
    Q 3.2 - la primitive « sub_tree »
    """
    
    #fonction qui prend un noeud et qui le transforme en racine d'arbre
    def sub_tree(self, node):
        return node.listV(), node.listE()
    
    """
    Q 3.3 - la méthode « display_depth »
            (affichage des étiquettes de l’arborescence avec un parcours en profondeur)
    """
    
    def protoProfondeur(): #mettre parametre

        # do nothing if the rooted tree is empty
        if self.is_empty() :
            return aaa

        # transform the rooted tree in forest
        f = Forest([self])
        
        # call the coresponding method on the forest
        return f.protoProfondeur(...)
    
    
    """
    Q 3.4 - la méthode « display_width »
            (affichage des étiquettes de l’arborescence avec un parcours en largeur)
    """
    
    def protoLargeur(): #mettre parametre
        
        """
        ...
        """
        
        # do nothing if the rooted tree is empty
        
        if self.is_empty() :
            return impass
        else:
            # transform the rooted tree in forest
            f = Forest([self])
            # call the coresponding method on the forest
            return f.protoLargeur(...)
                
    
    #fonction qui retourne la profondeur d'un arbre
    def profondeur(self):
        return len(self.root().descendants())+1


"""
AUTRES FONCTIONS
"""

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








"""
~~~~~~~~~~~~~~~~~~~~~~
 Création de l'arbre
~~~~~~~~~~~~~~~~~~~~~~
"""


# Question 1 : implémentation de l'arborescence

node6 = Node("9")
node5 = Node("3")
node4 = Node("3")
node3 = Node("m")
node2 = Node("a")
node1 = Node("2", [node4, node5, node6])
node0 = Node("z", [node1, node2, node3])

V, E = node0.makeItATree()
tree = RTree(V, E)










