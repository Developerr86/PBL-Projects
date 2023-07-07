#FPB without GUI
#Ashish Tembhekar // Roll no.2 // NCER // FE-D // CSE-AI // 7666081264

#library imports
from random import sample

#Function to get digits from user
def get_digits():
    try:
        digits=int(input("\nEnter the number of digits: (minimum 3, maximum 6)"))
        if digits>6 or digits<3:
            print("invalid number of digits, try again\n")
            digits=get_digits()
    except ValueError:                          #occurs when user leaves the digit entry empty
        print("Invalid, Try agian.")
        digits=get_digits()
    return digits

#Function to ask users for having Zeros in FPB
def Allow_zeros():
    AllowZero=input("Allow zeros? (Yes/No):")
    if AllowZero=="yes" or AllowZero=="Yes" or AllowZero=="y" or AllowZero=="Y":
        AllowZero=True
    elif AllowZero=="no" or AllowZero=="No" or AllowZero=="n" or AllowZero=="N":
        AllowZero=False
    else:
        print("Invalid answer, try again")
        AllowZero=Allow_zeros()
    return AllowZero

#Function to generate a random FPB number
def generate_FPB_number(Z,D):
    if Z:                                       #Z is a boolean, indicates if zeros are allowed or not
        return sample("1234567890",D)           #D is the number of digits
    else:
        return sample("123456789",D)

#function to compare user input with FPB
def compare_guess_with_FPB(G,FPB,D):            #G is the guess input from the user
    output=""
    #print(list(G),FPB)
    if list(G)==FPB:
        output="Fermi!"*D
        gamewin=True                            
    else:
        for x in range(D):
            if G[x]==FPB[x]:
                output=output+" Fermi"
            elif G[x] in FPB:
                output=output+" Pico"
        gamewin=False
    if output=="":
        output="Bagel"
        gamewin=False
    return output,gamewin

#Function to ask the user if they wanna play again
def play():
    play_again=input("\nDo you wanna play again? (Yes/No) :")
    if play_again=="yes" or play_again=="Yes" or play_again=="y" or play_again=="Y":
        state=True
    elif play_again=="no" or play_again=="No" or play_again=="n" or play_again=="N":
        state=False
    else:
        print("Invalid response, try again")
        state=play()
    return state

#Main GameLoop
while True:
    game_digits=get_digits()
    Zeros=Allow_zeros()
    FPB_number=generate_FPB_number(Zeros,game_digits)
    chances=3+(3*(game_digits))                 #My equation for number of chances, depends on the number of digits
    Attempted_guesses=[]
    while chances>0:
        try:
            guess=int(input("\nEnter your guess:"))
        except:
            print("Invalid guess, try agian.")
            continue
        if guess in Attempted_guesses:
            print("You have tried this number already.")
            continue
        elif (len(set(str(guess)))) < len(FPB_number):
            print("Not enough unique digits, try again.")
            continue
        elif len(str(guess)) > len(FPB_number):
            print("Too many digits entered, try agian.")
            continue
        checkFPB=compare_guess_with_FPB(str(guess),FPB_number,game_digits)
        print("\n {} \n Chances left: {}".format(checkFPB[0],chances))
        if checkFPB[0]=="Fermi!"*game_digits:
            break
        Attempted_guesses.append(guess)
        chances-=1
    if checkFPB[1]:
        print("\nGame Won!")
    else:
        print("\nGame Lost!")
    play_again=play()
    if play_again:
        pass
    else:
        print("\n\nFPB Game Over.")
        break

"""issues:
"""