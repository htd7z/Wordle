# Wordle by Ty'rese H. — March 2022

\[v1] Wordle game using console I/O only (not shown, needs fixing).

\[v2] Wordle game using console I/O and Python turtle graphics.

* Use the console to guess a five-letter word within six tries.
* Gray/Black highlighting means that the letter is not in the word at all.
* Yellow highlighting means that the letter is in the word, but in the wrong spot.
* Green highlighting means that the letter is in the word and is in the right spot.

_See documentation below under the screenshot._

<img src="screen.png"
     alt="screenshot"
     style="float: left; margin-right: 10px;" 
     width="417" 
     height="305"/>
     

### DATA ORGANIZATION AND VISUALS
```words.txt``` holds words separated by newline characters.

Turtle and ANSI colors are saved as strings.

```board``` is a two-dimensional list of tuples representing the boxes on the board.
Each tuple contains the letter and the fill color for that box. _Example:_ ```("A", green)```.

The default value for the tuples is ```("", white)```, meaning no letter has been guessed yet.

The ```draw_box()``` function draws a box at ```x,y``` and fills it with current turtle fill color. It also writes ```text``` (a letter) in the center of the box. For clarity, filling in a box is the same thing as highlighting a letter.


The ```draw_board()``` function iterates through the tuples in ```board``` and draws the boxes in a grid format. It uses the tuples to get the right fill color and letter for the box.


### COLOR-CODING THE LETTERS IN A GUESS WORD
The ```colorize()``` function determines the color of each box by looping through the letters in ```guess``` and comparing them to those in ```actual```.
It directly modifies the tuples in ```board``` by changing their contained letters and colors.

```tries``` keeps track of how many guesses a user has made thus far. It is also used to determine which row in ```board``` the letters in ```guess``` will be placed in. _Example: If a user has made 2 guesses so far, row 2 will be filled in after the next guess is made._

The algorithm to highlight letters is mostly trivial. Each letter in ```guess``` is compared to the corresponding letter from ```actual```. However, there are two edge cases involving duplicate letters that ```colorize()``` accounts for.

**(1) If a letter from ```guess``` is in ```actual``` but is in the wrong spot it would normally be highlighted in yellow. However, if the letter has been used in ```guess``` more times than it exists in ```actual```, it should be highlighted in gray/black. _Example: if the actual word is "TEASE" and the guessed word is "EREEN", there should only be two yellow "E"s, not three. The third "E" should be highlighted in gray/black (see screenshot below)_.**

```lgc``` (letter guess counter) is a dictionary where each key is a letter in the actual word and its value is the number of times that letter has been guessed thus far. It is used to highlight a letter from ```guess``` in gray/black if it is used more times than it exists in ```actual```.


**(2) If a letter from ```guess``` is in ```actual``` and is in the right spot it should be highlighted in green no matter what, even if it has been used too many times. _Example: if the actual word is "TEASE" and the guessed word is "EMCEE", there should only be one yellow "E", not two. The second "E" should be highlighted in gray/black. Though the last "E" is the third time that "E" is used, it should still be highlighted in green because it is in the right spot. If the guess is "GREEN" however, both "E"s should be highlighted in yellow (see screenshot below)_.**

To account for this, green highlighting takes priority over yellow and gray/black highlighting. The first ```for i in range(5)``` loop only does green highlighting and counts letter guesses. The second ```for i in range(5)``` skips over green highlighting completely, does yellow and gray/black highlighting, and counts letter guesses.

### GAME FUNCTIONALITY
```while True``` is the main loop that runs the game.


Correct output for edge cases:

<img src="screen2.png"
     alt="screenshot2"
     style="float: left; margin-right: 10px;" 
     width="429" 
     height="403"/>
