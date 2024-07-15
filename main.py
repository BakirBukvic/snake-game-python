import pygame
import time
import random





def create_food():
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    if foodx == dis_width -1:
        foodx = dis_width-3
    elif foodx == 1:
        foodx= 3
    if foody == dis_height -1:
        foody = dis_height -3
    elif foody == 0:
        foody=3
        

    print("Food spawned on")
    print(foodx,foody)
    return foodx, foody



pygame.init()


snake_len=1
snake_list=[]

# [x1,y1][x2,y2][x3,y3]


font_style = pygame.font.SysFont(None,50)
dis_width=800
dis_height=600


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)


dis = pygame.display.set_mode((dis_width, dis_height))

 
game_over = False
 
x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0
snake_block=10
snake_speed=10
foodx, foody= create_food()
clock = pygame.time.Clock()


def eat():
    print("mmm")


def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])



while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 
    x1 += x1_change
    y1 += y1_change

    if x1 >= 800 or x1<=0:
        game_over=True
    elif y1>=600 or y1<=0:
        game_over=True

    dis.fill(white)
    
    

    snake_head=[]
    snake_head.append(x1)
    snake_head.append(y1)

    snake_list.append(snake_head)


    if len(snake_list) > snake_len:
        del snake_list[0]


    for x in snake_list[:-1]:
        if x==snake_head:
            game_over=True


    for i in snake_list:
        pygame.draw.rect(dis, black, [i[0], i[1], snake_block,snake_block])
 

    pygame.draw.rect(dis, red, [foodx, foody, snake_block,snake_block])



    if x1==foodx and y1==foody:
        foodx,foody=create_food()
        if foodx == dis_width-1:
            foodx=foodx - 3
        elif foodx==1:
            foox=4

        if foody == dis_height-1:
            foody=dis_height-3
        elif foody == 1:
            foody=3
        
        snake_speed+=1
        snake_len+=1


    value =font_style.render("Your Score: " + str(snake_len-1), True,green)

    dis.blit(value, [0, 0])

    pygame.display.update()
 
    clock.tick(snake_speed)
 


message("You lost",red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()