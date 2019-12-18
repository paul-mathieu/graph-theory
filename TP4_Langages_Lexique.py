# -*- coding: utf-8 -*-
'''
Created on Wed Dec 18 07:27:12 2019

@author: Paul MATHIEU
'''


'''
Acces aux donnees

    Les données peuvent être accédées au travers de ressources. Une ressource 
    est représentée :
        • soit par une URI sous forme de chaîne de caractères,
        • soit par une ressource interne définie par un nom (qui peut être vu 
        comme un nom de variable).
        
    La récupération d'un sous ensemble de données s'effectue par le mot clé 
    « get ». Ce dernier doit prendre en paramètre :
        • une liste de ressources
        • une contrainte spécifiant le contenu recherché dans les ressources
        
    Une contrainte est une expression booléenne utilisant les mots clés 
    « contains » et « excludes » suivis d'une chaîne de caractères permettant 
    de rechercher respectivement les données contenant et ne contenant pas la 
    chaîne de caractères. Une contrainte pourra être composée de plusieurs
    contraintes liées par les mots clés « and » ou « or ».
    
    Dans tous les cas, le résultat d'un « get » fournit une ressource interne 
    qui doit absolument être nommée.

Manipulation de données

    La manipulation des données consiste en un calcul statistique sur les 
    ressources internes. Le mot clé permettant de faire ce calcul est « stat ». 
    Cette opération prend en paramètre :
        • un ensemble de ressources internes qui sont liées par les mot clés 
        « union », « intersect » et « diff ».
        • un ensemble de groupes de contraintes
        
    Le résultat de cette opération est un dictionnaire d'une analyse 
    statistique qui contiendra au minimum :
        • le nombre d'éléments de l'ensemble des ressources internes en tenant 
        compte des liens définis,
        • pour chaque contrainte, le rapport entre le nombre d'éléments 
        validant la contrainte par le nombre total d'éléments.

'''

import ply.lex as lex

# =============================================================================
# Lexer
# =============================================================================

tokens = ['GET', 
          'CONTAINS', 'EXCLUDES', 'AND', 'OR', 'STAT', 'UNION', 'INTERSECT', 'DIFF', 
          'NAME', 'VARIABLE', 
          'URL']

t_ignore = ' \t'

t_GET = r'get'
t_CONTAINS = r'contains'
t_EXCLUDES = r'excludes'
t_AND = r'and'
t_OR = r'or'
t_STAT = r'stat'
t_UNION = r'union'
t_INTERSECT = r'intersect'
t_DIFF = r'diff'

t_NAME = r'[\w\-\.~:\\\/?#\[\]!\$&\+,=.]+'
t_VARIABLE = r'[\w\-\.~:\\\/?#\[\]!\$&\+,=.]+'

t_URL = r'(?:http(s)?:\/\/)?[\w-]+(\.[\w-]+)+(\/[\w\-\.~:\/?#\[\]!\$&\+,=.]+)?'

def t_error(t):
    t.type = t.value[0]
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

lex.lex() #Build the lexer




















