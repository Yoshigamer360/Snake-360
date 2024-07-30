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
