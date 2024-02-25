def print_statement(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

def instructions():
    print_statement("The Ultimate Conversion Calculator", "_")
    print("""1. Select the conversion category.
2. Enter a number.
3. Enter its SI unit.
4. Enter the SI unit that you want to convert it to.""")

def get_input(question, units):
    while True:
        response = input(question).lower()
        if response in units:
            print("Unit found!")
            return response
        else:
            print(f"Error: unit type not found in the {category} category.\n")

def unit_convert(amount, si_old, si_new):
    standard = amount * si_new[1]
    result = standard / si_old[1]
    return result

categories = {
    "distance": {
        "mm": ["millimetres", 1000],
        "cm": ["centimetres", 100],
        "m": ["metres", 1],
        "km": ["kilometres", 0.001]
    },
    "mass": {
        "mg": ["milligrams", 1000],
        "g": ["grams", 1],
        "kg": ["kilograms", 0.001],
        "t": ["tonnes", 0.000001]
    },
    "time": {
        "ms": ["milliseconds", 60000],
        "s": ["seconds", 60],
        "min": ["minutes", 1],
        "h": ["hours", 0.01666666666666666666666666666667]
    },
    "volume": {
        "ml": ["millilitres", 1000],
        "l": ["litres", 1],
        "kl": ["kilolitres", 0.001],
        "Ml": ["megalitres", 0.000001]
    }
}

want_instructions = input("Press <enter> to read the instructions or any key to continue ")
if want_instructions == "":
    instructions()

while True:
    print("---")
    category = input("Select category: Distance, Mass, Time, or Volume:\n(Press 'xxx' to quit) ").lower()
    if category == "xxx":
        print("Bye bye :D")
        break
    elif category in categories:
        number = float(input("Enter number: "))
        unit_old = get_input("What unit is it in? ", categories[category])
        unit_new = get_input("Convert to? ", categories[category])
        convert = unit_convert(number, categories[category][unit_old], categories[category][unit_new])
        print(f"{number} {unit_old} is {convert} {unit_new}")
    else:
        print("Error: category not recognised.")
