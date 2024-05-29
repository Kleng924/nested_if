# Question 1 Task 1

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

# Question 1 Task 2

if place == "cave":
    action = input("light a torch or proceed in the dard?")
    if action == "light a torch":
        print("You found a treasure!")
    if action == "proceed in the dark":
        print("You fall in a pit!")

# Question 1 Task 3

if place == "cave":
    pass

print("You find the hidden treasure!")
