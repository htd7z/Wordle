# Wordle by Ty'rese H. — March 2022

Wordle game using Python turtle graphics (v2)

* Use the console to guess a 5-letter word within 6 tries.
* Black/Gray highlighting means that the letter is not in the word at all.
* Yellow highlighting means that the letter is in the word, but in the wrong spot.
* Green highlighting means that the letter is in the word and is in the right spot.

_See documentation below under the screenshot.
<img src="screen.png"
     alt="screenshot"
     style="float: left; margin-right: 10px;" 
     width="417" 
     height="305"/>
     

A 2d-list is used to store tuples containing (1) the letter for the box (2) the background color for the box. The draw_box function draws the box, fills it with the right background color, and writes the proper letter on top of it.
