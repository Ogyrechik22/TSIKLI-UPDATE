# size(1000,1000)
# i = 0
# a = 0
# fill(255,0,0)
# for i in 5,15,20,50,80:
#     rect(a,0,i,i)
#     a = a + i + 150

# size(1000,1000)
# i = 0
# fill(28,255,0)
# for i in 50,110,180,260,350,450,560,680,810,940:
#     ellipse(i,i,30,30)

# size(1000,1000)
# i = 0
# x = 0
# fill(255,234,0)
# for x in 275,375,475,575,675:
#     rect(475,x,50,50)
# for i in 275,375,475,575,675:
#     rect(i,475,50,50)

# size(1000,1000)
# i = 0
# fill(28,255,0)
# for i in range(10):
#     ellipse(50,50,30,30)
#     translate(50 + 10 * (i + 1),50 + 10 * (i + 1))

# size(1000,1000)
# i = 0
# x = 0
# a = 0
# b = 0
# for i in range(12):
#     for x in range(300):
#         rect(a,b,5,10)
#         fill(random(1,255),random(1,255),random(1,255))
#         a += 5
#     b += 20
#     a = 0

# size(1000,1000)
# i = 0
# x = 0
# for i in range(12):
#     for x in range(250):
#         rect(0,0,5,10)
#         fill(random(1,255),random(1,255),random(1,255))
#         translate(5,0)
#     translate(-1250,20)

# size(1000,1000)
# i = 0
# x = 0
# a = 0
# b = 0
# for i in range(250):
#     fill(random(1,255),random(1,255),random(1,255))
#     for x in range(12):
#         rect(a,b,5,10)
#         b += 20
#     b = 0
#     a += 5

# def setup():
#     frameRate(1)
#     size(1000,1000)
# def draw():
#     i = 0
#     x = 0
#     a = 0
#     b = 0
#     y = 0
#     for x in range(9):
#         y = random(1,100)
#         fill(random(1,255),random(1,255),random(1,255))
#         a = random(1,1000)
#         b = random(1,1000)
#         ellipse(a,b,y,y)

# def setup():
#     frameRate(1)
#     size(1000,1000)
# def draw():
#     i = 0
#     y = 0
#     z = 300
#     o = 0
#     s = 0
#     for i in range(5):
#         fill(random(1,255),random(1,255),random(1,255))
#         ellipse(500,z,50,50)
#         z += 100
#     i = 0
#     z = 700
#     o = 300
#     for i in range(5):
#         fill(random(1,255),random(1,255),random(1,255))
#         ellipse(z,o,50,50)
#         z -= 100
#         o += 100
#     i = 0
#     z = 500
#     o = 300
#     for i in range(5):
#         fill(random(1,255),random(1,255),random(1,255))
#         ellipse(o,z,50,50)
#         o += 100
#     i = 0
#     z = 300
#     o = 300
#     for i in range(5):
#         fill(random(1,255),random(1,255),random(1,255))
#         ellipse(z,o,50,50)
#         z += 100
#         o += 100

def col(x,y,z,l,x1,y1,d):
    testX = x1
    testY = y1
    if x1 < x:
        testX = x
    elif x1 > x + z:
        testX = x + z
    if y1 < y:
        testY = y
    elif y1 > y + l:
        testY = y + l
    distance = dist(x1,y1,testX,testY)
    if distance <= d/2:
        return True
    else:
        return False
x = 25
y = 25
mon = 0
def setup():
    size(1000,1000)
def draw():
    global x,y,mon
    background(1)
    if keyPressed:
        if key == 'w' or key == 'W':
            y -= 5
        if key == 'a' or key == 'A':
            x -= 5
        if key == 's' or key == 'S':
            y += 5
        if key == 'd' or key == 'D':
            x += 5
    if col(930,930,70,70,x,y,50):
        if mon > 499:
            fill(200) #primer
    if col(0,300,50,50,x,y,50):
    else:
        ellipse(x,y,50,50)
        rect(930,930,70,70)
        rect(0,300,50,50)
    
        
    
    
    
    
    
        
            

        
        
        


        
