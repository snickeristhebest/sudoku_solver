import pygame
import random
pygame.init()


# functions
#   sudoku solving logic
#       solve checks if a specific number works for the board
M = 9
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
 #       sudoku is the backtracking algorithm that solves the board
def Suduko(grid,row,col):
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


#  pygame stuff

def mouse_closest_cords(x_cord,y_cord):
    x_index = 0
    y_index = 0
    for h in range(9):
        if (x_cord <= cols[h]+40 and x_cord >= cols[h]-30):
            x_index = h
        
        if (y_cord <= rows[h]+50 and y_cord >= rows[h]-15):
            y_index = h
            
    
    return x_index,y_index

def mouse_in_range(x_cord,y_cord):
    g = False
    j = False
    for c in range(9):
        if (cols[c] == x_cord): 
            g = True
        if(rows[c] == y_cord):
            j = True
    h = g and j
    return h

def draw_number(num,x_cord,y_cord):
        if (mouse_in_range(x_cord,y_cord)):
            screen.blit(num,(x_cord,y_cord))
    
def draw_grid(grid):
    for x in range(9):
        for y in range(9):
            if(grid[x][y] != 0):
                draw_number(texts[(grid[x][y]-1)],cols[x],rows[y])

def blacklisted(x,y):
      
    if(grid[x][y] != 0):
        print(x,y)
        print("blacklisted")
        return True  
   
    print("lited")
    return False

def number_wrong(bo,num,x_cord,y_cord):
    if bo[x_cord][y_cord] == num:
        print("right")
        return False
        
    else:
        
        print("wrong")
        return True


def display_wrong(wrongs):

    dis_wrong = font.render(str(wrong), True, red, white)
    screen.blit(dis_wrong,(x-150,(y/2)))
    




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
grid_solved =[
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

solvable = Suduko(grid_solved, 0, 0)

# pygame stuff

background_colour = (234, 212, 252)
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)

cols = [32,95,158,225,288,351,419,483,548,615]
rows = [25,90,155,220,285,350,415,480,545,610]

#window size
x = 800
y = 600

screen = pygame.display.set_mode((x,y))

#window title
pygame.display.set_caption('sudoku')

#fill background
screen.fill(background_colour)

#create surface object, image is drawn on it.
imp = pygame.image.load("sudoku_blank.png")

#resize image
imp_size = (600,600)
imp = pygame.transform.scale(imp, imp_size)

#put sudoku board in the top left
screen.blit(imp, (0,0))

font = pygame.font.Font('freesansbold.ttf', 32)

texts = [   font.render('1', True, black, white),
            font.render('2', True, black, white),
            font.render('3', True, black, white),
            font.render('4', True, black, white),
            font.render('5', True, black, white),
            font.render('6', True, black, white),
            font.render('7', True, black, white),
            font.render('8', True, black, white),
            font.render('9', True, black, white)
]


wrong_text = font.render('Wrong', True, red, white)
screen.blit(wrong_text,(x-150,(y/2)-50))




draw_grid(grid)


pygame.display.flip()


running = True
num = 0
selected = False
wrong = 0
current_x_index = 0

current_y_index = 0

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            current_x_cords,current_y_cords = pygame.mouse.get_pos()
            current_x_index,current_y_index = mouse_closest_cords(current_x_cords,current_y_cords)
            print(current_x_index,current_y_index)


            if(not blacklisted(current_x_index,current_y_index)):
                selected = True

        if event.type == pygame.KEYDOWN:
            if selected:
                if event.key == pygame.K_1:

                    if(not number_wrong(grid_solved,1,current_x_index,current_y_index)):
                        screen.blit(texts[0],(cols[current_x_index],rows[current_y_index]))
                        grid[current_x_index][current_y_index] = 1
                    else:
                        wrong += 1
                        print(wrong)
                    selected = False

                if event.key == pygame.K_2:

                    if(not number_wrong(grid_solved,2,current_x_index,current_y_index)):
                        screen.blit(texts[1],(cols[current_x_index],rows[current_y_index]))
                        grid[current_x_index][current_y_index] = 2
                    else:
                        wrong += 1
                        print(wrong)
            
                    selected = False

                if event.key == pygame.K_3:
                    if(not number_wrong(grid_solved,3,current_x_index,current_y_index)):
                        screen.blit(texts[2],(cols[current_x_index],rows[current_y_index]))
                        grid[current_x_index][current_y_index] = 3
                    else:
                        wrong += 1
                        print(wrong)
                    
                    selected = False

                if event.key == pygame.K_4:
                        if(not number_wrong(grid_solved,4,current_x_index,current_y_index)):
                            screen.blit(texts[3],(cols[current_x_index],rows[current_y_index]))
                            grid[current_x_index][current_y_index] = 4
                        else:
                            wrong += 1
                            print(wrong)
                        
                        selected = False

                if event.key == pygame.K_5:
                    if(not number_wrong(grid_solved,5,current_x_index,current_y_index)):
                        screen.blit(texts[4],(cols[current_x_index],rows[current_y_index]))
                        grid[current_x_index][current_y_index] = 5
                    else:
                        wrong += 1
                        print(wrong)
                    
                    selected = False

                if event.key == pygame.K_6:
                    if(not number_wrong(grid_solved,6,current_x_index,current_y_index)):
                        screen.blit(texts[5],(cols[current_x_index],rows[current_y_index]))
                        grid[current_x_index][current_y_index] = 6
                    else:
                        wrong += 1
                        print(wrong)
        
                    selected = False

                if event.key == pygame.K_7:
                    if(not number_wrong(grid_solved,7,current_x_index,current_y_index)):
                        screen.blit(texts[6],(cols[current_x_index],rows[current_y_index]))
                        grid[current_x_index][current_y_index] = 7
                    else:
                        wrong += 1
                        print(wrong)
                    
                    selected = False

                if event.key == pygame.K_8:
                    if(not number_wrong(grid_solved,8,current_x_index,current_y_index)):
                        screen.blit(texts[7],(cols[current_x_index],rows[current_y_index]))
                        grid[current_x_index][current_y_index] = 8
                    else:
                        wrong += 1
                        print(wrong)
                 
                    selected = False

                if event.key == pygame.K_9:
                    if(not number_wrong(grid_solved,9,current_x_index,current_y_index)):
                        screen.blit(texts[8],(cols[current_x_index],rows[current_y_index]))
                        grid[current_x_index][current_y_index] = 9
                    else:
                        wrong += 1
                        print(wrong)
                    selected = False

        
        display_wrong(wrong)
            
        pygame.display.flip()
  
        