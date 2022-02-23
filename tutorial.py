print('''
Welcome to...

\u001b[32;1mGabriel Thompson's Magical Wordle Solver!\033[0m (not the official name)

In each move, the program will tell you what word to enter.
The program will then prompt you to enter the result of entering that word, which you can write in the following form:

 > \u001b[37;1mGray\033[0m squares    = 0
 > \u001b[33;1mYellow\033[0m squares  = 1
 > \u001b[32;1mGreen\033[0m squares   = 2

For example, if entering a word yields "\u001b[32;1mGreen\033[0m, \u001b[37;1mGrey\033[0m, \u001b[33;1mYellow\033[0m, \u001b[37;1mGrey\033[0m, \u001b[32;1mGreen\033[0m", you would write this as "20102".

The average Wordle can be solved in 3.61 guesses. Almost all Wordles are solved in 3 or 4 guesses.

''')
