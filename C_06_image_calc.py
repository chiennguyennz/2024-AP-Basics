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

# calculates how many bits are needed to represent an integer
def image_calc():
    # Get the image dimensions
    width = int_check("width: ", 1)  
    height = int_check("height: ", 1)

    # calculate the nunber of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set up answer and return it
    answer = (f"\nNumber of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# Main routine goes here
image_ans = image_calc()
print(image_ans)