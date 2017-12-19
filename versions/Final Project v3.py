from livewires.beginners import *
from random import randrange

laserList = []

shipSpeed = 10
asteroidSpeed = 5
laserSpeed = 50

is_pressed = False
shipDestroyed = False
game_Over = False

screen.background = "space4.jpg"
ship = Sprite(image = "ship2.png", x = 70, y = screen.height/2)
asteroid1 = Sprite(image = "asteroid.png", x = 600, y = randrange(1,screen.height/2))
asteroid2 = Sprite(image = "asteroid2.png", x = 700, y = randrange(1,screen.height/2))
asteroid3 = Sprite(image = "asteroid3.png", x = 800, y = randrange(1,screen.height/2))
asteroid4 = Sprite(image = "asteroid4.png", x = 900, y = randrange(1,screen.height/2))
asteroid5 = Sprite(image = "blackhole.png", x = 1000, y = randrange(1,screen.height/2))
score = Text(value = 0, size = 50, color = white, x = 600, y = 50)
gameOver = Text(value = "", size = 100, color = white, x = screen.width/2, y = screen.height/2)
shipExplosion = Sound("ship explosion.wav")
asteroidExplosion = Sound("asteroid explosion.wav")
laserBlast = Sound("laser blast.wav")
graphicExplosion = ["graphics explosions 1.png", 
                    "graphics explosions 2.png", 
                    "graphics explosions 3.png",
                    "graphics explosions 4.png",
                    "graphics explosions 5.png",
                    "graphics explosions 6.png",
                    "graphics explosions 7.png",
                    "graphics explosions 8.png",
                    "graphics explosions 9.png",
                    "graphics explosions 10.png",
                    "graphics explosions 11.png",
                    "graphics explosions 12.png",
                    "graphics explosions 13.png",
                    "graphics explosions 14.png",
                    "graphics explosions 15.png",
                    "graphics explosions 16.png",
                    "graphics explosions 17.png",
                    "graphics explosions 18.png",
                    "graphics explosions 19.png",
                    "graphics explosions 20.png",
                    "graphics explosions 21.png",
                    "graphics explosions 22.png",
                    "graphics explosions 23.png",
                    "graphics explosions 24.png",
                    "graphics explosions 25.png",
                    "graphics explosions 26.png",
                    "graphics explosions 27.png",
                    "graphics explosions 28.png",]
explosions = []
    
for explosion in range(1):
    explosion = Animation(images = graphicExplosion, x = 70, y = ship.y, n_repeats = 1, repeat_interval = 1)
    explosions.append(explosion)    

while not keyboard.is_pressed(K_ESCAPE):
    
    #erase
    ship.erase()
    asteroid1.erase()
    asteroid2.erase()
    asteroid3.erase()
    asteroid4.erase()
    asteroid5.erase()
    score.erase()
    gameOver.erase()
    for i in laserList:
        i.erase()
    for explosion in explosions:
        if game_Over == True:
            explosion.erase()
    
    #update sprites
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
    
    #explosion animation
    for explosion in explosions:
        explosion.tick()
        if explosion.is_over:
            explosions.remove(explosion)

    #makes laser shoot
    if keyboard.is_pressed(K_SPACE):
        for i in range(1):
            laser = Sprite(image = "laser.bmp", x = 70, y = ship.y, dx = laserSpeed)
        
    if keyboard.is_pressed(K_SPACE):
        if is_pressed == False:
            laserList.append(Sprite(image = "laser.bmp", x = 70, y = ship.y, dx = laserSpeed))
            laserBlast.play()
        is_pressed = True
        
    if not keyboard.is_pressed(K_SPACE):
        is_pressed = False
        for i in range(1):
            laser = Sprite(image = "laser.bmp", x = 70, y = ship.y, dx = laserSpeed)
        
    for i in laserList:
        i.x += laserSpeed
        
        #when laser hits an asteroid
        if i.overlaps(asteroid1):
            asteroid1.y = 1000
            score.value += 10
            asteroidExplosion.play()
        if i.overlaps(asteroid2):
            asteroid2.y = 1000
            score.value += 10
            asteroidExplosion.play()
        if i.overlaps(asteroid3):
            asteroid3.y = 1000
            score.value += 10
            asteroidExplosion.play()
        if i.overlaps(asteroid4):
            asteroid4.y = 1000
            score.value += 10
            asteroidExplosion.play()
        if i.overlaps(asteroid5):
            asteroid5.y = 1000
            score.value += 25
            asteroidExplosion.play()            
            
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
        
    #when asteroid hits ship
    if asteroid1.overlaps(ship) and game_Over == False:
        shipDestroyed = True
        game_Over = True
        gameOver.value = "Game Over"
        shipExplosion.play()
        explosions.append(Animation(images = graphicExplosion, x = 70, y = ship.y, n_repeats = 1, repeat_interval = 1))
    if asteroid2.overlaps(ship) and game_Over == False:
        shipDestroyed = True
        game_Over = True
        gameOver.value = "Game Over"
        shipExplosion.play()
        explosions.append(Animation(images = graphicExplosion, x = 70, y = ship.y, n_repeats = 1, repeat_interval = 1))
    if asteroid3.overlaps(ship) and game_Over == False:
        shipDestroyed = True
        game_Over = True
        gameOver.value = "Game Over"
        shipExplosion.play()
        explosions.append(Animation(images = graphicExplosion, x = 70, y = ship.y, n_repeats = 1, repeat_interval = 1))
    if asteroid4.overlaps(ship) and game_Over == False:
        shipDestroyed = True
        game_Over = True
        gameOver.value = "Game Over"
        shipExplosion.play()
        explosions.append(Animation(images = graphicExplosion, x = 70, y = ship.y, n_repeats = 1, repeat_interval = 1))
    if asteroid5.overlaps(ship) and game_Over == False:
        shipDestroyed = True
        game_Over = True
        gameOver.value = "Game Over"
        shipExplosion.play()
        explosions.append(Animation(images = graphicExplosion, x = 70, y = ship.y, n_repeats = 1, repeat_interval = 1))    
        
    #draw
    if shipDestroyed == False:
        ship.draw()
    asteroid1.draw()
    asteroid2.draw()
    asteroid3.draw()
    asteroid4.draw()
    asteroid5.draw()
    score.draw()
    gameOver.draw()
    for i in laserList:
        i.draw()
    for explosion in explosions:
        if game_Over == True:
            explosion.draw()     
    
    screen.update()