# Progam which takes the book price of a car and adds on lots of extras. Some
# extras will be a % or the base price (i.e. sales tax etc) and some will be
# fixed chanrges such as anti-rust undercoat etc.

print("** I'll have to ask the boss if he'll let me give you this sweet deal... **\n \
**************************************************\n")
carPrice = float(input("What's the book price of the car? "))

salesTax = carPrice * 0.20
licenseFee = carPrice * 0.07

dealerPrep = 150.00
relocationFee = 250.00
undercoat = 525.00
topSkim = 150


print("\n\nI can sell you this fine automobile for the low low price of", \
      carPrice + salesTax + licenseFee + dealerPrep + relocationFee + undercoat + topSkim, \
      "including all taxes, extras, non-reundable deductables and fees")


input("\n\nPress the enter key to exit.")

