my_list = []
print(type(my_list))
my_list = list()
print(type(my_list))
number = [2, 6, 10, 12.5, 0]
print(number)
print(type(number))
print(type(number[1]))
print([2, 6, 10, 12.5, 0][1])
print(type(number[1]*2.5))

print(number[3])
print(type(number[3]))

foods = ["pizza", "tacos", "din sum", "sushi"]
print(foods[1])
print(type(foods[1]))
print(foods[1].upper())
print(foods[0].title())


x = 12
y = 15.5
z = "Z"
random_list = [x, y, z]
print(type(random_list[0]))
print(type(random_list[1]))
print(type(random_list[2]))

my_fav_num = random_list[0]
print(my_fav_num)

foods = ["pizza", "tacos", "din sum", "sushi"]
foods.append("cheeseburger")
print(foods)

#DO NOT foods = foods.append("cheeseburger") and then try to print(foods) 
#because you haven't put it in the list yet. you're reassigning the foods list to something that's not there. 

foods = ["pizza", "tacos", "din sum", "sushi"]
foods.insert(0, "pho")
print(foods)

foods.remove("pho")
print(foods)

foods = ["pizza", "tacos", "din sum", "sushi"]
foods.append("pizza")
print(foods)
foods.remove("pizza")
print(foods)
foods.remove("pizza")
print(foods)

foods = ["pizza", "tacos", "din sum", "sushi"]
del foods[1]
print(foods)

foods = ["pizza", "tacos", "din sum", "sushi"]
print(foods.pop())
print(foods)

foods = ["pizza", "tacos", "din sum", "sushi"]
print(foods.sort())
print(foods)
print(foods.sort(reverse=True))
print(foods)

foods = ["pizza", "tacos", "din sum", "sushi"]
print(sorted(foods))
print(foods)
foods = sorted(foods, reverse = True)
print(foods)
foods.reverse()
#returns NONE until you print(foods)
print(foods)

