import random

move = input("what would you like to do? walk, shop or end? :")
possibledabloons = ("2", "4", "6")
dabloonrandomizer = random.choice(possibledabloons)
dabloonsgot = dabloonrandomizer
dabloons = 0
shop = "soup: 2DB drink: 1DB"
nextmove = ""
moveaftersoup = ""
moveafterdrink = ""
soupchoice = ""
drinkchoice = ""
buydrink = ""
boughtdrink = ""
buysoup = ""
boughtsoup = ""

if move == "walk":
    print("you found "+str(dabloonrandomizer)+" dabloons!")
    dabloons = dabloonsgot
    print("you now have "+str(dabloons)+" dabloons!")
    nextmove = input("would you like to go to the shop(y/n)? :")
elif move == "shop":
    print("welcome to the shop!")
    print("what would you like?")
    print("you have no money! goodbye traveller! :]")
elif move == "end":
    print("ok! be safe traveller :]")

#Shop system.

if nextmove == "y":
    print("welcome to the shop!")
    print("what would you like?")
    print(shop)
    choice = input("item:")
    if choice == "soup":
        print("here you go! be safe traveller :]")
        moveaftersoup = input("what would you like to do? walk, items or end? :")
    elif choice == "drink":
        print("here you go! be safe :)")
        moveafterdrink = input("what would you like to do? walk, items or end? :")

#Move after soup.

if moveaftersoup == "walk":
    print("you found "+str(dabloonrandomizer)+" dabloons!")
    dabloons = dabloonsgot
    print("you now have "+str(dabloons)+" dabloons!")
    nextmove = input("would you like to go to the shop(y/n)? :")
    if nextmove == "y":
        print("welcome to the shop!")
        print("what would you like?")
        print("drink 1DB")
        buydrink = input("would you like to buy drink(y/n)? :")
        if buydrink == "y":
            print("ok! here you go!")
            boughtdrink = input("would you like to drink drink(y/n)? :")
            if boughtdrink == "y":
                print("you drank drink!")
                print("it does nothing.")
            elif boughtdrink == "n":
                print("ok")
        elif buydrink == "n":
            print("ok! be safe traveller :]")
elif moveaftersoup == "items":
    print("items: soup")
    soupchoice = input("would you like to drink soup(y/n)? :")
    if soupchoice == "y":
        print("you drank soup!")
        print("it does nothing.")
    elif soupchoice == "n":
        print("ok, you didnt drink soup.")
elif moveaftersoup == "end":
    print("ok! be safe traveller :]")

#Move after drink.

if moveafterdrink == "walk":
    print("you found "+str(dabloonrandomizer)+" dabloons!")
    dabloons = dabloonsgot
    print("you now have "+str(dabloons)+" dabloons!")
    if nextmove == "y":
        print("welcome to the shop!")
        print("what would you like?")
        print("soup 2DB")
        buysoup = input("would you like to buy soup(y/n)? :")
        if buysoup == "y":
            print("ok! here you go!")
            boughtsoup = input("would you like to drink soup(y/n)? :")
            if boughtsoup == "y":
                print("you drank soup!")
                print("it does nothing.")
            elif boughtsoup == "n":
                print("ok")
        elif buysoup == "n":
            print("ok! be safe traveller :]")
elif moveafterdrink == "items":
    print("items: drink")
    drinkchoice = input("would you like to drink drink(y/n)? :")
    if drinkchoice == "y":
        print("you drank drink!")
        print("it does nothing.")
    elif drinkchoice == "n":
        print("ok, you didnt drink drink.")
elif moveafterdrink == "end":
    print("ok! be safe traveller :]")