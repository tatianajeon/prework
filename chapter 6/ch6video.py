# dictionary is a collection of key-value pairs

steve = {
    'name' : 'Steve',
    'weight' : 155.5,
    'height' : 70, 
    'foods' : ['country fried steak', 'fried chicken', 'collard greens'],
    'ice cream': {
        'vanilla' : False,
        'chocolate' : True,
        'coffee' : False
    },
    10 : 'this has an integer key'
    }
print(steve['name'])
print(type(steve['name'][1]))
print("\n\n")
print(steve[10])
print(type(steve[10])) # "this has an integer key"
print(steve['ice cream']) # lists the ice cream dictionary
print(steve['ice cream']['vanilla']) # boolean, produces "false"
print(steve.get('candies')) # returns "none" because you don't have candies
print(steve.get('name')) # returns "Steve"
print(steve.get('candies', 'no candy list')) # returns "no candy list" 
steve['name'] = 'Stephen'
print(steve) # prints the whole list but instead it says "Stephen"
my_list = [1, 2, 3]
my_list[1] = "wow"
print(my_list) #just replaced the index 1 (so #2) to "wow"
steve.update(
    {
        'candies': ['snickers', 'mars', 'm&ms']
    }
)
print("\n\n")
print(steve)

del steve['candies']
print(steve)
print("\n\n")
print(steve.keys())
 

print(steve.values())
for value in steve.values():
    print(value)
    print(type(value)) 

print(steve.items())
for tup in steve.items():
    print(tup)
# prints as a tuple
# 'name', 'Stephen')
#('weight', 155.5)
# ('height', 70)
# ('foods', ['country fried steak', 'fried chicken', 'collard greens'])
# ('ice cream', {'vanilla': False, 'chocolate': True, 'coffee': False})
# (10, 'this has an integer key')

print(steve.items())
for key,value in steve.items():
    print(key)
    print(value)
# name
# Stephen
#weight
# 155.5
# height
# 70
# foods
# ['country fried steak', 'fried chicken', 'collard greens']
# ice cream
# {'vanilla': False, 'chocolate': True, 'coffee': False}
# 10
# this has an integer key

# or you can print it together

print(steve.items())
for key,value in steve.items():
    print(key, end = " ") 
    print(value)
# name Stephen
# weight 155.5
# height 70
# foods ['country fried steak', 'fried chicken', 'collard greens']
# ice cream {'vanilla': False, 'chocolate': True, 'coffee': False}
# 10 this has an integer key

print(steve.items())
for key, value in steve.items():
    if isinstance(value,list): # if there's a list in a value
        print(f"\n\nthe list is at {key}") # locate the key in which the list is in the value
# "the list is at foods"
