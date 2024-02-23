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

# Ask user for integer and loop until they
# enter an integer that is more than zero 
def int_check(question, low):


    error = f"Please enter an integer that is more than zero or equal to {low}\n"
    while True:

        try:
            # ask the uesr for an integer   
            response = int(input(question))

            # check that the integer is more than zero   
            if response >= low:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

# Main Routine Goes Here
for item in range(0, 2):
    integer = int_check("Integer: ", 0)
    print(integer)

print()

for item in range(0, 2):
    width = num_check("width: ")  
    print(width)

print()

for item in range(0, 3):
    height = num_check("height: ")  
    print(height)