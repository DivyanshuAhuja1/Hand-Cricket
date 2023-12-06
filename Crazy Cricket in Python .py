import random

def input_num(min, max):
    num=int(input())

    if num>max or num<min:
        print("Enter valid choice")
        return input_num(min, max)
    else:
        return num
    
def innings(batsman, to_chase):
    
    total=0

    while True:
        print("Enter numbers between 1 and 6. If bowler chooses one bigger or one less than the batsman then it will be out. If you both choose the same number then " + batsman + " will get the square of the number." )
        pnum=input_num(1, 6)
        cnum=random.randint(1, 6)

        print("User chose", pnum)
        print("Computer chose", cnum)

        if pnum==cnum+1 or pnum==cnum-1:
            print(batsman + " is out")
            return total
        if pnum==cnum or cnum==pnum:
            if batsman=="User":
                total=total+pnum**2
            else:
                total=total+cnum**2
           
        else:
            if batsman=="User":
                total=total+pnum
            else:
                total=total+cnum
           
            print(batsman + " score is", total)
            if to_chase is not None and total > to_chase:
                return total
        print ("score=",total)


print("Time for toss, Enter 0 for Heads and 1 for Tails")
choice=input_num(0, 1)
coin=random.randint(0, 1)
player_bowls = False

if coin==choice:
    print("You have won the toss")
    print("Select 0 to bat, 1 to bowl ")
    player_bowls = input_num(0, 1) == 1

    if player_bowls:
        print("You chose to bowl")
    else:
        print("You chose to bat")
else:
    print("Computer won the toss")
    player_bowls = random.randint(0, 1) == 1

    if player_bowls:
        print("Computer chose to bat")
    else:
        print("Computer chose to bowl")

if player_bowls:
    comp_score=innings("Computer", None)
    user_score=innings("User", comp_score)
else:
    user_score=innings("User", None)
    comp_score=innings("Computer", user_score)

if comp_score<user_score:
    print("User wins")
elif user_score<comp_score:
    print("Computer wins")
else:
    print("Match draw")


