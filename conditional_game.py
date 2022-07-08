from random import randint
import time

# -------------------------------------------- 

    # You've just learned about variables, conditionals.
    # Just from knowing those two topics, you can do so much!
    
    # Let's try to make a simple program that responds to the user.
    # We're going to recreate the Magic 8 Ball!!!
            
            # Never heard of it? That's ok!

                    # You got this!

  # -------------------------------------------- 

    # How a Magic 8 Ball Works:

    # The user asks a question and vigoriously shakes the ball. 
    # Then the ball will respond with one of twenty responses, chosen at random. 

    # That's pretty simple right?

 # -------------------------------------------- 

    # Part 1: 
    # Print instructions on the screen and 
    # prompt the user to ask a question

    

  # --------------------------------------------
print("Ask a question and the 8 Ball will answer!")
user_input = input("Enter a question: ")














# -------------------------------------------- 

    # Part 2: Next, we need to randomly select a response from 20 options.

    # Randomly select a number from 0 - 19 
    # Use that to select from the following responses:
        # 0 - It is certain.
        # 1 - It is decidedly so.
        # 2 - Without a doubt.
        # 3 - Yes - definitely.
        # 4 - You may rely on it.
        # 5 - As I see it, yes.
        # 6 - Most likely.
        # 7 - Outlook good.
        # 8 - Yes.
        # 9 - Signs point to yes.
        # 10 - Reply hazy, try again.
        # 11 - Ask again later.
        # 12 - Better not tell you now.
        # 13 - Cannot predict now.
        # 14 - Concentrate and ask again.
        # 15 - Don't count on it.
        # 16 - My reply is no.
        # 17 - My sources say no.
        # 18 - Outlook not so good.
        # 19 - Very doubtful.

    # Look up random.rand_int to see how you can use it to select a random number.

  # -------------------------------------------- 

rand = randint(1,19)

output = dict([
        # 0,It is certain.
        ( 1,"It is decidedly so.") ,
        ( 2,"Without a doubt."),
        ( 3,"Yes - definitely."),
        ( 4,"You may rely on it."),
        ( 5,"As I see it, yes."),
        ( 6,"Most likely."),
        ( 7,"Outlook good."),
        ( 8,"Yes."),
        ( 9,"Signs point to yes."),
        ( 10,"Reply hazy, try again."),
        ( 11,"Ask again later."),
        ( 12,"Better not tell you now."),
        ( 13,"Cannot predict now."),
        ( 14,"Concentrate and ask again."),
        ( 15,"Don't count on it."),
        ( 16,"My reply is no."),
        ( 17,"My sources say no."),
        ( 18,"Outlook not so good."),
        (19,"Very doubtful.")

])
print(output[rand])

















# -------------------------------------------- 

    # Part 3: Customize it!

    # Select your own theme and use case and modify your code!
    
# -------------------------------------------- 

#fortune teller

teller = dict([
            (1,"Ask again later."),
            (2,"Better not tell you now."),
            (3,"Cannot predict now"),
            (4,"Most likely"),
            (5,"As I see it, yes"),
            (6,"It is decidedly so"),
            (7,"Yes definitely"),
            (8,"You may rely on it"),
            (9,"Without a doubt"),
            (10,"It is certain"),
            (11,"Yes"),
            (12,"Signs point to yes"),
            (13,"No."),
            (14,"Don’t count on it"),
            (15,"Outlook not so good"),
            (16,"My sources say no"),
            (17,"Very doubtful"),
            (18,"Sucks to suck ¯\_(ツ)_/¯"),
            (19,"Lmao no"),
            (20,"Not at all, you utter buffoon."),
            (21,"Cannot predict now"),
            (22,"Reply hazy try again"),
            (23,"My reply is no"),
            (24,"Yikes! I don't think you would like the answer. One word: Xanax")
])

question = input("Enter a question: ")

colors = ["BLUE", "GREEN", "ORANGE", "RED"]
num_list_1 = [1,2,5,6]
num_list_2 = [3,8,4,7]

print(colors)
pick_colors = input("Pick a color: ")

temp = ""
temp_arr = []

for i in colors:
  if pick_colors.upper() == i:
    temp = i
    break
for i in range(0, len(temp)):
  if(i % 2 ==0):
    print(f"{temp[i]}\n{num_list_1}")
    temp_arr = num_list_1
  else:
    print(f"{temp[i]}\n{num_list_2}")
    temp_arr = num_list_2
  time.sleep(1)
pick_num =None
while pick_num not in temp_arr:
  pick_num = input("Pick a number below the last letter of your color: ")
  pick_num = int(pick_num)
  if pick_num not in temp_arr:
    print("Please pick the numbers below the last letter")
    time.sleep(1)

temp_arr_1 = []
for i in range(1,int(pick_num)+1):
  if i % 2 == 0:
    print(f"{i}\n{str(num_list_2)}")
    temp_arr_1 = num_list_2
  else:
    print(f"{i}\n{str(num_list_1)}")
    temp_arr_1 = num_list_1
  time.sleep(1)
choice = None
while choice not in temp_arr_1:
  print("Pick a number from your list")
  choice = int(input())

choice = choice * randint(1,3)
print(teller[choice])





