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
Turtle and ANSI colors are saved as string variables.

_board_ is a 6 two-dimensional list storing tuples. 
Each tuple contains (1) the letter for the box (2) the background color for the box. Ex: ("A", green).
_board_ is initialized using list comprehension where each tuple is ("", white).

The _draw_box()_ function draws a box at _x, y_, fills it with current turtle fill color, and writes _text_ in the center of it.

The _draw_board()_ function uses nested-loops to iterate through the tuples in _board_ and draw the boxes in a grid format.
It also uses the tuples to change the fill color for each box. 

### COLOR-CODING THE LETTERS IN A GUESS WORD.
