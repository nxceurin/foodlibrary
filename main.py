import os, recipelist, listmod, msvcrt

def clear():
    if os.name == 'nt': 
        _ = os.system('cls')

def search(L):
    try:
        match= float(input("Minimum % of matched ingredients (default=60): ")) 
    except ValueError:
        print("Enter a valid numerical value between 0 and 100!")
    else:
        matched= recipelist.totalret(L, match, True)
        print("Recipes that have", str(match)+"%", "or more matching ingredients with those in your pantry:")
        matcha= {}
        sorted_keys = sorted(matched, key=matched.get, reverse= True)
        for x in sorted_keys:
            matcha[x]= matched[x]
        for x in matcha:
            print(x, " | match % =", matcha[x])

def modif(L):
    while True:
        print("[1] Add items\n[2] Remove items\n[3] View pantry\n[4] Search for dishes using existing pantry\n[5] View all ingredients\n[6] View all dishes\n[7] View a dish's details\n[8] Exit")
        try:
            ans= int(input())
        except ValueError:
            print("Uh-oh! That's not a valid choice!")
        else:
            if ans not in [1, 2, 3, 4, 5, 6, 7, 8]:
                print("Uh-oh! That's not a valid choice!")
                clear()
            elif ans==1:
                listmod.addstuff(L)
            elif ans==2:
                listmod.removestuff(L)
            elif ans==3:
                listmod.viewpantry(L)
            elif ans==4:
                search(L)
            elif ans==5:
                recipelist.showIList()
            elif ans==6:
                recipelist.showRecipe()
            elif ans==7:
                dname=input("Dish name:")
                clear()
                recipelist.showInfo(dname)
            else: break
            msvcrt.getch()
            clear()
          
# main
userL= []
clear()

print("Note: The dishes mentioned in the demo run are mostly fictional.")
print("Welcome to foodLibrary! Get started by adding some ingredients to your inventory~")
msvcrt.getch()
modif(userL) #first run

# if len(userL)==0:
#     print("Looks like your pantry is empty. Start by adding some ingredients!")
# else:
#     listmod.viewpantry(userL)
# print("number of recipes that can be made with ingredients in pantry:", recipelist.totalret(userL))
#print(userL)