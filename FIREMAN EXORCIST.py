import pygame, sys, random, time
from pygame.locals import *

WWD = 1280
WHT = 800

INT = 40
FPS = 60 # Frames per second

fs = 6 # Foreground scrolling speed
bs = 3 # Background scrolling speed

BLACK = (0,0,0) # Colors
RED = (255,0,0)
BLUE = (0,255,255)
WHITE = (255,255,255)

background_surface1 = pygame.image.load('BG.jpg')
size1 = (width, height) = background_surface1.get_size()
Level1 = pygame.display.set_mode(size1)

pygame.init()
pygame.key.set_repeat(INT,INT) # pygame.init disables keyboard repetition.
                                # This reenables it with a delay and rep interval

######JOYSTICK CONTROL####
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count != 0:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        buttons = joystick.get_numbuttons()
        axes = joystick.get_numaxes()
        for i in range( axes ):
            axis = joystick.get_axis( i )
        for i in range( buttons ):
            button = joystick.get_button( i )
        hats = joystick.get_numhats()
        for i in range( hats ):
            hat = joystick.get_hat( i )
else:
    pygame.joystick.quit()

mainClock = pygame.time.Clock()


class Label:
    def __init__(self,surf,cx,cy,fsize,strng,fcolor,bcolor):
        self.screen = surf
        self.fc = fcolor
        self.bc = bcolor
        self.font = pygame.font.SysFont(None,fsize)
        self.cx = cx
        self.cy = cy
        self.str = strng
        self.vis = False # tells if the label is visible

    def draw(self):
        self.text = self.font.render(self.str,True,self.fc,self.bc)
        self.rect = self.text.get_rect()
        self.rect.centerx = self.cx
        self.rect.centery = self.cy
        self.screen.blit(self.text,self.rect)
        pygame.display.update([self.rect])
        self.vis = True

    def undraw(self):
        self.text.fill(self.bc)
        self.screen.blit(self.text,self.rect)
        pygame.display.update([self.rect])
        self.vis = False

#####################################################################################
##############################NON-LEVEL SCRENES######################################
#####################################################################################


#####################################################################################
##########################OPENING SCREEN#############################################
#####################################################################################
def OpeningScreen(Scr):
    STOP = False
    OPTION1 = True
    OPTION2 = False
    pygame.key.set_repeat()
    while not STOP:
        for event in pygame.event.get():
            L1 = Label(Display,WWD//2,WHT//4,WHT*5//50,"FIREMAN EXORCIST", RED, BLACK)
            if OPTION1 == True:
                P = Label(Display,WWD//2,WHT*6//8,WHT*5//50,"PLAY", WHITE, BLACK)
                Q = Label(Display,WWD//2,WHT*7//8,WHT*5//50,"QUIT", RED, BLACK)
            elif OPTION1 == False:
                P = Label(Display,WWD//2,WHT*6//8,WHT*5//50,"PLAY", RED, BLACK)
                Q = Label(Display,WWD//2,WHT*7//8,WHT*5//50,"QUIT", WHITE, BLACK)
            L1.draw()
            P.draw()
            Q.draw()
            if event.type == QUIT:
                L1.undraw()
                P.undraw()
                Q.undraw()
                Quit(Display)

        ########JOYSTICK COMMANDS##################
            if pygame.joystick.get_init() == True:
                if event.type == JOYBUTTONDOWN:
                    if event.button == 7:
                        STOP = True
                    if event.button == 0:
                        if OPTION1 == True:
                            STOP = True
                        if OPTION2 == True:
                            L1.undraw()
                            P.undraw()
                            Q.undraw()
                            Quit(Display)
                if event.type == JOYAXISMOTION or event.type == JOYHATMOTION:
                    if joystick.get_axis(1) == -1 or joystick.get_axis(1) == 1 or joystick.get_hat(0) == (0,-1) or joystick.get_hat(0) == (0,1):
                        if OPTION1 == True:
                            OPTION1,OPTION2 = OPTION2,OPTION1
                        elif OPTION2 == True:
                            OPTION1,OPTION2 = OPTION2,OPTION1

        ########KEYBOARD COMMANDS##################
            if event.type == KEYDOWN:
                if event.key == K_DOWN or event.key == K_UP:
                    if OPTION1 == True:
                        OPTION1,OPTION2 = OPTION2,OPTION1
                    elif OPTION2 == True:
                        OPTION1,OPTION2 = OPTION2,OPTION1
                if event.key == K_RETURN:
                    if OPTION1 == True:
                        STOP = True
                    if OPTION2 == True:
                        L1.undraw()
                        P.undraw()
                        Q.undraw()
                        Quit(Display)

####QUIT MENU###
def Quit(Scr):
    STOP = False
    OPTION1 = True
    OPTION2 = False
    pygame.key.set_repeat()
    while not STOP:
        for event in pygame.event.get():
            pygame.display.update()
            L2 = Label(Display,WWD//2,WHT//4,WHT*5//50,"Are you sure you want to quit the game?", RED, BLACK)
            if OPTION1 == True:
                Y = Label(Display,WWD//2,WHT//3,WHT*5//50,"Yes", WHITE, BLACK)
                N = Label(Display,WWD//2,WHT//2.4,WHT*5//50,"No", RED, BLACK)
            elif OPTION2 == True:
                Y = Label(Display,WWD//2,WHT//3,WHT*5//50,"Yes", RED, BLACK)
                N = Label(Display,WWD//2,WHT//2.4,WHT*5//50,"No", WHITE, BLACK)
            L2.draw()
            Y.draw()
            N.draw()
            if event.type == QUIT:
                pygame.quit()

            ########JOYSTICK COMMANDS##################
            if pygame.joystick.get_init() == True:
                if event.type == JOYAXISMOTION or event.type == JOYHATMOTION:
                    if joystick.get_axis(1) == -1 or joystick.get_axis(1) == 1 or joystick.get_hat(0) == (0,-1) or joystick.get_hat(0) == (0,1):
                        if OPTION1 == True:
                            OPTION1,OPTION2 = OPTION2,OPTION1
                        elif OPTION2 == True:
                            OPTION2,OPTION1 = OPTION1,OPTION2
                if event.type == JOYBUTTONDOWN:
                    if event.button == 0:
                        if OPTION1 == True:
                            pygame.quit()
                            a = False
                            STOP = True
                        if OPTION2 == True:
                            L2.undraw()
                            Y.undraw()
                            N.undraw()
                            a = True
                            STOP = True

            ########KEYBOARD COMMANDS##################
            if event.type == KEYDOWN:
                if event.key == K_DOWN or event.key == K_UP:
                    if OPTION1 == True:
                        OPTION1,OPTION2 = OPTION2,OPTION1
                    elif OPTION2 == True:
                        OPTION1,OPTION2 = OPTION2,OPTION1
                if event.key == K_RETURN:
                    if OPTION1 == True:
                        pygame.quit()
                        a = False
                        STOP = True
                    if OPTION2 == True:
                        L2.undraw()
                        Y.undraw()
                        N.undraw()
                        a = True
                        STOP = True

            pygame.display.update()
    return a


####################################################################################################################
###################################################CUTSCENES########################################################
####################################################################################################################

def screen1(Scr):
    Scr.fill(BLACK)
    pygame.display.update()
    STOP = False
    pygame.key.set_repeat()
    while not STOP:
        for event in pygame.event.get():
            L1 = Label(Display,WWD//2,WHT//4,WHT*5//50,"LEVEL 1: Damned Necromancers", WHITE, BLACK)
            L1.draw()
            if event.type == QUIT:
                L1.undraw()
                Quit(Display)
                L1.draw()

            ########JOYSTICK COMMANDS##################
            if pygame.joystick.get_init() == True:
                if event.type == pygame.JOYBUTTONDOWN:
                    L1.undraw()
                    STOP = True
            ########KEYBOARD COMMANDS##################
            if event.type == KEYDOWN:
                L1.undraw()
                STOP = True

def screen2(Scr):
    Scr.fill(BLACK)
    pygame.display.update()
    STOP = False
    pygame.key.set_repeat()
    while not STOP:
        for event in pygame.event.get():
            L1 = Label(Display,WWD//2,WHT//4,WHT*5//50,"LEVEL 2: Hell breaks loose", WHITE, BLACK)
            L1.draw()
            if event.type == QUIT:
                L1.undraw()
                Quit(Display)
                L1.draw()

            ########JOYSTICK COMMANDS##################
            if pygame.joystick.get_init() == True:
                if event.type == pygame.JOYBUTTONDOWN:
                    L1.undraw()
                    STOP = True
            ########KEYBOARD COMMANDS##################
            if event.type == KEYDOWN:
                L1.undraw()
                STOP = True

def screen3(Scr):
    Scr.fill(BLACK)
    pygame.display.update()
    STOP = False
    pygame.key.set_repeat()
    while not STOP:
        L1 = Label(Display,WWD//2,WHT//4,WHT*5//50,"LEVEL 3", WHITE, BLACK)
        for event in pygame.event.get():
            L1.draw()
            if event.type == QUIT:
                L1.undraw()
                Quit(Display)
                L1.draw()

            ########JOYSTICK COMMANDS##################
            if pygame.joystick.get_init() == True:
                if event.type == pygame.JOYBUTTONDOWN:
                    L1.undraw()
                    STOP = True
            ########KEYBOARD COMMANDS##################
            if event.type == KEYDOWN:
                L1.undraw()
                STOP = True

def screen4(Scr):
    Scr.fill(BLACK)
    pygame.display.update()
    STOP = False
    pygame.key.set_repeat()
    while not STOP:
        L1 = Label(Display,WWD//2,WHT//4,WHT*5//50,"YOU HAVE COMPLETED FIREMAN EXORCIST", WHITE, BLACK)
        L2 = Label(Display,WWD//2,WHT//5,WHT*5//50,"THANK YOU FOR PLAYING!", WHITE, BLACK)
        for event in pygame.event.get():
            L1.draw()
            L2.draw()
            if event.type == QUIT:
                L1.undraw()
                Quit(Display)
                L1.draw()

            ########JOYSTICK COMMANDS##################
            if pygame.joystick.get_init() == True:
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 7:
                        L1.undraw()
                        L2.undraw()
                        STOP = True
            ########KEYBOARD COMMANDS##################
            if event.type == KEYDOWN:
                L1.undraw()
                L2.undraw()
                STOP = True
####################################################################################################################
#############################################PAUSE FUNCTIONS########################################################
####################################################################################################################
def Pause(Scr):
    STOP = False
    OPTION1 = True
    OPTION2 = False
    while not STOP:
        for event in pygame.event.get():
            L1 = Label(Display,WWD//2,WHT//4,WHT*5//50,"PAUSE", RED, BLACK)
            if OPTION1 == True:
                Resume = Label(Display,WWD//2,WHT//3,WHT*5//50,"RESUME", WHITE, BLACK)
                End = Label(Display,WWD//2,WHT//2.4,WHT*5//50,"QUIT", RED, BLACK)
            elif OPTION1 == False:
                Resume = Label(Display,WWD//2,WHT//3,WHT*5//50,"RESUME", RED, BLACK)
                End = Label(Display,WWD//2,WHT//2.4,WHT*5//50,"QUIT", WHITE, BLACK)
            L1.draw()
            Resume.draw()
            End.draw()

            ########JOYSTICK COMMANDS##################
            if pygame.joystick.get_init() == True:
                if event.type == QUIT:
                    L1.undraw()
                    Resume.undraw()
                    End.undraw()
                    Quit(Display)
                    a = False
                    STOP = True
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 7:
                        a = False
                        STOP = True
                    if event.button == 0:
                        if OPTION1 == True:
                            a = False
                            STOP = True
                        if OPTION2 == True:
                            L1.undraw()
                            Resume.undraw()
                            End.undraw()
                            a = Quit(Display)
                            STOP = True
                if event.type == JOYAXISMOTION or event.type == JOYHATMOTION:
                    if joystick.get_axis(1) == -1 or joystick.get_axis(1) == 1 or joystick.get_hat(0) == (0,-1) or joystick.get_hat(0) == (0,1):
                        OPTION1,OPTION2 = OPTION2,OPTION1

            ########KEYBOARD COMMANDS##################
            if event.type == KEYDOWN:
                if event.key == K_DOWN or event.key == K_UP:
                    OPTION1,OPTION2 = OPTION2,OPTION1
                if event.key == K_RETURN:
                    if OPTION1 == True:
                        a = False
                        STOP = True
                    if OPTION2 == True:
                        L1.undraw()
                        Resume.undraw()
                        End.undraw()
                        a = Sure(Display)
                        STOP = True
                if event.key == ord('p'):
                    a = False
                    STOP = True
                    
            pygame.display.update()
    return a


############################################################################################################
#############################################RETURN TO MAIN MENU############################################
############################################################################################################
def Sure(Scr):
    Scr.fill(BLACK)
    STOP = False
    OPTION1 = True
    OPTION2 = False
    while not STOP:
        for event in pygame.event.get():
            if OPTION1 == True:
                Y = Label(Display,WWD//2,WHT//3,WHT*5//50,"Yes",  WHITE, BLACK)
                N = Label(Display,WWD//2,WHT//2.4,WHT*5//50,"No", RED, BLACK)
            elif OPTION2 == True:
                Y = Label(Display,WWD//2,WHT//3,WHT*5//50,"Yes", RED, BLACK)
                N = Label(Display,WWD//2,WHT//2.4,WHT*5//50,"No", WHITE, BLACK)
            L2 = Label(Display,WWD//2,WHT//4,WHT*4//50,"Are you sure you want to return to the main menu?", RED, BLACK)
            L2.draw()
            Y.draw()
            N.draw()

            if event.type == QUIT:
                a = False
                #L2.undraw()
                STOP = True

            ##########JOYSTICK COMMANDS############
            if pygame.joystick.get_init() == True:
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 7:
                        a = False
                        STOP = True
                    if event.button == 0:
                        if OPTION2 == True:
                            a = False
                            STOP = True
                        if OPTION1 == True:
                            L2.undraw()
                            a = True
                            Y.undraw()
                            N.undraw()
                            STOP = True

                if event.type == JOYAXISMOTION or event.type == JOYHATMOTION:
                    if joystick.get_axis(1) == -1 or joystick.get_axis(1) == 1 or joystick.get_hat(0) == (0,-1) or joystick.get_hat(0) == (0,1):
                        OPTION1,OPTION2 = OPTION2,OPTION1

            ##########KEYBOARD COMMANDS############
            if event.type == KEYDOWN:
                if event.key == K_DOWN or event.key == K_UP:
                    OPTION1,OPTION2 = OPTION1,OPTION2
                if event.key == K_RETURN:
                    if OPTION1 == True:
                        a = False
                        STOP = True
                    if OPTION2 == True:
                        L2.undraw()
                        a = True
                        Y.undraw()
                        N.undraw()
                        STOP = True

                if event.key == K_RETURN:
                    if OPTION2 == True:
                        a = False
                        STOP = True
                    if OPTION1 == True:
                        L2.undraw()
                        a = True
                        Y.undraw()
                        N.undraw()
                        STOP = True


            pygame.display.update()

    return a


##############################################################################################
#################################################GAME OVER/RETRY SCREEN#############################
##############################################################################################
def retry(level):
    pygame.display.set_caption('FIREMAN EXORCIST')
    Display = pygame.display.set_mode((WWD,WHT),0,0)
    STOP = False
    while not STOP:
        for event in pygame.event.get():
            if level == 1:
                screen1(Display)
                SpritesGame(Display,1).run()
                level = 2

            if level == 2:
                screen2(Display)
                SpritesGame(Display,2).run()
                level = 3

            #RETRY LEVEL 3#
            if level == 3:
                screen3(Display)
                SpritesGame(Display,3).run()

            screen4(Display)
            OpeningScreen(Display)
    #        pygame.mixer.music.load('background.wav')
            Display = pygame.display.set_mode((WWD,WHT),0,0)
            pygame.mixer.music.stop()
            pygame.display.update()

def GameOver(Scr,level):
    Scr.fill(BLACK)
    GO = pygame.mixer.Sound("GameOver.wav")
    GO.play()
    STOP = False
    OPTION1 = True
    OPTION2 = False
    while not STOP:
        for event in pygame.event.get():
            if OPTION1 == True:
                Y = Label(Display,WWD//2,WHT//3,WHT*5//50,"YES",  WHITE, BLACK)
                N = Label(Display,WWD//2,WHT//2.4,WHT*5//50,"NO", RED, BLACK)
            elif OPTION2 == True:
                Y = Label(Display,WWD//2,WHT//3,WHT*5//50,"YES", RED, BLACK)
                N = Label(Display,WWD//2,WHT//2.4,WHT*5//50,"NO", WHITE, BLACK)
            L2 = Label(Display,WWD//2,WHT//4,WHT*4//50,"Looks like Satan wins this round. Play again?", RED, BLACK)
            L2.draw()
            Y.draw()
            N.draw()

            if event.type == QUIT:
                a = False
                STOP = True

            if pygame.joystick.get_init() == True:
                if event.type == JOYAXISMOTION or event.type == JOYHATMOTION:
                    if joystick.get_axis(1) == -1 or joystick.get_axis(1) == 1 or joystick.get_hat(0) == (0,-1) or joystick.get_hat(0) == (0,1):
                        OPTION1,OPTION2 = OPTION2,OPTION1

                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 7:
                        a = False
                        STOP = True
                    if event.button == 0:
                        if OPTION2 == True:
                            a = False
                            STOP = Quit()
                        if OPTION1 == True:
                            L2.undraw()
                            a = True
                            Y.undraw()
                            N.undraw()
                            retry(level)

            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    OPTION1,OPTION2 = OPTION2,OPTION1
                    L2.undraw()
                    a = False
                    STOP = True
                if event.key == K_RETURN:
                    if OPTION2 == True:
                        a = False
                        STOP = True
                    if OPTION1 == True:
                        L2.undraw()
                        a = True
                        Y.undraw()
                        N.undraw()
                        STOP = True
            pygame.display.update()
    return a

######################################################################################################################
#################################ALL MOVING OBJECTS###################################################################
######################################################################################################################

#BACKGROUND DISPLAY
class Background:
    def __init__(self,Scr,cx,cy,speed,bcolor):
        self.screen = Scr
        #self.surf = pygame.transform.scale(pygame.image.load('BG.jpg'), (WWD, WHT))
        self.surf = pygame.image.load('BG.jpg')
        self.rect = self.surf.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        self.speed = speed
        self.bc = bcolor
        self.dir = ''
        
    def draw(self):
        self.screen.blit(self.surf,self.rect)

    def move(self):
        if self.dir != '':
            if self.dir == 'l' and self.rect.left != 0:
                self.rect.left += self.speed * bs
            if self.dir == 'r':
                self.rect.right -= self.speed * bs

class Background2:
    def __init__(self,Scr,cx,cy,speed,bcolor):
        self.screen = Scr
        self.surf = pygame.image.load('BG2.jpg')
        self.rect = self.surf.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        self.speed = speed
        self.bc = bcolor
        self.dir = ''
        
    def draw(self):
        self.screen.blit(self.surf,self.rect)

    def move(self):
        if self.dir != '':
            if self.dir == 'l' and self.rect.left != 0:
                self.rect.left += self.speed * bs
            if self.dir == 'r':
                self.rect.right -= self.speed * bs

#FOREGROUND DISPLAY
class Foreground:
    def __init__(self,Scr,cx,cy,speed,bcolor):
        self.screen = Scr
        self.surf = pygame.transform.scale(pygame.image.load('FG.png'), (WWD, WHT/4))
        self.rect = self.surf.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        self.speed = speed
        self.bc = bcolor
        self.dir = ''

    def draw(self):
        self.screen.blit(self.surf,self.rect)

    def move(self):
        if self.dir != '':
            if self.dir == 'l' and self.rect.left != 0:
                self.rect.left += self.speed * fs
            if self.dir == 'r':
                self.rect.right -= self.speed * fs

################################################################################
####################INTERACTIVE OBJECTS#########################################
################################################################################                
class Obsticle:
    def __init__(self,Scr,cx,cy,fire,obj):
        self.screen = Scr
        self.surf = pygame.image.load('rubble.png')
        self.surf = pygame.transform.scale(self.surf, (WWD/4, WHT/4))
        self.rect = self.surf.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        self.start = cx
        self.speed = 6
        self.dir = ''
        self.fire = fire
        self.obj = obj
        self.move = True
        self.testspeed = 1

    def draw(self,speedstart = 3):
        pygame.time.set_timer(USEREVENT+1, 150)

        if self.fire == True and self.obj == 1:
            if self.testspeed <= speedstart and self.testspeed > (speedstart/2):
                self.surf = pygame.image.load('rubble.png')
            if self.testspeed <= (speedstart/2) and self.testspeed > 0:
                self.surf = pygame.image.load('rubble2.png')
            if self.testspeed == 0:
                self.testspeed = speedstart
            self.testspeed -= 1

        if self.obj == 2:
            if self.fire == True:
                if self.testspeed <= speedstart and self.testspeed > (speedstart-(speedstart/4)):
                    self.surf = pygame.image.load('FNME.png')
                if self.testspeed <= (speedstart-(speedstart/4)) and self.testspeed > (speedstart/2):
                    self.surf = pygame.image.load('FNME copy.png')
                if self.testspeed <= (speedstart/2) and self.testspeed > (speedstart/4):
                    self.surf = pygame.image.load('FNME2.png')
                if self.testspeed <= (speedstart/4) and self.testspeed > 0:
                    self.surf = pygame.image.load('FNME2 copy.png')
                if self.testspeed == 0:
                    self.testspeed = speedstart
                self.testspeed -= 1

            elif self.fire == False:
                if self.testspeed <= speedstart and self.testspeed > (speedstart/2):
                    self.surf = pygame.image.load('NME1.png')
                if self.testspeed <= (speedstart/2) and self.testspeed > 0:
                    self.surf = pygame.image.load('NME2.png')
                if self.testspeed == 0:
                    self.testspeed = speedstart
                self.testspeed -= 1

        if self.obj == 3:
            if self.fire == True:
                if self.testspeed <= speedstart and self.testspeed > (speedstart-(speedstart/4)):
                    self.surf = pygame.image.load('FRNME1.png')
                if self.testspeed <= (speedstart-(speedstart/4)) and self.testspeed > (speedstart/2):
                    self.surf = pygame.image.load('FRNME1 copy.png')
                if self.testspeed <= (speedstart/2) and self.testspeed > (speedstart/4):
                    self.surf = pygame.image.load('FRNME2.png')
                if self.testspeed <= (speedstart/4) and self.testspeed > 0:
                    self.surf = pygame.image.load('FRNME2 copy.png')
                if self.testspeed == 0:
                    self.testspeed = speedstart
                self.testspeed -= 1
            elif self.fire == False:
                if self.testspeed <= speedstart and self.testspeed > (speedstart/2):
                    self.surf = pygame.image.load('RNME.png')
                if self.testspeed <= (speedstart/2) and self.testspeed > 0:
                    self.surf = pygame.image.load('RNME2.png')
                if self.testspeed == 0:
                    self.testspeed = speedstart
                self.testspeed -= 1

        if self.obj == 4:
            speedstart = 12
            if self.fire == True:
                if self.testspeed <= speedstart and self.testspeed > (speedstart-(speedstart/4)):
                    self.surf = pygame.image.load('BossF1.png')
                if self.testspeed <= (speedstart-(speedstart/4)) and self.testspeed > (speedstart/2):
                    self.surf = pygame.image.load('BossF2.png')
                if self.testspeed <= (speedstart/2) and self.testspeed > (speedstart/4):
                    self.surf = pygame.image.load('BossF3.png')
                if self.testspeed <= (speedstart/4) and self.testspeed > 0:
                    self.surf = pygame.image.load('BossF4.png')
                if self.testspeed == 0:
                    self.testspeed = speedstart
                self.testspeed -= 1
            elif self.fire == False:
                self.surf = pygame.image.load('Boss7.png')
        self.screen.blit(self.surf,self.rect)
        pygame.display.update([self.rect])


###################################################################################################################
###################################################################################################################

######################################################################################################################
################################PLAYER MECHANICS######################################################################
######################################################################################################################
class Player:
    def __init__(self,Scr,cx,cy,speed,bcolor):
        self.screen = Scr
        self.surf = pygame.image.load('RS.png')
        self.rect = self.surf.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        self.speed = speed
        self.wdir = ''
        self.dir = ''
        self.ATK = ''
        self.testspeed = 1

    def draw(self):
        self.screen.blit(self.surf,self.rect)
        pygame.display.update([self.rect])

    #Movement
    def move(self, speedstart = 3):
        if self.dir != '':
            if self.dir == 'l':
                self.testspeed -= 1
                if self.testspeed <= speedstart and self.testspeed > (speedstart/2):
                    self.surf = pygame.image.load('LW1.png')
                if self.testspeed <= (speedstart/2) and self.testspeed > 0:
                    self.surf = pygame.image.load('Lw2.png')
                if self.testspeed == 0:
                    self.testspeed = speedstart
            if self.dir == 'r':
                self.testspeed -= 1
                if self.testspeed <= speedstart and self.testspeed > (speedstart/2):
                    self.surf = pygame.image.load('RW1.png')
                if self.testspeed <= (speedstart/2) and self.testspeed > 0:
                    self.surf = pygame.image.load('RW2.png')
                if self.testspeed == 0:
                    self.testspeed = speedstart
        if self.wdir != '':
            if self.wdir == 'l' and self.rect.left > 0:
                self.rect.left -= self.speed * fs
            if self.wdir == 'r' and self.rect.centerx != WWD/2:
                self.rect.right += self.speed * fs
            if self.wdir == 'l2' and self.rect.centerx != WWD/2:
                self.rect.centerx -= self.speed * fs
            if self.wdir == 'r2' and self.rect.right < WWD:
                self.rect.right += self.speed * fs
        pygame.display.update([self.rect])

#MELEE ATTACKS
class Attack:
    def __init__(self,Scr,cx,cy,speed,bcolor):
        self.screen = Scr
        self.surf = pygame.image.load('ATK1.png')
        self.rect = self.surf.get_rect()
        self.dir = 'r'
        self.ATK = ''
        self.rect.centerx = cx
        self.rect.centery = cy
        self.speed = speed
        self.testspeed = 1

    def draw(self,speedstart = 3):
        self.screen.blit(self.surf,self.rect)
        pygame.display.update([self.rect])

    def undraw(self):
        surf = self.surf.copy()
        self.screen.blit(surf,self.rect)
        pygame.display.update([self.rect])

#SPRAY WATER
class Water:
    def __init__(self,Scr,cx,cy,speed,bcolor):
        self.screen = Scr
        self.surf = pygame.image.load('Water.png')
        self.rect = self.surf.get_rect()
        self.dist = 50
        self.start = cx
        self.dir = 'r'
        self.rect.centerx = cx
        self.rect.centery = cy
        self.speed = speed

    def draw(self):
        self.rect.centerx = self.start + self.dist
        self.rect.centerx += self.dist
        self.screen.blit(self.surf,self.rect)
        pygame.display.update([self.rect])

    def undraw(self):
        surf = self.surf.copy()
        self.screen.blit(surf,self.rect)
        pygame.display.update([self.rect])

class Hydrant:
    def __init__(self,Scr,cx,cy,fire,obj):
        self.screen = Scr
        self.surf = pygame.image.load('hydrant.png')
        self.surf = pygame.transform.scale(self.surf, (WWD/4, WHT/4))
        self.rect = self.surf.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        self.start = cx
        self.speed = 6
        self.dir = ''
        self.fire = fire
        self.obj = obj
        self.move = True
        self.testspeed = 1

    def draw(self,speedstart = 3):
        pygame.time.set_timer(USEREVENT+1, 150)
        if self.testspeed <= speedstart and self.testspeed > (speedstart/2):
            self.surf = pygame.image.load('rubble.png')
        if self.testspeed <= (speedstart/2) and self.testspeed > 0:
            self.surf = pygame.image.load('rubble2.png')
        if self.testspeed == 0:
            self.testspeed = speedstart
        self.testspeed -= 1
######################################################################################################################
##############################PLAYING THE GAME########################################################################
######################################################################################################################

class SpritesGame:
    def __init__(self,Scr,level):
        self.P_health = 10
        self.ammo = 100
        self.Attack = 0
        self.HolyPower = 50
        self.repeat = True
        self.level = level
        self.Score = 0
        self.Scr = Scr
        self.testspeed = 2
        self.Background = Background(Scr,WWD/2,WHT/2,6,BLACK)
        self.Background2 = Background2(Scr,WWD/2,WHT/2,6,BLACK)
        self.Foreground = Foreground(Scr,WWD/2,WHT,6,BLACK)
        self.Player = Player(Scr,WWD/2,WHT-(WHT/4.6),6,BLACK)
        self.PlayerR = Player(Scr,(WWD/2)+25,WHT-(WHT/4.6),6,BLACK)
        self.PlayerL = Player(Scr,(WWD/2)-25,WHT-(WHT/4.6),6,BLACK)

        self.A1 = Attack(Scr,self.Player.rect.centerx,self.Player.rect.centery,6,BLACK)
        self.A1L = Attack(Scr,self.Player.rect.centerx-25,self.Player.rect.centery,6,BLACK)
        self.A1R = Attack(Scr,self.Player.rect.centerx+25,self.Player.rect.centery,6,BLACK)

        self.Water = Water(Scr,self.Player.rect.centerx,self.Player.rect.centery,6,BLACK)

        Tip1 = Label(Display,WWD//2,WHT*2//8,WHT*5//50,"Press X to destroy barriers", RED, BLACK)
        Tip2 = Label(Display,WWD//2,WHT*2//8,WHT*5//50,"Flaming Obsticles take longer to break", WHITE, BLACK)
        Tip3 = Label(Display,WWD//2,WHT*3//8,WHT*5//50,"Extinguish them with RT", WHITE, BLACK)
        Tip4 = Label(Display,WWD//2,WHT*3//8,WHT*5//50,"Block enemy attacks with LT", WHITE, BLACK)

        self.Barriers = [ ]

        #self.Barriers.append(Obsticle(Scr,self.Barriers[3].right-50,,WHT-(WHT/6),False,4))

        self.bScroll = [ ]
        self.fScroll = [ ]

        if self.level == 1:
            self.bScroll.append(Background(Scr,(WWD*2.5),WHT/2,6,BLACK))
            for j in range (0,4):
                self.fScroll.append(Foreground(Scr,(WWD*(j+0.5)),WHT,6,BLACK))
            for i in range(200,800,200):
                self.Barriers.append(Obsticle(Scr,(WWD)+(4*i),WHT-(WHT/6),True,1))
            for k in range(100,900,200):
                self.Barriers.append(Obsticle(Scr,(WWD)+(4*k),WHT-(WHT/6),False,1))

            self.Barriers.append(Obsticle(Scr,self.fScroll[-1].rect.right,WHT-(WHT/6),True,2))


        elif self.level == 2:
            self.bScroll.append(Background2(Scr,(WWD*2.5),WHT/2,6,BLACK))
            for j in range (0,10):
                self.fScroll.append(Foreground(Scr,(WWD*(j+0.5)),WHT,6,BLACK))
            for i in range(200,1600,200):
                self.Barriers.append(Obsticle(Scr,(WWD)+(4*i),WHT-(WHT/6),False,2))
            for k in range(100,1500,200):
                self.Barriers.append(Obsticle(Scr,(WWD)+(4*k),WHT-(WHT/6),False,3))
            #FLAMING ENEMIES#
            for i in range(2000,2800,200):
                self.Barriers.append(Obsticle(Scr,(WWD)+(4*i),WHT-(WHT/6),True,2))
            for k in range(1700,2900,200):
                self.Barriers.append(Obsticle(Scr,(WWD)+(4*k),WHT-(WHT/6),True,3))
                
        elif self.level == 3:
            self.bScroll.append(Background2(Scr,(WWD*2.5),WHT/2,6,BLACK))
            self.Barriers.append(Obsticle(Scr,(WWD),WHT/1.57,True,4))
            for j in range (0,4):
                self.fScroll.append(Foreground(Scr,(WWD*(j+0.5)),WHT,6,BLACK))

        self.startTime = time.clock()
        self.endTime = -1
        self.shooting = False
        self.move = False
        self.block = False
                                 

    def update(self):
        self.Background.draw()
        self.Background.move()
        self.Foreground.move()
        self.Foreground.draw()

        Tip1 = Label(Display,WWD//2,WHT*2//8,WHT*5//50,"Press X to destroy barriers", RED, BLACK)
        Tip2 = Label(Display,WWD//2,WHT*2//8,WHT*5//50,"Flaming Obsticles take longer to break", WHITE, BLACK)
        Tip3 = Label(Display,WWD//2,WHT*3//8,WHT*5//50,"Extinguish them with RT", WHITE, BLACK)
        Tip4 = Label(Display,WWD//2,WHT*3//8,WHT*5//50,"Block enemy attacks with LT", WHITE, BLACK)

        for s1 in self.bScroll:
            s1.draw()
            
        for s2 in self.fScroll:
            s2.draw()

        if (self.Player.rect.centerx >= self.fScroll[2].rect.centerx) and self.repeat == True:
            EAhead = pygame.mixer.Sound("EAhead.wav")
            EAhead.play()
            self.repeat = False

        if self.shooting == False:
            self.Water.rect.centerx = self.Player.rect.centerx
            self.Water.rect.centery = self.Player.rect.centery

        if self.Water.rect.left == 0:
            self.shooting == False


        if self.A1.dir == 'r':
            self.A1.rect.centerx = self.Player.rect.centerx + 25
            if self.Attack == 1:
                self.A1.surf = pygame.image.load('ATK1.png')
            elif self.Attack == 2:
                self.A1.surf = pygame.image.load('ATK2.png')
            elif self.Attack == 3:
                self.A1.surf = pygame.image.load('ATK3.png')

        if self.A1.dir == 'l':
            self.A1.rect.centerx = self.Player.rect.centerx
            if self.Attack == 1:
                self.A1.surf = pygame.image.load('ATK1L.png')
            elif self.Attack == 2:
                self.A1.surf = pygame.image.load('ATK2L.png')
            elif self.Attack == 3:
                self.A1.surf = pygame.image.load('ATK3L.png')

        if self.A1.dir == 'l' and self.move == False and self.shooting == False:
            self.Player.surf = pygame.image.load('LS.png')            
        if self.A1.dir == 'r' and self.move == False and self.shooting == False:
            self.Player.surf = pygame.image.load('RS.png')

        for b in self.Barriers:
            #REGULAR OBSTICLES
##            if 0 < self.Barriers[0].rect.left - self.Player.rect.right < WWD:
##                Tip1.draw()
##            if 0 < self.Barriers[1].rect.left - self.Player.rect.right < WWD:
##                Tip2.draw()
##                Tip3.draw()

            if b.obj == 1:
                if b.fire == True:
                    b.surf = pygame.image.load('Frubble.png')
                if b.fire == False:
                    b.surf = pygame.image.load('rubble.png')

            #MELEE ENEMIES
            elif b.obj == 2:
                if b.fire == True:
                    b.surf = pygame.image.load('FNMES.png')
                if b.fire == False:
                    b.surf = pygame.image.load('NME.png')

            #RANGED ENEMIES
            elif b.obj == 3:
                if b.fire == True:
                    b.surf = pygame.image.load('FRNMES.png')
                if b.fire == False:
                    b.surf = pygame.image.load('RNMES.png')

            elif b.rect.colliderect(self.Water.rect):
                b.fire = False
            b.draw()

        ##SPRAY WATER##
        if self.A1.dir == 'r' and self.shooting == True:
            self.move = False
            self.Player.surf = pygame.image.load("ShootR.png")

        if self.A1.dir == 'l' and self.shooting == True:
            self.move = False
            self.Player.surf = pygame.image.load("ShootL.png")

        ####BLOCK####
        if self.A1.dir == 'r' and self.block == True and self.HolyPower > 0:
            self.Player.surf = pygame.image.load("BlockHoly.png")
        if self.Water.dir == 'l' and self.block == True and self.HolyPower > 0:
            self.Player.surf = pygame.image.load("BlockHolyL.png")

        self.Player.draw()
        self.Player.move()
        
        Health = Label(Display,72,14,40,"HEALTH: " + str(self.P_health), WHITE, BLACK)
        Health.draw()
        if self.ammo > 0:
            Ammo = Label(Display,70,42,40,"AMMO: " + str(self.ammo), BLACK, BLUE)
        else:
            Ammo = Label(Display,70,42,40," AMMO: OUT", BLACK, BLUE)
        Ammo.draw()

        TotalScore = Label(Display,WWD//2,14,40,"SCORE: " + str(self.Score), WHITE, BLACK)
        TotalScore.draw()

        pygame.display.update()


##########################################################################################
####################################GAME EVENT############################################
##########################################################################################
        
    def run(self):
        pygame.mixer.music.load('background.wav')
        pygame.mixer.music.play(-1, 0.0)
        musicPlaying = True
        c = 0
        pygame.key.set_repeat(INT,INT)
        sHealth = 3
        oHealth = 3
        wSpeed = 50
        ammo = 0
        STOP = False
        PAUSE = False
        Track = False
        firstEn = True
        Sure = False
        a = 0
        a2 = 0
        Multiplier = 1
        inc = 0
        bHealth = 20
        bHit = 0
        bwHit = 0
        moveR = False
        moveL = False
        while not STOP:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.mixer.music.pause()
                    STOP = Quit(Display)
                    pygame.mixer.music.unpause()

                if self.Player.rect.right >= WWD:
                    pygame.mixer.music.stop()
                    STOP = True

            ####IF PLAYER DIES######
                if self.P_health <=0:
                    self.P_health = 1
                    pygame.mixer.music.stop()
                    STOP = GameOver(Display,self.level)

                if PAUSE == False:
                    #### ENEMY A.I ####
                    for b in self.Barriers:
                        if b.obj == 2:
                            if (b.rect.left - self.Player.rect.right) <= WWD/2 and a != 1:
                                EAhead = pygame.mixer.Sound("EAhead.wav")
                                EAhead.play()
                                Track = True
                            if not b.rect.colliderect(self.Player.rect) and Track == True:
                                b.rect.right -= 5
                            if self.Player.rect.colliderect(b.rect) and Track == True and self.block == False:
                                b.rect.right += (WWD/10)
                                self.P_health -= 1
                                a = 1
                                Multiplier = 1
                                Track = False
                            if self.Player.rect.colliderect(b.rect) and Track == True and self.block == True:
                                oHealth -= 3
                                b.rect.right += (WWD/4)
                                a = 1
                                Track = False

                        if b.obj == 3:
                            if (b.rect.left - self.Player.rect.right) <= WWD/2 and a2 != 1:
                                EAhead = pygame.mixer.Sound("EAhead.wav")
                                EAhead.play()
                                Track = True
                            if not b.rect.colliderect(self.PlayerL.rect) and Track == True:
                                b.rect.right -= 5
                            if self.Player.rect.colliderect(b.rect) and Track == True and self.block == False:
                                b.rect.right += (WWD/10)
                                self.P_health -= 1
                                a2 = 1
                                Multiplier = 1
                                Track = False
                            if self.Player.rect.colliderect(b.rect) and Track == True and self.block == True:
                                oHealth -= 3
                                b.rect.right += (WWD/4)
                                a2 = 1
                                Track = False

                            if b.obj == 4:
                                if (b.rect.left - self.Player.rect.right) <= WWD/2 and a != 1:
                                    EAhead = pygame.mixer.Sound("EAhead.wav")
                                    EAhead.play()
                                    Track = True
                                if not b.rect.colliderect(self.Player.rect) and Track == True:
                                    b.rect.right -= 5
                                if self.PlayerR.rect.colliderect(b.rect) and b.fire == True:
                                    self.Player.rect.right -= (WWD/4)
                                    self.P_health -= 3
                                    Multiplier = 1
                                    Track = False
                    
                    if a == 1:
                        inc += 1
                        if inc == 60:
                            a = 0
                            inc = 0

                    if a2 == 1:
                        inc += 1
                        if inc == 60:
                            a2 = 0
                            inc = 0

################################KEYBOARD COMMANDS####################################################

            ###KEYDOWN COMMANDS###
                    if event.type == KEYDOWN:

                    #####MOVING LEFT######
                        if event.key == K_LEFT or event.key == ord('a'):
                            moveR = False
                            moveL = True
                            self.shooting = False
                            self.move = True
                            self.A1.dir = 'l'
                            self.Player.dir = 'l'
                            self.Water.dir = 'l'
                            self.A1.wdir = 'l'
                            if moveL != False:
                                self.Background.dir = 'l'
                                self.Foreground.dir = 'l'
                                                        
                            for b in self.Barriers[:]:
                                if self.PlayerL.rect.collidelistall(self.Barriers[:]):
                                    self.Background.dir = ''
                                    self.Foreground.dir = ''
                                    moveL = False
                                else:
                                    moveL = True

                            if self.fScroll[0].rect.centerx == WWD/2 or self.Player.rect.centerx != WWD/2:
                                moveL = False
                                    
                            if self.fScroll[0].rect.centerx == WWD/2:
                                moveL = False
                                self.Player.wdir = 'l'
                                
                            if self.fScroll[-1].rect.centerx == WWD/2:
                                self.Player.wdir = 'l2'
                                
                            if moveL == True:
                                for s1 in self.bScroll[:]:
                                    s1.rect.centerx += 6 * bs
                                for s2 in self.fScroll[:]:
                                    s2.rect.centerx += 6 * fs
                                for b in self.Barriers[:]:
                                    b.rect.centerx += 6 * fs

                    #####MOVING RIGHT######
                        if event.key == K_RIGHT or event.key == ord('d'):
                            moveR = True
                            moveL = False
                            self.shooting = False
                            self.move = True
                            self.A1.dir = 'r'
                            self.Player.dir = 'r'
                            self.Water.dir = 'r'
                            self.A1.wdir = 'r'
                            if moveR != False:
                                self.Background.dir = 'r'
                                self.Foreground.dir = 'r'

                            for b in self.Barriers[:]:
                                if self.PlayerR.rect.collidelistall(self.Barriers[:]):
                                    self.Background.dir = ''
                                    self.Foreground.dir = ''
                                    moveR = False
                                else:
                                    move = True

                            if self.fScroll[-1].rect.centerx - (6 * fs) < WWD/2:
                               self.fScroll[-1].rect.centerx = WWD/2
                                
                            if self.fScroll[-1].rect.centerx == WWD/2 or self.Player.rect.centerx != WWD/2:
                                moveR = False

                            if self.fScroll[0].rect.centerx == WWD/2:
                                self.Player.wdir = 'r'

                            if self.fScroll[-1].rect.centerx == WWD/2:
                                self.Player.wdir = 'r2'
                                
                            if moveR == True:
                                for s1 in self.bScroll[:]:
                                    s1.rect.right -= 6 * bs
                                for s2 in self.fScroll[:]:
                                    s2.rect.right -= 6 * fs
                                for b in self.Barriers[:]:
                                    b.rect.right -= 6 * fs

                    #####MELEE######
                        if event.key == ord('c'):
                            self.Background.dir = ''
                            self.Foreground.dir = ''
                            self.Player.dir = ''
                            self.Player.wdir = ''
                            pygame.key.set_repeat()
                            c = c + 1
                            ATKsound = pygame.mixer.Sound('Swoosh.wav')
                            hit = pygame.mixer.Sound('hit.wav')
                            kill = pygame.mixer.Sound('kill.wav')
                            EHit = pygame.mixer.Sound('EHit.wav')
                            EDead = pygame.mixer.Sound('EDead.wav')
                            ATKsound.play()

                            #ATK 1#
                            if c == 1:
                                self.Attack = 1
                                
                            #ATK 2#
                            if c == 2:
                                self.Attack = 2
                                
                            #ATK 3#        
                            if c == 3:
                                self.Attack = 3
                                c = 0

                            self.A1.draw()  
                            ##DESTROY OBSTICLES##
                            for b in self.Barriers:
                                if self.A1.rect.colliderect(b.rect): #or self.A2.rect.colliderect(b.rect) or self.A3.rect.colliderect(b.rect):
                                    hit.play()
                                    if b.obj != 4:
                                        if oHealth > 0:
                                            if b.obj != 1:
                                                EHit.play()
                                        if b.fire == True:
                                            oHealth = oHealth - 0.34
                                        if b.fire == False:
                                            oHealth = oHealth - 1
                                        if oHealth <= 0:
                                            kill.play()
                                            self.Barriers.remove(b)
                                            oHealth = sHealth
                                            if b.obj != 1:
                                                EDead.play()
                                        if b.obj == 2:
                                            if self.Attack == 3:
                                                b.rect.right += 60
                                                hit.play()

                                    elif b.obj == 4:
                                        if b.fire == True:
                                            bHealth -= 1
                                        elif b.fire == False:
                                            bHealth -= 2
                                            bHit += 1
                                        if bHit == 5:
                                            b.fire = True
                                            bHit = 0
                                            bwHit = 0

                    ########SHOOTING########
                        if event.key == K_SPACE:
                            self.shooting = True
                            self.Player.dir = ''
                            self.Player.wdir = ''
                            self.Background.dir = ''
                            self.Foreground.dir = ''
                            self.move = False
                            self.Water.start = self.Player.rect.centerx
                            spraySound = pygame.mixer.Sound('water.wav')

                            #SHOOTING RIGHT#
                            if self.Water.dir == 'r' and self.shooting == True and self.ammo > 0:
                                spraySound.play()
                                self.ammo -= 1
                                wSpeed = 50
                                self.Water.dist = wSpeed
                                for i in range (10):
                                    self.Water.dist = wSpeed
                                    self.Water.draw()
                                    if not self.Water.rect.collidelistall(self.Barriers[:]): #and self.Water.rect.right < WWD:
                                        wSpeed += (WWD/50)
                                    else:
                                        self.shooting = False
                                        break

                            #SHOOTING LEFT#
                            if self.Water.dir == 'l' and self.shooting == True and self.ammo > 0:
                                spraySound.play()
                                self.ammo -= 1
                                wSpeed = -50
                                self.Water.dist = wSpeed
                                for i in range (10):
                                    self.Water.dist = wSpeed
                                    self.Water.draw()
                                    if not self.Water.rect.collidelistall(self.Barriers[:]): #and self.Water.rect.right < WWD:
                                        wSpeed -= (WWD/50)
                                    else:
                                        self.shooting = False
                                        break

                                #EXTINGUISH OBSTICLES#
                            for b in self.Barriers[:]:
                                if self.Water.rect.colliderect(b.rect) and ((b.rect.left - self.Player.rect.right) < WWD/2):
                                    if b.fire == True:
                                        b.fire = False
                                    if b.obj == 2:
                                        b.rect.right += 20

                        if event.key == ord('p'):
                            pygame.key.set_repeat()
                            self.Player.dir = ''
                            PAUSE = True
                            self.update()

            #####KEYUP COMMANDS######
                    if event.type == KEYUP:
                        ####MUTE MUSIC####
                        if event.key == ord('m'):
                            if musicPlaying == True:
                                pygame.mixer.music.stop()
                                musicPlaying = False
                            elif musicPlaying == False:
                                pygame.mixer.music.play(-1, 0.0)
                                musicPlaying = True

                        ####MOVE LEFT####                            
                        if event.key == K_LEFT or event.key == ord('a'):
                            self.Player.dir = ''
                            self.Background.dir = ''
                            self.Foreground.dir = ''
                            self.move = False
                            moveL = False

                        ####MOVE RIGHT####                            
                        if event.key == K_RIGHT or event.key == ord('d'):
                            self.Player.dir = ''
                            self.Player.wdir = ''
                            self.A1.dir = 'r'
                            self.Water.dir = 'r'                    
                            self.move = False
                            moveR = False
                        ####MELEE####
                        if event.key == ord('c'):
                            self.Background.dir = ''
                            self.Foreground.dir = ''
                            pygame.key.set_repeat(INT, INT)
                            
                        ####SHOOTING####
                        if event.key == K_SPACE:
                            self.Player.dir = ''
                            self.Background.dir = ''
                            self.Foreground.dir = ''
                            self.shooting = False
                            self.move = True

                    mainClock.tick(FPS)
                    pygame.time.set_timer(USEREVENT, 150)
                    self.update()

#############################JOYSTICK COMMANDS###########################################################

                ######MELEE ATTACKS######
                    if pygame.joystick.get_init() == True:
                        if event.type == pygame.JOYBUTTONDOWN:
                            if event.button == 2 or event.button == 0:
                                ATKsound = pygame.mixer.Sound('Swoosh.wav')
                                hit = pygame.mixer.Sound('hit.wav')
                                kill = pygame.mixer.Sound('kill.wav')
                                EHit = pygame.mixer.Sound('EHit.wav')
                                EDead = pygame.mixer.Sound('EDead.wav')
                                ATKsound.play()
                                self.Background.dir = ''
                                self.Foreground.dir = ''
                                self.Player.dir = ''
                                self.Player.wdir = ''
                                pygame.key.set_repeat()
                                c = c + 1

                                #ATK 1#
                                if c == 1:
                                    self.Attack = 1

                                #ATK 2#
                                if c == 2:
                                    self.Attack = 2
                                        
                                #ATK 3#        
                                if c == 3:
                                    self.Attack = 3
                                    c = 0

                                self.A1.draw()                            
                                    
                                ##DESTROY OBSTICLES##
                                for b in self.Barriers:
                                    if self.A1.rect.colliderect(b.rect):
                                        self.Score += 100 * Multiplier
                                        if b.obj != 4:
                                            if oHealth > 0:
                                                hit.play()
                                                if b.obj != 1:
                                                    EHit.play()
                                            if b.fire == True:
                                                oHealth = oHealth - 0.34
                                            if b.fire == False:
                                                oHealth = oHealth - 1
                                            if oHealth <= 0:
                                                kill.play()
                                                self.Barriers.remove(b)
                                                oHealth = sHealth
                                                if b.obj != 1:
                                                    EDead.play()
                                            if b.obj == 2:
                                                EHit.play()
                                                if self.Attack == 2:
                                                    b.rect.right += 60

                                        ###BOSS FIGHT###
                                        elif b.obj == 4:
                                            hit.play()
                                            if b.fire == True:
                                                bHealth -= 1
                                            elif b.fire == False:
                                                bHealth -= 2
                                                bHit += 1
                                            if bHit == 5:
                                                b.fire = True
                                                bHit = 0
                                                bwHit = 0
                                            if bHealth <= 0:
                                                STOP = True
                                        
                        #####PAUSE#####
                            if event.button == 7:
                                pygame.key.set_repeat()
                                self.Player.dir = ''
                                pygame.mixer.music.pause()
                                PAUSE = True
                                self.update()

                        if event.type == pygame.JOYBUTTONUP:
                            if event.button == 2:
                                pygame.key.set_repeat(INT,INT)
                            if event.button == 3:
                                self.Player.dir = ''
                                self.Background.dir = ''
                                self.Foreground.dir = ''
                                self.shooting = False
                                move = True
                            
                            
                            ####PAUSE####
                            if event.button == 7:
                                pygame.key.set_repeat()
                                self.Player.dir = ''
                                pygame.mixer.music.pause()
                                PAUSE = False
                                self.update()
                                pygame.mixer.music.unpause()
                #######BLOCKING########
                        if joystick.get_axis(2) > 0.1:
                            self.Player.dir = ''
                            self.Background.dir = ''
                            self.Foreground.dir = ''
                            self.block = True
                            self.move = False
                        if joystick.get_axis(2) == 0:
                            self.Player.dir = ''
                            self.Background.dir = ''
                            self.Foreground.dir = ''
                            self.block = False
                            self.move = True

                #######MOVEMENT########
                        #MOVE RIGHT#
                        if joystick.get_axis(0) > 0.1 or joystick.get_hat(0) == (1,0):
                            moveR = True
                            moveL = False
                            self.shooting = False
                            self.move = True
                            self.A1.dir = 'r'
                            self.Player.dir = 'r'
                            self.Water.dir = 'r'
                            self.A1.wdir = 'r'
                            if moveR != False:
                                self.Background.dir = 'r'
                                self.Foreground.dir = 'r'

                            for b in self.Barriers[:]:
                                if self.PlayerR.rect.collidelistall(self.Barriers[:]):
                                    self.Background.dir = ''
                                    self.Foreground.dir = ''
                                    moveR = False
                                else:
                                    move = True

                            if self.fScroll[-1].rect.centerx - (6 * fs) < WWD/2:
                               self.fScroll[-1].rect.centerx = WWD/2
                                
                            if self.fScroll[-1].rect.centerx == WWD/2 or self.Player.rect.centerx != WWD/2:
                                moveR = False

                            if self.fScroll[0].rect.centerx == WWD/2:
                                self.Player.wdir = 'r'

                            if self.fScroll[-1].rect.centerx == WWD/2:
                                self.Player.wdir = 'r2'
                                
                            if moveR == True:
                                for s1 in self.bScroll[:]:
                                    s1.rect.right -= 6 * bs
                                for s2 in self.fScroll[:]:
                                    s2.rect.right -= 6 * fs
                                for b in self.Barriers[:]:
                                    b.rect.right -= 6 * fs

                        #MOVE LEFT#
                        if joystick.get_axis(0) < -0.1 or joystick.get_hat(0) == (-1,0):
                            moveR = False
                            moveL = True
                            self.shooting = False
                            self.move = True
                            self.A1.dir = 'l'
                            self.Player.dir = 'l'
                            self.Water.dir = 'l'
                            self.A1.wdir = 'l'
                            if moveL != False:
                                self.Background.dir = 'l'
                                self.Foreground.dir = 'l'
                                                        
                            for b in self.Barriers[:]:
                                if self.PlayerL.rect.collidelistall(self.Barriers[:]):
                                    self.Background.dir = ''
                                    self.Foreground.dir = ''
                                    moveL = False
                                else:
                                    moveL = True

                            if self.fScroll[0].rect.centerx == WWD/2 or self.Player.rect.centerx != WWD/2:
                                moveL = False
                                    
                            if self.fScroll[0].rect.centerx == WWD/2:
                                moveL = False
                                self.Player.wdir = 'l'
                                
                            if self.fScroll[-1].rect.centerx == WWD/2:
                                self.Player.wdir = 'l2'
                                
                            if moveL == True:
                                for s1 in self.bScroll[:]:
                                    s1.rect.centerx += 6 * bs
                                for s2 in self.fScroll[:]:
                                    s2.rect.centerx += 6 * fs
                                for b in self.Barriers[:]:
                                    b.rect.centerx += 6 * fs

                        if -0.1 < joystick.get_axis(0) < 0.1 and joystick.get_hat(0) == (0,0):
                            if self.A1.dir == 'r':
                                self.A1.dir = 'r'
                                self.Water.dir = 'r'
                                self.Player.dir = ''
                                self.Player.wdir = ''
                                self.move = False
                                moveR = False
                            if self.A1.dir == 'l':
                                self.A1.dir = 'l'
                                self.Water.dir = 'l'
                                self.Player.dir = ''
                                self.Player.wdir = ''
                                self.move = False
                                moveL = False

                #######SHOOTING########
                if pygame.joystick.get_init() == True:
                    if joystick.get_axis(2) < -0.1:
                        self.shooting = True
                        self.move = False
                        self.Player.dir = ''
                        self.Player.wdir = ''
                        self.Background.dir = ''
                        self.Foreground.dir = ''
                        self.Water.start = self.Player.rect.centerx
                        spraySound = pygame.mixer.Sound('water.wav')
                        #SHOOTING RIGHT#
                        if self.Water.dir == 'r' and self.shooting == True and self.ammo > 0:
                            spraySound.play()
                            self.ammo -= 1
                            wSpeed = 50
                            self.Water.dist = wSpeed
                            for i in range (10):
                                self.Water.dist = wSpeed
                                self.Water.draw()
                                if not self.Water.rect.collidelistall(self.Barriers[:]): #and self.Water.rect.right < WWD:
                                    wSpeed += (WWD/50)
                                else:
                                    self.shooting = False
                                    break

                        #SHOOTING LEFT#
                        if self.Water.dir == 'l' and self.shooting == True and self.ammo > 0:
                            spraySound.play()
                            self.ammo -= 1
                            wSpeed = -50
                            self.Water.dist = wSpeed
                            for i in range (10):
                                self.Water.dist = wSpeed
                                self.Water.draw()
                                if not self.Water.rect.collidelistall(self.Barriers[:]): #and self.Water.rect.right < WWD:
                                    wSpeed -= (WWD/50)
                                else:
                                    self.shooting = False
                                    break

                        #EXTINGUISH OBSTICLES#
                        for b in self.Barriers[:]:
                            if self.Water.rect.colliderect(b.rect) and ((b.rect.left - self.Player.rect.right) < WWD/2):
                                if b.obj != 4:
                                    if b.fire == True:
                                        b.fire = False
                                    if b.obj == 2:
                                        b.rect.right += 20
                                if b.obj == 4:
                                    bwHit += 1
                                    if bwHit == 5:
                                        if b.fire == True:
                                            b.fire = False


                    ##STOP SHOOTING/BLOCKING##
                    if 0.1 > joystick.get_axis(2) > -0.1:
                        self.shooting = False
                        self.block = False
                        self.HolyPower = 50

            #####BLOCKING############
                    if joystick.get_axis(2) > 0.1 and self.HolyPower > 0:
                        self.move = False
                        self.shooting = False
                        self.block = True
                        self.HolyPower -= 15
                        self.Player.dir = ''
                        self.Player.wdir = ''
                        self.Background.dir = ''
                        self.Foreground.dir = ''
                    else:
                        self.block = False
###################################################PAUSED##########################################################################

                if PAUSE == True:
                    pygame.mixer.music.pause()
                    STOP = Pause(Display)
                    pygame.key.set_repeat(INT,INT)
                    pygame.mixer.music.unpause()                    
                    PAUSE = False

pygame.display.set_caption('FIREMAN EXORCIST')
Display = pygame.display.set_mode((WWD,WHT),0,0)
STOP = False
while not STOP:
    for event in pygame.event.get():
        OpeningScreen(Display)
        screen1(Display)
        SpritesGame(Display,1).run()
        screen2(Display)
        SpritesGame(Display,2).run()
        screen3(Display)
        SpritesGame(Display,3).run()
        screen4(Display)
        Display = pygame.display.set_mode((WWD,WHT),0,0)
        pygame.mixer.music.stop()
        pygame.display.update()

pygame.quit()
