# Wordle by Ty'rese H. — March 2022

Wordle game using Python turtle graphics (v2)

* Use the console to guess a 5-letter word within 6 tries.
* Black/Gray highlighting means that the letter is not in the word at all.
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

```board``` is a 6 two-dimensional list storing tuples. 
Each tuple contains (1) the letter for the box (2) the background color for the box. 
Ex: ```("A", green)``` 
```board``` is initialized using list comprehension where each tuple is ```("", white)```.

The ```draw_box()``` function draws a box at ```x,y``` and fills it with current turtle fill color.
It also writes ```text``` in the center of the box.

The ```draw_board()``` function iterates through the tuples in ```board``` and draws the boxes in a grid format.
It uses the tuples to get right fill color and letter for the box. 

### COLOR-CODING THE LETTERS IN A GUESS WORD
The ```find_matches()``` function determines the color each box should be based on the matches that are found.
It directly modifies the tuples in ```board```.

```tries``` keeps track of how many tries a user has made thus far.
It is also used to determine which row in ```board``` the letters from ```guess``` will be placed in.
Ex: If a user has made 2 guess so far, row 2 will be filled in afer the next guess is made.

The algorithm to find matches seems trivial until duplicate letters are involved.

