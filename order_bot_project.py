# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
        #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 

# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------


from re import M




# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------
def display_menu():
  #Meals
  print("******Meals******")
  print("[0] Big Mac: $4")
  print("[1] Spicy Chicken Sandwich: $5")
  print("[2] 10 Chicken Nuggets: $5")
  #Drinks
  print("******Drinks******")
  print("[3] Hi-C: $2")
  print("[4] Pepsi: $3")
  print("[5] Coke: $3")
  #Dessert
  print("******Desserts******")
  print("[6] McFlurry: $3")
  print("[7] Vanilla Cone: $1")
  print("[8] Hot Fudge Sundae: $2")


# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------
def take_order():
	global meal
	meal = None
	global meal_cost
	meal_cost = None
	meal_num = None
	while meal_num is not 0 or not 1 or not 2:
		meal = input("Choose your meal: ")
		meal_num = int(meal)
	if meal_num == 0:
		meal_cost = 4
		meal = "Big Mac"
	elif meal_num == 1:
		meal_cost = 5
		meal = "Spicy Chicken Sandwich"
	elif meal_num == 2:
		meal_cost = 5
		meal = "10 Chicken Nuggets"

	global drink
	drink = None
	global drink_cost
	drink_cost = None
	drink_num = None
	while drink_num is not 3 or not 4 or not 5:
		drink = input("Choose your drink: ")
		drink_num = int(drink)
	if drink_num == 3:
		drink_cost = 2
		drink = "Hi-C"
	elif drink_num == 4:
		drink_cost = 3
		drink = "Pepsi"
	elif drink_num == 5:
		drink_cost = 3
		drink = "Coke"
	#312
	
	global dessert
	dessert = None
	global dessert_cost
	dessert_cost = None
	dessert_num = None
	while dessert_num is not 6 or not 7 or not 8:
		dessert = input("Choose your dessert: ")
		dessert_num = int(dessert)
	if dessert_num == 6:
		dessert_cost = 3
		dessert = "McFlurry"
	elif dessert_num == 7:
		dessert_cost = 1
		dessert = "Vanilla Cone"
	elif dessert_num == 8:
		dessert_cost = 2
		dessert = "Hot Fudge Sundae"
	
	total = meal_cost + drink_cost + dessert_cost
	return total
		










# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 

def full_cost():
	total = take_order()
	tax = total * .10
	full_total = tax + total + tip
	return full_total




# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 

def receipt(meal, drink, dessert, meal_cost, drink_cost, dessert_cost, total_cost,tip):
	print("RECEIPT")
	print("*********************")
	print(f"{meal} ${meal_cost}")
	print(f"{drink} ${drink_cost}")
	print(f"{dessert} ${dessert_cost}")
	print(f"Cost: {total_cost}")
	print(f"Tip: {tip}")
	print(f"Tax {total_cost*.10}")
	print(f"Total: {total_cost+tip+(total_cost*.10)}")
	print("*********************")


# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------

display_menu()
total = take_order()

get_tip = input("Tip: ")
tip = int(get_tip)

tax = total * .10

full_total = total + tip + tax

receipt(meal,drink,dessert,meal_cost,drink_cost,dessert_cost,total,tip)



# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
