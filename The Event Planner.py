# Question 2 Task 1

attendees = int(input("Enter number of attendees:"))
venue = "large hall" 
print("large hall") if attendees > 100 else print("conference room")

# Question 2 Task 2

attendees = int(input("Enter number of attendees:"))
venue_over_100 = "large hall" 
venue_less_100 = "banquet room"

if attendees >= 100:
    print("large hall")
if attendees <= 100:
    print("banquet room") 
else:
    print("conference room")

# Question 2 Task 3

customer = input("Do you like Vegetarian food?")
yes = "We recommend Veggie Delight Cateres!"
no = "We recommend Gourmet Meals Caterers"
if customer == yes:
    print("We recommend Veggie Delight Cateres!")
elif customer == no:
    print("We recommend Gourmet Meals Caterers")
