foods = ["pizza", "tacos", "dim sum", "sushi"] 
# listname[index]
print(foods[1])


for food in foods:
    # code block
    # code block runs for every item in the list
    print(f"I like {food} because they are yummy")
    if food == "pizza":
        break # stop the loop at pizza
    
foods = ["pizza", "tacos", "dim sum", "sushi"] 
for food in foods:
    if food == "dim sum":
        continue
    print(f"I like {food} because it is great")

# loop of the index
for index in range(len(foods)):
    print(index)
    print(foods[index])

print(list(enumerate(foods)))
for index, food in enumerate(foods):
    print(f"my no. {index + 1} food is {food.title()}")



# TUPLE. can't change
my_tup = 1, 2
print (type(my_tup))
my_tup = (1, 2)
print(type(my_tup))
my_tup = my_tup + (3,4)
print(my_tup)

# SLICING 
my_string = "Hey guys lets learn python"
my_list = ["pizza", "tacos", "dim sum", "sushi"]
print(my_string[1:4])
# you get "ey" from "hey". 
print(my_string[4:7]) # you get the word "guy" 
# don't forget: ranges [:] start with the first number, end just before the second number
print(my_string[0:7])
print(my_string[8:]) # you get the rest of the string
print(my_string[::2]) # get the whole thing but you can go every 2nd/5th/etc number. or go bckwrds with -1
# you can also slice by doing [8:4:-1]
print(my_string[8:4:-2])
print(my_string[7:3:-1]) # you get "syug"

foods = ["pizza", "tacos", "dim sum", "sushi"] 
for food in foods:
    if food == "dim sum":
        continue
    print(f"It would be great if we had {food} for dinner tonight")


for index in range(len(foods)):
    print(index)
    print(foods[index])
# as a result you get 0 pizza 1 tacos 2 dim sum 3 sushi

# ENUMERATE
print(list(enumerate(foods)))
# turns out to be [(0, 'pizza'), (1, 'tacos'), etc]
# these are tuples (index and food are unchangable/connected)

print(list(enumerate(foods)))
for index, food in enumerate(foods):
    print(f"My number {index + 1} food is {food.title()}")

deck = ["one", "two", "three", "four"]
deck[3] = "five"
deck=deck.reverse()
print(deck)

my_string = " "
print(my_string)

my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
