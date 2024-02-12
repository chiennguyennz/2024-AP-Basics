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

# Main Routine Goes Here
for item in range(0, 2):
    width = num_check("width: ")  
    print(width)

print()

for item in range(0, 3):
    height = num_check("height: ")  
    print(height)