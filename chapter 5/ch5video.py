# Boolean = ON & OFF, Y & N, T & F
my_bool = True
print(my_bool)
my_bool =  False
print(my_bool)
print(bool(0))
print(bool(-123))
print(bool(" "))
print("dog" == "dog") # prints true
print("dog" == "cat") # prints false
print("dog" == "Dog".lower()) # prints true because you've made Dog into dog which is = dog
print(4 >= 6) # "false" can ask it questions like this. like in terminal

x = 10
print(5 < x < 20)

letter = "c" 
print(letter > "b") # prints true

letter = "a" 
print(letter > "b") # prints false

letter = "B" 
print(letter > "b") # false

letter = "b" 
print(letter > "B") # true
print(ord("A")) # 65 (order of alphabet)
print(ord("a")) # 97 (order in alphabet) 
# so it's A, B, C, D and then a, b, c, d

print("\n\n\n Lines 32-40")
x = 10
y = 10
z = 20
print(x == 10 and y == 10) # true
print(x == 10 and y == 10 and z == 10) # false
print(x == 10 or y == 10 or z == 10) # true because one of these is true
# basically like, "Are any of these True?" 
# the answer you get back is "yes, (at least) one of them is true"

print("\n\n\n Lines 42 to 48")
x = 8
y = 9
print(x == y) # false
print(x != y) # true
# OR
print(not x == y) # now you get true

print("\n\n\nLines 50 to 79")
# if BOOLEAN or BOOLEANE EXP:
    # codeblock
    # for if true
# else (though ifs dont need an else)
    # for the if false code block

height = 55
# must be 5' tall to ride
if height < 60: 
    print("Sorry, this ride is not suitable for you")
    print("Please refer to our other fun rides for individuals <60 in")
else: # if you change height to 65 it'll print the following
    print("Enjoy the ride!")
print("Thank you for visiting!")

print("\n\n")
#what if you must be under 6' tall to ride?
height = 55 # can play around with these numbers to test it out
if height <60: 
    print("Sorry, this ride is not suitable for you")
    print("Please refer to our other fun rides for individuals <60 in")
elif height > 72: 
    print("Sorry you are too tall for this ride")
    print("Please enjoy some of our other options!")
else:
    print("Enjoy the ride!")
# if these were all "if" statements, it would take more time to define boundaries
print("\n\n")
# Say my name, say my name if no one is around you say baby i love you 

