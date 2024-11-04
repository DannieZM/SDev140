
#Ititalize
the_sum = 0
count = 0

#while loop that reads user input
while True:
        number = input("Enter a number or press Enter to quit: ")
        #leaves loop
        if number == "":
            break

        the_sum += float(number)
        count += 1

#outputs the user's input
print("The sum is:", the_sum)
if count > 0:
        print("The average is", the_sum/count)