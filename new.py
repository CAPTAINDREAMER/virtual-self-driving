import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 155
car_y = 300
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()

def brake():
    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0

#Keyboard--------------------------------------------                
            if event.type == pygame.KEYDOWN:        
                
                if event.key == pygame.K_SPACE:
                    window.fill((0, 0, 0))
                    loop = 0
#Keyboard--------------------------------------------

#Mouse------------------------------------------- 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 1060 <= mouse[0] <= 1200 and 360 <= mouse[1] <= 400:
                    window.fill((0, 0, 0))
                    loop = 0
#Mouse------------------------------------------- 
                
        pygame.display.update()
        clock.tick(60)

white_color = (255,255,255)
color_on_hover = (255,0,0)
color_red = (100,0,0)

smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('Brake!' , True , white_color)


while drive:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
        if event.type == pygame.QUIT:
            pygame.quit()

        #mouse brake
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 1060 <= mouse[0] <= 1200 and 360 <= mouse[1] <= 400:
                brake()
        
        #keyboard brake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               brake()

    clock.tick(60)
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    #print(up_px, right_px, down_px)
	    

    # change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)
    # drive
    if direction == 'up' and up_px == 255:
        car_y = car_y - 2
    elif direction == 'right' and right_px == 255:
        car_x = car_x + 2
    elif direction == 'down' and down_px == 255:
        car_y = car_y + 2
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    
    if 1060 <= mouse[0] <= 1200 and 360 <= mouse[1] <= 400:
        pygame.draw.rect(window,color_on_hover,[1060,360,140,40])
    else:
        pygame.draw.rect(window,color_red,[1060,360,140,40])
    window.blit(text , (1090,365))

    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
