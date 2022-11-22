#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:28:47 2022

@author: andreakjellvang
"""

import turtle

class Tamagotchi: 
    def __init__(self, canvas, cat):
        self.canvas = canvas
        self.cat = cat
        
        self.cat.shape("cat.gif")
        self.cat.penup()
        
    
    def step(self):
        self.cat.run_ai(self.cat.pos(), self.cat.heading())
        
        
    def start(self, init_dist=400, ai_timer_msec=100):
        self.cat.setpos((-init_dist / 2, 0))
        self.cat.setheading(0)

        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, self.ai_timer_msec) 
        

class PetMovement(turtle.RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)

    def run_ai(self):
        self.forward(300)
    
    
if __name__ == '__main__':
    canvas = turtle.Screen()
    canvas.title("Andy's Tamagotchi")
    canvas.bgcolor("#8e8e8e")
    canvas.addshape("cat.gif")
    cat = PetMovement(canvas)
    
    game = Tamagotchi(canvas, cat)
    game.start()
    canvas.mainloop()
    
    
    