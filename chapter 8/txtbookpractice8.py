def say_hello(name, age):
    print(f"Hello {name}, you are {age} years old")

def say_goodbye():
    print("Goodbye")

def greet_back(feeling):
    if feeling == "good":
        print("Awesome! I feel good too!")
    elif feeling == "bad":
        print("I'm so sorry")
    elif feeling == "stressed":
        print("Coding can be hard to learn")
    else:
        print("well, have a good day!")
while True:
    response =  input("What do you want to do? Say hello [h], say goodbye [g], talk to me [t], or quit [q]")
    if response.lower() == 'q':
        say_goodbye()
        break
    elif response.lower() == 'h':
        name =  input("What is your name? ")
        age = input("What is your age? ")
        say_hello(name, age)
    elif response.lower() == 'g':
        say_goodbye()
    # elif response.lower == 't':
      #   feeling == input("How are you today?")
       # greet_back(feeling) 
    #else:
     #   print("Invalid input") 

