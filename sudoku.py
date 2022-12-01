import pygame
import random
pygame.init()

#functions

#draws number at specified coordinate
def draw_number(num,x_cord,y_cord):
        if (mouse_in_range(x_cord,y_cord)):
            screen.blit(num,(x_cord,y_cord))

#determines which cords to use for current mouse pos
def mouse_closest_cords(x_cord,y_cord):
    x_index = 0
    y_index = 0
    for h in range(9):
        if (x_cord <= column[h]+40 and x_cord >= column[h]-30):
            x_cord = column[h]
            x_index = h
        
        if (y_cord <= row[h]+50 and y_cord >= row[h]-15):
            y_cord = row[h]
            y_index = h
            
    
    return x_cord,y_cord,x_index,y_index

# determines if mouse is in range, necessary so that numbers only print in the specified cords
def mouse_in_range(x_cord,y_cord):
    g = False
    j = False
    for c in range(9):
        if (column[c] == x_cord): 
            g = True
        if(row[c] == y_cord):
            j = True
    h = g and j
    return h

#takes a grid, draws the number in the grid at the locations on the grid
def draw_grid(grid):
    for x in range(9):
        for y in range(9):
            if(grid[x][y] != 0):
                draw_number(scroll[(grid[x][y]-1)],column[x],row[y])

#sees if there is something drawn in location selected
def blacklisted(x,y):
    q = 0
    w = 0
    for h in range(9):
        if(column[h] == x):
            q = h
            #print(q)
    for j in range(9):
        if(row[j] == y):
            w = j
            #print(w)

    #print(grid[q][w])       
    if(grid[q][w] != 0):
        
        return True           
    return False

#checks if number entered is repeated in the same row or column
def number_repeated(grid,x,y,num):
    square_x = x // 3
    square_y = y // 3

    repeated = False
    for c in range(9):
        if grid[x][c] == num:
            repeated = True
    for j in range(9):
        if grid[j][y] == num:
            repeated = True

    for h in range(3):
        for k in range(3):
            if grid[h+(square_x * 3)][k+(square_y * 3)] == num:
                repeated = True
            
    return repeated

def backtrack(grid,column,row):
    counter_x = 0
    counter_y = 0
    run = True
    num = 1
    skip = 0
    while run:
        if counter_x < 0:
            counter_x = 8 - counter_x
            counter_y -= 1

        if counter_x == 9 and counter_y == 9:
            run = False
        if counter_x == 9:
            counter_x -= 9
            counter_y += 1
    
        if not blacklisted(column[counter_x],row[counter_y]):
            runn = True
            while runn:
                if num == 10:
                    grid[counter_x][counter_y] = 0
                    counter_x -= skip
                    num = 1
                    skip = 0
                    runn = False
                if number_repeated(grid,counter_x,counter_y,num):
                    num += 1
                else:
                    grid[counter_x][counter_y] = num
                    counter_x += 1
                    num = 1
                    runn = False
                    
        else:
            counter_x += 1
            skip += 1
    
    return grid





#background color
background_colour = (234, 212, 252)
# colors
white = (255,255,255)
black = (0,0,0)

#rows and columns
a,b,c,d,e,f,g,h,i,j= 32,95,158,225,288,351,419,483,548,615
column = [a,b,c,d,e,f,g,h,i]
one,two,three,four,five,six,seven,eight,nine,ten = 25,90,155,220,285,350,415,480,545,610
row = [one,two,three,four,five,six,seven,eight,nine]

#window size
x = 600
y = 600

screen = pygame.display.set_mode((x,y))

#window title
pygame.display.set_caption('sudoku')

#fill background
screen.fill(background_colour)

#create surface object, image is drawn on it.
imp = pygame.image.load("sudoku_blank.png")

#resize image
imp_size = (x,y)
imp = pygame.transform.scale(imp, imp_size)

#put sudoku board in the top left
screen.blit(imp, (0,0))

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
text1 = font.render('1', True, black, white)
text2 = font.render('2', True, black, white)
text3 = font.render('3', True, black, white)
text4 = font.render('4', True, black, white)
text5 = font.render('5', True, black, white)
text6 = font.render('6', True, black, white)
text7 = font.render('7', True, black, white)
text8 = font.render('8', True, black, white)
text9 = font.render('9', True, black, white)

scroll = [text1,text2,text3,text4,text5,text6,text7,text8,text9]

#grid is list of list
grid =[
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

backtrack(grid,column,row)
draw_grid(grid)
#paint screen one time
pygame.display.flip()

#prepare main loop
running = True
num = 0
selected = False
current_x_cords = 0
current_x_index = 0
current_y_cords = 0
current_x_index = 0

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            current_x_cords,current_y_cords = pygame.mouse.get_pos()
            current_x_cords,current_y_cords,current_x_index,current_y_index = mouse_closest_cords(current_x_cords,current_y_cords)

            print(current_x_cords,current_y_cords)
            if(not blacklisted(current_x_cords,current_y_cords)):
                selected = True

        if event.type == pygame.KEYDOWN:
            if selected:
                if event.key == pygame.K_1:

                    if(not number_repeated(grid,current_x_index,current_y_index,1)):
                        screen.blit(scroll[0],(current_x_cords,current_y_cords))
                        grid[current_x_index][current_y_index] = 1

                    selected = False

                if event.key == pygame.K_2:

                    if(not number_repeated(grid,current_x_index,current_y_index,2)):
                        screen.blit(scroll[1],(current_x_cords,current_y_cords))
                        grid[current_x_index][current_y_index] = 2
                    selected = False

                if event.key == pygame.K_3:
                    if(not number_repeated(grid,current_x_index,current_y_index,3)):
                        screen.blit(scroll[2],(current_x_cords,current_y_cords))
                        grid[current_x_index][current_y_index] = 3

                    selected = False

                if event.key == pygame.K_4:
                        if(not number_repeated(grid,current_x_index,current_y_index,4)):
                            screen.blit(scroll[3],(current_x_cords,current_y_cords))
                            grid[current_x_index][current_y_index] = 4

                        selected = False

                if event.key == pygame.K_5:
                    if(not number_repeated(grid,current_x_index,current_y_index,5)):
                        screen.blit(scroll[4],(current_x_cords,current_y_cords))
                        grid[current_x_index][current_y_index] = 5

                    selected = False

                if event.key == pygame.K_6:
                    if(not number_repeated(grid,current_x_index,current_y_index,6)):
                        screen.blit(scroll[5],(current_x_cords,current_y_cords))
                        grid[current_x_index][current_y_index] = 6

                    selected = False

                if event.key == pygame.K_7:
                    if(not number_repeated(grid,current_x_index,current_y_index,7)):
                        screen.blit(scroll[6],(current_x_cords,current_y_cords))
                        grid[current_x_index][current_y_index] = 7

                    selected = False

                if event.key == pygame.K_8:
                    if(not number_repeated(grid,current_x_index,current_y_index,8)):
                        screen.blit(scroll[7],(current_x_cords,current_y_cords))
                        grid[current_x_index][current_y_index] = 8

                    selected = False

                if event.key == pygame.K_9:
                    if(not number_repeated(grid,current_x_index,current_y_index,9)):
                        screen.blit(scroll[8],(current_x_cords,current_y_cords))
                        grid[current_x_index][current_y_index] = 9

                    selected = False

            
        pygame.display.flip()

    
    

