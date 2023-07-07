#missionaries and cannibals without GUI
#Ashish Tembhekar // Roll no.2 // NCER // FE-D // CSE-AI // 7666081264

def statusPrinter(direction,ml,cl,mr,cr):
    if direction=="R":
        print("\n")
        for i in range(0,ml):
            print("M ",end="")
        for i in range(0,cl):
            print("C ",end="")
        print("| \t-->B| ",end="")
        for i in range(0,mr):
            print("M ",end="")
        for i in range(0,cr):
            print("C ",end="")
        print("\n")
    elif direction=="L":
        print("\n")
        for i in range(0,ml):
            print("M ",end="")
        for i in range(0,cl):
            print("C ",end="")
        print("|B<--\t | ",end="")
        for i in range(0,mr):
            print("M ",end="")
        for i in range(0,cr):
            print("C ",end="")
        print("\n")
    

def checkBoatspace(x,y,ml,cl,mr,cr,direction):
    if x==0 and y==0:
        print("Boat can't move on its own")
        return False
    if direction=="R":
        if (x+y <=2) and ((ml-x)>=0 and (cl-y)>=0):
            return True
        else:
            print("Travel not possible")
            return False
    elif direction=="L":
        if ((x+y) <= 2) and ((mr-x)>=0) and ((cr-y)>=0):
            return True
        else:
            print("Travel not possible")
            return False
    else:
        print("\n Invalid input, try again")
        return False

def gamecheck():
    #print(ML,CL,MR,CR)
    #if(((CL==3)and(ML == 1))or((CL==3)and(ML==2))or((CL==2)and(ML==1))or((CR==3)and (MR == 1))or((CR==3)and(MR==2))or((CR==2)and(MR==1))):
    #    return False,False
    if ((ML!=0) and (ML<CL)) or ((MR!=0) and (MR<CR)):
        return False,False
    elif (ML==3)and(CL==3):
        return False,True
    return True,False

def LeftToRight(localML,localCL,localMR,localCR):
    
    print("Going Left to right")
    while True:
        Miss_on_boat=int(input("Enter number of Missionaries to get on boat :"))
        Cann_on_boat=int(input("Enter number of Cannibals to get on boat :"))
        if checkBoatspace(Miss_on_boat,Cann_on_boat,localML,localCL,localMR,localCR,"R")==True:
            break
    localML = (localML-Miss_on_boat)
    localCL = (localCL-Cann_on_boat)
    localMR += Miss_on_boat
    localCR += Cann_on_boat
    statusPrinter("R",localML,localCL,localMR,localCR)
    return localML,localCL,localMR,localCR
    
def RightToLeft(localML,localCL,localMR,localCR):
    print("Going Right to Left")
    while True:
        Miss_on_boat=int(input("Enter number of Missionaries to get on boat :"))
        Cann_on_boat=int(input("Enter number of Cannibals to get on boat :"))
        if checkBoatspace(Miss_on_boat,Cann_on_boat,localML,localCL,localMR,localCR,"L")==True:
            break
    localML += Miss_on_boat
    localCL += Cann_on_boat
    localMR -= Miss_on_boat
    localCR -= Cann_on_boat
    statusPrinter("L",localML,localCL,localMR,localCR)
    return localML,localCL,localMR,localCR

while True:
    #Game variables
    MR=3                                        #missionaries on right
    ML=0                                        #missionaries on left
    CR=3                                        #cannibals on right
    CL=0                                        #cannibals on left
    Miss_on_boat=0                              #no of missionaries on boat
    Cann_on_boat=0                              #no of cannibals on boat
    print("\n\n")
    print("Missionaries and Cannibals".center(50))
    print("\n","|\t\tB| M M M C C C".center(50),"\n")
    while True:
        #print(ML,CL,MR,CR)
        gameML,gameCL,gameMR,gameCR=RightToLeft(localML=ML,localCL=CL,localMR=MR,localCR=CR)
        ML,CL,MR,CR=gameML,gameCL,gameMR,gameCR
        if gamecheck()[0]==True:
            pass
        else:
            print("Game has ended!")
            break
        gameML,gameCL,gameMR,gameCR=LeftToRight(localML=ML,localCL=CL,localMR=MR,localCR=CR)
        ML,CL,MR,CR=gameML,gameCL,gameMR,gameCR
        if gamecheck()[0]==True:
            pass
        else:
            print("Game has ended!")
            break
    if gamecheck()[1]==True:
        print("\nCongratulations!, you've won the game!")
    else:
        print("Cannibals have eaten the missionaries.Game Lost!")
    again=input("Do you wanna play again?(Yes/No) :")
    if again=="Yes" or again=="yes" or again=="Y" or again=="y":
        pass
    elif again=="No" or again=="no" or again=="N" or again=="n":
        break
    else:
        print("Invalid input, game will end.".center(50))