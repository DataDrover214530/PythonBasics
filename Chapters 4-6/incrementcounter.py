# Counting program which lets the user enter a start,
# end and increment number for the count. 


print("** Welcome to the counting program. **\n \
*******************************************\n")

start = int(input("\nWhere shall we start? "))
end = int(input("\nWhere shall we end? "))
increment = int(input("\nWhat increment shall we use? "))

for i in range(start, end, increment):
    print (i, end=" ")


#hold window for user input
input("\n\nPress the enter key to exit.")
