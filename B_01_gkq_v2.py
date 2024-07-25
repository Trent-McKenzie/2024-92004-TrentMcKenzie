import random


# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

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


# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:

        error = "Please enter an integer that is 1 or more."

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

quiz_list = ["A", "B", "C", "D", "a", "b", "c", "d", "xxx"]
questions_list = []
answer_list = []

print("❓❔❓ General Knowledge Quiz ❓❔❓")
print()

# ask user if they want to see the instructions and display
# them if needed
want_instructions = string_checker("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
topic = int_check("What topic would you like? ")

if topic == "History":
    mode = "History"
    num_rounds = 5

    questions = ["Who was the first president of the United States?", "What year did World War 2 end?",
                 "What ancient civilization built the pyramids?", "What year was Napoleon born?"]

    options = ["A: George Washington\nB: Abraham Lincoln\nC: John F. Kennedy\nD: Joe Biden",
               "A: 1976\nB: 2001\nC: 1945\nD: 1865", "A: Greeks\nB: Egyptians\nC: Romans\nD: Australians",
               "A: 1784\nB: 1889\nC: 1769\nD: 1901"]

    answers = ["a", "c", "b", "c"]

    # Game loop starts here

    # Rounds headings (based on mode)
    if mode == "History":
        print()
        print("🧾🧾 Question 1 of History 🧾🧾🧾")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "a":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was A: George Washington")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "c":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was C: 1945")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🧾🧾🧾 Question 3 of History 🧾🧾🧾")
    print("What ancient civilization built the pyramids?")
    print("A: Greeks")
    print("B: Egyptians")
    print("C: Romans")
    print("D: Australians")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "b":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was B: Egyptians")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🧾🧾🧾 Question 4 of History 🧾🧾🧾")
    print("What year was Napoleon born?")
    print("A: 1784")
    print("B: 1889")
    print("C: 1769")
    print("D: 1901")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "c":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was C: 1769")

if topic == "Geography":
    mode = "Geography"
    num_rounds = 5

    # Rounds headings (based on mode)
    if mode == "Geography":
        print()
        print("🌏🌏🌏 Question 1 of Geography 🌏🌏🌏")

    print("What is the capital of Australia?")
    print("A: Perth")
    print("B: Sydney")
    print("C: Melbourne")
    print("D: Canberra")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "d":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was D: Canberra")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🌏🌏🌏 Question 2 of Geography 🌏🌏🌏")
    print("Which is the largest desert in the world?")
    print("A: Sahara")
    print("B: Antarctica")
    print("C: Arabian")
    print("D: Gobi")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "b":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was B: Antarctica")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🌏🌏🌏 Question 3 of Geography 🌏🌏🌏")
    print("What river runs through Paris?")
    print("A: Seine")
    print("B: Thames")
    print("C: Nile")
    print("D: Amazon")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "a":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was A: Seine")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🌏🌏🌏 Question 4 of Geography 🌏🌏🌏")
    print("In which country is Mount Everest located?")
    print("A: China")
    print("B: Canada")
    print("C: Nepal")
    print("D: New Zealand")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "c":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was C: Nepal")

if topic == "Science":
    mode = "Science"
    num_rounds = 5

    # Rounds headings (based on mode)
    if mode == "Science":
        print()
        print("🧪🧪🧪 Question 1 of Science 🧪🧪🧪")

    print("What planet is known as the Red Planet?")
    print("A: Venus")
    print("B: Mars")
    print("C: Jupiter")
    print("D: Saturn")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "b":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was B: Mars")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🧪🧪🧪 Question 2 of Science 🧪🧪🧪")
    print("Who developed the theory of relativity?")
    print("A: Isaac Newton")
    print("B: Robert Oppenheimer")
    print("C: Albert Einstein")
    print("D: Charles Darwin")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "c":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was C: Albert Einstein")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🧪🧪🧪 Question 3 of Science 🧪🧪🧪")
    print("What is the chemical symbol for gold?")
    print("A: Au")
    print("B: G")
    print("C: Go")
    print("D: Si")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "a":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was A: Au")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🧪🧪🧪 Question 4 of Science 🧪🧪🧪")
    print("What part of the cell contains the genetic material?")
    print("A: Mitochondria")
    print("B: Ribosomes")
    print("C: Cell Membrane")
    print("D: Nucleus")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "d":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was D: Nucleus")

if topic == "Literature":
    mode = "Literature"
    num_rounds = 5

    # Rounds headings (based on mode)
    if mode == "Literature":
        print()
        print("📕📕📕 Question 1 of Literature 📕📕📕")

    print("Who wrote Romeo and Juliet?")
    print("A: Charles Dickens")
    print("B: William Shakespeare")
    print("C: Ernest Hemingway")
    print("D: J.K Rowling")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "b":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was B: William Shakespeare")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("📕📕📕 Question 2 of Literature 📕📕📕")
    print("What is the title of the first Harry Potter book?")
    print("A: Goblet of Fire")
    print("B: Prisoner of Azkaban")
    print("C: Chamber of Secrets")
    print("D: Philosophers Stone")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "d":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was D: Philosophers Stone")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("📕📕📕 Question 3 of Literature 📕📕📕")
    print("Who is the author of To Kill a Mockingbird?")
    print("A: Stephen King")
    print("B: Mark Twain")
    print("C: Harper Lee")
    print("D: Edgar Allen Poe")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "c":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was C: Harper Lee")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("📕📕📕 Question 4 of Literature 📕📕📕")
    print("Which famous novel begins with the line, Call me Ishmael?")
    print("A: Moby Dick")
    print("B: Annabel Lee")
    print("C: A Tale of Two Cities")
    print("D: The Great Gatsby")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "a":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was A: Moby Dick")

if topic == "Sports":
    mode = "Sports"
    num_rounds = 5

    # Rounds headings (based on mode)
    if mode == "Sports":
        print()
        print("🏀⚽🏈 Question 1 of Sports 🏀⚽🏈")

    print("How many players are there in a soccer team?")
    print("A: 13")
    print("B: 11")
    print("C: 14")
    print("D: 12")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "b":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was B: 11")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🏀⚽🏈 Question 2 of Sports 🏀⚽🏈")
    print("In which sport would you perform a slam dunk?")
    print("A: Basketball")
    print("B: Hockey")
    print("C: Football")
    print("D: Tennis")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "a":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was A: Basketball")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🏀⚽🏈 Question 3 of Sports 🏀⚽🏈")
    print("Who has won the most Grand Slam titles in tennis?")
    print("A: Novak Djokovic")
    print("B: Carlos Alcaraz")
    print("C: Rafael Nadal")
    print("D: Daniil Medvedev")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "c":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was C: Rafael Nadal")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🏀⚽🏈 Question 4 of Sports 🏀⚽🏈")
    print("What country hosted the 2016 Summer Olympics?")
    print("A: United States")
    print("B: Brazil")
    print("C: China")
    print("D: Australia")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "b":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was B: Brazil")

if topic == "Entertainment":
    mode = "Entertainment"
    num_rounds = 5

    # Rounds headings (based on mode)
    if mode == "Entertainment":
        print()
        print("🎥🎬🎥 Question 1 of Entertainment 🎥🎬🎥")

    print("Who played the character of Jack Dawson in the movie Titanic?")
    print("A: Tom Holland")
    print("B: Chris Hemsworth")
    print("C: Cillian Murphy")
    print("D: Leonardo Di Caprio")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "d":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was D: Leonardo Di Caprio")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🎥🎬🎥 Question 2 of Entertainment 🎥🎬🎥")
    print("What is the highest-grossing film of all time?")
    print("A: Avengers: Endgame")
    print("B: Avatar")
    print("C: Titanic")
    print("D: Avatar: The Way of Water")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "b":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was B: Avatar")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🎥🎬🎥 Question 3 of Entertainment 🎥🎬🎥")
    print("Which animated film features the song Let It Go?")
    print("A: Inside Out")
    print("B: Ratatouille")
    print("C: Frozen")
    print("D: Shrek")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "c":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was C: Frozen")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🎥🎬🎥 Question 4 of Entertainment 🎥🎬🎥")
    print("Who is the creator of the Star Wars franchise?")
    print("A: James Cameron")
    print("B: Christopher Nolan")
    print("C: George Lucas")
    print("D: Tim Burton")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "c":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was C: George Lucas")

if topic == "Art and Music":
    mode = "Art and Music"
    num_rounds = 5

    # Rounds headings (based on mode)
    if mode == "Art and Music":
        print()
        print("🎨🎵🎨 Question 1 of Art and Music 🎨🎵🎨")

    print("Who painted the Mona Lisa?")
    print("A: Leonardo Da Vinci")
    print("B: Vincent Van Gogh")
    print("C: Pablo Picasso")
    print("D: Bob Ross")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "a":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was A: Leonardo Da Vinci")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🎨🎵🎨 Question 2 of Art and Music 🎨🎵🎨")
    print("What is the name of the famous music festival held annually in the desert in California?")
    print("A: Glastonbury")
    print("B: Woodstock")
    print("C: Boomtown")
    print("D: Coachella")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "d":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was D: Coachella")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🎨🎵🎨 Question 3 of Art and Music 🎨🎵🎨")
    print("Who composed the Four Seasons?")
    print("A: Beethoven")
    print("B: Mozart")
    print("C: Antonio Vivaldi")
    print("D: Richard Wagner")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "c":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was C: Antonio Vivaldi")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🎨🎵🎨 Question 4 of Art and Music 🎨🎵🎨")
    print("What is the term for a painting done on wet plaster?")
    print("A: Impressionism")
    print("B: Fresco")
    print("C: Oil Painting")
    print("D: Abstract")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "b":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was B: Fresco")

if topic == "Technology":
    mode = "Technology"
    num_rounds = 5

    # Rounds headings (based on mode)
    if mode == "Technology":
        print()
        print("📱💻📱 Question 1 of Technology 📱💻📱")

    print("Who is the founder of Microsoft?")
    print("A: Larry Page")
    print("B: Bill Gates")
    print("C: Steve Jobs")
    print("D: Tim Cook")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "b":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was B: Bill Gates")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("📱💻📱 Question 2 of Technology 📱💻📱")
    print("What year was the World Wide Web invented?")
    print("A: 1989")
    print("B: 1977")
    print("C: 1993")
    print("D: 1987")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "a":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was A: 1989")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("📱💻📱 Question 3 of Technology 📱💻📱")
    print("What was the first video game console ever released?")
    print("A: Playstation 1")
    print("B: Original Xbox")
    print("C: Nintendo Switch")
    print("D: Magnavox Odyssey")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "d":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was D: Magnavox Odyssey")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("📱💻📱 Question 4 of Technology 📱💻📱")
    print("What is the name of Apple's virtual assistant?")
    print("A: Siri")
    print("B: Google")
    print("C: Alexa")
    print("D: Cortana")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "a":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was A: Siri")

if topic == "Food and Drink":
    mode = "Food and Drink"
    num_rounds = 5

    # Rounds headings (based on mode)
    if mode == "Food and Drink":
        print()
        print("🍔🍺🍔 Question 1 of Food and Drink 🍔🍺🍔")

    print("What is sushi traditionally wrapped in?")
    print("A: Seaweed")
    print("B: Rice")
    print("C: Chicken")
    print("D: Bread")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "a":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was A: Seaweed")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🍔🍺🍔 Question 2 of Food and Drink 🍔🍺🍔")
    print("Which country is known for inventing pizza?")
    print("A: United States")
    print("B: China")
    print("C: Greece")
    print("D: Italy")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "d":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was D: Italy")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🍔🍺🍔 Question 3 of Food and Drink 🍔🍺🍔")
    print("What fruit is used to make wine?")
    print("A: Olives")
    print("B: Cherries")
    print("C: Apples")
    print("D: Grapes")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "d":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was D: Grapes")

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(quiz_list[:-1])
    print()
    print("🍔🍺🍔 Question 4 of Food and Drink 🍔🍺🍔")
    print("What is the main ingredient in guacamole?")
    print("A: Tomatoes")
    print("B: Avocados")
    print("C: Onions")
    print("D: Limes")

    # get user choice
    user_choice = string_checker("Enter answer: ", quiz_list)

    if user_choice == "b":
        print("Correct!")

    else:
        print("Incorrect.")
        print("The correct answer was B: Avocados")

    # Game loop ends here

    # Game history / Statistics area

if rounds_played > 0:
    # Calculate Statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    # Output Game Statistics
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"👍 Won: {percent_won:.2f} \t "
          f"😥 Lost: {percent_lost:.2f} \t ")
