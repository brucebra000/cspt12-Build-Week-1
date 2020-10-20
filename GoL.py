import pygame

pygame.init()

# ---Functions---


# ---Initialize game variables---

# width and height of the window
size = (630,680)
window = pygame.display.set_mode(size)

# make colors
black = (0, 0, 0)
white = (255, 255, 255)
dark_gray = (25, 25, 25)
gray = (85, 85, 85)
light_gray = (125, 225, 125)

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

# font
font_impact = pygame.font.SysFont('impact',30)

# text for buttons
text_start = font_impact.render('Start', True, white)


# ---Running the game---
run = True
while run:
    # mouse position
    pos = pygame.mouse.get_pos()

    # check for user input
    for event in pygame.event.get():
        # if game is closed, exit loop
        if event.type == pygame.QUIT:
            run = False

        # perform an action when the user clicks something
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # start button
            if 20 <= pos[0] <= 90 and 630 <= pos[1] <= 45: 
                pygame.quit()
            # cells
            else:
                col = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                grid[row][col] = 1
        

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
    if 20 <= pos[0] <= 90 and 630 <= pos[1] <= 45: 
        pygame.draw.rect(window, black, [20, 630, 90, 45])    
    else: 
        pygame.draw.rect(window, gray, [20, 630, 90, 45])
    window.blit(text_start, (33, 633)) 

    # update screen
    pygame.display.update()

    # fps
    clock.tick(60)

pygame.quit()
