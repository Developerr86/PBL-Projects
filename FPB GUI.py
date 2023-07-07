#FPB with GUI
#Ashish Tembhekar // Roll no.2 // NCER // FE-D // CSE-AI // 7666081264

from tkinter import *
from tkinter import Tk
from random import sample
import os

#Main UI // not resizeable
Game=Tk()
Game.title("Fermi-Pico-Bagels")
Game.geometry("800x600") 
Game.resizable(False,False)
digit_x_pos={"3":["290","370","450"],"4":["240","320","400","480"],"5":["190","270","350","430","510"]} #x-coordinate postions for input enrties, depending on the number of digits
digitlist=[] #will include all digit input entry widgets
no_of_digits="3" #default
digitss=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]

#My labels
Label(Game,font='Helvetica 18 bold',text="Fermi-Pico-Bagel (GUI)",justify="left").place(x="10",y="10")
Label(Game,font='Helvetica 14 ',text="by Ashish Tembhekar",justify="left").place(x="10",y="35")

#this function makes entry columns based on the number of digits of FPB number
def digitget():
    no_of_digits=digitoption.get()
    for xc in range(len(digitlist)):
        digitlist[0].destroy()
        digitlist.remove(digitlist[0])
    #print(digitlist)
    for i in range(int(no_of_digits)):
        #print(i)
        digitss[i].set("")
        digitlist.append(Entry(Game,textvariable=digitss[i],highlightcolor='green',font=("Arial",42),justify="center"))
        digitlist[i].place(x=digit_x_pos[no_of_digits][i],y="170",width="60",height="100")
    resetFPB()

#Spinbox widget to change the number of digits , also resets the FPB number
digitoption=Spinbox(Game,from_=3,to=5,font="Helvetica 14",command=digitget)
Label(Game,font='Helvetica 14',text="Digits").place(x="220",y="512")
digitoption.place(x="260",y="510",width=50)

#making the first 3 entry columns as the defualt number of digits is 3
for i in range(int(digitoption.get())):
    #print(i)
    digitlist.append(Entry(Game,textvariable=digitss[i],highlightcolor='green',font=("Arial",42),justify="center"))
    digitlist[i].place(x=digit_x_pos[no_of_digits][i],y="170",width="60",height="100")

#this function informs user if allow zero is toggled
def letuserknow():
    if Zeros.get()==1:
        status.config(text="Next reset will allow 0")
    else:
        status.config(text="Next reset wont allow 0")

#allow zero check box
Zeros=IntVar()
AllowZero=Checkbutton(Game,font='Helvetica 15',text="Allow Zero",onvalue=1,offvalue=0,variable=Zeros,command=letuserknow)
AllowZero.place(x="220",y="470")

#this function randomly generates a number for FPB with unique digits , and includes zero if toggeled on
def SampleFPB():
    #print("digits:",digitoption.get())
    if Zeros.get()==1:
        return sample("1234567890",int(digitoption.get()))
    else:
        return sample("123456789",int(digitoption.get()))
FPB=SampleFPB()

#this label dynamically changes to reflect the user's actions 
status=Label(Game,font='Helvetica 36 bold',text="Start",justify="center")
status.place(x="195",y="100")

#count users turns
Count=12
counter=Label(Game,font='Helvetica 20 bold',text="Chances left:"+str(Count),justify="center")
counter.place(x="220",y="380")
Game.count=Count

#this function turns the FPB number into a string,so it is iterable, makes for easier comparision with user input
def makefpbtext(FPB):
    ft=""
    for i in FPB:
        ft+=i
    return ft

#this label will hide FPB value until game is over
ran=Label(Game,font='Helvetica 24 bold',text="FPB: ???",justify="center")
ran.place(x="220",y="410")

#this list will store every attempted value by the user
Game.Attempts=[]
attemplist=Listbox(Game,font='Helvetica 14',width=20,justify="center")
attemplist.place(x="400",y="360")
guess=""

#the most important function, this checks the user input against the generated fpb
def checkFPB():
    fpbtext=makefpbtext(FPB)
    try:
        if (attemplist.get(0,len(Game.Attempts))[len(Game.Attempts)-1])==fpbtext:
            status.config(text="Bro you've already won")
            return None
    except:
        pass
    cond=False
    if Game.count<=0:
        status.config(text="Too bad!")
        ran.config(text="FPB: "+fpbtext)
        cond=True
    for d in range(int(digitoption.get())):
        try:
            if len(digitss[d].get()) >1:
                temp=int(digitss[d].get())
                temp=str(temp)
                digitss[d].set(temp[0])
        except:
            status.config(text="Enter numbers bro")
            return None
    guess=""
    #print(digitoption.get())
    for n in range(int(digitoption.get())):
        guess=guess+digitss[n].get()
    #print(guess)
    try:
        if guess not in Game.Attempts:
            Game.Attempts.append(guess)
            attemplist.insert(Game.Attempts.index(guess)+1,guess)
        else:
            status.config(text="Um.. you tried that before")
            for d in digitss:
                d.set("")
            return None
    except:
        return None
    output=[]
    if guess==fpbtext:
        StatusText="Fermi! "*int(digitoption.get())
        status.config(text=StatusText)
        ran.config(text="FPB: "+fpbtext)
        cond=True
        return None
    elif len(set(guess))<int(digitoption.get()):
        status.config(text="Not enough unique digits")
        cond=True
        attemplist.delete(Game.Attempts.index(guess))
        Game.Attempts.remove(guess)
    else:
        #print(guess,fpbtext)
        for i in range(len(fpbtext)):
            if guess[i]==fpbtext[i]:
                output.append("Fermi ")
            elif guess[i] in fpbtext:
                output.append("Pico ")
    #print(output)
    if cond:
        pass
    else:
        if len(output)==0:
            StatusText="Bagel"
            status.config(text=StatusText)
        else:
            StatusText=""
            for s in output:
                StatusText+=s
            #print(StatusText)
            status.config(text=StatusText)
        Game.count=Game.count-1
        counter.config(text="Chances:"+str(Game.count))
    for d in digitss:
        d.set("")

#check button
check=Button(Game,text="Check",font="Arial 25",height=1,width=10,justify="center",command=checkFPB).place(x="312",y="290")

#this function will reset the game
def resetFPB():
    Attemps=[]
    attemplist.delete(0,len(Game.Attempts))
    Game.Attempts=Attemps
    Count=3+(3*(int(digitoption.get())))
    Game.count=Count
    counter.config(text="Chances:"+str(Game.count))
    global FPB
    FPB=SampleFPB()
    for d in digitss:
        d.set("")
    ran.config(text="FPB: ???")
    status.config(text="Start")
    
#reset button
reset=Button(Game,text="Reset",font="Arial 20",height=1,width=8,justify="center",command=resetFPB).place(x="320",y="560")

#main game loop
Game.mainloop()

"""issues : too many variables used,
            not efficient organisation of variables,
            text input accepts more than 1 digit per entry (temporary fix is to take the first digit in the entry)
            Bad and inconsistent variable names,
            [Fixed] 2 text inputs would have same StringVar assigned,
            [Fixed] reset would generate 3 digit number when digits changed to 4,
            [Fixed] when game won with digits set to 5 , StatusText prints outside Game window
"""