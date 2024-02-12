# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the uesr for a nunber   
            response = float(input(question))

            # check that the number is more than zero   
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

# Main Routine starts here...
keep_going = ""
while keep_going == "":


    # Get width and height
     width = num_check("width: ")
     height = num_check("height: ")

    # Calculate area / perimeter
     area = (width * height)
     perimeter = (width * 2 + height * 2)
    
    # Output the area and perimeter
     print()
     print("Your area is", area, "cm\nYour perimeter is", perimeter, "cm")

    # Ask userif they want to keep going
     keep_going = input("Press enter to keep going or any key to quit? ")
     print()

print("thank you for using the area / perimeter calculator. ")