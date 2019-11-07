"""
TP1 : Arbres Génériques
"""

def test(variable):
    return globals()[variable]

a = 1


dictio = {'a':1,'b':2}

def var_name(var):
    for name, value in globals().items():
        if value is var:
            return name
    return 'inconnu'

x = [["a","b"], ["c"]]
y = (('node0', 'z'), [(('node1', '2'), [('node4', '3'), ('node5', '3'), ('node6', '9')]), ('node2', 'a'), ('node3', 'm')])

#result = []
#[ result.extend(el) for el in x] 

#for el in result:
#    print(el)
    
#
#flat_list=[]
#while sum(list(map(lambda x : not isTupleNode(x), y))) != 0:
#    for sublist in y:
#        #print(sublist)
#        if isTupleNode(sublist):
#            flat_list.append(sublist)
#        else:
#            for item in sublist:
#                flat_list.append(item)
#                
#    y, flat_list = flat_list, []
#    print(y)
#        
#print(y)

liste1 = [(1,2),(1,2),(1,2)]

liste2 = []

for b in a:
    
for a in liste1:
    
    
    
    
    