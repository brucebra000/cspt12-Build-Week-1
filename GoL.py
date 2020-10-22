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


# ---Running the game---
run = True
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
            # start button
            if 20 <= pos[0] <= 110 and 630 <= pos[1] <= 675:
                print('Starting simulation')
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
                print('Moving to the next generation')
            # cells
            elif 5 <= pos[0] <= 624 and 5 <= pos[1] <= 624:
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
    if 20 <= pos[0] <= 110 and 630 <= pos[1] <= 675:
        pygame.draw.rect(window, light_gray, [20, 630, 90, 45])    
    else: 
        pygame.draw.rect(window, gray, [20, 630, 90, 45])
    window.blit(text_start, (34, 633))

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
    

    # update screen
    pygame.display.update()

    # fps
    clock.tick(60)

pygame.quit()
