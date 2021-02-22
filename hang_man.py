# Constants
import random

# Create a tuple for the hangman graphics

HANGMAN = (
    """
    -----
    |    |
    |
    |
    |
    |
    |
___________
    """,

    """
     -----
    |    |
    |   O O
    |
    |
    |
    |
___________
    """,

    """
    -----
    |     |
    |    O O
    |   --+--
    |
    |
    |
___________
    """,

    """
    -----
    |     |
    |    O O
    |   /--+--
    |
    |
    |
___________
    """,

    """
    -----
    |     |
    |    O O
    |  /--+--/
    |
    |
    |
___________
    """,

    """
    -----
    |     |
    |    O O
    |  /--+--/
    |     |
    |     |
    |     
___________
    """,

    """
    -----
    |     |
    |    O O
    |  /--+--/
    |     |
    |   | | 
    |   |  
___________
    """,

    """
    -----
    |     |
    |    O O
    |  /--+--/
    |     |
    |   | | |
    |   |   |
___________
    """
)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("SCURRILOUS", "LIBEL", "VACCILATE", "EXTENUATE", "DESULTORY", "PREVARICATE", "ASPERSION", "STOLID", "BLASE", "ENTAIL")

word = random.choice(WORDS)  # The word to be guessed
so_far = "-" * len(word)
wrong = 0
used = []  # List of letter already guessed

print("Wel - Come to Hangman! Good luck")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("You've used the following letters : \n", used)
    print("The word so far guessed is : ", so_far)

    guess = input("Enter your guess :")
    guess = guess.upper()
    used.append(guess)

    # Checking the guess
    if guess in word:
        print("\n Yes! ", guess, "is in the word!")
        new = " "
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\n Sorry! the", guess, "isn't in the word")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("You know nothing palya....!")
else:
    print("Lord palya, you know everything!")
    print("The word was", word, "and it's meaning is still to come")

input("Press enter to exit")