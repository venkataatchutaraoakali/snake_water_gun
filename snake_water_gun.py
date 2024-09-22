import random
computer =random.choice([-1,0,1])
youtstr = input("enter your choice:")
youDict= {"s":1 ,"w":-1 ,"g": 0}
reverseDict ={1: "snake" ,-1: "water" ,0: "gun"}
you =youDict[youtstr]
print(f"computer choose {reverseDict[you]} you choose {reverseDict[computer]}")
if(computer==you):
    print("its a draw")
else:
    if(computer==-1 and you ==1):
        print("you won")

    elif(computer ==-1 and you ==0):
        print("you lose")
    elif(computer==1 and you ==-1):
        print("you lose")
    elif(computer==1 and you ==0):
        print("you lose")
    elif(computer==0 and you ==-1):
        print("you win")
    elif(computer==0 and you==1):
        print("youlose ")
    else:
        print("its a draw")