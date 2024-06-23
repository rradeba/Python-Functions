# task 1-3 

# global variables 
list_of_items = []
list_decision = input("Would you like to add(a), remove(r), view(v), or finish(f) the list?")

#functions for adding and removing items 
def add_to_list(a,b): 
    return a.append(b)

def remove_from_list(a,b): 
    return a.remove(b)

# loop to remain in list until 'f' is pressed  

while list_decision in  ['a', 'r', 'v']:
    if list_decision == 'a':
        add_item = input("What grocery item would you like to add to the list? ")
        add_to_list(list_of_items, add_item)
        list_decision = input("Would you like to add(a), remove(r), view(v), or finish(f) the list?")
    elif list_decision == 'r':
        remove_item = input("What grocery item would you like to remove from the list? ")
        if remove_item in list_of_items:
            remove_from_list(list_of_items, remove_item)
        else: print("Requested item is not in the list.")
        list_decision = input("Would you like to add(a), remove(r), view(v), or finish(f) the list?")
    elif list_decision == 'v':
        print(list_of_items)
        list_decision = input("Would you like to add(a), remove(r), view(v), or finish(f) the list?")

# execute if f is pressed     
if list_decision == 'f':
    print("Here is your finished list: " + str(list_of_items))
else: 
    print("Please type one of the listed characters.")



