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


def int_checker(question, valid_ans):
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


# checks for an available topic
def int_check(question):
    while True:

        error = "Please enter a topic from the instruction list."

        to_check = input(question)

        # check for history topic
        if to_check == "history":
            return "History"

        # check for history topic
        if to_check == "History":
            return "History"

        # check for geography topic
        if to_check == "geography":
            return "Geography"

        # check for geography topic
        if to_check == "Geography":
            return "Geography"

        # check for science topic
        if to_check == "science":
            return "Science"

        # check for science topic
        if to_check == "Science":
            return "Science"

        # check for literacy topic
        if to_check == "Literature":
            return "Literature"

        # check for literacy topic
        if to_check == "literature":
            return "Literature"

        # check for sports topic
        if to_check == "Sports":
            return "Sports"

        # check for sports topic
        if to_check == "sports":
            return "Sports"

        # check for sports topic
        if to_check == "Entertainment":
            return "Entertainment"

        # check for sports topic
        if to_check == "entertainment":
            return "Entertainment"

        # check for art and music topic
        if to_check == "Art and Music":
            return "Art and Music"

        # check for art and music topic
        if to_check == "art and music":
            return "Art and Music"

        # check for technology topic
        if to_check == "Technology":
            return "Technology"

        # check for technology topic
        if to_check == "technology":
            return "Technology"

        # check for food and drink topic
        if to_check == "Food and Drink":
            return "Food and Drink"

        # check for food and drink topic
        if to_check == "food and drink":
            return "Food and Drink"

        try:
            response = int(to_check)

        except ValueError:
            print(error)


def quiz_result(user, answer):
    if user == answer:
        round_result = "correct"

    # if it's not a win, then it's a loss
    else:
        round_result = "incorrect"

    return round_result


# Ask user for number of rounds / infinite mode
topic = int_check("What topic would you like? ")

rounds_played = 0
rounds_tied = 0
rounds_lost = 0
rounds_won = 0
yes_no = ['yes', 'no']
quiz_list = ["a", "b", "c", "d"]

questions_list = []
answer_list = []
game_history = []

if topic == "History":
    mode = "History"
    num_rounds = 4
    rounds_played = 0

    history_questions = ["Who was the first president of the United States?", "What year did World War 2 end?",
                         "What ancient civilization built the pyramids?", "What year was Napoleon born?\n"]

    history_options = ["\nA: George Washington\nB: Abraham Lincoln\nC: John F. Kennedy\nD: Joe Biden\nEnter Answer: ",
                       "A: 1976\nB: 2001\nC: 1945\nD: 1865\nEnter Answer: ",
                       "A: Greeks\nB: Egyptians\nC: Romans\nD: Australians\nEnter Answer: ",
                       "A: 1784\nB: 1889\nC: 1769\nD: 1901\nEnter Answer: "]

    history_answers = ["a", "c", "b", "c"]

    # Game loop starts here

    # Rounds headings (based on mode)
    if mode == "History":
        while rounds_played < num_rounds:
            print()
            print(f"🧾🧾 Question {rounds_played + 1} of {mode} 🧾🧾🧾")
            print(history_questions[rounds_played])

            # get user choice
            user_choice = string_checker(history_options[rounds_played], quiz_list)

            # Compare input to answer
            result = quiz_result(user_choice, history_answers[rounds_played])

            if result == "correct":
                print("Correct!")
                feedback = "Correct."
                rounds_won += 1

            else:
                print(f"Incorrect. The correct answer was {history_answers[rounds_played]}")
                feedback = f"Incorrect. The correct answer was {history_answers[rounds_played]}."
                rounds_lost += 1

            print(feedback)

            game_history.append(feedback)
            rounds_played += 1

# Statistics Area #

if rounds_played > 0:
    # Calculate Statistics
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    # Output Game Statistics
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"👍 Won: {percent_won:.2f} \t "
          f"😥 Lost: {percent_lost:.2f} \t ")

    # ask user if they want to see their game history and output it if requested.
    see_history = string_checker("\nDo you want to see your game history? ", yes_no)
    if see_history == "yes":
        for item in game_history:
            print(item)
