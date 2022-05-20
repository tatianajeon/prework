# 4-1 & 4-2
pizzas = ["plain", "margarita", "white"]
for pizza in pizzas:
    print(pizza)
    print("I like " + pizza + " pizza.")
print("Pizza is great for lunch, dinner, snacktime. \nPizza can be ound anywhere. \nI love all pizzas!")



# 4-3 to 4-9
print(list(range(1,21)))
print(max(range(1,21)))
print(min(range(1,21)))
print(sum(range(1,21)))
print(list(range(1,21,2)))
print(list(range(2,21,2)))
print(list(range(3,30,3)))

threes = (list(range(3,31,3)))
for number in threes: 
    print(number)

cubed = (list(range(1,10)))
for value in cubed:
    cubed = value**3
    print(cubed)

cubed = [value**3 for value in list(range(1,10))]
print(cubed)

squared = (list(range(1,10)))
for value in squared:
    squared = value**2
    print(squared)

squared = [value**2 for value in list(range(1,10))]
print(squared)
