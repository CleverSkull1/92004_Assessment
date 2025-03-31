# functions

def int_check(question, low=None, high=None, exit_code=None):
    """Checks users enter an integer more than or equal to 1"""

    if low is None and high is None:
        error = "Please enter an integer"
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")
    else:
        error = (f"Please enter an integer that"
                 f"is between {low} and {high} (inclusive)")
    while True:
        response = input(question).lower()

        if response == exit_code:
            return response
        try:
            response = int(response)
            if low is not None and response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# main routine

# rounds = "test"
# while rounds != "":
#     rounds = int_check("Rounds <enter for infinite>: ", low=1, exit_code="")
#     print(f"You asked for {rounds}")

# low_num = int_check("Low Number? ")
# print(f"You chose a low number of {low_num}")

# high_num = int_check("High Number? ")
# print(f"You chose a high number of {high_num}")


# check user guesses
guess = ""
while guess != "xxx":
    guess = int_check("Guess: ", low=0, high=10, exit_code="xxx")
    print(f"You guessed {guess}\n")


