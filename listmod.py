import recipelist

def viewpantry(L):
    try:
        print("Existing inventory:")
        for x in range(len(L)-1):
            print(L[x], end=", ")
        print(L[-1])
    except IndexError:
        print("Uh-oh, looks like your pantry is empty!")

#add items to pantry
def addstuff(L):
    print("Select available ingredients to add to pantry. Type 'view' to view available items, 'exit' to close.")
    while True:
        ing= input()
        if ing=="exit":
            break
        elif ing=="view":
            recipelist.showIList()
        elif ing not in recipelist.mIList:
            print("Uh oh! That's not a valid ingredient! Try 'view' to see a list of all valid items.")
        elif ing in L:
            print("That item is already in your pantry!")
        else:
            print(ing, "added to the pantry!")
            L.append(ing)


#remove items from pantry     
def removestuff(L):
    print("Select items to remove from your pantry. Type 'view' to view your current pantry, 'all' to clear pantry, 'exit' to close.")
    while True:
        inp= input()
        inp= inp.lower()
        if inp== "all":
            L= []
            break

        elif inp=="view":
            viewpantry(L)
            
        elif inp=="exit":
            break
        
        elif inp not in L:
            print("Looks like that ingredient is not in your pantry... type 'view' to check your inventory items.")
            
        else:
            print(inp, "removed from your pantry!")
            L.remove(inp)