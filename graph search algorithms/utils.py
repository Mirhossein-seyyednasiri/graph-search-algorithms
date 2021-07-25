class Queue():


    def __init__(self):
        self.queueList = list()

    
    def IsEmpty(self):

        if len(self.queueList) == 0 : 
            return True
        else:
            return False
    
    def Push(self , value ):
        self.queueList.append(value)

    
    def Pop(self ) :
        if self.IsEmpty() :
            return "No data exits"
        else:

            output = self.queueList[0]
            self.queueList = self.queueList[1:]
            return output


class Stack():

    def __init__(self):
        self.stackList = list()

    def IsEmpty(self ) :
        if len(self.stackList) == 0 :
            return True
        else:
            return False
    
    def Push(self , value) :
        self.stackList.append(value)

    def Pop(self ) :
        if not self.IsEmpty() :
            output = self.stackList[-1]
            self.stackList = self.stackList[:-1]
            return output
        else:
            return "No data exits"

class Node():


    def __init__(self , nodeName , neighbors ) :

        self.nodeName = nodeName
        self.neighbors = neighbors
        self.visited = False
        self.InQueue = False
        self.previousNode = None
        self.InStack = False
    
    def SetVisited(self , value) :
        self.visited = value


    def SetInQueue(self , value) :
        self.InQueue = value

    def SetInStack(self , value) :
        self.InQueue = value

    def SetPreviousNode(self , value) :
        self.previousNode = value



class Graph():

    def __init__(self , nodeList) :

        self.nodeList = nodeList
    

    def FindNode(self , nodeName ) :

        for node in self.nodeList :
            if node.nodeName == nodeName :
                return node

        return None


    def BFSSearch(self , start , goal):
        self.ClearNodeData()
        startNode = self.FindNode(start)
        goalNode = self.FindNode(goal)

        if startNode == None or goalNode == None :
            return "no valid data"
        else:
            queue = Queue()
            queue.Push(startNode)
            startNode.SetInQueue(True)

            while not queue.IsEmpty() :
                currentNode = queue.Pop()
                currentNode.SetVisited(True)
                if currentNode == goalNode :
                    return self.FindPath(start , goal)

                for neighbor in list(currentNode.neighbors.keys()):
                    neighborNode = self.FindNode(neighbor)
                    if neighborNode.visited == False and neighborNode.InQueue == False:
                        queue.Push(neighborNode)
                        neighborNode.SetInQueue(True)
                        neighborNode.SetPreviousNode(currentNode)


    def FindPath(self , start , goal ): 
        startNode = self.FindNode(start)
        goalNode = self.FindNode(goal)  
        path = ""
        currentNode = goalNode 

        while currentNode != startNode :
            path += currentNode.nodeName
            currentNode = currentNode.previousNode

            if currentNode == None:
                return "No path exists"

        path += startNode.nodeName 
        path = path[::-1]     
        return path
    

    def ClearNodeData(self) :
        for node in self.nodeList :
            node.SetVisited(False)
            node.SetInQueue(False)
            node.SetInStack(False)
            node.SetPreviousNode(None)
    

    def DFSSearch(self , start , goal) :
        self.ClearNodeData()
        startNode = self.FindNode(start)
        goalNode = self.FindNode(goal)

        if startNode == None or goalNode == None :
            return "no valid input"
        stack = Stack()
        stack.Push(startNode)
        path = ""
        while not stack.IsEmpty() :
            currentNode = stack.Pop()
            if currentNode.visited == True :
                pass
            currentNode.SetVisited(True)
            path += currentNode.nodeName 
            if currentNode == goalNode :
                return path
            
            forwardFlag = 0 

            for neighbor in list(currentNode.neighbors.keys()) :
                neighborNode = self.FindNode(neighbor)
                if neighborNode.visited == False :
                    forwardFlag = 1
                    stack.Push(neighborNode)
            
            if forwardFlag == 0 :
                path = path[:-1]

                