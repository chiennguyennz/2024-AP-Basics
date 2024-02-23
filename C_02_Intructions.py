# Generates headings (eg: ---- Heading ----) 2 usages
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("Instrucitons", "-")


    print('''
Instruction go here.
- instruction 1
- instruction 2
- etc
    ''')

# Main routine goes here
    
# Display instruction if requested
want_instructions = input("Press <enter> to read the intructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")