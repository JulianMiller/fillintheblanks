# IPND Stage 2 Final Project

#sets the blanks
blanks = ["___1___","___2___","___3___","___4___","___5___"]

#sets the levels
levels = ['EASY', 'MEDIUM', 'HARD']

#sets the paragraph levels
easy_level = "O ___1___ can you ___2___, by the ___3___'s early ___4___? "
medium_level = "What so ___1___ we ___2___, at the ___3___'s last ___4___."
hard_level = "and the ___1___'s red glare. The ___2___ bursting in air gave ___3___ through the ___4___"

#sets the answer key
easy_answers = ['say','see','dawn','light']
medium_answers = ['proudly','hailed','twilight','gleaming']
hard_answers = ['rocket','bombs','proof','night']

difficulty = raw_input("Please select difficulty level. easy, medium, or hard.\n").lower()


def level_choice(difficulty):

    if difficulty == "easy":
        print "Slow and steady wins the race. Ready...Set..Go!"
        return easy_level
    if difficulty == "medium":
        print "You are your only competition. Ready...Set..Go!"
        return medium_level
    if difficulty == "hard":
        print "Congrats! You're nutz!!! Buckle up buckeroo"
        return hard_level
    else:
        print "That is not one of the options listed, please try again."
        difficulty = raw_input("Please select difficulty level. easy, medium, or hard.\n").lower()
        level_choice(difficulty)


print level_choice(difficulty)
