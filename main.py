import turtle as t
import random

t.tracer(0)
t.hideturtle()

green = "#7aa86a" # letter is in right spot
yellow = "#c6b567" # letter exists but is in wrong spot
gray = "#787c7f" # letter does not exist in word
red = '\u001b[31m' # error text
reset = '\u001b[0m' # reset text color to default

words = open('words.txt').read().split("\n")
actual_word = random.choice(words).upper()

guess_word = ""
tries = 0


def draw_box(x, y, text, color):
  t.setheading(0)
  t.up(); t.goto(x,y); t.down()
  
  # draw square with side length 50
  t.pencolor("gray")
  t.fillcolor(color) # box color
  t.begin_fill()
  for i in range(4):
    t.forward(50)
    t.right(90)
  t.end_fill()
  t.up()

  # write letter
  t.goto(x + 27, y - 46)
  t.pencolor("white")
  t.write(text, align="center", font=("Arial", 25, "bold"))


# 10px of padding in between squares
def draw_board(): # start pos is -145, 175.
  for i in range(6):
    for j in range(5):
      draw_box(-145 + 60*j, 175 - 60*i, "", "white")
  t.update()


def colorize(guess, actual):
  # used to count times each letter was guessed
  lgc = {letter:0 for letter in actual} 
  
  for i in range(5): # first pass to prioritze green
    if guess[i] == actual[i]:
      draw_box(-145 + 60*i, 175 - 60*tries, guess[i], green)
      lgc[guess[i]] += 1 # count guess

      
  for i in range(5): # second pass
    if guess[i] == actual[i]: # skip greens
      continue
    
    elif guess[i] not in actual: # letter doesn't exist
      draw_box(-145 + 60*i, 175 - 60*tries, guess[i], gray)

    # letter exists but guessed too many times
    elif lgc[guess[i]] == actual.count(guess[i]):
      draw_box(-145 + 60*i, 175 - 60*tries, guess[i], gray)

    else: # right letter in wrong spot
      draw_box(-145 + 60*i, 175 - 60*tries, guess[i], yellow)
      lgc[guess[i]] += 1
      
           
#---------- GAME RUNS BELOW

      
draw_board()

while True:
  guess_word = input("GUESS A 5 LETTER WORD: ").upper()
  
  if len(guess_word) != 5 or not guess_word.isalpha():
    print(red + "INVALID INPUT" + reset)
    continue
    
  colorize(guess_word, actual_word)
  tries += 1

  if guess_word == actual_word:
    print("YOU WIN!")
    break
    
  if tries == 6:
    print("YOU LOST, THE WORD WAS: " + actual_word)
    break
