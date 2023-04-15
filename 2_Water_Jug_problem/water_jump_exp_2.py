

# I have three jug whose capacity are 8 lt.,5 lt. and 3 lt. and no one jug is calibrated then how
# can I divide 8 lt. water in two equal parts.
import tkinter as tk
import time
a_capacity = 8
b_capacity = 5
c_capacity = 3

goal_state = (4,4,0)
visited = []

WIDTH_RECT = 40
def getPath(state , ans_vector):
  # print(state , ans_vector)
  (a , b ,c) = state[0],state[1],state[2]
  if state == goal_state:
    print("YEs")
    # ans_vector.append(state)
    return True
  if state in visited or a > a_capacity or b > b_capacity or c > c_capacity:
    return False
  else:
    visited.append((state))

    if a > 0:
      if a+b <= b_capacity:
        if getPath((0,a+b,c) , ans_vector):
          ans_vector.append((a,a+b,c))
          return True  # we got the path 
      else:
        tup = (a-(b_capacity - b) , b_capacity , c) 
        if(getPath(tup, ans_vector)):
          ans_vector.append(tup)
          return True

      # pour water into 3rd jug
      if a + c <= c_capacity:
        if getPath((0,b,a+c) , ans_vector):
          ans_vector.append((0,b,a+c))
          return True
        else:
          tup = (a-(c_capacity - c) , b , c_capacity)
          if getPath(tup , ans_vector):
            ans_vector.append(tup)
            return True

    # when b jug is grater then zero
    if b > 0:
      if b + a <= a_capacity:
        if getPath((a+b,0,c) , ans_vector):
          ans_vector.append((a+b,0,c))
          return True
      else:
          tup = (a_capacity , (b - (a_capacity - a)) , c)
          if getPath(tup , ans_vector):
            ans_vector.append(tup)
            return True
      
      if b + c <= c_capacity:
        if getPath((a , 0 , b+c) , ans_vector):
          ans_vector.append((a,0,b+c))
          return True
      else:
        tup = (a , (b - (c_capacity - c)) , c_capacity)
        if getPath(tup , ans_vector):
          ans_vector.append(tup)
          return True
    # when c jug is filled with Water
    if c > 0:
      if c+a <= a_capacity:
        if getPath((a+c , b , 0) , ans_vector):
          ans_vector.append(((a+c),b,0))
          return True
      else:
        tup = (a_capacity , b , c - (a_capacity - a))
        if getPath(tup , ans_vector):
          ans_vector.append(tup)
          return True
      
      if c + b <= b_capacity:
        if getPath((a,b+c,0) , ans_vector):
          ans_vector.append((a,b+c,0))
          return True
      else:
        tup = (a,b_capacity , c - (b_capacity - b))
        if getPath(tup , ans_vector):
          ans_vector.append(tup)
          return True
        


def waterJugProblem(a,b,c):
  a_ans = []
  getPath((8,0,0) ,a_ans )
  a_ans.append((8,0,0))
  a_ans.append((a,b,c))
  a_ans.reverse()
  return a_ans
  # visited.clear()
  # getPath((0,5,0) ,b_ans )
  # b_ans.append((0,5,0))
  # b_ans.append((a,b,c))
  # b_ans.reverse()
  # visited.clear()
  # getPath((0,0,3) ,c_ans )
  # c_ans.append((0,0,3))
  # c_ans.append((a,b,c))
  # c_ans.reverse()
  # visited.clear()

window = tk.Tk()
window.geometry('300x300')
canvas = tk.Canvas(window )
def generate_frame(one,two,three):
  
  text = canvas.create_text(250,50 , text=f"({one},{two},{three})",font="Calibri 24")
  time.sleep(5)

  rect1 = canvas.create_rectangle(20, 220 - one*10 , 20+WIDTH_RECT , 220 , outline="blue",fill="blue")
  window.update()
  time.sleep(1)

  rect2 = canvas.create_rectangle(80, 220 - two*10 , 80+WIDTH_RECT , 220 ,outline="blue", fill="blue")
  window.update()
  time.sleep(2)

  rect3 = canvas.create_rectangle(140, 220 - three*10 , 140+WIDTH_RECT , 220 , outline="blue",fill="blue")
  window.update()
  time.sleep(3)

  canvas.delete(text)
  canvas.delete(rect1)
  canvas.delete(rect2)
  canvas.delete(rect3)
  window.update()

def create_app():
  canvas.pack()
  canvas.create_rectangle(20,  140, 20+WIDTH_RECT , 220  ,outline="red" )
  canvas.create_rectangle(80,  170, 80+WIDTH_RECT , 220  ,outline="green" )
  canvas.create_rectangle(140,  190, 140+WIDTH_RECT , 220  ,outline="black" )

    # time.sleep(1)

create_app()
ans = waterJugProblem(0,0,0)

for i in ans:
  one = i[0]
  two = i[1]
  three = i[2]
  generate_frame(one,two,three)
# window.update()

print("Ans is")
for i in ans:
  print(f"{i[0]},{i[1]},{i[2]}")

window.mainloop()
