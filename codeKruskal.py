class ...

    #prgm principal
    def kruskal(self):
        
        listArcs = triArc(self.getArcs())
                
        arbre = arbre()
        
        nbArcs = 0
        nbNoeudsT = len(self.getNoeuds())
        
        while nbArcs < nbNoeudsT - 1:
            
            #on prend le noeud le plus petit de la liste
            arc = pop(listeArcs)
            
            arbre.ajouterArc(arc) if not creeCycle(arc, arbre)
            
            nbArcs = len(listArcs)
            
        return arbre
    
    #fonction qui retourne un booléen qui informe si un cycle est créé
    def creeCycle(arc, arbre):
        return not arbre.existeChemin(arc.extremite1(), arc.extremite2())

















