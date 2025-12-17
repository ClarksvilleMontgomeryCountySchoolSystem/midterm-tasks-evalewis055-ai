
inital_slices = party_pizza_mini + large + medium
print(f" Total number of slices: 42")

people += 1
share = inital_slices // people
leftover = inital_slices % people
print(f"Each person gets: 4")
print(f"Leftover slices: 0")

people += 2 #Eric and Brandon are coming too.
New_share = inital_slices // people
New_leftover = inital_slices % people
print(f"Each person gets: 3")
print(f"Leftover slices: 1")

#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

total_slices = party_pizza_mini + party_pizza_mini + large + medium
Newest_share = total_slices // people
Newest_leftover = total_slices % people
print(f"Each person gets:4")
print(f" Left over slices: 6")
print("...for Mr. Hollow Leg")
