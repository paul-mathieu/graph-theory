class ...

    #prgm principal
    def djikstra(self, depart, arrive):
        
        nav = self.V
        dist = [math.inf]*len(nav)
        
        #la fonction init change les valeurs de nav et dist
        nav, dist, current = init(nav, dist, depart)
        
        
        #algo du chemin
        while not estArrive(nav):
            
            current, nav = majDistance(current, dist)
            dist = nouveauCurrent(...)
    
    
    #la fonction d'initialisation de dist et de nav
    def init(nav, dist, depart):
        
        a = 0
        
        #on cherche la valeur de départ
        while nav[a] != dep:
            a += 1
        
        #on remplace les valeurs
        nav[a] = ''
        dist[a] = 0
        
        return nav, dist
    
    
    #fonction qui regarde s'il ne reste qu'un élément dans la liste
    def estArrive(nav):
        
        #compte le nombre de '' et regarde si c'est égal à len(nav)+1
        return len([a for a in nav if nav[a] == '']) == len(nav)+1
    
    #fonction qui renvoie la nouvelle liste des distances avec le noeud count
    def majDistance(self, noeudCurrent, listDistance):
        
        for voisin in self.voisins(noeudCurrent):
            
            poids = self.poidsArc(noeudCurrent, voisin)
            distNoeudCurrent = listDistance[noeudCurrent]
            distConnueVersVoisin = listDistance[voisin]
            listDistance[voisin] = distNoeudCurrent + poids if distConnueVersVoisin > distNoeudCurrent + poids:
        
        return listDistance


