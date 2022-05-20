# running a code block WHILE a condition is true
# while Boolean or boolean expression (something being true or not)
    # if true, will run this code block


# height = 55
# while height < 60 : 
    # print("Sorry but this ride is not for you")
# if we run this, this condition will loop until it's not true anymore. 
# it will run forever

height = 55
while height < 60 : 
    print(f"Sorry you are currently {height} + this ride is not for you")
    print("Drink my magic potion")
    height += 1
print("Thanks for coming")

# this will print until 55 reaches 60. 

height = int(input("What is your height in inches? "))
while height < 60:
    print(f"Sorry you are currently {height} + this ride is not for you")
    print("Drink my magic potion")
    height += 1
print("Thanks for coming")

# when typing any number under 60, it'll continue to list up until 60. 
# if over 60 in, will just say thanks for coming

height = int(input("What is your height in inches? "))
while height < 60:
    print(f"Sorry you are currently {height} + this ride is not for you")
    print("Drink my magic potion")
    if height == 58:
        break
    height += 1
print("Thanks for coming")
# will state 55 to 58. break will cause stop after 58

# while true statments will imply running forever
while True:
    response = input("What do you want to do? Say hi [h], goodbye [g], or quit [q]? ")
    if response.lower() == "h":
        print("Hello!")
    elif response.lower() == 'g':
        print("Goodbye")
    elif response.lower() == 'q':
        break 
    else: 
        print("invalid option") 


