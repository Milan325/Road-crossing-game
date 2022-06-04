# Road-crossing-game
Simple road crossing game made using Python's `turtle` module.

## Rules
A turtle is crossing street, and it can move only forward. The point is to cross the road (get to the end of the window) without being hit by a car as many times. Each time the turtle crosses the road, speed of cars is increased. 

## Modules, classes and functions
This game uses `turtle` module for creating window, player's turtle, cars and scoreboard, and `random.choice()` and `random.randint` functions
### `player.py`
In this module, `Player()` subclass of Turtle class is defined. Module `move()` moves Player object at pace of 10px, and module `finish()` puts Player object at the starting position after reaching finishing line.

### `car_manager.py`
In this module, `CarManager()` class is defined. Initialized object is a list of Turtle objects, which behavior is regulated by `create()` and `move_cars()` modules used in game loop. `create()` module, when run through the while loop, picks a random number using `random.randint()` function. Only if the number is 2, new Turtle object is added to `all_cars` list. This is set so the module `create()` doesn't create a car every time loop iterates over it.

### `scoreboard.py`
In this module, `Scoreboard(Turtle)` class is defined. It defines looks and position of score on the screen. `Scoreboard()` object is an instance of `Turtle()` superclass. It functions as a text label at the top of the screen indicating game level using `turle.write()` method inside defined `update_sb()`. Methods `update_sb()` and `game_over()` are called in game engine to check end-of-level and end-of-game conditions.

## Game engine

Game engine starts by making `turtle.Screen()` object, and setting up game environment: making `Player()`, `CarManager()` and `Scoreboard()` objects. Screen takes input using `screen.listen()` function. Main part of the engine is `while` loop that:
- uses `time.sleep()` so the user does not see how CarManager objects are created at the screen center and moved to their position,
- updates the screen
- creates and adds turtle car object to the list using `car_men.create()`
- moves turtle objects from `all_cars` list using `car_men.move_cars()` module
- for loop is used to iterate over car objects, and, if Player object is within 20px from the center of a car, then the loop is broken, and `score_board.game_over()` module is initiated
- if statement is set to see if Player object crossed top of the window, so it can be put back to the bottom of the screen, and level can be updated.
If `running == False`, scoreboard object calls `game_over()` method to write "GAME OVER" at the center of the window.
At the breaking from the loop, `time.sleep(5)` is called, so the user can see "GAME OVER", because, screen object disappear once the end of the script is reached.


## Running the game
This game is intended to be run by Python IDE or other Python interpreter. 
To install Python 3 see [Tutorials Point page](https://www.tutorialspoint.com/how-to-install-python-in-windows).
