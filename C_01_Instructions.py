# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for element in valid_ans:
            # check if the user response is a word in the list
            if element == user_response:
                return element

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == element[0]:
                return element

        # print error if user does not enter something that is valid
        print(error)
        print()


# Displays instructions
def instruction():
    print('''

    **** Instructions ****

To begin, select the topic of the quiz.

The topics include:

- History
- Geography
- Science
- Literature
- Sports
- Entertainment
- Art & Music
- Technology
- Food & Drink

Then, you will be asked a question about that topic. Beneath the question will be a set of answers.
To select your answer enter the corresponding letter.


Good luck!

    ''')


yes_no = ['yes', 'no']

# ask user if they want to see the instructions and display
# them if needed
want_instructions = string_checker("Do you want to read the instructions? It is recommended, as it contains the topic "
                                   "list? ", yes_no)

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()
