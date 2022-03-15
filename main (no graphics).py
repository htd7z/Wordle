import random


words = open('words.txt').read().split("\n")
actual_word = random.choice(words).upper()
guess_word = ""


green = '\u001b[42m' # letter is in right spot
yellow = '\u001b[43m' # letter exists but is in wrong spot
black = '\u001b[40m' # letter does not exist in word
red = '\u001b[31m' # error
underline = '\u001b[4m'
reset = '\u001b[0m' # reset color to default


def show_matches(guess, actual):
  lgc = {} # dictionary to count letter guesses
  
  for letter in actual:
    lgc.update({letter: 0})
  matches = ""

  for i in range(5):
    if guess[i] not in actual: # wrong letter
      matches += black + guess[i]
      continue
      
    # right letter but guessed too many times
    if lgc[guess[i]] == actual.count(guess[i]):
      matches += black + guess[i] 
      continue
      
    # right letter in right spot
    if i == actual.find(guess[i], i):
      matches += green + guess[i]
    else: # right letter in wrong spot
      matches += yellow + guess[i]

    # count letter guess
    lgc[guess[i]] += 1 
          
  print(matches + reset + "\n")   
pass

# print("*** WELCOME TO WORDLE! THE OBJECTIVE OF THE GAME IS TO GUESS A 5 LETTER WORD IN 6 TRIES ***")
# print("\t" + "* A LETTER WILL BE HIGHLIGHTED IN GREEN IF IT IS IN THE WORD AND IS ALSO IN THE RIGHT SPOT")
# print("\t" + "* A LETTER WILL BE HIGHLIGHTED IN YELLOW IF IT IS IN THE WORD BUT IS NOT IN THE RIGHT SPOT")
# print("\t" + "* A LETTER WILL BE HIGHLIGHTED IN BLACK IF IT IS NOT IN THE WORD AT ALL")
# input("\n*** PRESS ENTER TO BEGIN ***")
# print("\n")

tries = 0

while True:
  guess_word = input("GUESS A 5 LETTER WORD: ").upper()
  
  if len(guess_word) != 5:
    print(red + "INVALID INPUT" + reset)
    continue
    
  show_matches(guess_word, actual_word)
  tries += 1
  print("TRIES LEFT:", 6 - tries)

  if guess_word == actual_word:
    print(underline + "YOU WON AFTER " + str(tries) + " TRIES!")
    break
  if tries == 6:
    print(underline + "YOU LOST, THE WORD WAS " + green + actual_word)
    break
    
