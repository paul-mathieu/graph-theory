class ...

    #prgm principal
    def prim(self):
        
        listArcs = triArc(self.getArcs())
        
        noeudDepart = self.getNoeuds()[0]
        
        arbre = arbre()
        
        arbre.getNoeud(noeudDepart)
        
        while not listArcs.isempty():
             
            arc, listeArc = prendreArc(arbre, listeArcs)
            
            arbre.ajouterArc(arc) if not creeCycle(arc, arbre)
        
        return arbre
    
    #fonction qui retourne un booléen qui informe si un cycle est créé
    def creeCycle(arc, arbre):
        return arbre.possede(arc.extremite1()) and arbre.possede(arc.extremite2())







