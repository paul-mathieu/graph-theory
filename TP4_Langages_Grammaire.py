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

import ply.yacc as yacc
import TP4_Langages_Lexique

tokens = TP4_Langages_Lexique.tokens

# =============================================================================
# Parser
# =============================================================================

#for element in [a + b + c for a in ['contrainte', 'contrainte_liee'] for b in [' AND ', ' OR '] for c in ['contrainte', 'contrainte_liee']]: print(element)

#def p_assign(p):
#    '''assign : NAME EQUALS'''

def p_defaut(p):
    '''defaut : assign
    | get 
    | stat'''
    
    p[0] = p[1]
    
    print(p[0])
    
    
def p_assign(p):
    '''assign : NAME EQUALS get'''
    
    print('assign')
    
def p_get(p):
    '''get : GET URL 
    | GET URL contrainte_liee'''
    
    
    p[0] = file_to_list(p[2])
    
    print(len(p))
    
def p_stat(p):
    '''stat : STAT NAME UNION NAME contrainte_liee 
    | STAT NAME INTERSECT NAME contrainte_liee'''
    
    print('stat')
    
def p_contrainte_liee(p):
    '''contrainte_liee : contrainte AND contrainte_liee 
    | contrainte OR contrainte_liee 
    | contrainte_liee AND contrainte 
    | contrainte_liee OR contrainte 
    | contrainte'''
    
    print('contrainte_liee')
    
def p_contrainte(p):
    '''contrainte : CONTAINS NAME
    | EXCLUDE NAME'''
    
    print('contrainte')


#if there is an error
def p_error(p):
    
    print('Syntax error in input !')



def file_to_list(file):
    text_file = open(file, 'r')
    row = []
    
    index = 0
    
    row = [line for line in text_file.readlines()]
    row = [element[0] for element in row]
    
    for element in row:
        index_beg = element.index('>')
        index_end = len(element) - element[::-1].index('>')
        
        row[index] = row[index][index_beg:index_end]
        
        index += 1
    
    return row

#def p_assign(p):
#    '''assign : NAME EQUALS expr'''
    
#def p_expr(p):
#    '''expr : expr PLUS term
#    | expr MINUS term
#    | term'''
    
#def p_term(p):
#    '''term  : term TIMES factor
#    | term DIVIDE factor
#    | factor'''

#def p_factor(p):
#    '''factor : NUMBER'''


# =============================================================================
# Variables de test
# =============================================================================

#Programme Idule initial :
test0 = 'get http://www.machin-truc.org/page.html'
 
#Programme Idule initial avec contrainte :
test1 = 'get http://www.machin-truc.org/page.html contains toto'

#Programme Idule initial avec groupe de contraintes :
test2 = 'get http://www.machin-truc.org/page.html contains toto and exclude titi or contains blabla'
test3 = 'get http://www.bidule.org/page.html contains bli or contains blu and exclude blo'

#Programme Idule initial avec stats :
test4 = 'r1 = get http://www.machin-truc.org/page.html contains toto and exclude titi or contains blabla'
test5 = 'r2 = get http://www.bidule.org/page.html contains bli or contains blu and exclude blo'
test6 = 'stat r1 union r2 contains Trump and exclude Clinton contains Clinton and exclude Trump contains Trump and contains Clinton'
test7 = 'stat r1 intersect r2 contains Trump and contains Clinton'


# =============================================================================
# Tests
# =============================================================================

#Tests du parser

#def p_error(p):
#    pass

data = TP4_Langages_Lexique.data

file = 'idule_content.html'

print(data, end = "\n\n")

parser = yacc.yacc() # build the parser

yacc.parse(data)



#while True:
#    try:
#        s = raw_input('calc > ')
#    if not s:
#        continue
#    result = parser.parse(s)
#    print(result)











