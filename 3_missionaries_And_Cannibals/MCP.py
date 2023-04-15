
import tkinter as tk

GOAL_STATE = (0,0,"right",3,3)
visited = []

class State():

    def __init__(self,cl,ml,boat,cr,mr) -> None:
        self.cl = cl
        self.ml = ml
        self.boat =boat
        self.mr = mr
        self.cr = cr
        self.parent = None

    def isSafe(self):
        if( self.ml >= 0 and self.mr >= 0 and self.cl >= 0 and self.cr >= 0 and (self.ml == 0 or self.ml >= self.cl) and (self.mr == 0 or self.mr >= self.cr) ):
            return True
        else :
            return False

    def isgoal(self):

        if self.cl == 0 and self.ml == 0 :
            return True
        else:
            return False


def find_successor(c_state):

    children = []

    if c_state.boat == "left":

        new_state = State(c_state.cl,c_state.ml-2,"right",c_state.cr,c_state.mr+2)
        if new_state.isSafe():
            new_state.parent = c_state
            children.append(new_state)
        
        # two cannibal to right
        new_state = State(c_state.cl-2,c_state.ml,"right",c_state.cr+2,c_state.mr)
        if new_state.isSafe():
            new_state.parent = c_state
            children.append(new_state)
        
        # 1 miss and 1 cann to right
        new_state = State(c_state.cl-1,c_state.ml-1,"right",c_state.cr+1,c_state.mr+1)
        if new_state.isSafe():
            new_state.parent = c_state
            children.append(new_state)

        # only 1 missionary to right
        new_state = State(c_state.cl,c_state.ml-1,"right",c_state.cr,c_state.mr+1)
        if new_state.isSafe():
            new_state.parent = c_state
            children.append(new_state)
        
        # only one cannibal
        new_state = State(c_state.cl-1,c_state.ml,"right",c_state.cr+1,c_state.mr)
        if new_state.isSafe():
            new_state.parent = c_state
            children.append(new_state)
    else :
        # two miss from right to left
        new_state = State(c_state.cl,c_state.ml+2,"left",c_state.cr,c_state.mr-2)
        if new_state.isSafe():
            new_state.parent = c_state
            children.append(new_state)
        
        # two cannibal to left
        new_state = State(c_state.cl+2,c_state.ml,"left",c_state.cr-2,c_state.mr)
        if new_state.isSafe():
            new_state.parent = c_state
            children.append(new_state)
        
        # 1 miss and 1 cann to left
        new_state = State(c_state.cl+1,c_state.ml+1,"left",c_state.cr-1,c_state.mr-1)
        if new_state.isSafe():
            new_state.parent = c_state
            children.append(new_state)

        # only 1 missionary to left
        new_state = State(c_state.cl,c_state.ml+1,"left",c_state.cr,c_state.mr-1)
        if new_state.isSafe():
            new_state.parent = c_state
            children.append(new_state)
        
        # only one cannibal
        new_state = State(c_state.cl+1,c_state.ml,"left",c_state.cr-1,c_state.mr)
        if new_state.isSafe():
            new_state.parent = c_state
            children.append(new_state)

    return children

def bfs():

    initial_state = State(3,3,"left",0,0)
    queue = list()
    queue.append(initial_state)

    while queue:
        state = queue.pop(0)
        if state.isgoal():
            return state
        visited.append(state)
        children = find_successor(state)
        for child in children:
            if( child not in visited )or(child not in queue):
                queue.append(child)
    return None
    
def printAns(sol):

    path = []
    path.append(sol)
    parent = sol.parent
    while parent:
        path.append(parent)
        parent  = parent.parent
    
    print("Order is (cl,ml,boat,cr,mr)")
    for t in range(len(path)):
        state = path[len(path)-t-1]
        print(f"({state.cl} , {state.ml} , {state.boat} , {state.cr} , {state.mr})")

# window = tk.Tk()
# window.geometry('300*300')
# canvas = tk.Canvas(window)
# def generateFrame(tup):
#     (cl,ml,boat,cr,mr) = tup

#     canl = canvas.create_rectangle(20,20 , 40,40,fill="red")
#     misl = canvas.create_rectangle(20,60 , 40,40,fill="green")


# def animateProblem(ans):

#     for a in ans : 
#         tup = a

#         generateFrame(tup)
#     pass
def main():
    ans = bfs()
    printAns(ans)
    # animateProblem(ans)

main()