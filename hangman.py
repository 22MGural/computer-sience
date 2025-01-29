
word = 'money'
blanks=["_"]*len(word)
lives=7
guessed_letters = set()
print(" ".join(blanks))
while lives > 0 and "_" in blanks:
    guess=input("Guess a letter:")
     if guess in guessed_letters:
           print("You've already guessed '{guess}'. Guessed letters: {', '.join(sorted(guessed_letters))}")
           continue
       guessed_letters.add(guess)
    if guess in word:
        for q, letter in enumerate(word):
            if letter == guess:
                blanks[q] = guess
    else:
        lives -= 1
        print("wrong, try again.")
    print(" ".join(blanks))
if "_" not in blanks:
    print("You win")
else:
    print("Game Over")
while True:
   replay = input("Do you want to play again? : ")
   if replay != "yes":
       break
    
    
    

            
