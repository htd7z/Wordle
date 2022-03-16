import turtle as t
import random

t.tracer(0)
t.ht()

white = "white" # empty
green = "#7aa86a" # letter is in right spot
yellow = "#c6b567" # letter exists but is in wrong spot
gray = "#787c7f" # letter does not exist in word
red = '\u001b[31m' # error text
reset = '\u001b[0m' # reset text color to default


words = open('words.txt').read().split("\n")
actual_word = random.choice(words).upper()
guess_word = ""
tries = 0 # also used to switch row after each try


# 6 by 5 2d list of tuples
# each tuple formatted as: (letter, box_color)
board = [[("", white) for j in range(5)] for i in range(6)]


def draw_box(x, y, text):
  t.setheading(0)
  t.up(); t.goto(x,y); t.down()

  # draw square
  t.pencolor("gray")
  t.begin_fill()
  for i in range(4):
    t.forward(50)
    t.right(90)
  t.end_fill()
  t.up()

  # write letter
  t.goto(x + 27, y - 46)
  t.pencolor(white)
  t.write(text, align="center", font=("Arial", 25, "bold"))
  

def draw_board():
  for i in range(6):
    for j in range(5):
      t.fillcolor(board[i][j][1]) # box color
      draw_box(-145 + 60*j, 175 - 60*i, board[i][j][0])
  t.update()


def find_matches(guess, actual):
  
  # handle duplicate letter guesses
  lgc = {letter:0 for letter in actual} 
  
  for i in range(5): # first pass, prioritize greens
    if guess[i] == actual[i]:
      board[tries][i] = (guess[i], green)
      lgc[guess[i]] += 1 # count guess
     
 
  for i in range(5): # second pass
    if guess[i] == actual[i]: # skip greens
      continue
    
    elif guess[i] not in actual: # letter doesn't exist
      board[tries][i] = (guess[i], gray)

    # letter exists but guessed too many times
    elif lgc[guess[i]] == actual.count(guess[i]):
      board[tries][i] = (guess[i], gray)

    else: # right letter in wrong spot
      board[tries][i] = (guess[i], yellow)
      lgc[guess[i]] += 1
           

#---------- GAME RUNS BELOW

draw_board()

while True:
  guess_word = input("GUESS A 5 LETTER WORD: ").upper()
  if len(guess_word) != 5 or not guess_word.isalpha():
    print(red + "INVALID INPUT" + reset)
    continue
    
  find_matches(guess_word, actual_word)
  tries += 1
  draw_board()

  if guess_word == actual_word:
    print("YOU WIN!")
    break
  if tries == 6:
    print("YOU LOST, THE WORD WAS: " + actual_word)
    break
