from livewires.beginners import *
from random import randrange

laserList = []

shipSpeed = 8
asteroidSpeed = 5
laserSpeed = 50
is_pressed = False
screen.background = "space4.jpg"
ship = Sprite(image = "ship2.png", x = 100, y = screen.height/2)
asteroid1 = Sprite(image = "asteroid.png", x = 600, y = randrange(1,screen.height/2))
asteroid2 = Sprite(image = "asteroid2.png", x = 600, y = randrange(1,screen.height/2))
asteroid3 = Sprite(image = "asteroid3.png", x = 600, y = randrange(1,screen.height/2))
#asteroid4 = Sprite(image = "asteroid4.png", x = 600, y = randrange(0,screen.height))
#asteroid5 = Sprite(image = "asteroid5.png", x = 600, y = randrange(0,screen.height))
score = Text(value = 0, size = 50, color = white, x = 600, y = 50)
gameOver = Text(value = "", size = 100, color = white, x = screen.width/2, y = screen.height/2)
music.track = "space.wav"
music.play(-1)


for i in range(1):
    laser = Sprite(image = "laser.bmp", x = 160, y = screen.height/2, dx = laserSpeed)
    laserList.append(laser)

while not keyboard.is_pressed(K_ESCAPE):
    
    #erase
    ship.erase()
    asteroid1.erase()
    asteroid2.erase()
    asteroid3.erase()
    #asteroid4.erase()
    #asteroid5.erase()        
    score.erase()
    gameOver.erase()
    for i in laserList:
        i.erase()    
    
    #update sprites
    #move ship with up and down arrow keys
    if keyboard.is_pressed(K_UP):
        ship.y -= shipSpeed
    if keyboard.is_pressed(K_DOWN):
        ship.y += shipSpeed
        
    if keyboard.is_pressed(K_SPACE):
       
        if is_pressed == False:
            laserList.append(Sprite(image = "laser.bmp", x = 100, y = screen.height/2, dx = laserSpeed))  
        is_pressed = True 
        
        
    if not keyboard.is_pressed(K_SPACE):
        is_pressed = False
    
 
    
    #makes laser shoot
    for i in laserList:
        
        #press the space bar to fire laser
        i.x += laserSpeed
        i.y = ship.y
        
        #when laser hits an asteroid
        if i.overlaps(asteroid1):
            asteroid1.y = 1000
            score.value += 10
            music.track = "collide.wav"
            music.play(1)                  
        if i.overlaps(asteroid2):
            asteroid2.y = 1000
            score.value += 10 
            music.track = "collide.wav"
            music.play(1)                  
        if i.overlaps(asteroid3): 
            asteroid3.y = 1000
            score.value += 10 
            music.track = "collide.wav"
            music.play(1)                  
    
    #move asteroids from right to left
    asteroid1.x -= asteroidSpeed 
    asteroid2.x -= asteroidSpeed 
    asteroid3.x -= asteroidSpeed
    
    if asteroid1.right < 0:
        asteroid1.right = screen.width
        asteroid1.y = randrange(1,screen.width)
        asteroidSpeed = asteroidSpeed + (asteroidSpeed * 0.001)
        
    if asteroid2.right < 0:
        asteroid2.right = screen.width
        asteroid2.y = randrange(1,screen.width)
        asteroidSpeed = asteroidSpeed + (asteroidSpeed * 0.001)
        
    if asteroid3.right < 0:
        asteroid3.right = screen.width
        asteroid3.y = randrange(1,screen.width)
        asteroidSpeed = asteroidSpeed + (asteroidSpeed * 0.001)
        
    #if asteroid4.right < 0:
     #asteroid4.right = 0
               #asteroid4.y = randrange(1,screen.width)
               #asteroidSpeed += (asteroidSpeed * 0.0001) 
           
    #if asteroid5.right < 0:
               #asteroid5.right = 0
               #asteroid5.y = randrange(1,screen.width)
               #asteroidSpeed += (asteroidSpeed * 0.0001) 
    
        
    #when asteroid hits the ship
    if asteroid1.overlaps(ship):
        ship.y = 1000
        gameOver.value = "Game Over"
    if asteroid2.overlaps(ship):
        ship.y = 1000
        gameOver.value = "Game Over" 
    if asteroid3.overlaps(ship):
        ship.y = 1000
        gameOver.value = "Game Over"
    
    #draw
    ship.draw()
    asteroid1.draw()
    asteroid2.draw()
    asteroid3.draw()
    #asteroid4.draw()
    #asteroid5.draw()     
    score.draw()
    gameOver.draw()
    for i in laserList:
        i.draw()     
    
    screen.update()