![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

The best Battleships

Welcome to the best Battleship. 
In this game, you will try to hit the opponent's ship by guessing its whereabouts. The game is built in python code

Here is the live version oj my project
https://sarabattleship-16aeb171f912.herokuapp.com/

## How you play the game

-The game is about trying to hit the computer ship. This is done by guessing what position the ship is in (ed, column)
-The game has three ships and a 5x5 playing field
-Gusses marks are marked on the board with an "X". Hits are indicated whit "-"
-The player and the computer you are spearing against take turns guessing. Note that you can only select a number once (otherwise a text will appear that you have already chosen the number)
-The winner is the player who sinks all their opponent´s battleships first. 

## Features

# Existing Features

    -The playing field shows both your and the opponent's (computer) plan at the same time. It is also possible to enter its name in an input at the start of the game

# Input validation

    -You must enter numbers
    -You cannot enter coordinates outside the size of the grid
    - You can not enter the same guess twice


# Future Features

    - Allow player to set the size of board and number of ships. 

## Data model

I have chosen to put the computer in a class called Battleshipboard. There it is defined size, number of ships, position and playing field. It runs twice.

## Testing

    - Passed the code through a PEP8 linter and confirmed there are no problems.
    - By my self i played the game many times. 
    - Tested in Heroku terminal
    - Tested in CSV terminal 

## Bugs

# Solved bugs
    - When computer picks position generated a new position. In the beginning, there could be duplicates of the position. I solved this by checking the position and if the DN was already used, a new position was generated.
    - Validation of data input. Checking the data that came in and it would continue as long as incorrect data is entered. It was resolved through a loop that was interrupted when the data was correct.

# Solved bugs

    - No bugs remaining

## Validator Testing
    - PEP8

### Deployment
This project i build in CSV. And then i send it up to Github and Heroku.

- Steps for deployments
    - I made a reprosity from https://github.com/Code-Institute-Org/p3-template
    - Created a new Heroku app
    - Set up buildpacks to Python and NodeJS

## Credits

- Wikipedia to understand what a Battleship game is
- Code institute github, movies and other          materials. 
- Freecodecmp.com to read about how i vould fix my bugs ( string to int)



When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
