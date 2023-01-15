import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


# There are two main objects:- Cube and Snake Objects.
# Snake object is going to contain a bunch of cube objects.
# Red squares in the game that is moving around is the cube objects and the whole thing is the snake object.
class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        # dirnx = 1 to make sure start moving right when we run the program. So, setting it with direction x
        # If dirnx = 0, had to click a key before snake starts moving
        # These are optional because when creating new cue object we don't have to implicitly say direction x is 1 and direction y is 0 because it's assumed its always going to be like that
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        # This is because there is snack for snake to collect. So to change the color
        # Since, changing direction x and y in the snake class, need to do it here so it stays with the object

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
        # self.pos[1] is the existing y value
        # self.pos[0] is the already existing position

    def draw(self, surface, eyes=False):
        # Distance between each x and each y value
        # If draw in pygame, it draws in top left hand corner of object
        # Draw cube, figure out x and y values for each cube when drawing to screen
        dis = self.w // self.rows
        # Same thing did when drawing grid to get distance between x and y values
        # dis is distance which is the gap
        i = self.pos[0]  # row
        j = self.pos[1]  # column
        # i is row and j is column

        # Draw rectangle
        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        # This is rectangle with x, y, width, height
        # This +1s and -2s here is to see the grid when drawing rectangle
        # Because if we were to draw with exactly the dimensions of the dis distance, we'd  cover white lines and will be weird
        # -2 just so drawing inside the square little bit
        if eyes:  # Draw eyes
            centre = dis // 2  # Middle of cube
            radius = 3
            circleMiddle = (
                i * dis + centre - radius, j * dis + 8)  # j*dis+8 find out random x by pputting 8 pixels up everytime
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            # Draw two circles based on circleMiddle and circleMiddle2 and the radius and color black
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class snake(object):
    # Going to have a list of cubes known as snake body
    # Create a list
    # In this list, can draw things, can move, can check, and want all our cubes to be ordered within list
    # That's why I put it first
    body = []
    turns = {}  # A set

    def __init__(self, color, pos):
        self.color = color
        # The head of the snake which is important because need to know where it is at all times so can move
        # accordingly is equal to a cube at the given position
        # The given position is the starting position of the snake
        self.head = cube(pos)
        # Append to the body the head
        self.body.append(self.head)
        # Have a direction for x and y respectively for moving snakes
        # If y or x is equal to 1 or -1 then other one will be 0 because can only move at one direction at same time
        # This keeps track of what direction we're moving in
        self.dirnx = 0
        self.dirny = 1

    # If you have one object moving around the screen, getting it to go left, straight, right
    # But snake object, has to turn at certain points
    # When clicked left, rest of the snake is still moving forward only when it reaches the point where head turned left, then it will turn.
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()  # A dictionary that has all the key values and if they were pressed or not

            # This for loop is going to give all of the keys and 1 or 0 values if they were clicked or not
            for key in keys:
                # Change direction according to what key clicked
                if keys[pygame.K_LEFT]:
                    # If going left, x negative to move more towards 0
                    # As the way coordinates work in pygame is in top left hand corner of screen is 00
                    self.dirnx = -1
                    self.dirny = 0
                    # Because don't want to be moving in two directions at once and go diagonal
                    # Need to remember where actually turned so the tail of cube can turn at that point
                    # Because if have multiple cubes, then need to turn left, right
                    # Add a key which is the current position of snake head and set equal to what direction turned
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    # If going right, x positive which is 1 for this as only moving 1 cube at a time to go more to right
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        # Move the cube
        # In this loop it moves all objects for us
        for i, c in enumerate(self.body):  # Look through the list of positions that we have on stake
            # i=index, c=cube object
            # Get the index and cube object in self.body(made up of cube objects (line 31))
            # For each c, grab the position (p) and see if position in turn list
            # Create and add to the turn list when clicked
            p = c.pos[:]  # Makes a copy so not changing position of snake
            if p in self.turns:  # Added position of head to turns, in this if statement if position in turns, then turn
                turn = self.turns[p]  # Actual turn (where actually moving) = turns list at index
                # Grab the turn at direction x and y which stored there
                c.move(turn[0], turn[1])  # Cube.move and giving it direction x and y which is turn[0] and turn[1]
                if i == len(self.body) - 1:
                    self.turns.pop(p)  # Remove it

            # If position not in list, still need to move snake because it's constantly moving
            else:
                # Checking whether reached the edge of the screen
                # Moving left and position so x position of cube <= 0 then change position, goes to right side of screen
                # Can do that by c.rows-1 because if start counting at 0 in computers if rows=20 then last cube=19
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                # Otherwise check if moving right and at the edge of the screen(c.rows-1), move back to the left side by putting 0
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                # If going down, checking less than or more than rows -1. If yes, move back to screen top (c.pos[0]) by changing y value to 0
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                # Same thing below if moving upwards
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                # If none is true, if not at screen edge, then move cube at direction x, y of the cube
                # If cube moving upwards, it's not turning, it's not going to screen edge, don't need to change
                # Keep moving at whatever direction it's going
                else:
                    c.move(c.dirnx, c.dirny)  # Not changing anything just move forward

    def reset(self, pos):
        # Get rid of turns and body and change direction x and y
        # Set new head which is equal to whatever position been given because can move at different position
        self.head = cube(pos)
        # Clearing self.body which is the class variable
        self.body = []
        # Adding head
        self.body.append(self.head)
        # Set turns equal to blank
        self.turns = {}
        # Direction x is 0 and y is 1 to start moving
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        # Where to add the snack or cube to the list
        # First, figure out where tail is
        tail = self.body[-1]  # -1 for last element in that list
        dx, dy = tail.dirnx, tail.dirny  # dx, dy is direction x and y

        # This loop below is going to check in what direction cube currently moving in
        # Then can make sure that when adding the cube, we know where to add it
        # So for adding to right, left, above or below the cube, can give correct direction to be moving
        if dx == 1 and dy == 0:
            # Append new cube to body, and it's position (here to the right because x = 1) is 1 less than x position of that tail
            # Whatever the last cube is, 1 less than that so that we don't add a cube to the right when moving to right
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            # Same thing here when moving left, need to add cube to right side
            # So one plus that tail of the x position of the snake so we can have it in proper position
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            # Same thing here with x and y
            # With y when moving up or down, we add it above otherwise put it below
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        # Set the direction for cube, if just left it like that it wouldn't be moving anywhere
        # Just need to change to the current direction of the tail
        # Wherever the tail is moving that's where the new cube is going to be moving in that direction
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy  # Where tail is moving at the current moment

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)  # When we draw the first snake object we add eyes to see the head
                # 'True' says to draw eyes if it's the first one, which is head, in the list
            else:
                c.draw(surface)


# Functions

def drawGrid(w, rows, surface):
    # When drawing grid, should figure out how big each square is going to be
    # Just draw lines going down and across
    # Figure out the gap between each lines

    # Variable size between = width divided by rows
    sizeBtwn = w // rows  # To not get large decimal numbers because that cannot be passed to draw line method

    x = 0
    y = 0
    # l is standing for lines
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        # Draw two lines for every loop of the for loop
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))  # Vertical line
        # for (x,0), change x but keep y at 0
        # for (x,w), stay at same x, keep y at screen width
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))  # Horizontal line
        # for (0,y), x at 0 but y will change
        # The argument is the surface and color is white
        # The (x,0), (x,w), (0, y) and (w, y) arguments are the start and end positions of line


def redrawWindow(surface):
    # Use global for reference
    global rows, width, s, snack
    # Fill the screen with black color
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    # Draw the grid and pass it out the same surface that were given
    drawGrid(width, rows, surface)
    # Update the display
    pygame.display.update()


def randomSnack(rows, item):  # item is snake object
    # For snake to eat
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            # Going to get a list of a filtered list
            # See if any of the positions are same like the current position of snake
            # Make sure not put snack on top of snake (Chances high if have long snake)
            # Using this can loop through every position in list, check against x and y and see if it's same. If same, continue else break and return
            continue
        else:
            break

    return (x, y)


def message_box(subject, content):
    # Creating a message box in pygame that shows up on top of the screen(that don't float below it or show up right away)
    root = tk.Tk()  # New tkinter window
    root.attributes("-topmost", True)  # Make sure window is on top of anything
    # If have bunch of different windows open, it just comes up on top
    root.withdraw()  # Make window invisible
    messagebox.showinfo(subject, content)  # Just shows info given whatever subject and content typed in
    try:
        root.destroy()  # Constantly keeps trying to destroy message box until x button is clicked
    except:
        pass


# Main loop
def main():
    # Use global so no need to pass everytime when drawing a grid
    global width, rows, s, snack
    # Variables (Do not need to use height variable because just going to draw a square surface everytime)
    # (Do not  need two variables for width and height as going to contain the same number)
    width = 500
    # The rows' value should divide 500 evenly otherwise, the rows will be looking weird
    rows = 20  # If set it to 10 for example then there won't be too much room for the snake to move around
    # And the game will go faster

    # Make a surface
    win = pygame.display.set_mode((width, width))
    # Make a snake object and give it a color which is red(255)
    s = snake((255, 0, 0), (10, 10))
    # Use the random snack function
    snack = cube(randomSnack(rows, s), color=(0, 255, 0))
    # snack = another cube as want to have same functionality, want to draw, and move it around so create new object
    # Give it a position of random snack and give it row and item which is s and change color to green

    flag = True  # Variable flag

    clock = pygame.time.Clock()

    while flag:
        # pygame tick
        pygame.time.delay(50)
        # Delay 50 milliseconds everytime so that the program doesn't run too fast
        # The lower this goes, the faster it's going to be
        clock.tick(10)
        # It is going to make sure that the game doesn't run more than 10 frames per second
        # The snake would be able to move 10 blocks in one second
        # To not be that fast, I am delaying it also by a few milliseconds
        # The lower this goes, the slower it's going to be
        # Call s.move, which is the snake object, everytime the main loop runs
        # Goingto go up to that method in snake and going to check everytime run the loop, if key is pressed if yes, move accordingly
        s.move()
        # Check if snake head has hit the snack, if yes, then add another part to the snake body, otherwise not going to do that
        if s.body[0].pos == snack.pos:  # Both are cube objects
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                # Looping through every cube in snake body
                # Check if position s.body[x].pos is in list of all the positions
                # This is how I am checking the collisions
                print('Score: ', len(s.body))
                message_box('You Lost! :(', 'Play again')
                s.reset((10, 10))  # Reset snake and take starting position which is 10, 10
                break # Because if collided once, don't really care if collided again and go back and continue the game with snake that has length 1

        redrawWindow(win) # Call redrawWindow and give a surface = win

    pass


main()

