# Ask the user for the width and height
# (assume they put in valid data)
width = (int(input("What is your width? ")))
height = (int(input("What is your height? ")))

# calculate the area / perimeter
area = (width * height)

perimeter = (width * 2 + height * 2)

# Output the area and perimeter
print("Your area is", area, "cm\nYour perimeter is", perimeter, "cm")
