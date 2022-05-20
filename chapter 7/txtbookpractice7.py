sandwiches = ['pastrami', 'tuna', 'veggie', 'pastrami','philly cheese', 'chicken', 'pastrami']
finished_sandies = []
 
for sandwich in sandwiches:
    if sandwich == 'pastrami':
        print("Sorry, we are out of pastrami")
        continue
    print("I made your " + sandwich + " sandwich.")
    finished_sandies.append(sandwich)
    if sandwich == 'pastrami':
        continue

print("List of completed sandwiches: ")
for finished in finished_sandies:
    print(finished)

print("\n\n")

# Dream Vacation
vacation = "If you could visit one place in the world, where would you go?" 
vacation += " To exit, type quit: " 
response = "" # why does this stop the infinite loop? bc it's 'no output'
while response != 'quit':
    response = input(vacation)
    if response != 'quit':
        print("I would love to visit the " + response + "!") # list all the conditions before you print
        

