# Algorithm_Programming_Final_Project_Shaan


# Description

The code is an implementation of a Snake game using the Pygame library and Python. The code defines two classes, "cube" and "snake," which handles the creation and movement of the snake, as well as drawing the snake on the screen.

The "cube" class is defined first, and it has some class level variable like "rows" which is used to define the number of rows in the screen, "w" which is used to define the width of the screen and some instance level variables like "pos" which is used to store the position of the cube, "dirnx" and "dirny" which are used to store the direction of movement of the cube in the x and y axis respectively, "color" which is used to store the color of the cube. The class also has an init method which initializes the instance variables with default or passed values. There is also a method called "move" which updates the position of the cube based on the direction of movement. And there is a method called "draw" which is used to draw the cube on the screen.

The "snake" class is defined next, which has some class level variables like "body" which is used to store the cubes of the snake and "turns" which is used to store the turns taken by the snake. And some instance level variables like "color" which is used to store the color of the snake, "head" which is used to store the head of the snake and "dirnx" and "dirny" which are used to store the direction of movement of the snake. The class also has an init method which initializes the instance variables with default or passed values, it also creates the head of the snake and appends it to the body. There is a method called "move" which updates the position of the snake based on the direction of movement and user input.

Additionally, the code also uses the Tkinter library to handle user input and the Pygame library to draw the game on the screen. The game can be controlled with the arrow keys and ends when the snake runs into a wall or itself.

# Use Case Diagram

![image](https://user-images.githubusercontent.com/114371881/212548874-021ccfd9-e3ab-4b6d-bb10-3ad6d9c4000f.png)

# Activity Diagram

![image](https://user-images.githubusercontent.com/114371881/212548933-8dfbd512-eeb1-4eb1-9e24-191713763671.png)


# Class Diagram

![image](https://user-images.githubusercontent.com/114371881/212548795-a1c1c111-b89a-415f-a0f0-7945d5497716.png)

The cube class has a one-to-many relationship with the snake class, which means that one cube object is used in multiple snake objects.
The snake class has a many-to-one relationship with the cube class, which means that multiple snake objects are composed of one cube object.
The pygame and tkinter classes have a one-to-one relationship with the cube and snake classes, which means that the pygame and tkinter classes are used to create the cube and snake classes.

In the class diagram, the multiplicities show the relationship between the classes and the number of objects involved in that relationship. For example, the multiplicity between the snake class and the cube class is represented as "1..*" because a snake object can have multiple cube objects (its body), but each cube object can only belong to one snake object.

The multiplicities in the diagram are:

The snake class has an attribute head of type cube, the multiplicity here is represented as 1..1, meaning that a snake object has exactly one cube object as its head.
The snake class has an attribute body of type List of cube, the multiplicity here is represented as 0..* , meaning that a snake object can have zero or more cube objects as its body.

# Modules
1. math: This module provides mathematical functions and constants

2. random: This module provides functions for generating random numbers

3. pygame: This module is a set of Python modules designed for writing games. 

4. tkinter: This module provides a powerful object-oriented interface for creating graphical user interfaces (GUIs) in Python.

5. messagebox: This module provides an easy way to display message boxes in tkinter

# Essential Algorithms
1. The move() method in the snake class: This method updates the position of the snake's body based on user input. It uses an event loop to listen for user input and updates the position of the snake's head and body accordingly.
2. The draw() method in the cube class: This method is responsible for rendering the snake's body on the screen. It uses the Pygame library to draw rectangles on the screen, which represent the snake's body.
3. The collision detection algorithm: This algorithm is used to detect when the snake collides with the walls or its own tail. It uses the current position of the snake's head and compares it to the positions of the walls and the snake's body.
4. The food placement algorithm: This algorithm is responsible for placing the food on the screen in a random location. It uses the random module to generate random coordinates for the food.
5. The game loop algorithm: The game loop is the main algorithm that controls the flow of the game. It repeatedly calls the move, draw, and collision detection methods, updates the game state, and renders the updated game state on the screen.


# Screenshot of the game
![image](https://user-images.githubusercontent.com/114371881/212542982-de8d921b-26a8-454e-936c-866c40bcc20f.png)


# Lesson learned/ Reflection

1. Understood the basics of game development: Creating a Snake game using Pygame library made me understand the basics of game development such as game loops, etc.

2. Familiarizing with Pygame library: By working with Pygame, I learnt about the different modules it provides for creating games such as handling input, etc.

3. Writing clean and maintainable code: As the game became more complex, I learnt how to write clean and maintainable code in order to easily update and debug the game.

4. Understood the importance of collision detection: Collision detection is a fundamental aspect of many games, understanding its importance was crucial for creating interactive games.

5. Understood the importance of game loops: Game loops are the backbone of any game, it was important to understand how they work and how to optimize them to improve performance.

6. Debugging and troubleshooting: As I worked on the game, I encountered bugs and errors. By debugging and troubleshooting the code, I learnt how to identify and fix issues in my code.

7. Understood the importance of testing and debugging: To improve the game, it was important to test and debug the code to find and fix bugs, as well as to improve performance.

8. Understood how to use libraries and modules: The python code uses several modules such as pygame, tkinter, random and math for certain functionality, understanding the use of these libraries and modules was crucial for creating a successful game.

9. Understood object-oriented programming: The code uses object-oriented programming concepts such as classes, objects, and inheritance. By working with these concepts, I learnt how to structure your code in a clear and organized way.

10. Understood the importance of game design: A good game design is important to make the game more enjoyable, the code has a good design in terms of the game flow and logic.

11. Understood the importance of user interaction: Games are interactive, I understood how to handle user input and how to use it to update the game state.

12. Understood the importance of game performance: The game performance is important for the user experience, understanding how to optimize the game performance through code optimization and debugging is crucial.

# Video Demo 3 minutes

https://app.screencast.com/kfbmGAl4cC4TP?conversation=MmLQqS1ELsG2cvlpwLpy1R
