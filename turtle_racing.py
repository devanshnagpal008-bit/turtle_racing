import turtle 
import time
import random

WIDTH , HEIGHT = 500 , 500 # define the dimensions of the racing screen
colours=['red','green','blue','orange','brown','black','pink','purple','cyan','yellow'] # define list of colours for the turtles


def get_racers():  # get input for number of turtles
    racers=int(input("enter the number of turtles to race (2-10) : "))
    if racers<2 or racers>10:
        print("enter valid number of racers between 2 and 10 . ")
        get_racers()
    return int(racers)

def init_race(): # initiate the graphical racing interface
    screen=turtle.Screen()
    screen.setup(WIDTH , HEIGHT)
    screen.title("Turtle Racing")

def race(colours): # make the turtles race and decide the winner
    turtles=create_turtles(colours)

    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)

            x ,y =racer.pos()
            if y >= HEIGHT //2 - 10:
                return colours[turtles.index(racer)]
        
    
    

def create_turtles(colours):  # create and allot colours to the turtles
    turtles=[]
    for i , color in enumerate(colours):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos((-200/(racers+1))*(i+1),-200)
        racer.pendown()
        turtles.append(racer)
    return turtles   

racers=get_racers()
init_race()

random.shuffle(colours)# shuffle colours so that each turtle gets a randomised colour
colours=colours[:racers]
winner=race(colours)
print (f" {winner} turtle won the race!!!!")
time.sleep(5) # gives 5 second before closing the screen to observe the winner






