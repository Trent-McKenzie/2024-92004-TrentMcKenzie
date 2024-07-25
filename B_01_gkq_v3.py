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


# compares user / computer choice and returns
# result (win / lose / tie)
def quiz_result(user, answer):
    if user == answer:
        round_result = "correct"

    # if it's not a win, then it's a loss
    else:
        round_result = "incorrect"

    return round_result


# Main Routine Starts here

# Initialise game variables
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0
rounds_won = 0
yes_no = ['yes', 'no']
quiz_list = ["a", "b", "c", "d"]

questions_list = []
answer_list = []
game_history = []

print("❓❔❓ Welcome to the General Knowledge Quiz ❓❔❓")
print()

# ask user if they want to see the instructions and display
# them if needed
want_instructions = string_checker("Do you want to read the instructions? It is recommended, as it contains the topic "
                                   "list? ", yes_no)

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
topic = int_check("What topic would you like? ")

# Topic Questions Area #

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

if topic == "Geography":
    mode = "Geography"
    num_rounds = 4
    rounds_played = 0

    geography_questions = ["What is the capital of Australia?", "Which is the largest desert in the world?",
                           "What river runs through Paris?", "In which country is Mount Everest located?"]

    geography_options = ["\nA: Perth\nB: Sydney\nC: Melbourne\nD: Canberra\nEnter Answer: ",
                         "A: Sahara\nB: Antarctica\nC: Arabian\nD: Gobi\nEnter Answer: ",
                         "A: Seine\nB: Thames\nC: Nile\nD: Amazon\nEnter Answer: ",
                         "A: China\nB: Canada\nC: Nepal\nD: New Zealand\nEnter Answer: "]

    geography_answers = ["d", "b", "a", "c"]

    # Game loop starts here

    # Rounds headings (based on mode)
    if mode == "Geography":
        while rounds_played < num_rounds:
            print()
            print(f"🌏🌏🌏 Question {rounds_played + 1} of {mode} 🌏🌏🌏")
            print(geography_questions[rounds_played])

            # get user choice
            user_choice = string_checker(geography_options[rounds_played], quiz_list)

            # Compare input to answer
            result = quiz_result(user_choice, geography_answers[rounds_played])

            if result == "correct":
                print("Correct!")
                feedback = "Correct."
                rounds_won += 1

            else:
                print(f"Incorrect. The correct answer was {geography_answers[rounds_played]}")
                feedback = f"Incorrect. The correct answer was {geography_answers[rounds_played]}."
                rounds_lost += 1

            game_history.append(feedback)
            rounds_played += 1

if topic == "Science":
    mode = "Science"
    num_rounds = 4
    rounds_played = 0

    science_questions = ["What planet is known as the Red Planet?", "Who developed the theory of relativity?",
                         "What is the chemical symbol for gold?", "What part of the cell contains the genetic material?"
                         ]

    science_options = ["\nA: Venus\nB: Mars\nC: Jupiter\nD: Saturn\nEnter Answer: ",
                       "A: Isaac Newton\nB: Robert Oppenheimer\nC: Albert Einstein\nD: Charles Darwin\nEnter Answer: ",
                       "A: Au\nB: G\nC: Go\nD: Si\nEnter Answer:",
                       "A: Mitochondria\nB: Ribosomes\nC: Cell Membrane\nD: Nucleus\nEnter Answer: "]

    science_answers = ["b", "c", "a", "d"]

    # Game loop starts here

    # Rounds headings (based on mode)
    if mode == "Science":
        while rounds_played < num_rounds:
            print()
            print(f"🧪🧪🧪 Question {rounds_played + 1} of {mode} 🧪🧪🧪")
            print(science_questions[rounds_played])

            # get user choice
            user_choice = string_checker(science_options[rounds_played], quiz_list)

            # Compare input to answer
            result = quiz_result(user_choice, science_answers[rounds_played])

            if result == "correct":
                print("Correct!")
                feedback = "Correct."
                rounds_won += 1

            else:
                print(f"Incorrect. The correct answer was {science_answers[rounds_played]}")
                feedback = f"Incorrect. The correct answer was {science_answers[rounds_played]}."
                rounds_lost += 1

            game_history.append(feedback)
            rounds_played += 1

if topic == "Literature":
    mode = "Literature"
    num_rounds = 4
    rounds_played = 0

    literature_questions = ["Who wrote Romeo and Juliet?", "What is the title of the first Harry Potter book?",
                            "Who is the author of To Kill a Mockingbird?",
                            "Which famous novel begins with the line, Call me Ishmael?"]

    literature_options = ["\nA: Charles Dickens\nB: William Shakespeare\nC: Ernest Hemingway\nD: J.K Rowling"
                          "\nEnter Answer: ",
                          "A: Goblet of Fire\nB: Prisoner of Azkaban\nC: Chamber of Secrets\nD:Philosophers Stone"
                          "\nEnter Answer: ",
                          "A: Stephen King\nB: Mark Twain\nC: Harper Lee\nD: Edgar Allen Poe\nEnter Answer: ",
                          "A: Moby Dick\nB: Annabel lee\nC: A Tale of Two Cities\nD: The Great Gatsby\nEnter Answer: "]

    literature_answers = ["b", "d", "c", "a"]

    # Game loop starts here

    # Rounds headings (based on mode)
    if mode == "Literature":
        while rounds_played < num_rounds:
            print()
            print(f"📕📕📕 Question {rounds_played + 1} of {mode} 📕📕📕")
            print(literature_questions[rounds_played])

            # get user choice
            user_choice = string_checker(literature_options[rounds_played], quiz_list)

            # Compare input to answer
            result = quiz_result(user_choice, literature_answers[rounds_played])

            if result == "correct":
                print("Correct!")
                feedback = "Correct."
                rounds_won += 1

            else:
                print(f"Incorrect. The correct answer was {literature_answers[rounds_played]}")
                feedback = f"Incorrect. The correct answer was {literature_answers[rounds_played]}."
                rounds_lost += 1

            game_history.append(feedback)
            rounds_played += 1

if topic == "Sports":
    mode = "Sports"
    num_rounds = 4
    rounds_played = 0

    sports_questions = ["How many players are there in a soccer team?", "In which sport would you perform a slam dunk?",
                        "Who has won the most Grand Slam titles in tennis?",
                        "What country hosted the 2016 Summer Olympics?"]

    sports_options = ["\nA: 13\nB: 11\nC: 14\nD: 12\nEnter Answer: ", "A: Basketball\nB: Hockey\nC: Football\nD:Tennis"
                                                                      "\nEnter Answer: ",
                      "A: Novak Djokovic\nB: Carlos Alcaraz\nC: Rafael Nadal\nD: Daniil Medvedev\nEnter Answer: ",
                      "A: United States\nB: Brazil\nC: China\nD: Australia\nEnter Answer: "]

    sports_answers = ["b", "a", "c", "b"]

    # Game loop starts here

    # Rounds headings (based on mode)
    if mode == "Sports":
        while rounds_played < num_rounds:
            print()
            print(f"🏀⚽🏈 Question {rounds_played + 1} of {mode} 🏀⚽🏈")
            print(sports_questions[rounds_played])

            # get user choice
            user_choice = string_checker(sports_options[rounds_played], quiz_list)

            # Compare input to answer
            result = quiz_result(user_choice, sports_answers[rounds_played])

            if result == "correct":
                print("Correct!")
                feedback = "Correct."
                rounds_won += 1

            else:
                print(f"Incorrect. The correct answer was {sports_answers[rounds_played]}")
                feedback = f"Incorrect. The correct answer was {sports_answers[rounds_played]}."
                rounds_lost += 1

            game_history.append(feedback)
            rounds_played += 1

if topic == "Entertainment":
    mode = "Entertainment"
    num_rounds = 4
    rounds_played = 0

    entertainment_questions = ["Who played the character of Jack Dawson in the movie Titanic?",
                               "What is the highest-grossing film of all time?",
                               "Which animated film features the song Let It Go?",
                               "Who is the creator of the Star Wars franchise?"]

    entertainment_options = ["\nA: Tom Holland\nB: Chris Hemsworth\nC: Cillian Murphy\nD: Leonardo Di Caprio"
                             "\nEnter Answer: ",
                             "A: Avengers: Endgame\nB: Avatar\nC: Titanic\nD: Avatar 2: The Way of Water"
                             "\nEnter Answer: ",
                             "A: Inside Out\nB: Ratatouille\nC: Frozen\nD: Shrek\nEnter Answer: ",
                             "A: James Cameron\nB: Christopher Nolan\nC: George Lucas\nD: Tim Burton\nEnter Answer: "]

    entertainment_answers = ["d", "b", "c", "c"]

    # Game loop starts here

    # Rounds headings (based on mode)
    if mode == "Entertainment":
        while rounds_played < num_rounds:
            print()
            print(f"🎥🎬🎥 Question {rounds_played + 1} of {mode}🎥🎬🎥")
            print(entertainment_questions[rounds_played])

            # get user choice
            user_choice = string_checker(entertainment_options[rounds_played], quiz_list)

            # Compare input to answer
            result = quiz_result(user_choice, entertainment_answers[rounds_played])

            if result == "correct":
                print("Correct!")
                feedback = "Correct."
                rounds_won += 1

            else:
                print(f"Incorrect. The correct answer was {entertainment_answers[rounds_played]}")
                feedback = f"Incorrect. The correct answer was {entertainment_answers[rounds_played]}."
                rounds_lost += 1

            game_history.append(feedback)
            rounds_played += 1

if topic == "Art and Music":
    mode = "Art and Music"
    num_rounds = 4
    rounds_played = 0

    art_and_music_questions = ["Who painted the Mona Lisa?",
                               "What is the name of the iconic music festival held annually in the desert in California"
                               "?", "Who composed the Four Seasons?",
                               "What is the term for a painting done on wet plaster?"]

    art_and_music_options = ["\nA: Leonardo Da Vinci\nB: Vincent Van Gogh\nC: Pablo Picasso\nD: Bob Ross"
                             "\nEnter Answer: ",
                             "A: Glastonbury\nB: Woodstock\nC: Boomtown\nD: Coachella\nEnter Answer: ",
                             "A: Beethoven\nB: Mozart\nC: Antonio Vivaldi\nD: Richard Wagner\nEnter Answer: ",
                             "A: Impressionism\nB: Fresco\nC: Oil Painting\nD: Abstract\nEnter Answer: "]

    art_and_music_answers = ["a", "d", "c", "b"]

    # Game loop starts here

    # Rounds headings (based on mode)
    if mode == "Art and Music":
        while rounds_played < num_rounds:
            print()
            print(f"🎨🎵🎨 Question {rounds_played + 1} of {mode}🎨🎵🎨")
            print(art_and_music_questions[rounds_played])

            # get user choice
            user_choice = string_checker(art_and_music_options[rounds_played], quiz_list)

            # Compare input to answer
            result = quiz_result(user_choice, art_and_music_answers[rounds_played])

            if result == "correct":
                print("Correct!")
                feedback = "Correct."
                rounds_won += 1

            else:
                print(f"Incorrect. The correct answer was {art_and_music_answers[rounds_played]}")
                feedback = f"Incorrect. The correct answer was {art_and_music_answers[rounds_played]}."
                rounds_lost += 1

            game_history.append(feedback)
            rounds_played += 1

if topic == "Technology":
    mode = "Technology"
    num_rounds = 4
    rounds_played = 0

    technology_questions = ["Who is the founder of Microsoft?", "What year was the World Wide Web invented?",
                            "What was the first video game console ever released?",
                            "What is the name of Apple's virtual assistant?"]

    technology_options = ["\nA: Larry Page\nB: Bill Gates\nC: Steve Jobs\nD: Tim Cook\nEnter Answer: ",
                          "A: 1989\nB: 1977\nC: 1993\nD: 1987\nEnter Answer: ",
                          "A: Playstation 1\nB: Original Xbox\nC: Nintendo Switch\nD: Magnavox Odyssey\nEnter Answer: ",
                          "A: Siri\nB: Google\nC: Alexa\nD: Cortana\nEnter Answer: "]

    technology_answers = ["b", "a", "d", "a"]

    # Game loop starts here

    # Rounds headings (based on mode)
    if mode == "Technology":
        while rounds_played < num_rounds:
            print()
            print(f"📱💻📱 Question {rounds_played + 1} of {mode}📱💻📱")
            print(technology_questions[rounds_played])

            # get user choice
            user_choice = string_checker(technology_options[rounds_played], quiz_list)

            # Compare input to answer
            result = quiz_result(user_choice, technology_answers[rounds_played])

            if result == "correct":
                feedback = "Correct."
                rounds_won += 1

            else:
                print(f"Incorrect. The correct answer was {technology_answers[rounds_played]}")
                feedback = f"Incorrect. The correct answer was {technology_answers[rounds_played]}."
                rounds_lost += 1

            game_history.append(feedback)
            rounds_played += 1

if topic == "Food and Drink":
    mode = "Food and Drink"
    num_rounds = 4
    rounds_played = 0

    food_and_drink_questions = ["What is sushi traditionally wrapped in?",
                                "Which country is known for inventing pizza?",
                                "What fruit is used to make wine?",
                                "What is the main ingredient in guacamole?"]

    food_and_drink_options = ["\nA: Seaweed\nB: Rice\nC: Chicken\nD: Bread\nEnter Answer: ",
                              "A: United States\nB: China\nC: Greece\nD: Italy\nEnter Answer: ",
                              "A: Olives\nB: Cherries\nC: Apples\nD: Grapes\nEnter Answer: ",
                              "A: Tomatoes\nB: Avocados\nC: Onions\nD: Limes\nEnter Answer\nEnter Answer: "]

    food_and_drink_answers = ["a", "d", "d", "b"]

    # Game loop starts here

    # Rounds headings (based on mode)
    if mode == "Food and Drink":
        while rounds_played < num_rounds:
            print()
            print(f"🍔🍺🍔 Question {rounds_played + 1} of {mode}🍔🍺🍔")
            print(food_and_drink_questions[rounds_played])

            # get user choice
            user_choice = string_checker(food_and_drink_options[rounds_played], quiz_list)

            # Compare input to answer
            result = quiz_result(user_choice, food_and_drink_answers[rounds_played])

            if result == "correct":
                feedback = "Correct."
                rounds_won += 1

            else:
                print(f"Incorrect. The correct answer was {food_and_drink_answers[rounds_played]}")
                feedback = f"Incorrect. The correct answer was {food_and_drink_answers[rounds_played]}."
                rounds_lost += 1

            game_history.append(feedback)
            rounds_played += 1

    # Game loop ends here

    # Game history / Statistics area

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
