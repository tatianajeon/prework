alien_0 = {'x_position': 0, 'y_position': 25, 'speed':'medium'}
print('original x-position:' + str(alien_0['x_position']))
print('move to right: ' + str(alien_0['y_position']))
print('current speed: ' + str(alien_0['speed']))
print("\n")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed']== 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x-position: " + str(alien_0['x_position'])) # new x-position: 2
print('original position: ' + str(alien_0['x_position'])) # original position: 2

print("\n\n")
favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python', 
}
print("Sarah's favorite language is " + favorite_language['sarah'].title() + ".")

print('\n\n"Try it yourself 6-1, 2, 3"')
Gregory = {
    'name' : 'Gregory',
    'age' : 30,
    'birthday' : 'August 29, 1991', 
    'city' : 'Nashville',
    'occupation' : 'Family Medicine',
}
print(Gregory)
print("Introducing " + Gregory['name'])
print("\nBorn on " + Gregory['birthday'] + ", Gregory is " + str(Gregory['age']) + " years old.")
print("Gregory lives in " + Gregory['city'] + ", where he practices " + Gregory['occupation'] + ".")
# Born on August 29, 1991, Gregory is 30 years old.
# Gregory lives in Nashville, where he practices Family Medicine.
# don't forget to make the interval (age) a string

favorite_numbers = {
    'Janet' : 6,
    'Lucy' : 8,
    'Jeremy' : 19,
    'George' : 7,
}
print("\nFavorite Numbers: ")
print("Janet's favorite number is " + str(favorite_numbers['Janet']) + ".")
print("Lucy's favorite number is " + str(favorite_numbers['Lucy']) + ".")
print ("Jeremy's favorite number is " + str(favorite_numbers['Jeremy']) + ".")
print("George's favorite number is " + str(favorite_numbers['George']) + ".")


glossary = {
    'braces' : 'used for dictionary lists',
    'string' : 'a set of non variable data, absent of a function',
    'int' : 'numbers that are calculatable, has function, is not a string',
    'boolean' : 'used to provide simple  yes and nos, true and falses',
    'range' : 'a set of numbers that can be looped',
}

print("\nThis is what I've learned in Coding Temple so far:")
print("Braces: " + glossary['braces'] + ".")
print("Strings: " + glossary['string'] + ".")
print("Int: " + glossary['int'] + ".")
print("Boolean: " + glossary['boolean'] + ".")
print("Range: " + glossary['range'] + ".")

print('\n\n')
user_0 = {
'username': 'efermi',
              'first': 'enrico',
              'last': 'fermi',
              }
for key, value in user_0.items():
    print("\nkey: " + key)
    print("value: " + value)
# key: username
# value: efermi
# key: first
# nvalue: enrico
# key: last
# value: fermi

print(favorite_language)
for key, value in favorite_language.items():
    print(key.title() + "'s favoriate language is " + value + ".") 

message_friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())
    if name in message_friends:
        print("Hi " + name.title() +
        ", I see your favorite language is " + 
        favorite_language[name].title() + "!")
# why favorite_language[name]

message_friends = ['phil', 'sarah']
for name in favorite_language.keys():
    if name in message_friends:
        print("\nHi " + name.title() + ", I see your favorite language is " + favorite_language[name].title() + "!")

if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_language.keys()):
    print(name.title() + ", thank you for taking the poll.")
# alphabetical order
for value in sorted(favorite_language):
    print("Most loved languages: " + favorite_language[value].title())

print("The following languages have been mentioned:")
for language in set(favorite_language.values()):
    print(language.title())


# try it yourself
print("\n\nTry it Yourself 6-4, 5, 6")
print("\n")


for key,value in glossary.items():
        print("\nWords: " + "\n" + key)
        print ("\nDefinitions: " + "\n" + value)
# for word, definition in glossary.items():
    # print(f"\n{word.title()}: {definition}")

glossary['mkdir'] = 'make a new directory'
glossary['reverse'] = 'reverse the order of a list'
glossary['sorted'] = 'temporarily sort the list in alphabetical order'
glossary['type'] = 'identifies the type content'
glossary['rstrip()'] = 'strips the empty white space and condenses text'

print(glossary)
print("\n\n")
for word, definition in glossary.items():
    print(word.title() + ": " + definition + ".")
    

rivers = {
    'colorado' : 'USA',
    'nile' : 'egypt',
    'columbian' : 'canada',
}

print(rivers.values())
print(rivers.keys())

for river,country in rivers.items():
    print("\nThe " + river.title() + " river runs through " + country.title() + ".")

aliens = []
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points': 5, 'speed' : 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
           'first': 'marie',
           'last': 'curie',
           'location': 'paris',
           },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# Username: aeinstein
       # Full name: Albert Einstein
       # Location: Princeton

# Username: mcurie
       # Full name: Marie Curie
       # Location: Paris

print("\n\nTry It Yourself 6-7")
classmates = {
    'Paul': {
        'class' : 'social studies',
        'locker' : 307,
        'bus' : 27,
    },
    'Sammie' : {
        'class' : 'Biology',
        'locker' : 28,
        'bus' : 65,
    },
    'Kaleigh' : {
        'class' : 'European History',
        'locker' : 62,
        'bus' : 1,
    },
    'Ali' : {
        'class' : 'US History',
        'locker' : 99,
        'bus' : 3,
    } ,
    'Kazuki' : {
        'class' : 'Art History',
        'locker' : 44,
        'bus' : 12,
    }
    }

for person, info in classmates.items():
    print("\nName: " + person)
    classmate = info['class']
    locker = info['locker']
    bus = info['bus']

    print("\tMet in " + classmate + ", locker number " + str(locker)
    + ", and bus number " + str(bus) + ".") 


childhood_friends = {
    'Sharon' : {
        'last name' : 'Liu',
        'city' : 'Kendall Park',
        'school' : 'South Brunswick Middle School',
    },
    'Autumn' : {
        'last name' : 'Yun',
        'city' : 'South Brunswick',
        'school' : 'SBHS',
    },
    'Gina' : {
        'last name' : 'Kang',
        'city' : 'Duluth',
        'school' : 'Andrews University',
    },
    'Victoria' : {
        'last name' : 'Chung',
        'city' : 'Loma Linda',
        'school' : 'LLU'},
}

for friend, info1 in childhood_friends.items():
    last_name = info1['last name']
    city = info1['city']
    school = info1['school']
    print("I met " + friend + " " + last_name + " at " +
    school + " in " + city + ".")


pets = {
    'Momo' : {
        'owner' : 'Scarlet',
        'type' : "Pomoranian",},
    'Molly' : {
        'owner' : 'Kaitlyn',
        'type' : 'Maltipoo'},
    'Zeebo' : {
        'owner' : 'Jeremy',
        'type' : 'Cattle herd breed',}
    }
print(pets)
print("\n\nThere are so many friendly dogs in Loma Linda. ")
for dog, info2 in pets.items():
    owner = info2['owner']
    breed = info2['type']
    print("\tThere's", dog, "who is a", breed,"and is owned by", owner, ".")
