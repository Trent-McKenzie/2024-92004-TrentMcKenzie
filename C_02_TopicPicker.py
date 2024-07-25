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


# Ask user for number of rounds / infinite mode
topic = int_check("What topic would you like? ")
