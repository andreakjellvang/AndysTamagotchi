#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:36:19 2022

@author: andreakjellvang
"""

import pygame
from pygame import mixer
from pygame.locals import QUIT, USEREVENT
from sys import exit
import random

pygame.init()
mixer.init()

# Colors
white = 255, 255, 255
black = 44, 44, 44

# Load background music
mixer.music.load("theme_song.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()

# Creating the game display and implementing time as well as system font
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Andy's Tamagotchi")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Kitchen Sink", 15)

# Background image and center placement using get_rect()
background_image = pygame.image.load("tamagotchi.png").convert()
image_rect = background_image.get_rect(center = screen.get_rect().center)

# Cat image and center placement using get_rect()
cat = pygame.image.load("cat.png")
cat_rect = cat.get_rect(center = screen.get_rect().center)

# Button icons
food = pygame.image.load("food.png").convert_alpha()
heart = pygame.image.load("heart.png").convert_alpha()
toilet = pygame.image.load("toilet.png").convert_alpha()
treatment = pygame.image.load("treatment.png").convert_alpha()
fun = pygame.image.load("fun.png").convert_alpha()

class Button():
    # Code borrowed from https://www.youtube.com/watch?v=G8MYGDf_9ho
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False
            
        def draw(self):
            action = False
            
            screen.blit(self.image, (self.rect.x, self.rect.y))
            
            position = pygame.mouse.get_pos()
            
            if self.rect.collidepoint(position):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked == True
                    action = True   
                    
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked == False
                
            return action
        
        
# Create the buttons            
food_btn = Button(265, 235, food)   
heart_btn = Button(335, 223, heart)    
toilet_btn = Button(442, 235, toilet)    
treatment_btn = Button(520, 226, treatment) 
fun_btn = Button(630, 225, fun)
            
# Setting game icon as cat
pygame.display.set_icon(cat)

# Loading images used as pop-ups
feeding = pygame.image.load("feeding.png").convert_alpha()
peeing = pygame.image.load("peeing.png").convert_alpha()
petting = pygame.image.load("petting.png").convert_alpha()
treating = pygame.image.load("treating.png").convert_alpha()
playing = pygame.image.load("playing.png").convert_alpha()

class Happiness(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.current_happiness = 100
        self.max_happiness = 1000
        self.happiness_bar_length = 480
        self.happiness_bar_ratio = self.max_happiness / self.happiness_bar_length
        self.happiness_level = ""
        
    def update(self):
        self.happinessBar()
        self.writeText()
        
    def getSad(self, amount):
        if self.current_happiness > 0:
            self.current_happiness -= amount
        if self.current_happiness <= 0:
            self.current_happiness = 0
            pygame.quit()
        
    def getHappiness(self, amount):
        if self.current_happiness < self.max_happiness:
            self.current_happiness += amount
        if self.current_happiness >= self.max_happiness:
            self.current_happiness = self.max_happiness
    
    def happinessBar(self):
        pygame.draw.rect(screen, black , (260, 630, self.current_happiness/self.happiness_bar_ratio, 20))
        pygame.draw.rect(screen, white, (260, 630, self.happiness_bar_length, 20), 2)
        
            
    def writeText(self):  
        self.text = font.render("Happiness level: " , True, black)
        screen.blit(self.text, (260, 610))
        
            
happiness_bar = pygame.sprite.GroupSingle(Happiness())  
             

#  Main game loop
def main_loop():
         
    # Enable movement for cat
    direction = 1
    speed_x = 3

    # Create event to make happiness level go down by itself
    get_sad = USEREVENT + 0
    pygame.time.set_timer(get_sad, 2000)
    
    game_execution = True
    while game_execution:
        
        # Exiting game when closing window
        for event in pygame.event.get():
            if event.type == QUIT:
                game_execution == False
                pygame.quit()
                print("Exiting...")
                exit()
            # Initiate event to make happiness level go down by itself
            if event.type == get_sad:
                happiness_bar.sprite.getSad(70)
                    
                
        # Make pet move 
        if cat_rect.left >= 0 or cat_rect.right >= 0:
            direction *= -1
            speed_x = random.randint(0, 1) * direction
            if speed_x == 0:
                speed_x = random.randint(0, 1) * direction
                    
            cat_rect.right += speed_x
            cat_rect.left += speed_x
    
        
        
        # White background and placement of background image
        screen.fill(white)
        screen.blit(background_image, image_rect)
        
        # Place pet on display screen
        screen.blit(cat, cat_rect)
        
        # Add happiness bar text
        Happiness().writeText()
        
        # Give functionality to buttons
        if food_btn.draw():
            screen.blit(feeding, [375, 320])
            happiness_bar.sprite.getHappiness(30)
            print("Feeding...")
        if heart_btn.draw():
            screen.blit(petting, [375, 320])
            happiness_bar.sprite.getHappiness(30)
            print("Petting...")
        if toilet_btn.draw():
            screen.blit(peeing, [375, 320])
            happiness_bar.sprite.getHappiness(30)
            print("Peeing...")
        if treatment_btn.draw():
            screen.blit(treating, [375, 320])
            happiness_bar.sprite.getHappiness(30)
            print("Treating...")
        if fun_btn.draw():
            screen.blit(playing, [375, 320])
            happiness_bar.sprite.getHappiness(30)
            print("Dancing...")
            
        
        happiness_bar.update()
        pygame.display.update()
        clock.tick(60)
        
              
main_loop()
            
            
        



