import pickWord
import string
import visualization


def hangman():
    lives = 4
    word = pickWord.randomWord()        # pick random word 
    wordLetters = set(word)     # letters in word
    alphabet = set(string.ascii_uppercase)      # to use only ASCII uppercase letters
    usedLetters = set()     # list with letters already used
    # print(word) # helps testing if You can win, just delete hashtag.
    
    while len(wordLetters)!=0 and lives!=0: # condition which run game untill lost all lifes or win 
        visualization.visualization(lives)
        print(f"\n Lives left: {lives} \n")
        print(f"You have already used letters: {', '.join(usedLetters)}")   # used letters
        hangmanWord = [letter if letter in usedLetters else "-" for letter in word ]
        print(f"Current word: {''.join(hangmanWord)} \n") # shows encrypted word on current stage of game
        
        #getting player input
        guessLetter = input("Guess what letter is in the word \n >>  ").upper()
        if guessLetter in alphabet - usedLetters:
            usedLetters.add(guessLetter)
            
            if guessLetter in wordLetters:
                wordLetters.remove(guessLetter)
            
            else:   # incorrect letter = lose 1 live 
                lives-=1
                print(f"This letter is not in word. You lose 1 live")
        
        elif guessLetter in usedLetters:    # already used char
            print("You've already used this character. Try again.")        
        
        else:   # not a letter char
            print("Not a letter. Try again.")
    
    
    if lives ==0:   # lose
        visualization.visualization(lives)
        print(f"Sorry, You lost this time. Guessing word was: {word}")
    else:   # win
        visualization.visualizationWin()
        print(f"Congratulations!!! \nYou guessed {word}, and won the game. ")
    

hangman()

