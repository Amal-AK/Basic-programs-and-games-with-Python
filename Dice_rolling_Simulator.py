import random

print( " Hello ! welcome to Dice rolling simulator ")
exit = "y"
while ( exit =='y' or exit=="Y" ):
    x= random.randint(1,6)
    if (x==1):
        print( "-----------")
        print("|         |")
        print("|    o    |")
        print("|         |")
        print( "-----------")

    elif (x==2) :
        print( "-----------")
        print("|         |")
        print("| o     o |")
        print("|         |")
        print( "-----------")

    elif( x==3) :
        print( "-----------")
        print("|    o    |")
        print("|    o    |")
        print("|    o    |")
        print( "-----------")
    elif (x==4) :
        print( "------------")
        print("| o      o |")
        print("|          |")
        print("| o      o |")
        print( "------------")
    elif (x==5) :
        print( "-------------")
        print("| o      o |")
        print("|     o    |")
        print("| o      o |")
        print( "-------------")
    else :
        print( "------------")
        print("| o      o |")
        print("| o      o |")
        print("| o      o |")
        print( "------------")

    exit = input("Enter 'y' to roll again , 'n' to exit :    ")
