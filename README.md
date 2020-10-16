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
utilizes a 25 by 25 grid. The user can select which cells are alive before starting the simulation.

# How do I use the app?