#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/

active = True

print("Welcome to Shopping List!")

welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n To check list you can type 'check' \nTo exit type 'exit' "

print(welcome_message)


#-->Todo: declare a shopping_list list
shopping_list = []


def prompt_user():

    reply = input("What do you want to add or remove?  >>  ")

    return reply

def check_answer(ans):
    x = True
    for i in range(0, len(shopping_list)):
        if shopping_list[i] == ans.split()[-1]:
            x = False
    return x

def add_item(string):
#this function can take in a string and store it in an array
    if check_answer(string):
        shopping_list.append(string.split()[-1])
    else:
        print(f"You already have {string.split()[-1]} in your shopping list!")


def remove_item(item):
    item = item.split()[-1]
    if item in shopping_list:
        shopping_list.remove(item) 
    else:
        print(f"{item} is not in the shopping list!")
 


while active:
    reply = prompt_user() #this makes the program continously prompt and check response while the boolean 'active' returns True
    if reply == 'exit':
        print("SHOPPING LIST")
        print("******************")
        for i in range(0,len(shopping_list)):
             print(shopping_list[i])
        print("******************")
        break
    elif reply[0] == 'a':
        add_item(reply)
    elif reply[0] == 'r':
        remove_item(reply)
