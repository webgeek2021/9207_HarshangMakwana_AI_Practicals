 while True:

        curr = open[0]

        for i in curr.data:
            for j in i:
                print(j , end = " ")
            print("")
        
        if getHscore(curr.data , goal_puzzle) == 0 :
            break

        for i in curr.generate_child_Node():
            i.f_score = getFscore(i , goal_puzzle)
            open.append(i)
        
        closed.append(curr)
        del open[0]

        open.sort(key= lambda x : x.f_score,reverse=False)