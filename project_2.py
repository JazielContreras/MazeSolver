#Jaziel Contreras | Project 2 | 11/27/2019
#
#This program is designed to navigate it's way through a maze from the startpoint 'S' to the endpoint 'E'.
#
#Algorithm/Psuedocode
#
#In this program six different functions are used to navigate through a maze. The printmaze function is used to take a variable called maze and it uses a for loop to
#iterate through the contents of maze and join them into a string called mazestr. This function will print out the maze that is given. The next function that was used was the
#startpoint function. this function takes in a variable called maze. A value called row_count and column_count are defined as zero. The function then uses nested for loops
#to go through the maze element by element changing row and column accordingly based on its iteration. The function then checks to see if the element at the given row and column is an "S".
#If no startpoint is found in the maze the program will return -1,-1 which will trigger an error statement in the main function otherwise it will return the row and column the 'S' is at.
#The next function that I used is called mazemovement. This function takes in three values called maze, row and column. The function then executes the code within it while
#maze at point row,column doesn't equal an "E". The function checks to see if maze at position (row,column) is an "S". If it is then the function will change the position at which
#you are currently at within the maze without writing over the "S". If the position you're currently at isn't an "S" then the function will jump into another if block where it will check
#for white space above, below, to the right and left of it. The space you are currently at is then filled with a character indicating what direction you will be moving to. The program then checks to see if you have encountered a dead end by checking
#if there are any characters such as #, ., <, >, v, or ^ in its surrounding. If there are then the backtracking will be used. In the backtracking the program checks to see if there is a
#character facing you in any of the four directions surrounding your current position. If there is something that is facing you then you set your current position to a point and jump onto the next available element.
#The program will then change column or row depending on which way you are moving relative to the maze. The program then prints the maze and prints some lines of white space to
#distinguish between the different mazes. The next function I used was the endpoint function. In this function two for loops iterate through the maze element by element searching for an 'E'. If
#no 'E' is found then the function will return -1,-1 which will print out an error in the main function otherwise it will return the columna and row that the 'E' was at.
#The next function I used was to check to make sure that the maze solver would stay within the boundaries
#of the maze. The checkbounds function takes in a row, column and maze. The function checks to make sure that the row and column are within the boundaries of the maze.
#If you're within the boundaries of the mazethen the function returns True otherwise it will return False.
#The final function is the main function where the maze that is being used is defined. The function takes in a file as input. If the file doesn't exist then the program will
#not run and an error statement will be printed out. The function then checks to make sure that the maze doesn't contain any invalid character.
#If the maze contains invalid characters then the function prints out an error stating the line the invalid character is in and what the
#invalid character is. The function also checks to make sure that the file isn't empty, if it is then an error is printed out stating that the
#file contains no maze. The function also calls the startpoint and endpoint function in order to verify that there is a start and end point. If there is no start point or endpoint
#then the function prints out an error. If no errors are found then the program will
#run. The function then calls the mazemovement function in order to solve the maze.

def main():
      try:
            file=input("Enter the file name: ")                                                 #Takes in a file as input
            mazeto = []                                                                         #An empty list that will end up being the list that contains the contents of the maze
            blocks = ["#"," ","S","E"]                                                          #Valid characters that can be used in the maze
            row = 0
            check = 0                                                                           #Used as a validity check
            filename=open(file,'r')                                                             #Opens the file that the user input
            for line in filename:                                                               #Iterates through the lines in the file
                  l1 = list(line)                                                               #Creates a list of the characters in the line
                  if(l1[-1] == '\n'):                                                           #Checks to see if 
                     l1 = l1[:-1]
                  if check == 1:                                                                #If the program already found an invalid character then it will break out of the for loop
                        break
                  for char in l1:
                        if not(char in blocks):
                              print("Error: Maze contains invalid characters. Line",row,"contains invalid character \'"+char+"\'")
                              check+=1
                              break      
                  mazeto.append(l1)                                                             #Appends the contents of l1 into an empty list called mazeto
                  row += 1                                                                      #One is added to row after each iteration in the for loop
            if row==0:
                  print("Error: Specified file contains no maze.")
            elif check != 1:                                                                    #If an invalid character wasn't found than this block will run
                  row,column=startpoint(mazeto)
                  endrow,endcolumn=endpoint(mazeto)
                  if (row == -1 and column == -1):                                              #Checks to see if row and column is -1. This means that no S was found
                        print("Error: No start position found.")
                  elif (endrow == -1 and endcolumn == -1):                                      #Checks to see if endrow and endcolumn is -1. This means that no E was found
                        print("Error: No end position found.")
                  else:                                                                         #If no errors were found in the maze then the maze solver will run.
                        row,column=startpoint(mazeto) 
                        mazemovement(mazeto,row,column)                                         #Runs the maze solver if no errors are found in the maze
            filename.close()                                                                    #Closes the file
            
      except FileNotFoundError:                                                                 #If no file is found then this error statement is printed out
            print("Error: Specified file does not exist.")

           
def printmaze(maze):
      mazestr=""
      for row in maze:                                                                    #Iterates through each line of the maze
            temp_1="".join(row)                                                           #Joins the characters in the list as one line and saves it in the row variable
            mazestr=mazestr+"\n" + temp_1                                                 #All the lines of the maze are stored into a string in order to speed up the printing process.
      print(mazestr+"\n")                                                                 #Prints out the maze            

def startpoint(maze):
      row_count=0
      for i in maze:                                                                      #Iterates through the rows in the maze
            column_count=0
            for j in i:                                                                   #Iterates through the columns in the maze
                  if j=="S":                                                              #Checks to see if the position that for loops are at is an "S"
                        return row_count,column_count                                     #Returns the index of the row and column at which the start of the maze is
                  column_count+=1                                                         #Adds one to the index of the column of the maze
            row_count+=1                                                                  #Adds one to the index of the row of the maz
      return -1,-1

def mazemovement(maze,row,column):
      blocks = ["#", "^","<",">","v","."]
      while(maze[row][column]!="E"):                                                      #Executes everything within the function while maze[row][column] doesn't equal "S"
            if maze[row][column]=="S":                                                    #If your current position is an S then it will not write over the S
                  if checkBounds(maze, row, column - 1):                                  #Checks to make sure that you are staying within the boundaries of the maze
                        if maze[row][column-1]==" ":                                      #Checks to the left of the current position
                              column-=1                                                   #Moves the current position of the maze over to the left by one
                              printmaze(maze)                                             #Prints the maze
                              continue                                                    #Continues back up to the loop continuation condition
                  if checkBounds(maze, row-1, column):
                        if maze[row-1][column]==" ":                                      #Checks above your current position
                              row-=1                                                      #Moves your current position over to the left by one
                              printmaze(maze)
                              continue
                  if checkBounds(maze, row+1, column):                                    #Checks to make sure that you are staying within the boundaries of the maze
                        if maze[row+1][column]==" ":                                      #Checks below the current position
                              row+=1                                                      #Moves the current position down by one
                              printmaze(maze)
                              continue
                  if checkBounds(maze, row, column+1):                                    #Checks to make sure that you are staying within the boundaries of the maze
                        if maze[row][column+1]==" ":                                      #Checks to the right of the current position
                              column+=1                                                   #Moves the current position to the right by one
                              printmaze(maze)
                              continue
                  print("Error: No route could be found from start to end. Maze unsolvable.")   #If the program ends up back at S and you can't move anywhere this error will print out.
                  break
            
            if maze[row][column]!="S":                                                          #If your current position isn't an S this block will run
                  if checkBounds(maze, row, column - 1):
                        if maze[row][column-1]==" " or maze[row][column-1]=="E":                #Checks to see if space to left is blank space or an "E"
                              maze[row][column]="<"                                             #Changes current position to indicate that it is moving left
                              column-=1                                                         #Moves the current position to the left
                              printmaze(maze)
                              continue                                                          #Prints the maze
                  if checkBounds(maze, row-1, column):
                        if (maze[row-1][column]==" ") or (maze[row-1][column]=="E"):            #Checks to see if the space above is blank space or an "E"
                              maze[row][column]="^"                                             #Changes the current position to indicate that it is moving up
                              row-=1                                                            #Moves the current position up by one
                              printmaze(maze)
                              continue
                  if checkBounds(maze, row+1, column):                                          #Checks to see if you are staying within the bounds of the maze
                        if (maze[row+1][column]==" ") or (maze[row+1][column]=="E"):            #Checks to see if the space below is blank spare or an "E"
                              maze[row][column]="v"                                             #Changes current position to a v to indicate that it is going down
                              row+=1                                                            #Moves the current position down by one
                              printmaze(maze)
                              continue
                  if checkBounds(maze, row, column+1):
                        if (maze[row][column+1]==" ") or (maze[row][column+1]=="E"):            #Checks to see if right space is blank or an "E"
                              maze[row][column]=">"                                             #Changes current position to a > to indicate that it is going to the right
                              column+=1                                                         #Moves the current position in the maze over to the right by one
                              printmaze(maze)
                              continue
                        
                  ##Backtracking     
                  if checkBounds(maze, row, column - 1):                                        #Checks to see if this position in the maze is within the bounds of the maze
                        if (maze[row][column-1] == ">" or maze[row][column-1] == "S"):          #Checks to the left of your current position for a > or a S
                              maze[row][column]="."                                             #Changes your current position to a dot
                              column-=1                                                         #Changes your current position by one to the left
                              printmaze(maze)                                                   #Prints the maze
                              continue                                                          #Continues to the while loop
                        
                  if checkBounds(maze, row-1 , column):                                         #Checks to make sure you are staying within the boundaries of the maze.
                        if (maze[row-1][column] == "v" or maze[row-1][column] == "S"):          #Checks above your current position for a ^ or a S
                              maze[row][column]="."                                             #Replaces current position with a dot.
                              row-=1                                                            #Changes row by -1 meaning you will move up a row
                              printmaze(maze)
                              continue
                  if checkBounds(maze, row, column+1):                                          #Checks to make sure that you are staying within the boundaries of the maze
                        if (maze[row][column+1] == "<" or maze[row][column+1] == "S"):          #Checks to the right of your current position for a <  or a S
                              maze[row][column]="."                                             #Replaces current position with a dot.
                              column+=1                                                         #Moves your current position over to the right by one
                              printmaze(maze)
                              continue
                  if checkBounds(maze, row+1, column):
                        if (maze[row+1][column] == "^" or maze[row+1][column] == "S"):          #Checks below your current position for a ^ or a S
                              maze[row][column]="."                                             #Replaces current position with a dot
                              row+=1                                                            #Changes the row by 1. Making it a row below
                              printmaze(maze)
                              continue                                                          #Continues back to loop continuation condition

def endpoint(maze):
      row_count=0
      for i in maze:                                                                      #Iterates through the rows in the maze
            column_count=0
            for j in i:                                                                   #Iterates through the columns in the maze
                  if j=="E":                                                              #Checks to see if the position that for loops are at is an "E"
                        return row_count,column_count                                     #Returns the index of the row and column at which the start of the maze is
            
                  column_count+=1                                                         #Adds one to the index of the column of the maze
            row_count+=1                                                                  #Adds one to the index of the row of the maz
      return -1,-1                                                                        #Returns -1,-1 if no E is found


def checkBounds(maze, row, column):
      if((row>=0 and row < len(maze)) and (column >=0 and column < len(maze[0]))):        #Checks to see if the current row in the maze is within the length of the maze. Also checks to see if current column is within the boundaries of the maze.
            return True                                                             
      else:
            return False
      
main()
