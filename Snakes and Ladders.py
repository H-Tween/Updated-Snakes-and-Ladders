from tkinter import *
from tkinter import messagebox
import time,os,sys,random
from tkinter import ttk



def Play():
    global playButton, quitButton1
    playButton = Button(root, text = "Play", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                        activebackground = rgbToColour((41, 236, 242)), command = ChoosePlayer) # creates a button called play that begins the game
    playButton.place(x=810, y=300, height = 100, width = 300)	# placement of the button
    quitButton1 = Button(root, text = "Quit", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                          activebackground = rgbToColour((41, 236, 242)), command = chow)
    quitButton1.place(x=1700, y=75, height = 100, width = 125)

def rgbToColour(rgb):			# allows any colour variation to become rgb colour
    return "#%02x%02x%02x" % rgb

def ChoosePlayer():
    playButton.destroy()		# removes the button "play"
    quitButton1.destroy()
    global computerButton, playerButton, backButtonPlay
    backButtonPlay = Button(root, text = "Back", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                          activebackground = rgbToColour((41, 236, 242)), command = lambda:[Play(), computerButton.destroy(),
                                                                                            playerButton.destroy(), backButtonPlay.destroy()])	
    backButtonPlay.place(x=1700, y=75, height = 100, width = 125)
    computerButton=Button(root, text = "Against Computer", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                          activebackground = rgbToColour((41, 236, 242)), command = lambda:[setVs('Computer'), Theme()])# creates a button named "Against Computer"
    computerButton.place(x=660, y=500, height = 100, width =600)			# places the button in a certain position
    playerButton = Button(root, text = "Against Player", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                          activebackground = rgbToColour((41, 236, 242)), command = lambda:[setVs('Player'), Theme()])	# creates a button named "Against Player"
    playerButton.place(x=660, y=300, height = 100, width =600)				# places the button in a certain position												

def setVs(vsChoice):
    global vs
    vs = vsChoice
    ##print (vs)


def Theme():
    computerButton.destroy()    #removes the previous buttons
    playerButton.destroy()
    global title1, jungleButton, desertButton, volcanicButton, backButtonChoose    #allows the variables to be used in other functions
    title1 = Label(root, text = "Themes:",  font = ("Calibri", 48)) #creates title
    title1.place(x=810, y=75, height = 100, width = 300)            #places title
    backButtonChoose = Button(root, text = "Back", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                          activebackground = rgbToColour((41, 236, 242)), command = lambda:[volcanicButton.destroy(), jungleButton.destroy(), desertButton.destroy(),
                                                                                            title1.destroy(), ChoosePlayer(), backButtonChoose.destroy()])
    backButtonChoose.place(x=1700, y=75, height = 100, width = 125)
    volcanicButton = Button(root, text = "Volcanic", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                            activebackground = rgbToColour((41, 236, 242)), command = lambda:[setTheme('volcanic'), ColourCounterOne()]) #creates button for volcanic
    volcanicButton.place(x=735, y=250, height = 100, width =450)                                                                      #places button volcanic                                          
    jungleButton = Button(root, text = "Jungle", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),          
                            activebackground = rgbToColour((41, 236, 242)), command = lambda:[setTheme('jungle1'), ColourCounterOne()]) #creates button for jungle
    jungleButton.place(x=735, y=400, height = 100, width =450)                                                                      #places button jungle
    desertButton = Button(root, text = "Desert", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                            activebackground = rgbToColour((41, 236, 242)), command = lambda:[setTheme('desert'), ColourCounterOne()]) #creates button for desert
    desertButton.place(x=735, y=550, height = 100, width =450)                                                                      #places button desert

def setTheme(themeChoice):
    global theme
    theme = themeChoice 
    #print(theme)

def ColourCounterOne():
    volcanicButton.destroy()
    jungleButton.destroy()      #removes previous buttons
    desertButton.destroy()
    title1.destroy()            #removes previous title
    backButtonChoose.destroy()
    global title2, redButton, blueButton, greenButton, orangeButton, purpleButton, pinkButton                                          
    title2 = Label(root, text = "Player One\n Choose Colour Counter:",  font = ("Calibri", 48)) #creates title
    title2.place(x=575, y=50, height = 200, width = 750)            #places title
    backButtonTheme = Button(root, text = "Back", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                          activebackground = rgbToColour((41, 236, 242)), command = lambda:[redButton.destroy(), blueButton.destroy(),
                                                                                            greenButton.destroy(), orangeButton.destroy(),
                                                                                            purpleButton.destroy(), pinkButton.destroy(),
                                                                                            title2.destroy(), Theme(),
                                                                                            backButtonTheme.destroy()])
    backButtonTheme.place(x=1700, y=75, height = 100, width = 125)
    redButton = Button(root, text = "Red", font = ("Calibri", 40), background = rgbToColour((230, 21, 37)),     #creates button for red
                            activebackground = rgbToColour((255, 0, 20)), command = lambda:[setColour1('Red'), ColourCounterTwo()])                                          
    redButton.place(x=100, y=300, height=100, width=200)                                                        #places button called red
    blueButton = Button(root, text = "Blue", font = ("Calibri", 40), background = rgbToColour((18, 170, 230)),  #creates button for blue
                            activebackground = rgbToColour((0, 183, 255)), command = lambda:[setColour1('Blue'), ColourCounterTwo()])                                          
    blueButton.place(x=400, y=300, height=100, width=200)                                                       #places button called blue
    greenButton = Button(root, text = "Green", font = ("Calibri", 40), background = rgbToColour((33, 214, 13)), #creates button for green
                            activebackground = rgbToColour((27, 245, 2)), command = lambda:[setColour1('Green'), ColourCounterTwo()])                                        
    greenButton.place(x=700, y=300, height=100, width=200)                                                      #places button called green
    orangeButton = Button(root, text = "Orange", font = ("Calibri", 40), background = rgbToColour((235, 120, 5)),#creates button for orange
                            activebackground = rgbToColour((255, 127, 0)), command = lambda:[setColour1('Orange'), ColourCounterTwo()])                                       
    orangeButton.place(x=1000, y=300, height=100, width=200)                                                    #places button called orange
    purpleButton = Button(root, text = "Purple", font = ("Calibri", 40), background = rgbToColour((181, 6, 204)),#creates button for purple
                            activebackground = rgbToColour((226, 3, 255)), command = lambda:[setColour1('Purple'), ColourCounterTwo()])                                       
    purpleButton.place(x=1300, y=300, height=100, width=200)                                                    #places button called purple
    pinkButton = Button(root, text = "Pink", font = ("Calibri", 40), background = rgbToColour((212, 19, 128)), #creates button for pink
                            activebackground = rgbToColour((235, 16, 140)), command = lambda:[setColour1('Pink'), ColourCounterTwo()])                                                                                 
    pinkButton.place(x=1600, y=300, height=100, width=200)                                                      #places button called pink

def ColourCounterTwo():
    redButton.destroy()
    blueButton.destroy()
    greenButton.destroy()
    orangeButton.destroy()
    purpleButton.destroy()
    pinkButton.destroy()
    title2.destroy()
    global title3, redButton1, blueButton1, greenButton1, orangeButton1, purpleButton1, pinkButton1, backButtonCounter1
    if vs == 'Player':
        title3 = Label(root, text = "Player Two\n Choose Colour Counter:",  font = ("Calibri", 48)) #creates title
        title3.place(x=575, y=50, height = 200, width = 750)            #places title
        backButtonCounter1 = Button(root, text = "Back", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                          activebackground = rgbToColour((41, 236, 242)), command = lambda:[redButton1.destroy(), blueButton1.destroy(), greenButton1.destroy(), orangeButton1.destroy(),
                                                                                            purpleButton1.destroy(), pinkButton1.destroy(), title3.destroy(), ColourCounterOne(), backButtonCounter1.destroy()])
        backButtonCounter1.place(x=1700, y=75, height = 100, width = 125)
        redButton1 = Button(root, text = "Red", font = ("Calibri", 40), background = rgbToColour((230, 21, 37)),     #creates button for red
                            activebackground = rgbToColour((255, 0, 20)), command = lambda:[setColour2('Red'), Board()])                                          
        redButton1.place(x=100, y=300, height=100, width=200)                                                        #places button called red
        blueButton1 = Button(root, text = "Blue", font = ("Calibri", 40), background = rgbToColour((18, 170, 230)),  #creates button for blue
                            activebackground = rgbToColour((0, 183, 255)), command = lambda:[setColour2('Blue'), Board()])                                          
        blueButton1.place(x=400, y=300, height=100, width=200)                                                       #places button called blue
        greenButton1 = Button(root, text = "Green", font = ("Calibri", 40), background = rgbToColour((33, 214, 13)), #creates button for green
                            activebackground = rgbToColour((27, 245, 2)), command = lambda:[setColour2('Green'), Board()])                                        
        greenButton1.place(x=700, y=300, height=100, width=200)                                                      #places button called green
        orangeButton1 = Button(root, text = "Orange", font = ("Calibri", 40), background = rgbToColour((235, 120, 5)),#creates button for orange
                            activebackground = rgbToColour((255, 127, 0)), command = lambda:[setColour2('Orange'), Board()])                                       
        orangeButton1.place(x=1000, y=300, height=100, width=200)                                                    #places button called orange
        purpleButton1 = Button(root, text = "Purple", font = ("Calibri", 40), background = rgbToColour((181, 6, 204)),#creates button for purple
                            activebackground = rgbToColour((226, 3, 255)), command = lambda:[setColour2('Purple'), Board()])                                       
        purpleButton1.place(x=1300, y=300, height=100, width=200)                                                    #places button called purple
        pinkButton1 = Button(root, text = "Pink", font = ("Calibri", 40), background = rgbToColour((212, 19, 128)), #creates button for pink
                            activebackground = rgbToColour((235, 16, 140)), command = lambda:[setColour2('Pink'), Board()])                                                 ####remove board and put it in second iteration                                 
        pinkButton1.place(x=1600, y=300, height=100, width=200)                                                      #places button called pink
        exec("%sButton1.config(text='Taken', background = rgbToColour((93, 94, 94)), activebackground = rgbToColour((125, 128, 128)), command='')" % player1Colour.lower())
    else:
        colours=["Red", "Blue", "Green", "Orange", "Purple", "Pink"] #array of colours
        if player1Colour in colours:
            colours.remove(player1Colour)
            print(colours)
        computerColour = random.randint(1, len(colours)) #randomly chooses a number
        #print(computerColour) #testing that the random number was chosen
        setColour2(colours[(computerColour-1)])#calls the function setColour2 and passes the colour chosen at random from the array.
        Board()
        
    
##def Confirm():
##    if vs =="Player":
##        redButton1.destroy()
##        blueButton1.destroy()
##        greenButton1.destroy()
##        orangeButton1.destroy()
##        purpleButton1.destroy()
##        pinkButton1.destroy()
##        title3.destroy()
##    global confirmButton, backButtonCounter2, title4
##    title4 = Label(root, text = "Do you wish to continue\n with these settings?",  font = ("Calibri", 48)) #creates title
##    title4.place(x=610, y=50, height = 200, width = 750)            #places title
##    confirmButton = Button(root, text = "Continue", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
##                            activebackground = rgbToColour((41, 236, 242)), command = Board()) # creates a button called play that begins the game
##    confirmButton.place(x=810, y=300, height = 100, width = 300)	# placement of the button
##    backButtonCounter2 = Button(root, text = "Back", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
##                                  activebackground = rgbToColour((41, 236, 242)), command = lambda:[title4.destroy(), confirmButton.destroy(), ColourCounterTwo(), backButtonCounter2.destroy()]) ################ do this idiot
##    backButtonCounter2.place(x=1700, y=75, height = 100, width = 125)
    
    



def setColour1(colourChoice):
    global player1Colour
    player1Colour = colourChoice
    print("Player 1 Colour:", player1Colour)

def setColour2(colourChoice):
    global player2Colour
    player2Colour = colourChoice
    print("Player 2 Colour:", player2Colour)





def Counter():
    global counterLabel, counter
    if vs == "Player":
        if counter == 2:
            counter = 1
            turn = "Player 2"
        else:
            counter = 2
            turn = "Player 1"
    else:
        if counter == 1:
            counter = 2
            turn = "Player 1"
        else:
            counter = 1
            turn = "Computer"
    counterLabel = Label(root, text = "Current turn:\n %s" % (turn), font = ("Calibri", 40))                   
    counterLabel.place(x=1110, y=75, height = 150, width = 400)
        

def Roll():
    global background_label2, img, counter, rollButton
    rollButton=Button(root, text = "Roll", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                          activebackground = rgbToColour((41, 236, 242)), command = lambda:[exec('rollButton["state"] = DISABLED'),
                                                                                            Dice(), Counter(), Facts(), exec('move%s()' % (counter))])  
    rollButton.place(x=1360, y=550, height = 100, width = 200)
    img=PhotoImage(file='1.png')
    background_label2 = Label(root, image=None)

def RollC():
    global background_label2, img, counter, rollButton1
    rollButton1=Button(root, text = "Roll", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                          activebackground = rgbToColour((41, 236, 242)), command = lambda:[exec('rollButton1["state"] = DISABLED'),
                                                                                            Dice(), Counter(), Facts(), move1(), myCanvas.after(1500, move2)])  
    rollButton1.place(x=1360, y=550, height = 100, width = 200)
    img=PhotoImage(file='1.png')
    background_label2 = Label(root, image=None)    
        

    

def Dice():
    global dice, filename2, background_label2
    dice = random.randint(1, 6)
    filename2 = PhotoImage(file = "%s.png" % (dice))
    background_label2.config(image = filename2)
    background_label2.place(x=1360, y=680)
    background_label2.image = filename2

def Quit():
    quitButton = Button(root, text = "Quit", font = ("Calibri", 40), background = rgbToColour((37, 213, 219)),
                          activebackground = rgbToColour((41, 236, 242)), command = chow)
    quitButton.place(x=1700, y=75, height = 100, width = 125)


def chow():
    root.destroy()

def Facts():
    fact = ["Russia has 11 times zones", "Bats have eco-location", "Snakes smell with their tongue", "Snakes have hundreds of ribs", "Snakes shed their skin", "Ladder accidents are common", "Chris Argyris invented the ladder"]
    randomNumber = random.randint(1, len(fact))
    #print(fact[randomNumber])
    factsLabel = Label(root, text = "Cool Facts:\n%s" % (fact[randomNumber-1]),  font = ("Calibri", 40)) #+ typingPrint(fact[randomNumber-1]) ############################problem
    factsLabel.place(x=1010, y=300, height = 200, width = 900)

    
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)                     ##########################################
    sys.stdout.flush()
    time.sleep(0.05)

def Counter_Create():
    global filenamePlayer1, myCanvas, player1
    player1Coords = coordstoXY1(player1)
    filenamePlayer1 = PhotoImage(file = "%s.png" % (player1Colour))
    myCanvas.create_image(player1Coords, image=filenamePlayer1, tag='p1')
    

def Counter_Create1():
    global filenamePlayer2, myCanvas, player2
    player2Coords = coordstoXY2(player2)
    filenamePlayer2 = PhotoImage(file = "%s.png" % (player2Colour))
    myCanvas.create_image(player2Coords, image=filenamePlayer2, tag='p2')



    

def movePlayer1():
    global myCanvas, player1, player1direction
    if player1 == [0, 0]:
        movePiece2()
    elif (player1[0] == 9 and player1[1] % 2 != 0) or (player1[0] == 0 and player1[1] % 2 == 0): #if x = 9 and y = even it moves up and the same for the other side (reaches end of board)
        myCanvas.move('p1', 0, -80) #moves the counter up
        player1[1] = player1[1] - 1 #sets the y in array to 1 less so it moves up
        player1direction = player1direction * -1 #changes the direction the counter moves
    else:
        myCanvas.move('p1', 80*player1direction, 0) #moves counter left and right
        player1[0] = player1[0] + player1direction #gives the array the correct position
    move1()

def move1():
    global dice                                                             #for i in range(dice): #moves the player by the number the dice rolled
    if dice > 0:
        dice = dice - 1
        myCanvas.after(200, movePlayer1)
    else:
        movePiece1()
    if dice == 0 and vs == "Player":
        rollButton["state"] = NORMAL
    if dice == 0 and vs == "Computer":
        rollButton1["state"] = NORMAL


def movePlayer2():
    global myCanvas, player2, player2direction
    if player2 == [0, 0]:
        movePiece2()
    elif (player2[0] == 9 and player2[1] % 2 != 0) or (player2[0] == 0 and player2[1] % 2 == 0):
        myCanvas.move('p2', 0, -80)
        player2[1] = player2[1] - 1
        player2direction = player2direction * -1
    else:
        myCanvas.move('p2', 80*player2direction, 0)
        player2[0] = player2[0] + player2direction
    move2jump()

def move2jump():
    global dice
    if dice > 0:
        dice = dice - 1
        myCanvas.after(200, movePlayer2)
    else:
        movePiece2()
    if dice == 0 and vs == "Computer":
        rollButton1["state"] = NORMAL
    if dice == 0 and vs == "Player":
        rollButton["state"] = NORMAL


def move2():
    global dice 
    if vs =="Computer":
        time.sleep(0.2)
        dice = random.randint(1,6)
        Counter()
        filename2 = PhotoImage(file = "%s.png" % (dice))
        background_label2.config(image = filename2)
        background_label2.place(x=1360, y=680)
        background_label2.image = filename2
    move2jump()
    
    




def snakes():
    global snake1, snake2, snake3, snake4, snake8, snake5
    snake1 = PhotoImage(file = "snake1.png")
    myCanvas.create_image(300, 430, image=snake1)                  
    snake2 = PhotoImage(file = "snake2.png")
    myCanvas.create_image(610, 235, image=snake2)
    snake3 = PhotoImage(file = "snake3.png")
    myCanvas.create_image(670, 630, image=snake3)
    snake4 = PhotoImage(file = "snake4.png")
    myCanvas.create_image(300, 140, image=snake4)
    snake8 = PhotoImage(file = "snake8.png")
    myCanvas.create_image(250, 745, image=snake8)
    snake5 = PhotoImage(file = "snake9.png")
    myCanvas.create_image(360, 630, image=snake5)       
    
    
def ladders():
    global ladder1, ladder2, ladder3, ladder4, ladder5
    ladder1 = PhotoImage(file = "ladder1.png")
    myCanvas.create_image(535, 430, image=ladder1)                   
    ladder2 = PhotoImage(file = "ladder2.png")
    myCanvas.create_image(855, 740, image=ladder1)
    ladder3 = PhotoImage(file = "ladder3.png")
    myCanvas.create_image(540, 515, image=ladder3)
    ladder4 = PhotoImage(file = "ladder4.png")
    myCanvas.create_image(760, 120, image=ladder4)
    ladder5 = PhotoImage(file = "ladder3.png")
    myCanvas.create_image(140, 115, image=ladder3)




##def Chance():                                                         #### a piece on the board, if a player roles the same number twice


def movePiece1():                                                      
    global player1, player1direction, rollButton, rollButton1
    if player1 == [8, 9]:               # ladder1
        player1 = [9, 7]
        messagebox.showinfo("Ladder", "You have landed on a ladder!")
        myCanvas.move('p1', 80, -160)   
    if player1 == [6, 8]:               # ladder2 
        player1 = [5, 7]
        messagebox.showinfo("Ladder", "You have landed on a ladder!")
        myCanvas.move('p1', -80, -80)
        player1direction = player1direction * -1
    if player1 == [0, 7]:               # snake1
        player1 = [3, 8]
        messagebox.showinfo("Snake", "You have landed on a snake!")
        myCanvas.move('p1', 240, 80)
        player1direction = player1direction * -1
    if player1 == [3, 6]:               # snake2
        player1 = [4, 8]
        messagebox.showinfo("Snake", "You have landed on a snake!")
        myCanvas.move('p1', 80, 160)
    if player1 == [8, 5]:               # snake3
        player1 = [7, 8]
        messagebox.showinfo("Snake", "You have landed on a snake!")
        myCanvas.move('p1', -80, 240)
        player1direction = player1direction * -1
    if player1 == [4, 5]:               # ladder3
        player1 = [5, 3]
        messagebox.showinfo("Ladder", "You have landed on a ladder!")
        myCanvas.move('p1', 80, -160)
    if player1 == [1, 3]:               # ladder4
        player1 = [0, 2]
        messagebox.showinfo("Ladder", "You have landed on a ladder!")
        myCanvas.move('p1', -80, -80)
        player1direction = player1direction * -1
    if player1 == [3, 2]:               # snake4
        player1 = [1, 5]
        messagebox.showinfo("Snake", "You have landed on a snake!")
        myCanvas.move('p1', -160, 240)
        player1direction = player1direction * -1
    if player1 == [8, 2]:               # ladder5
        player1 = [9, 1]
        messagebox.showinfo("Ladder", "You have landed on a ladder!")
        myCanvas.move('p1', 80, -80)
        player1direction = player1direction * -1
    if player1 == [4, 1]:               # snake5
        player1 = [7, 3]
        messagebox.showinfo("Snake", "You have landed on a snake!")
        myCanvas.move('p1', 240, 160)
    if player1 == [1, 0]:               # snake6
        player1 = [3, 1]
        messagebox.showinfo("Snake", "You have landed on a snake!")
        myCanvas.move('p1', 160, 80)
        player1direction = player1direction * -1
    if player1 == [0, 0]:
        if vs == "Player":
            rollButton["state"] = DISABLED
        if vs == "Computer":
            rollButton1["state"] = DISABLED
        messagebox.showinfo("Winner", "Player One Wins!")
        messagebox.showinfo("End", "Click Quit to leave!")


        

def movePiece2():                                                      
    global player2, player2direction, rollButton, rollButton1
    if player2 == [8, 9]:               # ladder1
        player2 = [9, 7]
        if vs == "Computer":
            messagebox.showinfo("Ladder", "Computer has landed on a ladder!")
        else:
            messagebox.showinfo("Ladder", "You have landed on a ladder!")
        myCanvas.move('p2', 80, -160)   
    if player2 == [6, 8]:               # ladder2 
        player2 = [5, 7]
        if vs == "Computer":
            messagebox.showinfo("Ladder", "Computer has landed on a ladder!")
        else:
            messagebox.showinfo("Ladder", "You have landed on a ladder!")
        myCanvas.move('p2', -80, -80)
        player2direction = player2direction * -1
    if player2 == [0, 7]:               # snake1
        player2 = [3, 8]
        if vs == "Computer":
            messagebox.showinfo("Ladder", "Computer has landed on a snake!")
        else:
            messagebox.showinfo("Ladder", "You have landed on a snake!")
        myCanvas.move('p2', 240, 80)
        player2direction = player2direction * -1
    if player2 == [3, 6]:               # snake2
        player2 = [4, 8]
        if vs == "Computer":
            messagebox.showinfo("Ladder", "Computer has landed on a snake!")
        else:
            messagebox.showinfo("Ladder", "You have landed on a snake!")
        myCanvas.move('p2', 80, 160)
    if player2 == [8, 5]:               # snake3
        player2 = [7, 8]
        if vs == "Computer":
            messagebox.showinfo("Ladder", "Computer has landed on a snake!")
        else:
            messagebox.showinfo("Ladder", "You have landed on a snake!")
        myCanvas.move('p2', -80, 240)
        player2direction = player2direction * -1
    if player2 == [4, 5]:               # ladder3
        player2 = [5, 3]
        if vs == "Computer":
            messagebox.showinfo("Ladder", "Computer has landed on a ladder!")
        else:
            messagebox.showinfo("Ladder", "You have landed on a ladder!")
        myCanvas.move('p2', 80, -160)
    if player2 == [1, 3]:               # ladder4
        player2 = [0, 2]
        if vs == "Computer":
            messagebox.showinfo("Ladder", "Computer has landed on a ladder!")
        else:
            messagebox.showinfo("Ladder", "You have landed on a ladder!")
        myCanvas.move('p2', -80, -80)
        player2direction = player2direction * -1
    if player2 == [3, 2]:               # snake4
        player2 = [1, 5]
        if vs == "Computer":
            messagebox.showinfo("Ladder", "Computer has landed on a snake!")
        else:
            messagebox.showinfo("Ladder", "You have landed on a snake!")
        myCanvas.move('p2', -160, 240)
        player2direction = player2direction * -1
    if player2 == [8, 2]:               # ladder5
        player2 = [9, 1]
        if vs == "Computer":
            messagebox.showinfo("Ladder", "Computer has landed on a ladder!")
        else:
            messagebox.showinfo("Ladder", "You have landed on a ladder!")
        myCanvas.move('p1', 80, -80)
        player2direction = player2direction * -1
    if player2 == [4, 1]:               # snake5
        player2 = [7, 3]
        if vs == "computer":
            messagebox.showinfo("Ladder", "Computer has landed on a snake!")
        else:
            messagebox.showinfo("Ladder", "You have landed on a snake!")
        myCanvas.move('p2', 240, 160)
    if player2 == [1, 0]:               # snake6
        player2 = [3, 1]
        if vs == "Computer":
            messagebox.showinfo("Ladder", "Computer has landed on a snake!")
        else:
            messagebox.showinfo("Ladder", "You have landed on a snake!")
        myCanvas.move('p2', 160, 80)
        player2direction = player2direction * -1
    if player2 == [0, 0]:
        if vs == "Computer":
            rollButton1["state"] = DISABLED
        else:
            rollButton["state"] = DISABLED
        messagebox.showinfo("Winner", "Player Two Wins!")
        messagebox.showinfo("End", "Click Quit to leave!")
        
        



#def movePiece1():




##def Movement():
##    global total1, player1, player2, total2, direction
##    if direction == 1:
##        if player1[0] > 9:
##            player1[0] = 9
##            player1[1] = player1[1] -1
##            player1[0] = player1[0] - (dice-1)
##            direction = 2
##            total1 = total1 + dice
##            Counter_Create()
##        else:
##            player1[0] = player1[0] + dice
##            total1 = total1 + dice
##            Counter_Create()
##    else:
##        if player1[0] < 0:
##            player1[0] = 0
##            player1[1] = player1[1] -1
##            player1[0] = player1[0] + (dice-1)
##            direction = 1
##            total1 = total1 + dice
##            Counter_Create()
##        else:
##            player1[0] = player1[0] + dice
##            total1 = total1 + dice
##            Counter_Create()
##            
                
                
        







    
##    for x in range(dice):
##        if counter == 1:
##            if player1[0] > 9 or row == 2:
##                player1[1] = player1[1]-1
##                player1[0] = player1[0]-(x-1)
##                total1 = total1+dice
##                print("Player 1", total1)
##                Counter_Create()
##            elif player1[0] < 0 or row == 1:
##                player1[0] = player1[0]+x
##                total1 = total1+dice
##                print("Player 1", total1)
##                Counter_Create()
        
        
##    if counter == 1:
##        if player1[0] > 9:
##            player1[1] = player1[1]-1
##            player1[0] = player1[0]-(dice-1)
##            total1 = total1+dice
##            print("Player 1", total1)
##            Counter_Create()
##        else:
##            player1[0] = player1[0]+dice
##            total1 = total1+dice
##            print("Player 1", total1)
##            Counter_Create()
##    else:
##        if player2[0] > 9:
##            player2[1] = player2[1]-1
##            player2[0] = player2[0]-(dice-1)
##            total2 = total2+dice
##            print("Player 2", total2)
##            Counter_Create()
##        else:
##            player2[0] = player2[0]+dice
##            total2 = total2+dice
##            print("Player 2", total2)
##            Counter_Create()
##            



##def Counter_Create():
##    global filenamePlayer1, myCanvas
##    player1 = [0, 9]
##    player1Coords = coordstoXY(player1)
##    filenamePlayer1 = PhotoImage(file = "%s.png" % (player1Colour))
##    myCanvas.create_image(player1Coords, image=filenamePlayer1)
##    myCanvas.image = filenamePlayer1
##
##def Counter_Create2():
##    global filenamePlayer2, myCanvas
##    player2 = [0, 9]
##    player2Coords = coordstoXY(player2)
##    filenamePlayer2 = PhotoImage(file = "%s.png" % (player2Colour))
##    myCanvas.create_image(player2Coords, image=filenamePlayer2)
##    myCanvas.image = filenamePlayer2


def coordstoXY1(coords):
    coords = [(coords[0]*tilewidth)+(tilewidth/2)-10, (coords[1]*tilewidth)+(tilewidth/2)]
    return coords
    
def coordstoXY2(coords):
    coords = [(coords[0]*tilewidth)+(tilewidth/2)+10, (coords[1]*tilewidth)+(tilewidth/2)]
    return coords


##def Counter_Movement1():
##    global dice, x1, x2, y1, y2, tilewidth, coordinates, direction, count, temp
##    if x1 >= 750:
##        if temp == 1:
##            y1 = y1-80
##            temp = 2
##        if temp == 2:
##            direction = -1
##            if count == 2:
##                x1 = x1-(1*tilewidth)
##            Counter_Create()
##            count = count + 1
##    elif x1 <= 30:
##        if temp ==2:
##            y1 = y1-80
##            x1 = x1+(1*tilewidth)
##            temp = 1
##        if temp == 1:
##            direction = 1
##            if count ==1:
##                x1 = x1+(1*tilewidth)
##            Counter_Create()
##            count = count-1
##    elif direction == -1:
##        x1 = x1-(1*tilewidth)
##        Counter_Create()
##    elif direction == 1:
##        x1 = x1+(1*tilewidth)
##        Counter_Create()



    
            

#def Counter_Movement2():
    
    


def Board():
    global myCanvas, coordinates, tilewidth, player1direction, player2direction
    tilewidth = 80
    if vs == "Player":
        redButton1.destroy()
        blueButton1.destroy()
        greenButton1.destroy()
        orangeButton1.destroy()
        purpleButton1.destroy()
        pinkButton1.destroy()
        title3.destroy()
 #  print(theme)
    background_label.destroy()
    filename1 = PhotoImage(file = "%s.png" % (theme))
    background_label1 = Label(root, image=filename1)
    background_label1.place(x=0, y=0, relwidth=1, relheight=1)
    background_label1.image = filename1
    myCanvas = Canvas(root, bg='white', height=800, width=800)
    myCanvas.place(x=50, y=50)

    #coordinates = [(column*tilewidth), (row*tilewidth), (column*tilewidth)+tilewidth, (row*tilewidth)+tilewidth] # coordinates of each tile


    for row in range(10): # for each row
        for column in range(10): # for each column
            coordinates = [(column*tilewidth), (row*tilewidth), (column*tilewidth)+tilewidth, (row*tilewidth)+tilewidth] # coordinates of each tile
            if (row+column) % 2 == 0: # draws the tile with a checkerboard pattern
                if theme == "jungle1":
                    tileColour = rgbToColour((12, 171, 17)) # sets colour
                elif theme == "desert":
                    tileColour = rgbToColour((245, 188, 44)) # sets colour
                elif theme == "volcanic":
                    tileColour = rgbToColour((133, 132, 127)) # sets colour
            else:
                if theme == "jungle1":
                    tileColour = rgbToColour((102, 73, 4)) # sets colour
                elif theme == "desert":
                    tileColour = rgbToColour((242, 178, 0)) # sets colour
                elif theme == "volcanic":
                    tileColour = rgbToColour((201, 52, 2)) # sets colour
            myCanvas.create_rectangle(coordinates, fill=tileColour, outline=tileColour) # draws the tile
            if row % 2 == 0: #if the row is even
                number = 100-((column)+(row*10))#the number displayed within the box is 10x whe row it is in + the coloumn number. Then 100- flips the entire board into the correct position
            else:           #if the row is odd
                number = 100-((10-column)+(row*10)-1) #the same happens again but the order is flipped as it goes in the reverse order
            
            myCanvas.create_text((column*tilewidth)+(tilewidth/2), (row*tilewidth)+(tilewidth/2), text=number, font='Calibri 20')
    player1direction = 1
    player2direction = 1
    Counter()
    Quit()
    Facts()
    if vs == "Player":
        Roll()
    if vs == "Computer":
        RollC()
    snakes()
    ladders()
    Counter_Create()
    Counter_Create1()

            

counter = 1
root = Tk() #sets up the window
filename = PhotoImage(file = "S&LBackground.png") #sets the variable filename to the image used
background_label = Label(root, image=filename) #creates the background with the image
background_label.place(x=0, y=0, relwidth=1, relheight=1) #places the image on the background
root.geometry('1920x1080')# creates a window
Play()
player1 = [0, 9]
player2 = [0, 9]
total1 = 0
total2 = 0

root.mainloop()



##filename2 = PhotoImage(file = "%s.png" % (dice))
##    background_label2 = Label(root, image=filename2)
##    background_label2.place(x=300, y=300) ##########################
##    background_label2.image = filename2
##
##
##    
##
