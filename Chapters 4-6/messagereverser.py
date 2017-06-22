# Counting program which lets the user enter a start,
# end and increment number for the count. 


print("** Welcome to the message reverser. **\n \
*******************************************\n")

message = input("\nPlease type a message: ")

print ("Your message in reverse is:", end=" ")

i = len(message) -1 
for letter in message:
    print (message[i], end="")
    i -=1


#hold window for user input
input("\n\nPress the enter key to exit.")
