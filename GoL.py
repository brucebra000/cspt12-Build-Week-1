import pygame
import random

pygame.init()

# ---Functions---
def check_neighbors(grid):
    new_grid = [[0 for x in range(25)] for y in range(25)]
    for row in range(25):
        for col in range(25):
            n = 0
            # top, left
            if row != 0:
                if col != 0:
                    if grid[row-1][col-1] == 1:
                        n += 1
            # top, middle
            if row != 0:
                if grid[row-1][col] == 1:
                    n += 1
            # top, right
            if row != 0:
                if col != 24:
                    if grid[row-1][col+1] == 1:
                        n += 1
            # middle, left
            if col != 0:
                if grid[row][col-1] == 1:
                    n += 1
            # middle, right
            if col != 24:
                if grid[row][col+1] == 1:
                    n += 1
            # bottom, left
            if col != 0:
                if row != 24:
                    if grid[row+1][col-1] == 1:
                        n += 1
            # bottom, middle
            if row != 24:
                if grid[row+1][col] == 1:
                    n += 1
            # bottom, right
            if row != 24:
                if col != 24:
                    if grid[row+1][col+1] == 1:
                        n += 1

            # if a live cell has 2 or 3 neighbors, it will survive
            if grid[row][col] == 1:
                if n == 2 or n == 3:
                    new_grid[row][col] = 1
                else:
                    new_grid[row][col] = 0
            # if a dead cell has 3 neighbors, it will become alive
            else:
                if n == 3:
                    new_grid[row][col] = 1
    grid = new_grid
    return grid

# ---Initialize game variables---

# width and height of the window
size = (630,680)
window = pygame.display.set_mode(size)

# make colors
black = (0, 0, 0)
white = (255, 255, 255)
dark_gray = (25, 25, 25)
gray = (85, 85, 85)
light_gray = (155, 155, 155)

# set caption
pygame.display.set_caption("Game of Life")

# size of cells
width = 20
height = 20
margin = 5

# grid size
grid = [[0 for x in range(25)] for y in range(25)]

# control fps
clock = pygame.time.Clock()

# simulation speed
speed = 30
speed_check = 0

# generation
generation = 0

# font
font_impact = pygame.font.SysFont('impact',30)
font_impact_small = pygame.font.SysFont('impact',20)

# text for buttons
text_start = font_impact.render('Start', True, white)
text_speed = font_impact_small.render('Speed', True, white)
text_right_arrow = font_impact.render('>', True, white)
text_left_arrow = font_impact.render('<', True, white)
text_speed_value = font_impact_small.render(str(speed), True, white)
text_next = font_impact.render('Next', True, white)
text_stop = font_impact.render('Stop', True, white)
text_clear = font_impact.render('Clear', True, white)
text_random = font_impact.render('Random', True, white)
text_generation = font_impact_small.render('Gen', True, white)
text_generation_value = font_impact_small.render(str(generation), True, white)

# ---Running the game---
run = True
simulation = False
while run:
    # mouse position
    pos = pygame.mouse.get_pos()

    # check for user input
    for event in pygame.event.get():
        # if game is closed, exit loop
        if event.type == pygame.QUIT:
            print('Closing game')
            run = False

        # perform an action when the user clicks something
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # start & stop buttons
            if 20 <= pos[0] <= 110 and 630 <= pos[1] <= 675:
                if simulation == False:
                    print('Starting simulation')
                    simulation = True
                else:
                    print('Stopping simulation')
                    simulation = False

            # speed down
            elif 130 <= pos[0] <= 150 and 635 <= pos[1] <= 670:
                if speed > 1:
                    speed = speed - 1
                    text_speed_value = font_impact_small.render(str(speed), True, white)

            # speed up
            elif 220 <= pos[0] <= 240 and 635 <= pos[1] <= 670:
                if speed < 60:
                    speed = speed + 1
                    text_speed_value = font_impact_small.render(str(speed), True, white)

            # next step
            elif 260 <= pos[0] <= 350 and 630 <= pos[1] <= 675:
                generation += 1
                text_generation_value = font_impact_small.render(str(generation), True, white)
                grid = check_neighbors(grid)

            # clear all cells & reset generation
            elif 495 <= pos[0] <= 585 and 630 <= pos[1] <= 675:
                for row in range(25):
                    for col in range(25):
                        grid[row][col] = 0
                generation = 0
                text_generation_value = font_impact_small.render(str(generation), True, white)
                print('Cleared board')
            
            # generate a random configuration
            if 370 <= pos[0] <= 475 and 630 <= pos[1] <= 675:
                generation = 0
                text_generation_value = font_impact_small.render(str(generation), True, white)
                for row in range(25):
                    for col in range(25):
                        grid[row][col] = random.randint(0, 1)

            # cells
            elif simulation != True:
                if 5 <= pos[0] <= 624 and 5 <= pos[1] <= 624:
                    col = pos[0] // (width + margin)
                    row = pos[1] // (height + margin)
                    if grid[row][col] == 0:
                        grid[row][col] = 1
                    else:
                        grid[row][col] = 0
        
    # start the simulation
    if simulation == True:
        if speed_check < speed:
            speed_check = speed_check + 1
        else:
            # move forward a generation
            grid = check_neighbors(grid)
            generation += 1
            text_generation_value = font_impact_small.render(str(generation), True, white)
            speed_check = 0

    # draw the grid
    window.fill(dark_gray)
    for row in range(25):
        for col in range(25):
            if grid[row][col] == 1:
                color = black
            else:
                color = white
            pygame.draw.rect(window, color, [margin + (margin + width) * col, margin + (margin + height) * row, width, height])
    

    # create buttons

    # start
    if 20 <= pos[0] <= 110 and 630 <= pos[1] <= 675:
        pygame.draw.rect(window, light_gray, [20, 630, 90, 45])    
    else: 
        pygame.draw.rect(window, gray, [20, 630, 90, 45])
    if simulation == False:
        window.blit(text_start, (34, 633))
    else:
        window.blit(text_stop, (34, 633))

    # speed
    if 130 <= pos[0] <= 150 and 635 <= pos[1] <= 670:
        pygame.draw.rect(window, light_gray, [130, 635, 20, 35])
    else:
        pygame.draw.rect(window, gray, [130, 635, 20, 35])
    if 220 <= pos[0] <= 240 and 635 <= pos[1] <= 670:
        pygame.draw.rect(window, light_gray, [220, 635, 20, 35])
    else:
        pygame.draw.rect(window, gray, [220, 635, 20, 35])
    window.blit(text_speed, (161, 628))
    window.blit(text_speed_value, (175, 652))
    window.blit(text_left_arrow, (132, 633))
    window.blit(text_right_arrow, (222, 633))

    # next
    if 260 <= pos[0] <= 350 and 630 <= pos[1] <= 675:
        pygame.draw.rect(window, light_gray, [260, 630, 90, 45])
    else:
        pygame.draw.rect(window, gray, [260, 630, 90, 45])
    window.blit(text_next, (277, 633))

    # random
    if 370 <= pos[0] <= 475 and 630 <= pos[1] <= 675:
        pygame.draw.rect(window, light_gray, [370, 630, 105, 45])
    else:
        pygame.draw.rect(window, gray, [370, 630, 105, 45])
    window.blit(text_random, (372, 633))

    # clear
    if 495 <= pos[0] <= 585 and 630 <= pos[1] <= 675:
        pygame.draw.rect(window, light_gray, [495, 630, 90, 45])
    else:
        pygame.draw.rect(window, gray, [495, 630, 90, 45])
    window.blit(text_clear, (507, 633))


    # display generation
    window.blit(text_generation, (590, 628))
    window.blit(text_generation_value, (600, 652))

    # update screen
    pygame.display.update()

    # fps
    clock.tick(60)

pygame.quit()
