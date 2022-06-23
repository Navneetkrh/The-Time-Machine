import pygame
import math
import sys
pygame.init()
dis_width=1200
dis_height=500
# Creating window
screen = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game - Blank")
clock = pygame.time.Clock()

# Game specific variables
exit_game = False
game_over = False

white=(100,150,200)
x=300
y=300


x1 = 0
y1 = 0
player_bullets=[]
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

        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 5)





while not exit_game:
    mouse_x,mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullets.append(PlayerBullet(x,y, mouse_x, mouse_y))
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_d:

                x1=10
                y1=0
            elif event.key == pygame.K_a:

                x1=-10
                y1=0
            elif event.key== pygame.K_w:

                y1=-10
                x1=0
            elif event.key== pygame.K_s:
                y1=10
                x1=0

    if (x>= dis_width-20):
        x1=-x1
    elif (x<=0+20):
        x1=-x1
    if(y>=dis_height-20):
        y1=-y1
    elif(y<=0+20):
        y1=-y1
    x+=x1
    y+=y1




    screen.fill(white)

    pygame.draw.circle(screen, (200, 10, 25), [x,y], 15)
    for bullet in player_bullets:
        bullet.main(screen)
    pygame.display.flip()
    clock.tick(30)




pygame.quit()
quit()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


