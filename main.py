import pygame

print("start")
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print("end")

print("Loop start")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
