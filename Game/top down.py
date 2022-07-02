import pygame
import sys
import math
pygame.init()
display = pygame.display.set_mode((1080,720))
clock = pygame.time.Clock()
prev=[0,0]
fin=open("OBSTACLE.txt","r")
fout=open("LODA.txt","w")
obstacle=[]


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def main(self, display):
        pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))
    
# CLASS BULLET

class PlayerBullet:
    def __init__(self,x,y,mouse_x,mouse_y):
        self.x=x
        self.y=y
        self.mouse_x=x
        self.mouse_y=y
        self.speed = 15
        self.angle=math.atan2(y-mouse_y,x-mouse_x)
        self.x_vel = math.cos(self.angle)*self.speed
        self.y_vel = math.sin(self.angle)*self.speed
    def main(self,display):
        self.x-= int(self.x_vel)
        self.y-= int(self.y_vel)
        pygame.draw.circle(display, (0, 0, 0), (self.x, self.y), 5)


# CLASS MAPOBJECTS
class OBSTACLE:
    def __init__(self,x1,y1,x2,y2):
        if x1>x2:
            x1,x2=x2,x1
        if y1>y2:
            y1,y2=y2,y1
        self.x1=x1-10
        self.y1=y1-10
        self.x2=x2+10
        self.y2=y2+10

    def main(self,scroll):
        if self.x1<scroll[0]<self.x2 and self.y1<scroll[1]<self.y2:
            #print("COLLISION")
            return True
        else:
            return False

obstacle=[]
obstacle_coordinartes=fin.read().split("\n")
#obstacle_coordinartes.remove("")
#print(obstacle_coordinartes)
n=len(obstacle_coordinartes)
for i in range(0,n,2):
    p1,p2=map(int,obstacle_coordinartes[i].split())
    q1,q2=map(int,obstacle_coordinartes[i+1].split())
    obstacle.append(OBSTACLE(p1,p2,q1,q2))


player=Player(400,300,32,32)

display_scroll=[0,0]

# Importing images from Green Forest

fin=open("Green-Forest.txt","r")
map=[]

for i in range(46):
    img=fin.readline()
    img="Green-Forest/"+img[:len(img)-1]
    map.append(pygame.image.load(img))


player_bullets=[]
walkleft=[]
walkleft.append(pygame.image.load('ddc_graphics/walk_left (2).png'))
walkleft.append(pygame.image.load('ddc_graphics/walk_left (3).png'))
walkleft.append(pygame.image.load('ddc_graphics/walk_left (4).png'))
walkleft.append(pygame.image.load('ddc_graphics/walk_left (5).png'))
i=0
walkdown=[]
walkdown.append(pygame.image.load('ddc_graphics/walk_down2.png'))
walkdown.append(pygame.image.load('ddc_graphics/walk_down3.png'))
i1=0
walkup=[]
walkup.append(pygame.image.load('ddc_graphics/walk_up1.png'))
walkup.append(pygame.image.load('ddc_graphics/walk_up2.png'))
i2=0

playerface=[]
playerface.append(pygame.image.load('ddc_graphics/stand_up.png'))
playerface.append(pygame.image.load('ddc_graphics/stand_down.png'))
playerface.append(pygame.image.load('ddc_graphics/stand_left.png'))
playerface.append(pygame.image.load('ddc_graphics/stand_right.png'))
playerimage=playerface[0]

# GAME LOOP

bgk=0
lst=[0,0]
register=0;
MapObjects=[]
while True:
    # obstacle
    bg=map[bgk%46]
    bgk+=1
    bg=pygame.transform.scale(bg, (976*2,436*2))

    display.fill((0,0,0,0))

    mouse_x,mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print(lst)
            
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_o:
                fout.write(str(lst[0])+" "+str(lst[1])+"\n")

                print("NOTED "+str(register%2))
                register+=1
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))

    keys = pygame.key.get_pressed()

# WHITE BLOCKS
    prev=[display_scroll[0],display_scroll[1]]


    display.blit(bg, (0-display_scroll[0], 0-display_scroll[1]))
    lst[0]=display_scroll[0]
    lst[1]=display_scroll[1]
    
    # if event.type==pygame.KEYDOWN:
        
    # print(lst)

    if event.type == pygame.KEYUP:
        if event.key==pygame.K_w:
            # print(lst)
            playerimage=playerface[0]
        elif event.key==pygame.K_a:
            playerimage=playerface[3]
        elif event.key==pygame.K_s:
            playerimage=playerface[1]
        elif event.key==pygame.K_d:
            playerimage=playerface[2]
    #pygame.draw.rect(display,(0,0,0), pygame.Rect(515-display_scroll[0],550-display_scroll[1],200,300))      
    if keys[pygame.K_a]:
        display_scroll[0]-=5
        playerimage=pygame.transform.rotate (pygame.transform.flip(walkleft[i//5], False, True),180)

        i+=1
        if(i==20):
            i=0

        for bullet in player_bullets:
            bullet.x +=5

    if keys[pygame.K_w]:
        if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_s]:
            playerimage=walkup[i2//5]
            i2+=1
            if(i2==10):
                i2=0
        display_scroll[1]-=5
        for bullet in player_bullets:
            bullet.y +=5

    if keys[pygame.K_s]:
        if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w]:
            playerimage=walkdown[i1//5]
            i1+=1
            if(i1==10):
                i1=0

        for bullet in player_bullets:
            bullet.y -=5
        display_scroll[1]+=5
        
    if keys[pygame.K_d]:
        playerimage=walkleft[i//5]
        i+=1
        if(i==20):
            i=0

        display_scroll[0]+=5
        for bullet in player_bullets:
            bullet.x -=5
   
    # if  (100<display_scroll[0]<300)and(200<display_scroll[1]<500):

    #     display_scroll[0]=prev[0]
    #     display_scroll[1]=prev[1]   
    for obstacle_object in obstacle: 
        if obstacle_object.main(display_scroll):
            display_scroll[0]=prev[0]
            display_scroll[1]=prev[1]
            break

    for bullet in player_bullets:
        bullet.main(display)

    display.blit(playerimage,(400,300))
    clock.tick(30)

    pygame.display.update()
fout.close()
fin.close()
