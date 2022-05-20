cars = ['audi', 'bmw', 'subaru', 'toyota']
requested_car = "subaru"
if requested_car != "bmw":
    print("Sorry, we're out of other cars")

banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(user.title() + ", your comment has been approved")



cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'subaru':
        print("I predict true")
    if car == 'audi':
        print("I predict false")
# I predict false
# I predict true
# printed this way because in the list, audi comes first. 

baked_pies = ["pecan", "banana cream", "peach", "apple"]
for baked_pie in baked_pies:
    if baked_pie == "banana cream":
        print("\ntwo for one special on the banana cream pie!")
    if baked_pie != "banana cream":
        print("\nyou should consider the banana cream pie")

age = 21 # try switching out the numbers
if age < 21: 
    print("too young")
if age > 21:
    print("pass")

# if you type in 21, you get "no output"

banned_user = ["Jamie", "Jonathan", "Jessica"]
user = "JoAnne"
if user not in banned_user:
    print("\nWelcome ," + user.title() + ", you are welcome to access this page")

age = 18
if age >=18:
    print("You are old enough to vote!")
# if age is less than 19, just no output
    print("have you registered to vote yet?")
else: 
    print("Please come back after your 18th birthday!")

age = 66
if age <5: 
    print("Admission tickets free")
elif age <=18:
    print("student discount, $5/ticket")
elif age <65: 
    print("Admission tickets $10")
elif age >= 65: 
    print("Senior discount: $5 per ticket")



requested_toppings = ['mushroom', 'extra cheese', 'olives']
for requested_topping in requested_toppings:
    if 'mushroom' in requested_topping: 
        print("Topping: mushrooms")
    elif 'extra cheese' in requested_topping:
        print("Topping: extra cheese")
else:
    print("Plain pizza coming right up!")
print("\nFinish customizing your pizza!")


# 5-3 thru 5-5 Alien Colors
alien_color = ["green", "yellow", "red"]
alien_color = "green"
if "green" in alien_color:
    print("you've just won 5 points!")

alien_color = ["green", "yellow", "red"]
alien_color = "green"
if "green" in alien_color:
    print("You've just won 5 points!")
else: 
    print("You've earned 10 points!")

alien_color = ["green", "yellow", "red"]
alien_color = "yellow"
if not "green" in alien_color:
    print("you've earned 10 points!")
    
alien_color = ["green", "yellow", "red"]
alien_color = "yellow"
if not "green" in alien_color:
    print("you've earned 10 points!")

age = 65
if age <2:
    print("this is a baby")
elif age <4 : 
    print("this is a toddler")
elif age < 13:
    print("this is a child")
elif age < 20:
    print("this is a teenager")
elif age < 65:
    print("this is an adult")
else:
    print("this is a senior/elderly")

requested_toppings = ['mushroom', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("adding " + requested_topping.title() + ".")
print("\nYour pizza is in the oven!")

requested_toppings = ['mushroom', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("We're so sorry, we're out of green peppers! Please select a different item")
    else:
     print("adding " + requested_topping + ".")

requested_toppings = ["mushroom"]
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + " to your pizza")
else:
    print("Are you sure you want a plain pizza")


available_toppings = ["mushroom", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushroom", "olives", "pineapple", "jalapeno"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ", please choose an item on the list.")
print("\nLet's eat some pizza!")

usernames = []
if usernames:
    for username in usernames: 
        if "admin" in username:
            print("\nHello admin, would you liike to view your status report?")
        elif username in usernames: 
            print("\nWelcome back, " + username + ", thank you for logging in!")
else: 
    print("We need to find some users!!")
  
# layers of if/else: have to do an if for if a username is this or that
# then there is a layer of if/slse for if there even is a username. 

