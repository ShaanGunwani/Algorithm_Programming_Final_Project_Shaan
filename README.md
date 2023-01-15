# Algorithm_Programming_Final_Project_Shaan


#Brief Description

The code is a simple implementation of the classic game Snake using the Pygame library and Python. The code defines two classes, "cube" and "snake," which handle the creation and movement of the snake, as well as drawing the snake on the screen.

The "cube" class is defined first, and it has some class level variable like "rows" which is used to define the number of rows in the screen, "w" which is used to define the width of the screen and some instance level variables like "pos" which is used to store the position of the cube, "dirnx" and "dirny" which are used to store the direction of movement of the cube in the x and y axis respectively, "color" which is used to store the color of the cube. The class also has an init method which initializes the instance variables with default or passed values. There is also a method called "move" which updates the position of the cube based on the direction of movement. And there is a method called "draw" which is used to draw the cube on the screen.

The "snake" class is defined next, which has some class level variables like "body" which is used to store the cubes of the snake and "turns" which is used to store the turns taken by the snake. And some instance level variables like "color" which is used to store the color of the snake, "head" which is used to store the head of the snake and "dirnx" and "dirny" which are used to store the direction of movement of the snake. The class also has an init method which initializes the instance variables with default or passed values, it also creates the head of the snake and appends it to the body. There is a method called "move" which updates the position of the snake based on the direction of movement and user input.

Additionally, the code also uses the Tkinter library to handle user input and the Pygame library to draw the game on the screen. The game can be controlled with the arrow keys and ends when the snake runs into a wall or itself.


math: This module provides mathematical functions and constants
random: This module provides functions for generating random numbers
pygame: This module is a set of Python modules designed for writing games. It is built on top of the SDL library, which provides low-level access to audio, keyboard, mouse, and display functions.
tkinter: This module provides a powerful object-oriented interface for creating graphical user interfaces (GUIs) in Python.
messagebox: This module provides an easy way to display message boxes in tkinter
