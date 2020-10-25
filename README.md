# cspt12-Build-Week-1
# Brandon Bruce
# The guidlines for this project can be found here: https://github.com/LambdaSchool/CS-Build-Week-1

#  What is Conway's 'Game of Life'?

John Conway's 'Game of Life' is from a computer science program from 1970. The program
simulates a cellular automaton. An automaton is a mechanical device that tries to imitate
human behavior. This is a game that has no players. The user will set some parameters 
before running the simulation and then will watch to see how the cell evolves based on those
parameters.

# The rules

There is a grid of square cells. Each cell is either alive or dead. The game moves in steps.
For each step, every cell will check its eight surrounding neighbors. The follow events will occur
during each step:

    If a live cell has fewer than 2 live neighbors, it will die.
    If a live cell has exactly 2 or 3 live neighbors, it will survive.
    If a live cell has more than 3 live neighbors, it will die.
    If a dead cell has exactly 3 live neighbors, it will become alive.

# What does this app do?

This app will recreate Conway's 'Game of Life'. It is built entirely from scratch. This app
utilizes a 25 by 25 grid. The user can select which cells are alive before starting the simulation
by clicking on the grid. There is also a random button that will assign each cell dead or alive
values randomly. Once the user is pleased with their current arangment, they can begin the
simulation by pressing 'Start' or they can manulaly move forward one generation by pressing 'Next'.
Using the arrows next to the speed counter, the user can freely adjust the speed of the simulation
from 1 to 60 ticks per second. The user can reset the board by using the 'Clear button'. This board
does not wrap around to the other side. The edges of the grid are like walls, so there are no cells
 outside of view.


# How do I use the app?
Run the GoL.py file to begin the application after installing the requirments.

Click on the grid to toggle the state of each cell. White cells are dead and black cells are
alive. You can't click on the grid while a simulation is running.

Press 'Random' to randomly assign each cell a dead or alive state. This will reset the generation.

Use 'Clear' to remove any live cells from the grid. This will reset the generation.

Use 'Next' to move forward one generation.

You can press the arrows on the speed slider to to adjust the speed of the simulation. The slowest is
60 ticks per second and the fastest is 1 tick per second.

Click 'Start' to begin the simulation. While the simulation is running, you can no longer click on the
grid. The simulation will move forward one generation every 'speed' amount of ticks per second. The
'Start' button will be replace by a 'Stop' button while the simulation is running. Pressing 'Stop' will
freeze the simulation, allowing you to manipulate it once again.