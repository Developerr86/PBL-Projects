#missonaries and cannibals GUI
#Ashish Tembhekar // Roll no.2 // NCER // FE-D // CSE-AI // 7666081264

import turtle as tl
import os

#setting up the window
wn = tl.Screen()
wn.title("Missonaries and Cannibals GUI")
wn.bgcolor('green')
wn.setup(width=1280,height=720)
wn.tracer(1)
rectCors = ((-10,20),(10,20),(10,-20),(-10,-20))
wn.register_shape('rectangle',rectCors)
miss=[]
can=[]

#drawing the layout
ghost=tl.Turtle()
ghost.color("black")
ghost.shape("square")
ghost.speed(5)
ghost.penup()
ghost.setposition(-630,350)
ghost.pendown()
ghost.pensize(10)
ghost.forward(630)
ghost.right(90)
ghost.forward(700)
ghost.right(90)
ghost.forward(630)
ghost.right(90)
ghost.forward(700)
ghost.penup()
ghost.setposition(-420,350)
ghost.right(180)
ghost.pendown()
ghost.forward(700)
ghost.penup()
ghost.setposition(-210,350)
ghost.pendown()
ghost.forward(700)
ghost.penup()
ghost.setposition(130,150)
ghost.write("Missonaries and Cannibals",move=False,font=('Arial',32,'bold'))
ghost.setposition(130,130)
ghost.write("by Ashish Tembhekar",move=False,font=('Arial',18,'bold'))
ghost.setposition(130,-135)
ghost.write("Click on missionaries/cannibals",move=False,font=('Arial',18,'normal'))
ghost.setposition(130,-155)
ghost.write("to get them on\off boat",move=False,font=('Arial',18,'normal'))
ghost.setposition(130,-185)
ghost.write("Click on the boat to move it across",move=False,font=('Arial',18,'normal'))
ghost.hideturtle()

#setting up another turtle to write game messages
ghost2=tl.Turtle()
ghost2.color("black")
ghost2.shape("square")
ghost2.speed(5)
ghost2.penup()
ghost2.pensize(10)
ghost2.hideturtle()

#boat turtle
boat=tl.Turtle()
boat.color("brown")
#boat.shape("square")
boat.speed(5)
boat.shapesize(3)
boat.shape('rectangle')
boat.turtlesize(stretch_wid=1.2,stretch_len=3)
boat.penup()
boat.setposition(-250,0)
boat.side="R"
boat.right(180)
#global mcount
#global ccount
#mcount=0
#ccount=0
direc=1

#making a function for each missionary turtle
#Very inefficient 
def m0onboard(x,y):
    boatspace=0
    for m in miss:
        if m.on_boat:
            boatspace+=1
        else:
            pass
    for c in can:
        if c.on_boat:
            boatspace+=1
        else:
            pass
    #print(boatspace)
    if boatspace <= 1:
        if not miss[0].on_boat:
            if boat.side==miss[0].bank:
                miss[0].sidey=miss[0].ycor()
                miss[0].setposition(boat.space[boatspace],0)
                ghost2.clear()
                miss[0].on_boat=not miss[0].on_boat
            else:
                pass
        else:
            if boat.side=="L":
                miss[0].setposition(-525,miss[0].sidey)
            elif boat.side=="R":
                miss[0].setposition(-105,miss[0].sidey)
            miss[0].on_boat=not miss[0].on_boat
    elif boatspace==2:
        if miss[0].on_boat:
            if boat.side=="L":
                miss[0].setposition(-525,miss[0].sidey)
            elif boat.side=="R":
                miss[0].setposition(-105,miss[0].sidey)
            miss[0].on_boat=not miss[0].on_boat
        else:
             #print("Boat is full")
             ghost2.clear()
             ghost2.setposition(130,90)
             ghost2.write("The boat is full!",move=False,font=('Arial',24,'bold'))
    else:
        pass
    #print(miss[0].on_boat)

def m1onboard(x,y):
    boatspace=0
    for m in miss:
        if m.on_boat:
            boatspace+=1
        else:
            pass
    for c in can:
        if c.on_boat:
            boatspace+=1
        else:
            pass
    #print(boatspace)
    if boatspace <= 1:
        if not miss[1].on_boat:
            if boat.side==miss[1].bank:
                miss[1].sidey=miss[1].ycor()
                miss[1].setposition(boat.space[boatspace],0)
                ghost2.clear()
                miss[1].on_boat=not miss[1].on_boat
            else:
                pass
        else:
            if boat.side=="L":
                miss[1].setposition(-525,miss[1].sidey)
            elif boat.side=="R":
                miss[1].setposition(-105,miss[1].sidey)
            miss[1].on_boat=not miss[1].on_boat
    elif boatspace==2:
        if miss[1].on_boat:
            if boat.side=="L":
                miss[1].setposition(-525,miss[1].sidey)
            elif boat.side=="R":
                miss[1].setposition(-105,miss[1].sidey)
            miss[1].on_boat=not miss[1].on_boat
        else:
             #print("Boat is full")
             ghost2.clear()
             ghost2.setposition(130,90)
             ghost2.write("The boat is full!",move=False,font=('Arial',24,'bold'))
    else:
        pass
    #print(miss[1].on_boat)

def m2onboard(x,y):
    boatspace=0
    for m in miss:
        if m.on_boat:
            boatspace+=1
        else:
            pass
    for c in can:
        if c.on_boat:
            boatspace+=1
        else:
            pass
    #print(boatspace)
    if boatspace <= 1:
        if not miss[2].on_boat:
            if boat.side==miss[2].bank:
                miss[2].sidey=miss[2].ycor()
                miss[2].setposition(boat.space[boatspace],0)
                ghost2.clear()
                miss[2].on_boat=not miss[2].on_boat
            else:
                pass
        else:
            if boat.side=="L":
                miss[2].setposition(-525,miss[2].sidey)
            elif boat.side=="R":
                miss[2].setposition(-105,miss[2].sidey)
            miss[2].on_boat=not miss[2].on_boat
    elif boatspace==2:
        if miss[2].on_boat:
            if boat.side=="L":
                miss[2].setposition(-525,miss[2].sidey)
            elif boat.side=="R":
                miss[2].setposition(-105,miss[2].sidey)
            miss[2].on_boat=not miss[2].on_boat
        else:
             #print("Boat is full")
             ghost2.clear()
             ghost2.setposition(130,90)
             ghost2.write("The boat is full!",move=False,font=('Arial',24,'bold'))
    else:
        pass
    #print(miss[2].on_boat)

#creating missionaries 
for m in range(3):
    miss.append(tl.Turtle())
for m in miss:
    m.color("white")
    m.shape("circle")
    m.penup()
    m.speed(5)
    m.shapesize(1.7)
    m.ndx=miss.index(m)
    m.ypos=-300+(m.ndx*100)
    m.setposition(-105,m.ypos)
    m.on_boat=False
    m.bank="R"

#making a function for each cannibal turtle
#Very inefficient 
def c1onboard(x,y):
    boatspace=0
    for m in miss:
        if m.on_boat:
            boatspace+=1
        else:
            pass
    for c in can:
        if c.on_boat:
            boatspace+=1
        else:
            pass
    #print(boatspace)
    if boatspace <= 1:
        if not can[1].on_boat:
            if boat.side==can[1].bank:
                can[1].sidey=can[1].ycor()
                can[1].setposition(boat.space[boatspace],0)
                ghost2.clear()
                can[1].on_boat=not can[1].on_boat
            else:
                pass
        else:
            if boat.side=="L":
                can[1].setposition(-525,can[1].sidey)
            elif boat.side=="R":
                can[1].setposition(-105,can[1].sidey)
            can[1].on_boat=not can[1].on_boat
    elif boatspace==2:
        if can[1].on_boat:
            if boat.side=="L":
                can[1].setposition(-525,can[1].sidey)
            elif boat.side=="R":
                can[1].setposition(-105,can[1].sidey)
            can[1].on_boat=not can[1].on_boat
        else:
             #print("Boat is full")
             ghost2.clear()
             ghost2.setposition(130,90)
             ghost2.write("The boat is full!",move=False,font=('Arial',24,'bold'))
    else:
        pass
    #print(can[1].on_boat)


def c0onboard(x,y):
    boatspace=0
    for m in miss:
        if m.on_boat:
            boatspace+=1
        else:
            pass
    for c in can:
        if c.on_boat:
            boatspace+=1
        else:
            pass
    #print(boatspace)
    if boatspace <= 1:
        if not can[0].on_boat:
            if boat.side==can[0].bank:
                can[0].sidey=can[0].ycor()
                can[0].setposition(boat.space[boatspace],0)
                ghost2.clear()
                can[0].on_boat=not can[0].on_boat
            else:
                pass
        else:
            if boat.side=="L":
                can[0].setposition(-525,can[0].sidey)
            elif boat.side=="R":
                can[0].setposition(-105,can[0].sidey)
            can[0].on_boat=not can[0].on_boat
    elif boatspace==2:
        if can[0].on_boat:
            if boat.side=="L":
                can[0].setposition(-525,can[0].sidey)
            elif boat.side=="R":
                can[0].setposition(-105,can[0].sidey)
            can[0].on_boat=not can[0].on_boat
        else:
             #print("Boat is full")
             ghost2.clear()
             ghost2.setposition(130,90)
             ghost2.write("The boat is full!",move=False,font=('Arial',24,'bold'))
    else:
        pass
    #print(can[0].on_boat)



def c2onboard(x,y):
    boatspace=0
    for m in miss:
        if m.on_boat:
            boatspace+=1
        else:
            pass
    for c in can:
        if c.on_boat:
            boatspace+=1
        else:
            pass
    #print(boatspace)
    if boatspace <= 1:
        if not can[2].on_boat:
            if boat.side==can[2].bank:
                can[2].sidey=can[2].ycor()
                can[2].setposition(boat.space[boatspace],0)
                ghost2.clear()
                can[2].on_boat=not can[2].on_boat
            else:
                pass
        else:
            if boat.side=="L":
                can[2].setposition(-525,can[2].sidey)
            elif boat.side=="R":
                can[2].setposition(-105,can[2].sidey)
            can[2].on_boat=not can[2].on_boat
    elif boatspace==2:
        if can[2].on_boat:
            if boat.side=="L":
                can[2].setposition(-525,can[2].sidey)
            elif boat.side=="R":
                can[2].setposition(-105,can[2].sidey)
            can[2].on_boat=not can[2].on_boat
        else:
             #print("Boat is full")
             ghost2.clear()
             ghost2.setposition(130,90)
             ghost2.write("The boat is full!",move=False,font=('Arial',24,'bold'))
    else:
        pass
    #print(can[2].on_boat)

#creating cannibals
for c in range(3):
    can.append(tl.Turtle())
for c in can:
    c.color("black")
    c.shape("circle")
    c.penup()
    c.speed(5)
    c.shapesize(1.8)
    c.ndx=can.index(c)
    c.ypos=300-(c.ndx*100)
    c.setposition(-105,c.ypos)
    c.on_boat=False
    c.bank="R"

#function for boat operations
def move_boat(x,y):
    boatspace=0
    for m in miss:
        if m.on_boat:
            boatspace+=1
        else:
            pass
    for c in can:
        if c.on_boat:
            boatspace+=1
        else:
            pass
    #print(boatspace)
    if boatspace != 0:
        if boat.side=="R":
            direc=1
            boat.side="L"
        else:
            direc=-1
            boat.side="R"
        boat.forward(direc*150)
        for m in miss:
            if m.on_boat:
                m.forward(-direc*150)
                if m.bank=="L":
                    m.bank="R"
                else:
                    m.bank="L"
            else:
                pass
        for c in can:
            if c.on_boat:
                c.forward(-direc*150)
                if c.bank=="L":
                    c.bank="R"
                else:
                    c.bank="L"
            else:
                pass
    else:
        
        #print("Boat cannot move on its own")
        ghost2.clear()
        ghost2.setposition(130,90)
        ghost2.write("The boat cannot move on its own!",move=False,font=('Arial',24,'bold'))
    #print(boat.side,c.bank,m.bank)

#Game variables
ML=0
CL=0
MR=0
CR=0
Gamewoncheck=False
def Gamewon():
    global Gamewoncheck
    Gamewoncheck = True

#main gameloop check function
def gamecheck(MR,ML,CR,CL):
    for m in miss:
        if m.bank=="L":
            ML=ML+1
        elif m.bank=="R":
            MR=MR+1
        else:
            pass
    for c in can:
        if c.bank=="L":
            CL=CL+1
        elif c.bank=="R":
            CR=CR+1
        else:
            pass
    if MR != 0 and MR<CR:
        #print("Game ends")
        return False
    elif ML!= 0 and ML<CL:
        #print("Game ends")
        return False
    elif ML==3 and CL==3:
        #print("Game Won")
        Gamewon()
        return False
    else:
        return True

#miss[0].onclick(m0onboard,btn=1)
#miss[1].onclick(m1onboard,btn=1)
#miss[2].onclick(m2onboard,btn=1)
#can[0].onclick(c0onboard,btn=1)
#can[1].onclick(c1onboard,btn=1)
#can[2].onclick(c2onboard,btn=1)

#main gameloop
while gamecheck(MR,ML,CR,CL):
#while True:
    boat.space=[boat.xcor()-30,boat.xcor()+30]
    boat.onclick(move_boat,btn=1)
    miss[0].onclick(m0onboard,btn=1)
    miss[1].onclick(m1onboard,btn=1)
    miss[2].onclick(m2onboard,btn=1)
    can[0].onclick(c0onboard,btn=1)
    can[1].onclick(c1onboard,btn=1)
    can[2].onclick(c2onboard,btn=1)

#tl.write("Game Over",move=False,align="left",font=('Arial',10,'normal'))

#display game result
if Gamewoncheck:
    ghost.setposition(130,50)
    ghost.write("Everyone got across safely!",move=False,font=('Arial',24,'bold'))
    ghost.setposition(130,80)
    ghost.write("Game Won!",move=False,font=('Arial',24,'bold'))
else :
    ghost.setposition(130,50)
    ghost.write("Cannibals have eaten the missonaries!",move=False,font=('Arial',24,'bold'))
    ghost.setposition(130,80)
    ghost.write("Game Lost!",move=False,font=('Arial',24,'bold'))
    for m in miss:
        m.hideturtle()


#print("Game Ended")

"""issues:very very inefficient
          theres a same function for every turtle rather than one function for all turtles (can use classes/methods to fix),
          too many variables than needed,
          on board turtles flicker (loop redraws turtles on screen),
          [fixed] game quits before missionary gets off boat,
          [fixed] slow performance,
          no turn counter,
          boat is always drawn on top of missionaries/cannibals
          some turtles get alloted the same position, end uo staying on top of each other,
          no reset/play again prompt 
"""