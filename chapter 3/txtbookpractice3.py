guests = ["jamie", "jonathan", "jessica"]
print(guests)
print("We would like to invite " + guests[0] + " to our semiformal")
print("We would like to invite " + guests[1] + " to our semiformal")
print("We would like to invite " + guests[2] + " to our semiformal")

flowers = ["daisies", "sunflowers", "lilies", "tulips", "craspedia"]
flowers.append("peonies")
print(flowers)
flowers[1] = "rannunculas"
print(flowers)
flowers.insert(3, "roses")
print(flowers)
del flowers[2]
print(flowers)
flowers[2] = "pansies"
print(flowers)
flowers.insert(0, "bell flowers")
print(flowers)
reorder = flowers.pop()
print("I would like to reorder " + reorder)
restock = flowers.pop(-1)
print("I would like a restock on " + restock)
cancel = "bell flowers"
cancel_order = flowers.remove("bell flowers")
print("I would like to discontinue my order of " + cancel)
print("I have yet to order these remaining flowers: " + "\nflowers left to order: ") 
print(flowers)
flowers.sort()
print(flowers)
flowers.reverse()
print(flowers)
len(flowers)




#3-8 Five Places to Visit
islands = ["Maui", "Kauai", "Oahu", "Hawaii", "Molokai", "Lanai"]
print(islands)
print(sorted(islands))
print(islands)
print(sorted(islands, reverse = True))
print(islands)
islands.reverse()
print(islands)
islands.reverse()
print(islands)
islands.sort()
print(islands)
islands.sort(reverse=True)
print(islands)








surfboards = ["jimmy lewis", "wavestorm", "torq", "kazuma"]
print(surfboards)
print(sorted(surfboards))
print(surfboards)
print(sorted(surfboards,reverse = True))
print(surfboards)
surfboards.reverse()
print(surfboards)
surfboards.reverse()
print(surfboards)
surfboards.sort()
print(surfboards)
surfboards.sort(reverse = True)
print(surfboards)
print(len(surfboards))
surfboards.append("almond")
print(surfboards)
surfboards.insert(1, "channel islands")
print(surfboards)
surfboards[3] = "lost"
print(surfboards)
del surfboards[1]
print(surfboards)
pulled_from_inventory = surfboards.pop(2)
print("We've officially pulled " + pulled_from_inventory + " from our shelves")
print(surfboards)
print(len(surfboards))
print(surfboards[-1])

