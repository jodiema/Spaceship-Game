from livewires.beginners import *
from random import randrange

laserList = []
shipList = []

shipSpeed = 10
asteroidSpeed = 5
laserSpeed = 50

is_pressed = False

screen.background = "space4.jpg"

asteroid1 = Sprite(image = "asteroid.png", x = 600, y = randrange(1,screen.height/2))
asteroid2 = Sprite(image = "asteroid2.png", x = 700, y = randrange(1,screen.height/2))
asteroid3 = Sprite(image = "asteroid3.png", x = 800, y = randrange(1,screen.height/2))
asteroid4 = Sprite(image = "asteroid4.png", x = 800, y = randrange(1,screen.height/2))
asteroid5 = Sprite(image = "blackhole.png", x = 800, y = randrange(1,screen.height/2))
score = Text(value = 0, size = 50, color = white, x = 600, y = 50)
gameOver = Text(value = "", size = 100, color = white, x = screen.width/2, y = screen.height/2)

#music.track = "space.wav"
#music.play(-1)

for e in range(1):
    ship = Sprite(image = "ship2.png", x = 70, y = screen.height/2)
    shipList.append(ship)

while not keyboard.is_pressed(K_ESCAPE):
    
    #erase

    asteroid1.erase()
    asteroid2.erase()
    asteroid3.erase()
    asteroid4.erase()
    asteroid5.erase()
    score.erase()
    gameOver.erase()
    for i in laserList:
        i.erase()  
    for e in shipList:
        ship.erase()
    
    
    
    #update sprites
    for e in shipList:
        #move ship with up and down arrow keys
        if keyboard.is_pressed(K_UP):
            ship.y -= shipSpeed
        if keyboard.is_pressed(K_DOWN):
            ship.y += shipSpeed
        
        #keep ship on sceen
        if ship.top < 0:
            ship.top = 0
        if ship.bottom > screen.height:
            ship.bottom = screen.height
            
        #when asteroid hits the ship
        if asteroid1.overlaps(e):
            shipList.remove(e)
            gameOver.value = "Game Over!"
            music.track = "over.wav"
            music.play(1)             
        if asteroid2.overlaps(e):
            shipList.remove(e)
            gameOver.value = "Game Over!" 
            music.track = "over.wav"
            music.play(1)            
        if asteroid3.overlaps(e):
            shipList.remove(e)
            gameOver.value = "Game Over!"  
            music.track = "over.wav"
            music.play(1) 
        if asteroid4.overlaps(e):
            shipList.remove(e)
            gameOver.value = "Game Over!"  
            music.track = "over.wav"
            music.play(1) 
        if asteroid5.overlaps(e):
            shipList.remove(e)
            gameOver.value = "Game Over!"  
            music.track = "over.wav"
            music.play(1)         

    if keyboard.is_pressed(K_SPACE):
        for i in range(1):
            laser = Sprite(image = "laser.bmp", x = 70, y = ship.y, dx = laserSpeed)           
        
    #makes laser shoot
    if keyboard.is_pressed(K_SPACE):
        if is_pressed == False:
            laserList.append(Sprite(image = "laser.bmp", x = 70, y = ship.y, dx = laserSpeed))
        is_pressed = True
        
    if not keyboard.is_pressed(K_SPACE):
        is_pressed = False
        for i in range(1):
            laser = Sprite(image = "laser.bmp", x = 70, y = ship.y, dx = laserSpeed)        
        
    for i in laserList:
        #press the space bar to fire laser
        i.x += laserSpeed
        
        #when laser hits an asteroid
        if i.overlaps(asteroid1):
            asteroid1.y = 1000
            score.value += 10
            music.track = "explosion1.wav"
            music.play(1)                              
        if i.overlaps(asteroid2):
            asteroid2.y = 1000
            score.value += 10 
            music.track = "explosion1.wav"
            music.play(1)             
        if i.overlaps(asteroid3):
            asteroid3.y = 1000
            score.value += 10 
            music.track = "explosion1.wav"
            music.play(1)  
        if i.overlaps(asteroid4):
            asteroid4.y = 1000
            score.value += 10 
            music.track = "explosion1.wav"
            music.play(1)
        if i.overlaps(asteroid4):
            asteroid4.y = 1000
            score.value += 10 
            music.track = "explosion1.wav"
            music.play(1)            
       
            
        if i.left > screen.width:
            laserList.remove(i)
    
    #move asteroids from right to left
    asteroid1.x -= asteroidSpeed 
    asteroid2.x -= asteroidSpeed 
    asteroid3.x -= asteroidSpeed
    asteroid4.x -= asteroidSpeed
    asteroid5.x -= asteroidSpeed
    
    #if asteroid goes off screen it comes back and gains speed
    if asteroid1.right < 0:
        asteroid1.right = screen.width
        asteroid1.y = randrange(1,screen.width)
        asteroidSpeed = asteroidSpeed + (asteroidSpeed * 0.01)
        
    if asteroid2.right < 0:
        asteroid2.right = screen.width
        asteroid2.y = randrange(1,screen.width)
        asteroidSpeed = asteroidSpeed + (asteroidSpeed * 0.01)
        
    if asteroid3.right < 0:
        asteroid3.right = screen.width
        asteroid3.y = randrange(1,screen.width)
        asteroidSpeed = asteroidSpeed + (asteroidSpeed * 0.01)    
    
    if asteroid4.right < 0:
        asteroid4.right = screen.width
        asteroid4.y = randrange(1,screen.width)
        asteroidSpeed = asteroidSpeed + (asteroidSpeed * 0.01)
    
    if asteroid5.right < 0:
        asteroid5.right = screen.width
        asteroid5.y = randrange(1,screen.width)
        asteroidSpeed = asteroidSpeed + (asteroidSpeed * 0.01)            
    
    
    #draw
   
    asteroid1.draw()
    asteroid2.draw()
    asteroid3.draw()
    asteroid4.draw()
    asteroid5.draw()
    score.draw()
    gameOver.draw()
    for i in laserList:
        i.draw()  
    for e in shipList:
        ship.draw()
    
    screen.update()