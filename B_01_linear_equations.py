import random


# functions

def make_statement(statement, decoration, amount):
    """Adds additional characters to the start and end of headings as decoration"""
    print(f"\n{decoration * amount} {statement} {decoration * amount}")


def int_check(question, low=None, high=None, exit_code=None):
    """Checks users enter an integer more than or equal to 1"""

    if low is None and high is None:
        error = "Please enter an integer\n"
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}\n")
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")
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


def string_checker(question, valid_ans=('yes', 'no')):
    """Check that users have entered a valid option based on a list"""
    error = f"Please enter one of the following: " \
            f"{valid_ans}"

    while True:
        # get user response and make sure its lower case
        user_response = input(question).lower()

        for ans in valid_ans:

            # check if the user response is a word in the list
            if ans == user_response:
                return ans

            elif user_response == ans[0]:
                return ans

            # print error if user enters invalid
        print(error)
        print()


def instructions():
    """Prints instructions"""

    make_statement("Instructions", "*", 3)
    print("""
[placeholder]
   """)


# get game parameters
gamemode = "regular"
rounds_played = 0
questions_right = 0
questions_wrong = 0
equation_variables = ["a", "b", "c", "x", "y"]
operations = ["+", "-", "*", "/"]
quiz_history = []
statistics = []

# main routine

# print a heading and ask for instructions
make_statement("Linear Equations Quiz", "❓", 3)
want_instructions = string_checker("Would you like to view the instructions? ").lower()

# Display the instructions if the user wants to see them.
if want_instructions == "yes":
    instructions()

# ask the user for the amount of rounds they would like to play, infinite is an option
rounds = int_check("\nHow many questions would you like? (Press <enter> for infinite) ", low=1, exit_code="")
if rounds == "":
    gamemode = "infinite"
    rounds = 1

# ask the user for the difficulty they would like to play
difficulty = int_check("\nDifficulty? (1-3) ", low=1, high=3)

# quiz loop begins
while rounds_played < rounds:
    # print heading
    make_statement(f"Question {rounds_played + 1}", "*", 3)
    print()

    # choose a variable to be used in the equation from the {equation_variables} list
    question_variable = (random.choice(equation_variables))

    # generate the operation to be used for the equations
    random_operation = random.choice(operations)

    if random_operation != "/":
        # generate the random value and value of x
        numerical_value = random.randint(0, (10 * difficulty))
        x_value = random.randint(numerical_value, (20 * difficulty))
    else:
        # and make sure division doesn't have a decimal
        numerical_value = random.randint(1, (10 * difficulty))  # to ensure no division by zero
        result = random.randint(1, (20 * difficulty))  # expected answer
        x_value = result * numerical_value  # to ensure integer division

    # to ensure that it's not multiplying x by 0 as x could be any number from 0 to 20
    while random_operation == "*" and x_value == 0:
        x_value = random.randint(numerical_value, (20 * difficulty))

    # generate the expression to get the correct answer
    expression = f"{x_value} {random_operation} {numerical_value}"

    # solve the expression and record the answer, then convert the answer to integer in case of division
    result = eval(expression)
    result = int(result)

    # generate the equation
    equation = (f"{question_variable} {random_operation} {numerical_value} = {result}\n"
                f"Solve for {question_variable}: ")

    # ask the user the equation
    user_answer = int_check(equation, low=None, high=None, exit_code="xxx")

    # if user enters the error code
    if user_answer == "xxx":
        break
    # checks if the user got it correct and prints as appropriate
    elif int(user_answer) == round(int(x_value), 1):
        make_statement("Correct!", "👍", 2)
        quiz_history.append(f"Question {rounds_played + 1}\n\n{equation}\nYour answer: "
                            f"{user_answer}\nCorrect answer: {x_value}\n")
        statistics.append(1)
        questions_right += 1
    else:
        make_statement("Incorrect!", "👎", 2)
        quiz_history.append(f"Question {rounds_played + 1}\n\n{equation}\nYour answer: "
                            f"{user_answer}\nCorrect answer: {x_value}\n")
        statistics.append(0)
        questions_wrong += 1

    # update variables in between rounds
    if gamemode == "infinite":
        rounds += 1
    rounds_played += 1

# stats and history
if rounds_played > 0:
    # calculates the percentage of correct answers
    percentage = (sum(statistics) / len(statistics)) * 100
    percentage = round(percentage)
    # outputs statistics / results
    print()
    make_statement("Statistics", "📊", 3)
    print(f"Correct: {questions_right}  | Incorrect: {questions_wrong}  | Percentage: {percentage}%\n")
    # optionally outputs game history
    see_history = string_checker("Would you like to see your game history? ")
    if see_history == "yes":
        print()
        for item in quiz_history:
            print(item)
