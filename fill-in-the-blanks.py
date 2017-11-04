# IPND Stage 2 Final Project

# sets the blanks
blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]

# sets the levels
levels = ['EASY', 'MEDIUM', 'HARD']

# sets the paragraph levels
easy_level = "O, ___1___ can you ___2___, by the ___3___'s early ___4___? "
medium_level = "What so ___1___ we ___2___, at the ___3___'s last ___4___."
hard_level = "and the ___1___'s red glare. The ___2___ bursting in air gave ___3___ through the ___4___"

# sets the answer key
easy_answers = ['say', 'see', 'dawn', 'light']
medium_answers = ['proudly', 'hailed', 'twilight', 'gleaming']
hard_answers = ['rocket', 'bombs', 'proof', 'night']

#welcome message for players
print "Welcome to Fill in the Blanks!!!"

#difficulty selection
difficulty = raw_input("Please select difficulty level. easy, medium, or hard.\n").lower()

#sets the levels
def level_choice(difficulty):
    """
    Input:
        param1: difficulty:
    Behavior:
        sets the level of the game and prints an encouraging message
    Output:
        Game level and encouraging message
    """
    if difficulty == "easy":
        #print "Slow and steady wins the race!\n"
        return easy_level and easy_answers
    if difficulty == "medium":
        #print "You are your only competition"
        return medium_level
    if difficulty == "hard":
        #print "You must be fun at parties!!!"
        return hard_level
    else:
        print "That is not one of the options listed, please try again."
        difficulty = raw_input("Please select difficulty level. easy, medium, or hard.\n").lower()
        return level_choice(difficulty)


print level_choice(difficulty)

#sets the anwser key
def level_answers(difficulty):
    """
    Input:
        param1: difficulty:
    Behavior:
        Takes the user's level selection and attaches the correct answer key
    Output:
        Returns the correct answer key
    """
    if level_choice(difficulty) == easy_level:
        return easy_answers
    if level_choice(difficulty) == medium_level:
        return medium_answers
    if level_choice(difficulty) == hard_level:
        return hard_answers

#combines the level, the guess, and the key to determine correctness
def correctness(user_guess, answers, correctness_index):
    """
    Inputs:
        param1: user_guess:
        param2: answers:
        param3: correctness_index:
    Behavior:
        Checks to see if user's guess == answer at the corresponding index
   Output:
        True if correct, else False
    """
    if user_guess == answers[correctness_index]:
        return True
    return False

#combines all the elements into the game
def start_quiz():
    quiz_selection = level_choice(difficulty)
    answers = level_answers(difficulty)
    blanks_index = 0
    correctness_index = 0
    while blanks_index < len(blanks):
        while correctness_index < len(answers):
            user_guess = raw_input("What word goes in here " + blanks[blanks_index] + "?\n")
            while correctness(user_guess, answers, correctness_index) == False:
                user_guess = raw_input(
                    "Oh, I'm sorry. try again.\n" + "What word goes in here " + blanks[
                        blanks_index] + "?\n")
            if correctness(user_guess, answers, correctness_index) == True:
                print "You're on fire!"
                quiz_selection = quiz_selection.replace(blanks[blanks_index], user_guess)
                print quiz_selection
                blanks_index += 1
                correctness_index += 1
print start_quiz()