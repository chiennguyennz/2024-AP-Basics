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
    width = int_check("width: ", 1)  
    print(width)

print()

for item in range(0, 3):
    height = int_check("height: ", 1)  
    print(height)
