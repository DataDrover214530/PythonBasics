# Progam which calculates what tip you should leave based on the price
# of the meal that you enter. Gives both 15% and 20%

print("** Welcome to the tip calculator program. **\n \
*******************************************\n")
mealPrice = float(input("What did your bill for the meal com to come to?: "))

print("\nIf you want to tip 15% then leave", mealPrice * 0.15, "for your waitstaff")
print("\nIf you want to tip 20% then leave", mealPrice * 0.20, "for your waitstaff")

input("\n\nPress the enter key to exit.")

