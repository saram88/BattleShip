
# The best Battleships

Welcome to the best Battleship. 
In this game, you will try to hit the opponent's ship by guessing its whereabouts. The game is built in python code

Here is the live version of my <a href="https://sarabattleship-16aeb171f912.herokuapp.com/">project</a>


# How you play the game

- The game is about trying to hit the computer ship. This is done by guessing what position the ship is in (ed, column)
- The game has three ships and a 5x5 playing field
- Gusses marks are marked on the board with an "X". Hits are indicated whit "-"
- The player and the computer you are spearing against take turns guessing. Note that you can only select a number once (otherwise a text will appear that you have already chosen the number)
- The winner is the player who sinks all their opponent´s battleships first. 

# Features

## Existing Features

- The playing field shows both your and the opponent's (computer) plan at the same time. It is also possible to enter its name in an input at the start of the game

## Future Features

- Allow player to set the size of board and number of ships. 

## Input validation

- You must enter numbers
- You cannot enter coordinates outside the size of the grid
-  You can not enter the same guess twice

# Data model

I have chosen to put the model in a class called Battleshipboard. There it is defined size, number of ships, position and playing field. It runs both for player and computer.

# Testing

- Passed the code through a PEP8 linter and confirmed there are no problems.
- By my self i played the game many times. 
- Tested in Heroku terminal
- Tested in CSV terminal 

# Bugs

## Solved bugs

- When computer picks position generated a new position. In the beginning, there could be duplicates of the position. I solved this by checking the position and if the DN was already used, a new position was generated.
- Validation of data input. Checking the data that came in and it would continue as long as incorrect data is entered. It was resolved through a loop that was interrupted when the data was correct.

## Remaining bugs

- No bugs remaining

# Validator Testing

- PEP8
    - No errors where found in https://pep8ci.herokuapp.com/


# Deployment

This project i build in CSV. And then i send it up to Github and Heroku.

Steps for deployments:
- I made a reprosity from https://github.com/Code-Institute-Org/p3-template
- Created a new Heroku app
- Set up buildpacks to Python and NodeJS

# Credits

- Wikipedia to understand what a Battleship game is
- Code institute github, movies and other          materials. 
- Freecodecamp.com to read about how i vould fix my bugs ( string to int)
