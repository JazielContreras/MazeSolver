# MazeSolver
Python program that solves maze that comes from .dat files

This program is designed to navigate it's way through a maze from the startpoint 'S' to the endpoint 'E'.
Algorithm/Psuedocode
In this program six different functions are used to navigate through a maze. The printmaze function is used to take a variable called maze and it uses a for loop to
iterate through the contents of maze and join them into a string called mazestr. This function will print out the maze that is given. The next function that was used was the
startpoint function. this function takes in a variable called maze. A value called row_count and column_count are defined as zero. The function then uses nested for loops
to go through the maze element by element changing row and column accordingly based on its iteration. The function then checks to see if the element at the given row and column is an "S".
If no startpoint is found in the maze the program will return -1,-1 which will trigger an error statement in the main function otherwise it will return the row and column the 'S' is at.
The next function that I used is called mazemovement. This function takes in three values called maze, row and column. The function then executes the code within it while
maze at point row,column doesn't equal an "E". The function checks to see if maze at position (row,column) is an "S". If it is then the function will change the position at which
you are currently at within the maze without writing over the "S". If the position you're currently at isn't an "S" then the function will jump into another if block where it will check
for white space above, below, to the right and left of it. The space you are currently at is then filled with a character indicating what direction you will be moving to. The program then checks to see if you have encountered a dead end by checking
if there are any characters such as #, ., <, >, v, or ^ in its surrounding. If there are then the backtracking will be used. In the backtracking the program checks to see if there is a
character facing you in any of the four directions surrounding your current position. If there is something that is facing you then you set your current position to a point and jump onto the next available element.
The program will then change column or row depending on which way you are moving relative to the maze. The program then prints the maze and prints some lines of white space to
distinguish between the different mazes. The next function I used was the endpoint function. In this function two for loops iterate through the maze element by element searching for an 'E'. If
no 'E' is found then the function will return -1,-1 which will print out an error in the main function otherwise it will return the columna and row that the 'E' was at.
The next function I used was to check to make sure that the maze solver would stay within the boundaries
of the maze. The checkbounds function takes in a row, column and maze. The function checks to make sure that the row and column are within the boundaries of the maze.
If you're within the boundaries of the mazethen the function returns True otherwise it will return False.
The final function is the main function where the maze that is being used is defined. The function takes in a file as input. If the file doesn't exist then the program will
not run and an error statement will be printed out. The function then checks to make sure that the maze doesn't contain any invalid character.
If the maze contains invalid characters then the function prints out an error stating the line the invalid character is in and what the
invalid character is. The function also checks to make sure that the file isn't empty, if it is then an error is printed out stating that the
file contains no maze. The function also calls the startpoint and endpoint function in order to verify that there is a start and end point. If there is no start point or endpoint
then the function prints out an error. If no errors are found then the program will
run. The function then calls the mazemovement function in order to solve the maze.
