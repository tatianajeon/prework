# 3-1 to 3-3
friends = ["sophia", "jennifer", "alyssia", "jae"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

print("Are you free for brunch, " + friends[0].title() + "?")
print("Are you free for brunch, " + friends[1].title() + "?")
print("Are you free for brunch, " + friends[2].title() + "?")
print("Are you free for brunch, " + friends[3].title() + "?")

cars = ["Subaru", "Toyota", "Lexus", "Fiat"]
print(cars)
print("\nI would love for my next car to be a " + cars[0] + ".")

# 3-4 to 3-7
guests = ["Caitlyn", "Jenna", "Sydney", "Joyce"]
print("We would like to invite " + guests[0] + " to dinner at the Jeon's")
print("We would like to invite " + guests[1] + " to dinner at the Jeon's")
print("We would like to invite " + guests[2] + " to dinner at the Jeon's")
print("We would like to invite " + guests[3] + " to dinner at the Jeon's")

cancelled = guests.pop(2)
print("\nWe're sorry to hear that " + cancelled + " is unable to make it.")
guests.append("Jennifer")
print("Our new guest list will include the following:")
print(guests)
print("\nWe have expanded our guest lists due to increased seating availability!")
guests.insert(0, "Lauren")
guests.insert(3, "Sophia")
guests.append("Riley")
print("\nOur new list includes the following guests:")
print(guests)
for guest in guests:
    print("Please join us, " + guest.title() +", for dinner and desserts on Tuesday night!")
print("We can't wait to see you!")
print(guests)
print("\nWe can only invite two people now because the table won't come on time")
print("I'm so sorry, " + guests.pop(0) + ", we will have to postpone.")
print("I'm so sorry, " + guests.pop(1) + ", we will have to postpone.")
print("I'm so sorry, " + guests.pop(2) + ", we will have to postpone.")
print("I'm so sorry, " + guests.pop(3) + ", we will have to postpone.")
for index, guest in enumerate(guests):
    print(f'index: {index}. guest: {guest}.')


# 3-8 to 3-10
surfing_locations = ["Maui", "Australia", "Costa Rica", "Oahu", "French Polynesia"]
print("\n\n\nI would love to visit these locations to surf")
print(surfing_locations)
print(sorted(surfing_locations))
print(surfing_locations)
print(sorted(surfing_locations, reverse = True))
print(surfing_locations)
surfing_locations.reverse()
print(surfing_locations)
surfing_locations.reverse()
print(surfing_locations)
surfing_locations.sort()
print(surfing_locations)
surfing_locations.sort(reverse = True)
print(surfing_locations)

print(len(guests))

