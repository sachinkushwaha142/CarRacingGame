"""Hi Everyone. This game is simple car racing game to enjoy ride"""

import pygame
import random
import time
pygame.init()

#display width and height
display_width = 800
display_height = 600

#set display
gameDisplay = pygame.display.set_mode((display_width,display_height))

#title of game
pygame.display.set_caption('Formula One Race')

#colors
black = (0,0,0)
white = (255,255,255)
red=(255,0,0)
pink=(255,20,147)
darkgreen=(105,139,105)
clock = pygame.time.Clock()


# car width
car_width=70
car_height=140


#carImg=pygame.transform.scale(carImg,(100,50))

#draw lines 
def line(lineX, lineY, lineW, lineH, color): 
    pygame.draw.rect(gameDisplay, color, [lineX, lineY, lineW, lineH])


#this fuction for display thing image on screen
def display_thing(x,y,thing_name):
    Img = pygame.image.load(thing_name)
    gameDisplay.blit(Img, (x,y))

#thid fuction for display massage on screen
def display_msg(msg,game_score):
    font=pygame.font.SysFont("comicsansms",50)
    msg=font.render(msg,True,red)
    gameDisplay.blit(msg, (20,200))
    
    score="Final score :"
    score+=str(game_score)
    font=pygame.font.SysFont("comicsansms",50)
    score=font.render(score,True,red)
    gameDisplay.blit(score, (20,240))
    time.sleep(2)

#this fuction for game
def game_loop():
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change=0
    global game_score
    game_score=0

    #the random module generate the value in given range thing means car,tree etc
    thing_startx = random.randrange(155, display_width - 200)
    thing_starty = -600
    thing_speed = 4
    thing_width=70
    thing_height=140
    
    #line height width 
    lineY = 0
    lineX=400
    lineW=20
    lineH=450
    line_speed = 10

    tree_h=600
    tree_y_left=50
    tree_y_right=600
    
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
        x += x_change

       #fill background color         
        gameDisplay.fill(darkgreen)
        
        line(150, 0, 20, display_height, black)
        line(display_width-150, 0, 20, display_height, black)

        #load image and scaling
        display_thing(thing_startx,thing_starty,'car.png')
        display_thing(40,tree_y_left,'tree1.png')
        display_thing(670,tree_y_right,'tree2.png')
        display_thing(x,y,'car1.png')
        
        
        thing_starty+=thing_speed
        lineY+=line_speed
        tree_y_left+=thing_speed
        tree_y_right+=thing_speed
        
        if x>display_width-car_width-150 or x<150 :
            msg="your car is out of road "
            crash_sound = pygame.mixer.Sound("crash.wav")
            pygame.mixer.Sound.play(crash_sound)
            display_msg(msg,game_score)
            crashed=True

        if(thing_starty>display_height):
            thing_starty=0-thing_height
            thing_startx=random.randrange(170,display_width-thing_width-150)
            game_score+=1
            thing_speed+=1/20

        if(lineY>display_height):
            lineY=0-450
            thing_speed+=1/15

        if tree_y_left>display_height:
            tree_y_left=0-tree_h
            thing_speed+=1/15

        if tree_y_right > display_height:
            tree_y_right = 0 - tree_h 
            thing_speed += 1/15

        if y<(thing_starty+thing_height) and y+car_height>=thing_starty+thing_height:
            if x>thing_startx and x <thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
                crash_sound = pygame.mixer.Sound("crash.wav")
                pygame.mixer.Sound.play(crash_sound)
                msg="You crashed"
                display_msg(msg,game_score)
                clock.tick(100)
                crashed=True
        pygame.display.update()
        clock.tick(60)
def main():
    game_loop()
main()
pygame.quit()
quit()
