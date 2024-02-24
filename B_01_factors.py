# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("Instrucitons", "-")


    print('''
To use this program simply enter an integer between
1 and 200. the program will show the factors of your chosen integer.

It will also tell you if your chosen number...
- is a prime number (ie: it has two factors)
- is a perfect square

To exit the program, please type "xxx".
    ''')



# Ask user for an integer between 1 and 200.
def num_check(question):
    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:
        response = input(question).lower()  # Convert input to lowercase

        if response == "xxx":
            return response

        try:
            response = int(response)  # Convert input to integer

            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine Goes Here


statement_generator("The Ultimate Factor Finder", "-")

# Display instruction if requested
want_instructions = input("Press <enter> to read the intructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break