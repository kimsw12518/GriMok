import pygame
import sys
from pygame.locals import *    
    

width = 600
height = 400
white = (255, 255, 255)
black = (  0,   0,   0)
fps = 30
line=[[0],[0]]
stone=[[1]]
turn=2
cx,cy=0,0
draw=1
pygame.init()
act=0
timer=1350
prevtimer=1350
pr=1

pygame.display.set_caption('GriMOK')
displaysurf = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()
x,y=0,0

while True:
    for event in pygame.event.get():
        #종료
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#좌클
            if act==1 and draw==1:
                if len(line[0])<15:
                    x,y=pygame.mouse.get_pos()
                    i=0
                    while i in range(len(line[0])):
                        if x < line[0][i]:
                            line[0].insert(i,x)
                            stone.insert(i,[])
                            for j in range(len(line[1])):
                                stone[i].append(0)
                            break
                        i=i+1
                    if i==len(line[0]):
                        line[0].append(x)
                        stone.append([])
                        for j in range(len(line[1])):
                            stone[i].append(0)
                    cx=i
                    stone[cx][cy]=turn;
                    turn=turn%2+1
                    pr=pr+1
                    prevtimer=timer
                    timer=1350
            if act==2 and draw==1:
                if len(line[1])<15:
                    x,y=pygame.mouse.get_pos()
                    i=0
                    while i in range(len(line[1])):
                        if y < line[1][i]:
                            line[1].insert(i,y)
                            for j in range(len(line[0])):
                                stone[j].insert(i,0)
                            break
                        i=i+1
                    if i==len(line[1]):
                        line[1].append(y)
                        for j in range(len(line[0])):
                                stone[j].append(0)
                    cy=i
                    stone[cx][cy]=turn
                    turn=turn%2+1
                    pr=pr+1
                    prevtimer=timer
                    timer=1350
            if act==0 and stone[cx][cy]==0:
                stone[cx][cy]=turn
                pr=pr+1
                if draw==0 or pr == len(line[0])*len(line[1]):
                    turn=turn%2+1
                    draw=1
                    prevtimer=timer
                    timer=1350
                else:
                    draw=0
            if act==-1 and draw==0:
                turn=turn%2+1
                prevtimer=timer
                draw=1
                timer=1350
    for i in range(len(line[0])):
        if (line[0][i]+(-line[0][i] if i==0 else line[0][i-1]))/2<pygame.mouse.get_pos()[0]:
            cx=i
    for i in range(len(line[1])):
        if (line[1][i]+(-line[1][i] if i==0 else line[1][i-1]))/2<pygame.mouse.get_pos()[1]:
            cy=i
    displaysurf.fill(white)
    if abs(pygame.mouse.get_pos()[0]-300)<200:
        if (line[0][cx]-pygame.mouse.get_pos()[0])**2+(line[1][cy]-pygame.mouse.get_pos()[1])**2>36 and draw==1:#현재 마우스
            if len(line[0])<15 and abs(line[0][cx]-pygame.mouse.get_pos()[0])>abs(line[1][cy]-pygame.mouse.get_pos()[1]):
                pygame.draw.line(displaysurf,(100,100,100),(pygame.mouse.get_pos()[0],25),(pygame.mouse.get_pos()[0],375),3)
                pygame.draw.circle(displaysurf,(100,100,100),(pygame.mouse.get_pos()[0],line[1][cy]),7)
                pygame.draw.circle(displaysurf,white,(pygame.mouse.get_pos()[0],line[1][cy]),5)
                act=1
            elif len(line[1])<15 and abs(line[0][cx]-pygame.mouse.get_pos()[0])<=abs(line[1][cy]-pygame.mouse.get_pos()[1]):
                pygame.draw.line(displaysurf,(100,100,100),(125,pygame.mouse.get_pos()[1]),(475,pygame.mouse.get_pos()[1]),3)
                pygame.draw.circle(displaysurf,(100,100,100),(line[0][cx],pygame.mouse.get_pos()[1]),7)
                pygame.draw.circle(displaysurf,white,(line[0][cx],pygame.mouse.get_pos()[1]),5)
                act=2
        else:
            pygame.draw.circle(displaysurf,(100,100,100),(line[0][cx],line[1][cy]),7)
            pygame.draw.circle(displaysurf,white,(line[0][cx],line[1][cy]),5)
            act=0
    else:
        act=-1
    pygame.draw.rect(displaysurf,black,(110,10,380,380),3)
    pygame.draw.rect(displaysurf,black,(0,0,100,400))
    pygame.draw.rect(displaysurf,black,(500,0,100,400))
    for i in range(len(line[0])):#선그리기(가로,세로)
        pygame.draw.line(displaysurf,black,(line[0][i],25),(line[0][i],375),3)
    for i in range(len(line[1])):
        pygame.draw.line(displaysurf,black,(125,line[1][i]),(475,line[1][i]),3)
    for i in range(len(line[0])):#돌그리기
        for j in range(len(line[1])):
            if stone[i][j]==1:
                pygame.draw.circle(displaysurf,white,(line[0][i],line[1][j]),10)
                pygame.draw.circle(displaysurf,black,(line[0][i],line[1][j]),9)
            elif stone[i][j]==2:
                pygame.draw.circle(displaysurf,black,(line[0][i],line[1][j]),9)
                pygame.draw.circle(displaysurf,white,(line[0][i],line[1][j]),8)
    pygame.draw.line(displaysurf,(int(255*(675-timer-abs(timer-675))/1350+255),int(255*(timer-abs(timer-675)+675)/1350),0),(turn*430-346,390),(turn*430-346,390-timer/10),10)
    pygame.draw.line(displaysurf,(100,100,100),((3-turn)*430-346,390),((3-turn)*430-346,390-prevtimer/10),10)
    timer=timer-1
    pygame.display.update()#화면 업데이트
    for i in range(len(line[0])):#선 위치조정
        line[0][i]=int(((2 if abs(line[0][i]-(25*i-12.5*len(line[0])+312.5))>5 else 0)*line[0][i]+(3-(2 if abs(line[0][i]-(25*i-12.5*len(line[0])+312.5))>5 else 0))*(25*i-12.5*len(line[0])+312.5))/3+0.5)
    for i in range(len(line[1])):
        line[1][i]=int(((2 if abs(line[1][i]-(25*i-12.5*len(line[1])+212.5))>5 else 0)*line[1][i]+(3-(2 if abs(line[1][i]-(25*i-12.5*len(line[1])+212.5))>5 else 0))*(25*i-12.5*len(line[1])+212.5))/3+0.5)
    clock.tick(fps)
