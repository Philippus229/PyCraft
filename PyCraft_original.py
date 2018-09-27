import pygame
from math import *
import keyboard

pygame.init()
pygame.font.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW =(255, 255,   0)
ORANGE =(255, 128,   0)
BROWN = (255, 128, 128)
GREY =  (128, 128, 128)
PINK =  (  0, 255, 255)

HEIGHT = 480
WIDTH = 640

cubeMap = [[0,0,5],[0,1,5]]
camPosX = 0
camPosY = 0
camPosZ = 0
camRotX = 0
camRotY = 0

def my_sin(x):
    return sin((x*pi)/180)

def my_cos(x):
    return cos((x*pi)/180)

screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("PyCraft")
myfont = pygame.font.SysFont('Comic Sans MS', 30)
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keyboard.is_pressed("left"):
        camRotY = camRotY-2.5
    if keyboard.is_pressed("right"):
        camRotY = camRotY+2.5
    if camRotY > 360:
        camRotY = 0
    elif camRotY < 0:
        camRotY = 360
    if keyboard.is_pressed("down") and ((camRotX > 270 and camRotX <= 360) or (camRotX >= 0 and camRotX < 85)):
        camRotX = camRotX-2.5
    if keyboard.is_pressed("up") and ((camRotX > 265 and camRotX <= 360) or (camRotX >= 0 and camRotX < 90)):
        camRotX = camRotX+2.5
    if camRotX > 360:
        camRotX = 0
    elif camRotX < 0:
        camRotX = 360
    speed = 0
    if keyboard.is_pressed("w"):
        speed = 0.1
    elif keyboard.is_pressed("s"):
        speed = -0.1
    if not speed == 0:
        camPosX = camPosX+(my_sin(camRotY)*speed)
        camPosZ = camPosZ+(my_cos(camRotY)*speed)
    screen.fill(BLACK)
    for block in cubeMap:
        p0 = [block[0]-0.5,block[1]+0.5,block[2]-0.5]
        p1 = [block[0]-0.5,block[1]-0.5,block[2]-0.5]
        p2 = [block[0]+0.5,block[1]+0.5,block[2]-0.5]
        p3 = [block[0]+0.5,block[1]-0.5,block[2]-0.5]
        p4 = [block[0]+0.5,block[1]+0.5,block[2]+0.5]
        p5 = [block[0]+0.5,block[1]-0.5,block[2]+0.5]
        p6 = [block[0]-0.5,block[1]+0.5,block[2]+0.5]
        p7 = [block[0]-0.5,block[1]-0.5,block[2]+0.5]
        i = 0
        while i < 9:
            pTmp = [0,0,0]
            if i == 0:
                pTmp = p0
            elif i == 1:
                pTmp = p1
            elif i == 2:
                pTmp = p2
            elif i == 3:
                pTmp = p3
            elif i == 4:
                pTmp = p4
            elif i == 5:
                pTmp = p5
            elif i == 6:
                pTmp = p6
            elif i == 7:
                pTmp = p7
            elif i == 8:
                pTmp = block
            blockPosXRTC = ((my_cos(camRotY)*(pTmp[0]-camPosX))-(my_sin(camRotY)*(pTmp[2]-camPosZ)))
            blockPosZRTC = ((my_cos(camRotY)*(pTmp[2]-camPosZ))+(my_sin(camRotY)*(pTmp[0]-camPosX)))
            blockPosYRTC = -((my_cos(camRotX)*(pTmp[1]-camPosY))-(my_sin(camRotX)*blockPosZRTC))
            blockPosZRTC = ((my_cos(camRotX)*blockPosZRTC)+(my_sin(camRotX)*(pTmp[1]-camPosY)))
            if i == 8:
                textsurface0 = myfont.render(str(blockPosXRTC), False, (255, 255, 255))
                textsurface1 = myfont.render(str(blockPosYRTC), False, (255, 255, 255))
                textsurface2 = myfont.render(str(blockPosZRTC), False, (255, 255, 255))
                textsurface3 = myfont.render(str(camRotY), False, (255, 255, 255))
            if i == 0:
                p0 = [blockPosXRTC,blockPosYRTC,blockPosZRTC]
            elif i == 1:
                p1 = [blockPosXRTC,blockPosYRTC,blockPosZRTC]
            elif i == 2:
                p2 = [blockPosXRTC,blockPosYRTC,blockPosZRTC]
            elif i == 3:
                p3 = [blockPosXRTC,blockPosYRTC,blockPosZRTC]
            elif i == 4:
                p4 = [blockPosXRTC,blockPosYRTC,blockPosZRTC]
            elif i == 5:
                p5 = [blockPosXRTC,blockPosYRTC,blockPosZRTC]
            elif i == 6:
                p6 = [blockPosXRTC,blockPosYRTC,blockPosZRTC]
            elif i == 7:
                p7 = [blockPosXRTC,blockPosYRTC,blockPosZRTC]
            elif i == 8:
                block = [blockPosXRTC,blockPosYRTC,blockPosZRTC]
            i=i+1
        p00 = [(WIDTH/2)+((p0[0]/p0[2])*(HEIGHT/2)), (HEIGHT/2)+((p0[1]/p0[2])*(HEIGHT/2))]
        p01 = [(WIDTH/2)+((p1[0]/p1[2])*(HEIGHT/2)), (HEIGHT/2)+((p1[1]/p1[2])*(HEIGHT/2))]
        p02 = [(WIDTH/2)+((p2[0]/p2[2])*(HEIGHT/2)), (HEIGHT/2)+((p2[1]/p2[2])*(HEIGHT/2))]
        p03 = [(WIDTH/2)+((p3[0]/p3[2])*(HEIGHT/2)), (HEIGHT/2)+((p3[1]/p3[2])*(HEIGHT/2))]
        p04 = [(WIDTH/2)+((p4[0]/p4[2])*(HEIGHT/2)), (HEIGHT/2)+((p4[1]/p4[2])*(HEIGHT/2))]
        p05 = [(WIDTH/2)+((p5[0]/p5[2])*(HEIGHT/2)), (HEIGHT/2)+((p5[1]/p5[2])*(HEIGHT/2))]
        p06 = [(WIDTH/2)+((p6[0]/p6[2])*(HEIGHT/2)), (HEIGHT/2)+((p6[1]/p6[2])*(HEIGHT/2))]
        p07 = [(WIDTH/2)+((p7[0]/p7[2])*(HEIGHT/2)), (HEIGHT/2)+((p7[1]/p7[2])*(HEIGHT/2))]
        pygame.draw.lines(screen, WHITE, False, [p00, p01, p03, p02, p00], 1)
        pygame.draw.lines(screen, WHITE, False, [p02, p04, p05, p03], 1)
        pygame.draw.lines(screen, WHITE, False, [p04, p06, p07, p05], 1)
        pygame.draw.lines(screen, WHITE, False, [p06, p00, p01, p07], 1)
        screen.blit(textsurface0,(0,0))
        screen.blit(textsurface1,(0,30))
        screen.blit(textsurface2,(0,60))
        screen.blit(textsurface3,(0,90))
    pygame.display.flip()
pygame.quit()
