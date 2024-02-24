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



def factor(var_to_factor):
    all_factors = []

    for item in range(1, (to_factor+1)): #range is from 1 to to_factor
        factor_pair = to_factor // item #get the number that pairs with a factor (item)
        is_factor = to_factor % item #get remainder

        if is_factor == 0: #if no remainders, then is factor
            if item not in all_factors: #checks if factor and its pair exist in the list already
                all_factors.append(item)
            if factor_pair not in all_factors:
                all_factors.append(factor_pair)
            all_factors.sort()  # sort from smallest to biggest
                #print(f"{item} and {factor_pair} are factors of {to_factor}!")

    return all_factors

# Main Routine Goes Here


statement_generator("The Ultimate Factor Finder", "-")

# Display instruction if requested
want_instructions = input("Press <enter> to read the intructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    # ask user for number to be factorised
    to_factor = num_check("\nEnter an integer (or xxx to quit): ")

    if to_factor == "xxx":
        break

    # get factors for integers that are 2 or more
    elif to_factor != 1:
        all_factors = factor(to_factor)
    
    # Set up comment for unity
    else:
        all_factors = ""
        comment = "One is UNITY! It only has one factor. Itself :)"
    
    # comments for squares /  primes
    
    # Prime numbers have only two factors
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number"
    
    # check if the list has an odd nunber of factors
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    # Set up headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."
    # output factors and comment
    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("Thank you for using the factors calculator")