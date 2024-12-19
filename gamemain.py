import pygame as pg
import sys,time
pg.init()

class Game:
    def __init__(self):

        #setting window config

        self.width =600
        self.height=768
        self.scale_factor=1.5
        self.win=pg.display.set_mode((self.width,self.height))
        self.clock=pg.time.Clock()
        self.setupbgandground()
        self.move_speed=250
    
        
        self.gameloop()


    def gameloop(self,): 
        last_time=time.time()
        while True:
            #delta time calculation
            new_time=time.time()
            dt=new_time-last_time
            last_time=new_time
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.updateevery(dt)            
            self.drawing()
            pg.display.update()  
            self.clock.tick(60)

    def updateevery(self,dt):
        self.ground1_rect.x-=self.move_speed*dt
        self.ground2_rect.x-=self.move_speed*dt


        if self.ground1_rect.right<0:
            self.ground1_rect.x=self.ground2_rect.right
        if self.ground2_rect.right<0:
            self.ground1_rect.x=self.ground1_rect.right

    def drawing(self):
            self.win.blit(self.bg_img,(0,-320)) 
            self.win.blit(self.ground1_img,self.ground1_rect)
            self.win.blit(self.ground2_img,self.ground2_rect)

    def setupbgandground(self):
        
        self.bg_img=pg.transform.scale_by(pg.image.load("assets/bg.png").convert(),self.scale_factor)
        self.ground1_img=pg.transform.scale_by(pg.image.load("assets/ground.png").convert(),self.scale_factor)
        self.ground2_img=pg.transform.scale_by(pg.image.load("assets/ground.png").convert(),self.scale_factor)

        self.ground1_rect=self.ground1_img.get_rect()
        self.ground2_rect=self.ground2_img.get_rect()

        self.ground1_rect.x=0
        self.ground2_rect.x=self.ground1_rect.right
        self.ground1_rect.y=568
        self.ground2_rect.y=568


game=Game()                    
