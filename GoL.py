import pygame

pygame.init()

# ---Functions---


# ---Initialize game variables---

# width and height of the window
size = (630,630)
window = pygame.display.set_mode(size)

# make colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (75, 75, 75)

# set caption
pygame.display.set_caption("Game of Life")

# size of boxes
width = 20
height = 20
margin = 5

# grid size
grid = [[0 for x in range(25)] for y in range(25)]

# control fps
clock = pygame.time.Clock()


# ---Running the game---
run = True
while run:
    # check for user input
    for event in pygame.event.get():
        # if game is closed, exit loop
        if event.type == pygame.QUIT:
            run = False
        # click boxes
        elif event.type == pygame.MOUSEBUTTONDOWN:
            col = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            grid[row][col] = 1

    # mouse position
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    # draw the grid
    window.fill(gray)
    for row in range(25):
        for col in range(25):
            if grid[row][col] == 1:
                color = black
            else:
                color = white
            pygame.draw.rect(window, color, [margin + (margin + width) * col, margin + (margin + height) * row, width, height])
    
    # update screen
    pygame.display.flip()

    # fps
    clock.tick(60)

pygame.quit()
