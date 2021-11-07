#Turtle Draw 

# By Jaylen Johnson
#Credit to Prof. Pogue & Dr. Klump

import turtle
import math

Answer = input('Please Enter, turtle-draw.txt, to begin program.\n ')


TEXTFILENAME = 'turtle-draw.txt'


turtleBoarder = turtle.Screen()
turtleBoarder.setup(450, 450)

print('TurtleDraw')

TEXTCODE = Answer
turtleDraw = turtle.Turtle()
turtleDraw.speed(10)
turtleDraw.penup()



print('Reading a text file line by line')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()

totalDistance = 0
previousPoint = [0,0]



while line:
    print(line, end= '')
    parts = line.split(' ')

    if (len(parts) ==3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        currentPoint = [x,y]
        totalDistance = totalDistance + math.dist(previousPoint, currentPoint)
        print (math.dist(previousPoint, currentPoint))
        print (previousPoint)
        print (currentPoint)
        print ('Total Distance=' + str(totalDistance))

        previousPoint = currentPoint


        turtleDraw.color(color)
        turtleDraw.goto(x,y)
        turtleDraw.pendown()
        




    if (len(parts) ==1):
        turtleDraw.penup()



    line = turtleDrawTextfile.readline()

turtle.done()
input("\nPress 'Enter' to close the Application..." )
turtleDrawTextfile.close()


print('\nEnd')