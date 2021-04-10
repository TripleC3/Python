import pygame
run = True
n = -1
display = pygame.display.set_mode((50,50))

print("Press any key inside the little window")
while run:
    pygame.time.delay(100)
    var = pygame.key.get_pressed()
    for event in pygame.event.get():#track events
        if event.type == pygame.QUIT:#X = salir
            run = False
    for number in var:
        n += 1
        if number == 1:
            print("pygame code: " + str(n))
        if n == len(var):
            n = 0

pygame.quit()
