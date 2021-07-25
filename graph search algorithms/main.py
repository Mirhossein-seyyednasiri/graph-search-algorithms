from utils import Graph , Node , Queue




node1 = Node("S" , {"A" : 0 , "B" : 1})
node2 = Node("A" , {"C" : 0 , "D" : 1})
node3 = Node("B" , {"D" : 0 , "C" : 1})
node4 = Node("C" , {"G" : 0 , "A" : 1})
node5 = Node("D" , {"A" : 0 , "G" : 1})
node6 = Node("G" , {"A" : 0 , "S" : 1})



graph = Graph([node1 , node2 , node3 , node4 , node5 , node6])



print(graph.DFSSearch("S" , "G"))