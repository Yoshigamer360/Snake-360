# Remake of the arcade game Snake
# Date 27/7/24
# Created by Yoshi Gamer 360

styleChoice = input('What style do you want? A) Rainbow, B) Hacker, C) Plain: ').lower().strip()

# Imports
import pygame, random

# Initialize pygame engine
pygame.init()

# Set up the game window
screenWidth = 640
screenHeight = 480
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake Game - By Yoshi Gamer 360")

# Set up the game clock
clock = pygame.time.Clock()

# Define the colours
if styleChoice == 'b':
    colourBackground = (0, 0, 0)
    colourScore = (0, 255, 0)
else:
    colourBackground = (166, 227, 159)
    colourScore = (30, 0, 100)
colourFood = (250, 250, 5)

# Define snake colours array
if styleChoice == 'a':
    colourSnakeArray = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (143, 0, 255)]
elif styleChoice == 'b':
    colourSnakeArray = [(0, 255, 0)]
else:
    colourSnakeArray = [(30, 160, 30)]


# Define the block / pixel size and the snake speed
blockSize = 10
snakeSpeed = 15

# Define a font object
font = pygame.font.SysFont("Comic Sans MS", 25)

# Define the function to display the score
def displayScore(score):
    scoreText = font.render("Score: " + str(score), True, colourScore)
    screen.blit(scoreText, [10, 5])

# Define the main game function
def game():
    # Set up the intial snake position
    snakeHead = [screenWidth/2, screenHeight/2]
    snakeBody = [[screenWidth/2, screenHeight/2],
                  [screenWidth/2-blockSize, screenHeight/2],
                  [screenWidth/2-(blockSize*2), screenHeight/2]]
    
    # Set up the initial food position
    foodPos = [random.randrange(0, screenWidth - blockSize, blockSize),
                random.randrange(0, screenHeight - blockSize, blockSize)]

    # Set up the intial direction and change direction
    direction = "RIGHT"
    changeTo = direction

    # Set the initial score
    score = 0

    # Main game play loop
    gameOver = False
    while not gameOver:
        # Handle input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        changeTo = "LEFT"
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        changeTo = "RIGHT"
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        changeTo = "UP"
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        changeTo = "DOWN"
                    elif event.key == pygame.K_3:
                        snakeBody.append([snakeHead[0], snakeHead[1]])
                        score += 10
                        snakeBody.append([snakeHead[0], snakeHead[1]])
                        score += 10
                        snakeBody.append([snakeHead[0], snakeHead[1]])
                        score += 10
                        snakeBody.append([snakeHead[0], snakeHead[1]])
                        score += 10
                        snakeBody.append([snakeHead[0], snakeHead[1]])
                        score += 10
                        snakeBody.append([snakeHead[0], snakeHead[1]])
                        score += 10
                        
        # Check for invalid direction changes
        if changeTo == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        elif changeTo == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"
        elif changeTo == "UP" and direction != "DOWN":
            direction = "UP"
        elif changeTo == "DOWN" and direction != "UP":
            direction = "DOWN"

        # Move the snake
        if direction == "LEFT":
            snakeHead[0] -= blockSize
        elif direction == "RIGHT":
            snakeHead[0] += blockSize
        elif direction == "UP":
            snakeHead[1] -= blockSize
        elif direction == "DOWN":
            snakeHead[1] += blockSize

        # Check for collisions with walls
        if snakeHead[0] < 0 or snakeHead[0] >= screenWidth or \
           snakeHead[1] < 0 or snakeHead[1] >= screenHeight:
            gameOver = True

        # Check for collisions with snake's own body
        for block in snakeBody[1:]:
            if snakeHead[0] == block[0] and snakeHead[1] == block[1]:
                gameOver = True

        # Check for collisions with food
        if snakeHead[0] == foodPos[0] and snakeHead[1] == foodPos[1]:
            snakeBody.append([snakeHead[0], snakeHead[1]])
            foodPos = [random.randrange(0, screenWidth - blockSize, blockSize),
                random.randrange(0, screenHeight - blockSize, blockSize)]
            score += 10
            
        
        # Move the snake body
        snakeBody.insert(0, list(snakeHead))
        snakeBody.pop()


        # Render the game
        screen.fill(colourBackground)
        n = 0
        for block in snakeBody:
            pygame.draw.rect(screen, colourSnakeArray[n % len(colourSnakeArray)], [block[0], block[1], blockSize, blockSize])
            n+=1
        pygame.draw.rect(screen, colourFood, [foodPos[0], foodPos[1], blockSize, blockSize])
        displayScore(score)
        pygame.display.update()

        # Update the game clock for consistent frame rate
        clock.tick(snakeSpeed)

    # End the game and call quit
    pygame.quit()
    quit()

# Start the game
game()
