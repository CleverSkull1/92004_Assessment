# functions

def make_statement(statement, decoration):
    """Adds additional characters to the start and end of headings as decoration"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")


def string_checker(question, valid_ans=('yes', 'no')):
    """Check that users have entered a valid response"""
    error = f"Please enter one of the following: " \
            f"{valid_ans}"

    while True:
        # get user response and make sure its lower case
        user_response = input(question).lower()

        for item in valid_ans:

            # check if the user response is a word in the list
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

            # print error if user enters invalid
        print(error)
        print()


def instructions():
    """Prints instructions"""

    make_statement("Instructions", "*")
    print("""
Rock > Scissors
Scissors > Paper
Paper > Rock
    """)


#  Main routine
print("\n📈📈📈 Higher or Lower 📉📉📉\n")

want_instructions = string_checker("Would you like to view the instructions? ").lower()

# Display the instructions if the user wants to see them.
if want_instructions == "yes":
    instructions()

print()
print("Program continues")
