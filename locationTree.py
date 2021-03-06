
#Implmentation of tree DS to find the route details
#for a given destination buses available and bus stops info is returned
#Written by Navi


class Node:
    def __init__(self, value):
        self._parent = None  # pointer to parent Node
        self._value= value  # keep reference to id #            
        self._children = [] # collection of pointers to child Nodes

    def getParent(self):
        return self._parent  # simply return the object at the _parent pointer
    
    def getChildren(self):
        return self._children
    
    def getValue(self):
        return self._value

    def setParent(self, node):
        self._parent = node
        # add this node to parent's list of children
        node._children.append(self)  
        
    def find(self, value):
        if self._value == value:
            return self
        for node in self._children:
            n = node.find(value)
            if n: return n
        return None  

def createPath(val,parent):
    node = Node(val)
    node.setParent(parent)
    return node

locationTree=[]
bus=["A 1","A 2","B 2","D 2"]
arr=[
    [("center of maritime studies" , "opposite house 12") , ("pgp" , "prince george's park")],
    [("alumni house","opposite nuss") , ("school of computing","com 2"),("deck","com 2"), ("faculty of arts and social science","ventus"),("computer center","computer centre"),("library","computer centre"),("techno edge","computer centre") , ("faculty of engineering","computer centre") , ("yusof ishak house","opposite yusof ishak house") , ("museum","museum") , ("university health centre","university health centre") , ("sports hall","university health centre") , ("university hall","university hall") , ("faculty of science","s17") , ("kent ridge mrt","kent ridge mrt") , ("prince george's park","pgp")],
    [("alumni house","opposite nuss") , ("deck","opposite nuss") , ("faculty of arts and social science","ventus") , ("computer center","computer centre") , ("library","computer centre") , ("techno edge","computer centre") , ("faculty of engineering","computer centre") , ("yusof ishak house","opposite yusof ishak house") , ("university town","u town") , ( "raffles hall","raffles hall") , ("kent ridge bus terminal","kent ridge bus terminal")],
    [("alumni house","opposite nuss") , ("school of computing","com 2") , ("deck","com 2"), ("faculty of arts and social science","ventus"),("computer center","computer centre"),("library","computer centre"),("techno edge","computer centre") , ("faculty of engineering","computer centre") , ("yusof ishak house","opposite yusof ishak house") , ("museum","museum") , ("university town","u town")]
]


for r in bus:
    root=Node(r)
    
    for area,stop in arr[bus.index(r)]:
        createPath(stop,createPath(area,root))
        
    locationTree.append(root)


def getRouteDetails(location):
    res=''
    bus=[]
    area=[]
    stop=[]
    for root in locationTree:
        #print("Inside fun1")   
        #print(root.getValue()+'->')  #bus
        #for val in root.getChildren():
            #print('\t'+val.getValue()+'->')  #area
            #for val1 in val.getChildren():
                #print('\t\t'+val1.getValue())  #stop
        
        a=root.find(location)
        if a is not None:
            if not a.getChildren():
                bus.append(root.getValue())
                area.append((a.getParent()).getValue())
                stop.append(a.getValue())
            elif a.getParent() is None:
                print(a.getValue() +' is a bus')
            else:
                for val in a.getChildren():
                    bus.append(root.getValue())
                    area.append(a.getValue())
                    stop.append(val.getValue())
        else:
            print("Route not found in "+root.getValue())
    buses=""
    n=len(bus)
    for i in range(n):
        if n == 1:
            res="Please use the bus "+bus[i]+" and get down at stop "+stop[0]+" to reach " + area[0]
        else:
            buses+=bus[i]+ (',' if i<n-2 else ('' if i==n-1 else' or ' ))
            res="Please use one of the buses "+buses+" and get down at stop "+stop[0]+" to reach " + area[0]
    return res
                

        