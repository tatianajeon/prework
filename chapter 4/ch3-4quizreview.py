my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
for index in range(3):
    print(my_list[index], end = "  ") # chicken wing  chicken wing  hot dog  
# the range opperates in that it stops at the individual number, 
# or starts at the first number and stops at the second number


# my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
# my_string = " "
# for index in range(len(my_list)):
#     if index == 6:
#         my_string += "chillin"
#     my_string[index] = "chicken wing"
# print(my_string)
# ** this would be an error because: 
# my_string is not a set of numbers, it's a string. you can't have index for string


my_list = [1, 3.0, ['a', 'b', ['A', 'B', 'C'], 'd'], 'John']
for member in my_list:
    if isinstance(member, list):
        for m in member:
            if isinstance(m, list):
                print(m, end=". ") # ['A', 'B', 'C']
# so, for every isinstance you narrow down a list. 
# by the time you print, you're printing the 
# list inside a list inside a list


my_list = [1, 3.0, ['a', 'b', ['A', 'B', 'C'], 'd'], 'John']
print(my_list[2]) # ['a', 'b', ['A', 'B', 'C'], 'd']
print(my_list[2][2]) # ['A', 'B', 'C']
print(my_list[2][2][0]) # A 
# is this another way to say isinstance?


my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
for food in my_list:
    if food == "chicken wing":
        break
    print(food, end= " ") # no output
# "none" vs "no output"?
# no output is like, just a space. 


