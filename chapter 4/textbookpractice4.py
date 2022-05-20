magicians = ['alice', 'daid', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show")



#4-1 PIZZAS practice 
pizzas = ["margarita", "plain", "veggie"]
for pizza in pizzas:
    print("I like " + pizza.title() + " pizza.\n") 
print("Pizza is the greatest.")


#4-2 ANIMALS practice
dogs = ["wheatens", "goldendoodles", "maltipoos"]
for dog in dogs:
    print(dog.title() + " would make such amazing pets.") 
print("Any of these dogs would be welcome in my home any day!")




#Range function
for value in range(1,5):
    print(value)
for value in range(1,6):
    print(value)

even_numbers = list(range(2,11,2))
print(even_numbers)

odd_numbers = list(range(1,15,2))
print(odd_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)


squares = [value**2 for value in range(1,11)]
print(squares)

print(list(range(1,20,2)))

for value in range(1,30):
    value = (list(range(3,30,3)))
print(value)

cubed = []
for value in range(1,10):
    cube = value**3
    cubed.append(cube)
print(cubed)

cubed = [value**3 for value in range (1, 10)]
print(cubed)

evens = []
for value in range(1,10):
    even = value*2
    evens.append(even)
print(evens)



#splits
players = ['charles', 'martina', 'michael', 'florance', 'eli']
print(players[1:4])
print(players[:3])
print(players[0:3])

#looping through players in a list
players = ['charles', 'martina', 'michael', 'florance', 'eli']
for player in players[:3]:
    print(player.title() + ", you did an amazing job today. Keep up the good work!\n")
players = ['charles', 'martina', 'michael', 'florance', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


my_fav_foods = ["watermelon", "papaya", "yogurt and honey"]
my_friends_fav_foods = my_fav_foods[:]
print("My favorite foods are:")
print(my_fav_foods)

print("\nMy friend's favorite foods are:")
print(my_friends_fav_foods)
my_fav_foods.append("gummy bears")
my_friends_fav_foods.append("ice cream")
print("\nMy favorite foods are:")
print(my_fav_foods)
print("\nMy friend's favorite foods are:")
print(my_friends_fav_foods)

my_fav_foods[3] = "canoli"
print("\nMy favorite foods are:")
print(my_fav_foods)


#practice copying lists
my_islands = ["maui", "kauai", "oahu", "lanai"]
friends_island = my_islands[:]
friends_island.append("big island") 
friends_island.append("molokini")
print("\nI've been to the following islands:")
print(my_islands)
print("\nMy friend has been to more islands:")
print(friends_island)


dimensions = (200, 50)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


    #4-13 Buffet
menu = ("salmon", "pasta", "lasagna", "rissoto")
for food in menu[:3]:
    print("We are offering these specials tonight:" + food)

menu = ("mushroom steak", "pizza", "lasagna", "rissoto")
for food in menu[:3]:
    print("\nWe have modified our specials for tonight, please try our special, " + food)
