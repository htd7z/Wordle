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
It directly modifies the tuples in ```board``` by changing their letters and colors.

```tries``` keeps track of how many tries a user has made thus far. It is also used to determine which row in ```board``` the letters in ```guess``` will be placed in. _Example: If a user has made 2 guess so far, row 2 will be filled in after the next guess is made._

The algorithm to find matches is mostly trivial. Each letter in ```guess``` is compared to the corresponding letter from ```actual```. However, there are two edge cases involving duplicate letters that ```find_matches()``` accounts for.

**(1) If a letter from ```guess``` is in ```actual``` but is in the wrong spot it would normally be highlighted in yellow. However, if the letter has been used in ```guess``` more times than it exists in ```actual```, it should be highlighted in gray/black. _Example: if the actual word is "TEASE" and the guessed word is "EREEN", there should only be 2 yellow "E"s, not 3. The third "E" should be highlighted in gray/black (see screenshot below)_.**

```lgc``` (letter guess counter) is a dictionary where each key is a letter in the actual word, and its value is the number of times that letter has been guessed thus far. It is used to highlight a letter from ```guess``` in gray/black if it is used more times than it exists in ```actual```. This prevents incorrect duplicate yellow highlights but does not address the second edge case.

**(2) If a letter from ```guess``` is in ```actual``` and is in the right spot it should be highlighted in green no matter what, even if it has been used too many times. _Example: if the actual word is "TEASE" and the guessed word is "EMCEE", there should only be 1 yellow "E", not 2. The second "E" should be highlighted in gray/black. Though the last "E" is the third time that "E" is used, it should still be highlighted in green because it is in the right spot. (see screenshot below)_.**

To account for this, green match detection takes priority over yellow and gray/black match detection. The first ```for i in range(5)``` loop only detects green matches, and counts letter guesses. The second ```for i in range(5)``` skips over green matches and modifies the board 


