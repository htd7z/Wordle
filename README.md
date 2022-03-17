# Wordle by Ty'rese H. — March 2022

Wordle game using Python turtle graphics (v2)

* Use the console to guess a 5-letter word within 6 tries.
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
Each tuple contains the letter for the box and the background color for the box. _Example:_ ```("A", green)```.

The default value for the tuples is ```("", white)```, meaning no letter has been guessed yet.

The ```draw_box()``` function draws a box at ```x,y``` and fills it with current turtle fill color.
It also writes ```text``` (a letter) in the center of the box.

The ```draw_board()``` function iterates through the tuples in ```board``` and draws the boxes in a grid format. It uses the tuples to get right fill color and letter for the box.


### COLOR-CODING THE LETTERS IN A GUESS WORD
The ```find_matches()``` function determines the color of each box by looping through the letters in ```guess``` and comparing them to those in ```actual```.
It directly modifies the tuples in ```board```.

```tries``` keeps track of how many tries a user has made thus far. It is also used to determine which row in ```board``` the letters from ```guess``` will be placed in. _Example: If a user has made 2 guess so far, row 2 will be filled in afer the next guess is made._

The algorithm to find matches seems trivial until duplicate letters and letter ordering come into play. ==If a letter from ```guess_word``` is in ```actual_word``` but has been used too many times already, it should be highlighted in gray/black. _Example: if the actual word is "TEASE" and the guessed word is "EMCEE", there should only be 1 yellow "E", not 2. The second "E" should be highlighted in gray/black (see screenshot below)_==.

```lgc``` (letter guess counter) is a dictionary where each key is a letter in the actual word, and its value is the number of times that letter has been guessed.  shown as gray/black. 
