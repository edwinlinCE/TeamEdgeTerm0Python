
# -------------------------------------------- 
# Day 2 Challenges
# -------------------------------------------- 

from math import degrees


message = "Welcome to Day 2.\nToday we are learning about conditionals.\nLet's practice writing some conditionals of our own!"
print(message)
# -------------------------------------------- 

print("------------------- Challenge 1 -------------------")
# Can you drive?
   # Prompt the user to enter their age.
   # Write conditional statements that print out whether you can drive in your city. 

user_age = input("Enter your age: ")
if(int(user_age) >= 16):
   print("You are old enough to drive!")
else:
   print("You are not old enough to drive!")










# -------------------------------------------- 

print("------------------- Challenge 2 -------------------") 

# Who placed first?
   # Write conditional statements that checks which is the highest and prints the highest score. 
   # Hint: Create three variables and assign them random scores. 

#assuming the scores cannot be equal to each other
score_1 = 20
score_2 = 5
score_3 = 50

if score_1 > score_2 and score_1 > score_3:
   print(score_1)
elif score_2 > score_1 and score_2 > score_3:
   print(score_2)
else:
   print(score_3)







# -------------------------------------------- 

print("------------------- Challenge 3 -------------------")

# One of the most common parts of our daily routine is checking the weather. 
# Our outfit and accessories are dependent on the temperature and conditions outside. 
# ie. We're probably not going to wear shorts out when it's snowing...


# **** Challenge 3: Part 1 ****
# Write a conditional statement that checks the value of the weather variable 
# and prints out a weather report based on the current weather:
# Rainy: Bring an umbrella
# Sunny: Wear a hat and sunglasses
# Snowing: Wear gloves and a scarf 

# Here's a variable to get you started:
weather = "rainy"
degrees = 3020
if weather.lower() == "rainy":
   print("Bring an umbrella")
elif weather.lower() == "sunny":
   print("Wear a hat and sunglasses")
elif weather.lower() == "snowing":
   print("Wear gloves and a scarf")













# Tip: Try changing the value of the weather variable to test your other conditions.

# **** Challenge 3: Part 2 ****
# Now that you've written conditions for specific weather forecasts, let's also add in temperature! 
# You can't dress accordingly if you only know that it's raining outside but not how cold it is!
# For example:
    # If it's raining and 60 degrees, you might want to bring your umbrella and wear a light jacket.
    # However, if it's raining and 30 degrees, you might want to break out a warmer jacket with your umbrella instead. 
    
   # Add to your conditional statements above and modify your weather reports to also take into account the temperature. 
   # Make sure to account for at least three different temperatures!
   # Hint: You will need another variable to keep track of the temperature.



if weather.lower() == "rainy" and degrees >= 60:
   print("You might want to bring your umbrella and wear a light jacket")
elif weather.lower() == "rainy" and degrees <= 30:
   print("You might want to bring an umbrella and wear warm clothing")
elif weather.lower() == "sunny" and degrees >= 60:
   print("You might want to bring an umbrella and wear a short sleeved shirt")
elif weather.lower() == "sunny" and degrees <= 30:
   print("You might want to wear a long sleeved shirt")
elif weather.lower() == "snowing" and degrees >= 60:
   print("You might want to wear a hoodie.")
elif weather.lower() == "snowing" and degrees <= 30:
   print("You might want to wear a puffy jacket")









# -------------------------------------------- 

print("------------------- Challenge 4 -------------------")

# Prompt the user to enter the day of the week (1-7 representing Monday - Sunday)
# Write a set of conditionals that will take a number from 1 to 7 
# and print out the corresponding day of the week. 
# Make sure to add a statement that accounts for any numbers out of range! 



day_of_week = input("Enter the day of the week: ")
weekdays = dict([ (1,"Monday"),
                  (2,"Tuesday"),
                  (3,"Wednesday"),
                  (4,"Thursday"),  
                  (5,"Friday"),
                  (6,"Saturday"),
                  (7,"Sunday")

])
print(weekdays.get(int(day_of_week)))





# -------------------------------------------- 

print("------------------- Challenge 5 -------------------")

# A leap year is a calendar year that contains an additional day added 
# to keep the calendar year synchronized with the astronomical year or seasonal year.
# To calculate if a specific year is/was a leap year, you can follow the following steps:
     # 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
     # 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
     # 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
     # 4. The year is a leap year (it has 366 days).
     # 5. The year is not a leap year (it has 365 days).

# Those are a lot of conditions...
# Your challenge is to translate the steps above into conditionals which will evaluate if the 
# year stored in a variable is/was a leap year.

year = 2024
if year % 4 == 0:
   if year % 100 == 0:
      if year % 400 == 0:
         print(f"{year} is a leap year!")
      else:
         print(f"{year} is not a leap year!")
   else:
      print(f"{year} is a leap year!")
else:
   print(f"{year} is not a leap year!")
