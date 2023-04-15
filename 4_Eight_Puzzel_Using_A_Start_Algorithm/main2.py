
ROW = 3
COL = 3

class Node:

    def __init__(self , data , f_score,level) -> None:
        self.data = data
        self.f_score = f_score
        self.level = level

    def copyData(self,puz):
        temp = []

        for i in puz:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp
    
    def find(self , puz ,symbol ):

        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if(puz[i][j] == symbol):
                    return i,j

    def getCombination(self,puz,x1,y1 , x2,y2):

        if(x2 >= 0 and x2 < len(self.data) and  y2 >=0 and y2 < len(self.data)):
            temp_puz = []
            temp_puz = self.copyData(puz)
            temp = temp_puz[x2][y2]

            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
        
    def generate_child_Node(self):

        x,y = self.find(self.data , '_')

        direction = [[x,y-1], [x,y+1] , [x+1,y] , [x-1,y]]
        children = []
        for i in direction:
            child = self.getCombination(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child , 0,self.level+1)
                children.append(child_node)
        return children


def getMatrixInput():

    puz = []
    for i in range(0,ROW):
        temp = input().split(" ")
        puz.append(temp)
    return puz

def getHscore(start,goal):
    temp = 0
    for i in range(0,ROW):
        for j in range(0,COL):
            if start.data[i][j] != goal[i][j] and start.data[i][j] != '_':
                temp +=1
    
    return temp

def getFscore(start , goal):
    return getHscore(start , goal) + start.level 

def process():

    open = []
    closed = []
    print("Enter Start Puzzle")

    # start_puzzle = getMatrixInput()
    start_puzzle = [['1','2','3'],
                    ['_','4' ,'6'],
                    ['7','5','8']
                   ]

    print("Enter Goal Puzzle ")

    # goal_puzzle = getMatrixInput()
    goal_puzzle = [
                    ['1','2','3'],
                    ['4','5','6'],
                    ['7','8','_'] 
                  ]

    if len(start_puzzle) > ROW:
        print("Enter Matrix of Valid Size")
        return
    start_puzzle = Node(start_puzzle , 0 , 0)
    # print(start_puzzle)
    start_puzzle.f_score = getFscore(start_puzzle,goal_puzzle)

    open.append(start_puzzle)

    print("Puzzle Started ....")

    while True:

        # print(open)
        curr = open[0]

        for i in curr.data:
            for j in i:
                print(j , end = " ")
            print("")
        print("||")
        print("||")
        print(" V")
        if getHscore(curr , goal_puzzle) == 0 :
            break
        
        for i in curr.generate_child_Node():
            # print("CHILDREN")
            i.f_score = getFscore(i , goal_puzzle)
            open.append(i)
        closed.append(curr)
        del open[0]

        open.sort(key= lambda x : x.f_score,reverse=False)


process()


