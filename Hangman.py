import random
import hangman_art
import hangman_words


gameOn = True
chosen_word = random.choice(hangman_words.word_list)
diplay = []
for i in range(0,len(chosen_word)):
    diplay += "_"
print (hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

used_words = []
lives = 6
while gameOn == True:
    print (f"Used Letters: {used_words}")
    guess = (input("Guess a letter: ")).lower()
    if guess in chosen_word:
        if guess not in diplay:
            for i in range(0,len(chosen_word)):
                if guess == chosen_word[i]:
                    diplay[i] = guess
        else:
            print (f"You already guessed: {guess}")
    else:
        lives -= 1
    used_words += guess
    if "_" not in diplay or lives <= 0:
        gameOn = False
    print(hangman_art.stages[lives])
    print (f"{' '.join(diplay)}")
if lives > 0:
    print ("\nYou Win!")
else:
    print (f"\nThe word was: {chosen_word}\nYou Lose.")

