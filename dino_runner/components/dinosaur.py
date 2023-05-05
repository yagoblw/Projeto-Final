import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DUCKING, HAMMER_TYPE, RUNNING, JUMPING, DEFAULT_TYPE, SHIELD_TYPE,  JUMPING_SHIELD, RUNNING_SHIELD, RUNNING_HAMMER, JUMPING_HAMMER, RELOGIO_TYPE, PENA_TYPE
from dino_runner.utils.constants import FLY_RUNING, VOANDO,  SCREEN_HEIGHT, SOUNDS, HEART_TYPE, FLY_JUMP, RELOGIO_TYPE, RELOGIO


DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING, HAMMER_TYPE: DUCKING, RELOGIO_TYPE: DUCKING, PENA_TYPE: DUCKING, HEART_TYPE: DUCKING, RELOGIO_TYPE: DUCKING }
JUMP_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER,RELOGIO_TYPE: JUMPING, PENA_TYPE: FLY_JUMP, HEART_TYPE: JUMPING, RELOGIO_TYPE: JUMPING}
RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER,RELOGIO_TYPE: RUNNING, PENA_TYPE: FLY_RUNING, HEART_TYPE: RUNNING, RELOGIO_TYPE: RUNNING }
VOANDO_IMG = {PENA_TYPE:VOANDO }
X_POS = 80
Y_POS = 388
JUMP_VEL = 8.5


class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.step_indexMax = 9
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = JUMP_VEL
        self.pressed = False
        self.power_up_time = 0
        self.duraveis = {HEART_TYPE: list(), PENA_TYPE: list()}
        self.setup_state()
    
    def setup_state(self):
        self.has_power_up = False
        self.fly = False
        self.shield = False
        self.hammer = False

        self.show_text = False

    def update(self, user_input):
      
        if self.type == PENA_TYPE:
           if user_input[pygame.K_w]:
               self.fly = True
               self.dino_duck = False
               self.dino_run = False
               self.dino_jump = False
           if user_input[pygame.K_q]:
               self.fly = False
               self.dino_duck = False
               self.dino_run = False
               self.dino_jump = True

        if user_input[pygame.K_SPACE]  and not self.fly and  self.dino_rect.y == Y_POS:  
                self.dino_jump = True
                self.dino_run = False
                self.dino_duck = False

        elif user_input[pygame.K_s] and not self.dino_jump  and not self.fly:
    
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
            

        elif not self.dino_jump  and not self.dino_duck and not self.fly:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False
            #self.fly = False

        

        if self.dino_run:
                self.run()
               
        elif self.dino_jump:
                self.jump()
        elif self.dino_duck:
                self.duck()
        elif self.fly:
             self.flying(user_input)         

    def run(self):

        
        if self.step_index >= self.step_indexMax:
             self.step_index = 0

        if self.type == PENA_TYPE: 
            self.step_indexMax = 25
        else:
            self.step_indexMax = 9


        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        
        
        self.dino_rect.y = Y_POS      
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
          
    def jump(self):
        self.step_indexMax = 9

        if self.step_index >= self.step_indexMax:
           self.step_index = 0

        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4   
         

        if self.dino_rect.y == Y_POS - JUMP_VEL*4:
            SOUNDS["Jump"].set_volume(0.5)
            SOUNDS["Jump"].play() 
       
        self.jump_vel -= 0.8
       
        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

          

    def duck(self):
        self.step_indexMax = 9
        if self.step_index >= self.step_indexMax:
             self.step_index = 0
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 25
        self.step_index += 1
        self.dino_duck = False
        
    def flying (self, user_input): 
            self.step_indexMax = 9
            
            if self.step_index >= self.step_indexMax:
                self.step_index = 0
              
            self.image = VOANDO_IMG[self.type][self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = (SCREEN_HEIGHT //2) - 160
            self.step_index += 1
            if user_input[pygame.K_s] and self.fly:
                    self.dino_rect.y += 90
                
            elif user_input[pygame.K_SPACE] and self.fly:
                    self.dino_rect.y -= 90


    
                 
                
                     
               

     
         
        

        