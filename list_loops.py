songs = ["ROCKSTAR", "Do It", "For The Night"]
# will print Do It and For The Night
print(songs[1:3])
# update the last element
songs[2] = "Gods Plan"
# print the list
print(songs)
# adds a list to end of a list
songs.extend(["Top Off", "Greece", "Catch the Sun"])
print(songs)
songs.remove("Do It")
print(songs)

"""
1. Create another list called animals and fill it with 3 animal strings of your choice such as "Cat", "Dog", and "Bird"
2. Add another animal to your list
3. print out the 3rd animal in the list
4. Delete the first animal in the list
5. Use a loop to print out all the animals in your animals list
"""
animals = ["Lion", "Snake", "Cat"]
animals.append("Tiger")
print(animals)
print(animals[2])
animals.remove("Lion")
print(animals)
for count in range(0, len(animals)):
print(animals[count])



