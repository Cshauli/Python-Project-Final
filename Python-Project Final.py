from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=700,background='light green')
sq1 = drawpad.create_rectangle(0,0,100,100,fill= 'blue')
sq2 = drawpad.create_rectangle(100,0,200,100,fill= 'blue')
sq3 = drawpad.create_rectangle(200,0,300,100,fill= 'blue')
sq4 = drawpad.create_rectangle(300,0,400,100,fill= 'blue')
sq5 = drawpad.create_rectangle(400,0,500,100,fill= 'blue')
sq6 = drawpad.create_rectangle(500,0,600,100,fill= 'blue')
sq7 = drawpad.create_rectangle(600,0,700,100,fill= 'blue')
sq8 = drawpad.create_rectangle(700,0,800,100,fill= 'blue')
sq9 = drawpad.create_rectangle(700,100,800,200,fill= 'blue')
sq10 = drawpad.create_rectangle(700,200,800,300,fill= 'blue')
sq11 = drawpad.create_rectangle(600,200,700,300,fill= 'blue')
sq12 = drawpad.create_rectangle(500,200,600,300,fill= 'blue')
sq13 = drawpad.create_rectangle(400,200,500,300,fill= 'blue')
sq14 = drawpad.create_rectangle(300,200,400,300,fill= 'blue')
sq15 = drawpad.create_rectangle(200,200,300,300,fill= 'blue')
sq16 = drawpad.create_rectangle(100,200,200,300,fill= 'blue')
sq17 = drawpad.create_rectangle(0,200,100,300,fill= 'blue')
sq18 = drawpad.create_rectangle(0,300,100,400,fill= 'blue')
sq19 = drawpad.create_rectangle(0,400,100,500,fill= 'blue')
sq20 = drawpad.create_rectangle(100,400,200,500,fill= 'blue')

player = drawpad.create_oval(35,35,65,65, fill="red")
move = 2
a = 'Abraham Lincoln was our first president.'#f
b = 'There are 25 letters in the alphabet'#f
c = 'There were 8 colors of crayons in the original Crayola box.'
d = "The Beatles' song 'Come Together' was released in 1965"
e = 'In 1938, Adolf Hitler was featured as man of the year by TIME Magazine'
f = 'Turtles can breathe through their rear end.'
g = 'A statue of a horse with all four legs on the ground means the rider died in battle.'
h = 'A cow can go downstairs.'
i = 'US dollars are made from paper.'
j = 'Ireland is the second largest software producing country in the world.'
k = 'Only 2 animals known to man do not get cancer.'
l = 'Dolphins are the smartest animals on the planet.'
m = 'Male lions do the majority of the hunting.'
n = "You can tell a horse's gender by its teeth."
o = 'Like a finger, the tongue has its own unique print.'
p = 'Donald Duck films are allowed everywhere.'
q = 'The name Wendy did not exist before Peter Pan.(Worth 2x move)'
r = 'There is a city called Rome on every continent'
s = 'Left handed people live longer than right handed people.'
t = 'Donkeys can see all 4 legs at all times.'
u = 'The flamingo can only eat when its head is upside down'
v = 'Your fingernails grow faster in warm weather'
w = 'A baby rabbit is called a kitten.'#t
x = 'Small pox can be found outside of laboratories.'#f
y = 'Nachos were invented by a guy named Nacho.'#t
z = 'Australians have the lowest chance of skin cancer'#f
aa = 'You can never die from drinking too much water'#f
bb = 'The dead outnumber the living 15:1'#t
cc = 'Buzz Aldrin was the first man to urinate on the moon.'#t
dd = 'There is a Dutch Village that has no roads.'#t
ee = 'All snowflakes are the same size'#f
ff = 'Romans used to clean their teeth with urine.'#t
gg = 'Pigs can look at the sky.'#f
hh = 'The name of all the continents ends in the same letter as it starts with.'
ii = 'All of the kings in a card deck have mustaches.'#f

r1 = 'Correct!'
r2 = 'Wrong, try again.'
rList = [r1,r2]
qList = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii]


class MyApp:
    def __init__(self,parent):
        global drawpad
        self.myParent = parent  
       	self.myContainer1 = Frame(parent)
       	self.myContainer1.pack()
       	drawpad.pack(side=RIGHT)

        self.label1 = Label(root, text = 'Question 1: ' + qList[0], width=len(qList[0]),bg = 'white')
        self.label1.pack()
        root.bind_all('<Key>', self.key)
        
        self.animate()

    def moveRight(self):   
        global player
        drawpad.move(player,100,0)
       
    def moveLeft(self):   
        global player
        drawpad.move(player,-100,0)  
    
    def moveDown(self):
        global player
        drawpad.move(player,0,100)
        
    def key(self,event):
        global move
        if event.char == "t" or event.char == 'T':
            move = 1
        if event.char == "f" or event.char == 'F':
            move = 0
    
    
    def animate(self):
        global player
        global drawpad
        global moveRight
        global moveLeft
        global moveDown
        global move
        x1,y1,x2,y2 = drawpad.coords(player)
        print move
        if x1 == 35 and y1 == 35 and x2 == 65 and y2 == 65 and move == 0:#Q1 C
            self.moveRight()
            self.label1.configure(text= 'Question 2:' + qList[1], width=len(qList[1]))
            move = 2
        if x1 == 35 and y1 == 35 and x2 == 65 and y2 == 65 and move == 0:#Q1 W
            self.label1.configure(text=rList[1], width=len(rList[1]))
            drawpad.after(100,self.label1.configure(text=qList[0], width=len(qList[0])))
            move = 2
        if x1 == 135 and y1 == 35 and x2 == 165 and y2 == 65 and move == 0:#Q2 C
            self.moveRight()
            self.label1.configure(text= 'Question 3:' + qList[2], width=len(qList[2]))
            move = 2
        elif x1 == 135 and y1 == 35 and x2 == 165 and y2 == 65 and move == 1:#Q2 W
            self.label1.configure(text=rList[0], width=len(rList[0]))
            drawpad.after(100,self.label1.configure(text= 'Question 2:' + qList[1], width=len(qList[1])))
            move = 2
        if x1 == 235 and y1 == 35 and x2 == 265 and y2 == 65 and move == 1:#Q3 C
            self.moveRight()
            self.label1.configure(text= 'Question 4:' + qList[3], width=len(qList[3]))
            move = 2
        if x1 == 335 and y1 == 35 and x2 == 365 and y2 == 65 and move == 0:#Q4 C
            self.moveRight()
            self.label1.configure(text= 'Question 5:' + qList[4], width=len(qList[4]))
            move = 2
        if x1 == 435 and y1 == 35 and x2 == 465 and y2 == 65 and move == 1:#Q5 C
            self.moveRight()
            self.label1.configure(text= 'Question 6:' + qList[5], width=len(qList[5]))
            move = 2
        if x1 == 535 and y1 == 35 and x2 == 565 and y2 == 65 and move == 1:#Q6 C
            self.moveRight()
            self.label1.configure(text= 'Question 7:' + qList[6], width=len(qList[6]))
            move = 2
        if x1 == 635 and y1 == 35 and x2 == 665 and y2 == 65 and move == 0:#Q7 C
            self.moveRight()
            self.label1.configure(text= 'Question 8:' + qList[7], width=len(qList[3]))
            move = 2
        if x1 == 635 and y1 == 35 and x2 == 665 and y2 == 65 and move == 0:#Q8 C
            self.moveDown()
            self.label1.configure(text= 'Question 9:' + qList[8], width=len(qList[8]))
            move = 2
        if x1 == 735 and y1 == 35 and x2 == 765 and y2 == 65 and move == 0:#Q9 C
            self.moveDown()
            self.label1.configure(text= 'Question 9:' + qList[9], width=len(qList[9]))
            move = 2
        if x1 == 735 and y1 == 135 and x2 == 765 and y2 == 165 and move == 1:#Q10 C
            self.moveDown()
            self.label1.configure(text= 'Question 10:' + qList[10], width=len(qList[10]))
            move = 2
        if x1 == 735 and y1 == 235 and x2 == 765 and y2 == 265 and move == 1:#Q11 C
            self.moveLeft()
            self.label1.configure(text= 'Question 11:' + qList[11], width=len(qList[11]))
            move = 2
        if x1 == 635 and y1 == 235 and x2 == 665 and y2 == 265 and move == 0:#Q12 C
            self.moveLeft()
            self.label1.configure(text= 'Question 12:' + qList[12], width=len(qList[12]))
            move = 2
        if x1 == 535 and y1 == 235 and x2 == 565 and y2 == 265 and move == 0:#Q13 C
            self.moveLeft()
            self.label1.configure(text= 'Question 13:' + qList[13], width=len(qList[13]))
            move = 2
        if x1 == 435 and y1 == 235 and x2 == 465 and y2 == 265 and move == 1:#Q14 C
            self.moveLeft()
            self.label1.configure(text= 'Question 14:' + qList[14], width=len(qList[14]))
            move = 2
        if x1 == 335 and y1 == 235 and x2 == 365 and y2 == 265 and move == 1:#Q15 C
            self.moveLeft()
            self.label1.configure(text= 'Question 15:' + qList[15], width=len(qList[15]))
            move = 2
        if x1 == 235 and y1 == 235 and x2 == 265 and y2 == 265 and move == 0:#Q16 C
            self.moveLeft()
            self.label1.configure(text= 'Question 16:' + qList[16], width=len(qList[16]))
            move = 2
        if x1 == 135 and y1 == 235 and x2 == 165 and y2 == 265 and move == 1:#Q17 C
            self.moveLeft()
            self.label1.configure(text= 'Question 16:' + qList[17], width=len(qList[17]))
            move = 2
        #if x1 == 35 and y1 == 235 and x2 == 65 and y2 == 265 and move == 1:#Q18 C
            self.moveDown()
            self.label1.configure(text= 'Question 17:' + qList[18], width=len(qList[18]))
            move = 2
        if x1 == 35 and y1 == 335 and x2 == 65 and y2 == 365 and move == 0:#Q19 C
            self.moveRight()
            self.label1.configure(text= 'Question 18:' + qList[19], width=len(qList[19]))
            move = 2
        if x1 == 35 and y1 == 435 and x2 == 65 and y2 == 465 and move == 1:#Q20 C
            
            self.label1.configure(text= 'Congratulations! You win!')
          
        
        drawpad.after(1,self.animate)




app = MyApp(root)
root.mainloop()