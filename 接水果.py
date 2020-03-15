"""
关注“python趣味爱好者”微信公众号，
回复game1,game2,game3,game4获取飞机大战，贪吃蛇，接水果，生命游戏.....
创作方：python趣味爱好者，转载请标注来源。
游戏规则：
按左右键移动盘子
"""

import pygame
import sys
from pygame.locals import*
import numpy as np
from random import randint
pygame.init()

rect_width=10
size=width,height=300,500
COLOR=(0,225,0)#蛇的颜色
x_rect=int(width/rect_width)
y_rect=int(height/rect_width)#长宽格子有多个

speed=1
bg=(100,180,180)
bombcolor=(255,0,0)#炸弹的颜色
food_color=(255,255,0)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("python趣味爱好者")
#font=pygame.font.Font(None,20)

font1 = pygame.font.SysFont('宋体', 30, True)
font_list = pygame.font.get_fonts()
#render(text, antialias, color, background=None)
surface1 = font1.render(u'当前得分', True, [255, 0, 0])

food_live=1#食物的生命是否存在
Food=[12,18]#食物所在的坐标

ground=np.zeros([x_rect,y_rect])#全部的空间。

dish=[[12,y_rect-1],[13,y_rect-1],[14,y_rect-1],[15,y_rect-1]]
food_all=[[5,2],[8,5],[2,8]]#食物的位置。

score=0
def get_rect(row,column):#计算应该在哪里画方格，以右上角为点。
    x1=rect_width*row
    y1=rect_width*column

    return (x1,y1,rect_width,rect_width)

#pygame.draw.rect(screen,COLOR,get_rect(row,column),0)

def move_dish(speed,dish1):#左右移动盘子。
    for i in dish1:
        i[0]=i[0]+speed
 
def meet_food(dish_pos,food_pos):
    global score
    for i in food_pos:
        if i in dish_pos:
            score+=30
            food_all.remove(i)
        else:
            pass

def change_fruit(foods):
    for i in foods:
        if i[0]>y_rect:
            i[1]=6

def move_food(foods):
    for i in foods:
        i[1]=i[1]+2
        
def creat_food():
    food_all.append([randint(1,x_rect-1),randint(-8,0)])
    

def draw_dish(dish):#画那个盘子
    for i in dish:
        pygame.draw.rect(screen,COLOR,get_rect(i[0],i[1]),0)

def draw_food(foods):#画出所有符合条件的食物
    for i in foods:
        if i[0]>0 and i[0]<x_rect and i[1]>0 and i[1]<y_rect:
            pygame.draw.rect(screen,food_color,get_rect(i[0],i[1]),0)

k=0
score=30
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                speed=-1
            if event.key==K_RIGHT:
                speed=1

    k+=1

    meet_food(dish,food_all)
    if k>4:
        creat_food()
        k=0
    else:
        pass
    move_food(food_all)
    move_dish(speed,dish)
    change_fruit(food_all)
    screen.fill(bg)
    draw_dish(dish)
    draw_food(food_all)
    screen.blit(surface1, [20, 20])

    screen.blit(font1.render(u'当前得分：%d' % score, True, [255, 0, 0]), [20, 20])

    pygame.display.update()

    pygame.display.flip()
    pygame.time.delay(180)

