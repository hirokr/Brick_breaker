# import pygame  
  
# pygame.init()  
# screen = pygame.display.set_mode((400,500))  
# screen.fill('red')
# done = False  

# display_info = pygame.display.Info()
# width = display_info.current_w
# height = display_info.current_h

# print(width, height)

# def name():  
#     global done 
#     while not done:  
#         for event in pygame.event.get():  
#             if event.type == pygame.QUIT:  
#                 done = True  
#         pygame.display.flip()  

# a = name()

import pygame

pygame.init()

# Set up the initial screen size
size = (800, 600)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Update the screen size to match the new window size
            size = event.size
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    # Draw on the screen here

    pygame.display.update()

pygame.quit()
