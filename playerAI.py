import pygame
import random
import time
from player import *

class PlayerAI:
    def __init__(self, map, dna):
        self.player = Player(map)
        if dna is None:
            self.dna=[]
            self.create_dna_sequence()
        else:
            self.dna = dna
        self.currentAllele = 0
        self.delay = 100_000_000
        self.next_act = time.time_ns() + self.delay
        self.x = self.player.x
        self.y = self.player.y
        self.coins=self.player.coins

    def create_dna_sequence(self):
        # 0 - junk DNA - 80%
        # 1 - jump - 6%
        # 2 - move left - 7%
        # 3 - move right - 7%

        for i in range(200):
            choice = random.randint(1,100)
            if(choice <= 50): #junk
                self.dna.append(0)
            elif(choice <= 86): #jump
                self.dna.append(1)
            elif(choice <= 93): #move left
                self.dna.append(2)
            elif(choice <= 100): #move right
                self.dna.append(3)

    def create_dna_sequence(self):
        # 0 - junk DNA - 80%
        # 1 - jump - 6%
        # 2 - move left - 7%
        # 3 - move right - 7%

        for i in range(200):
            choice = random.randint(1,100)
            if(choice <= 50): #junk
                self.dna.append(0)
            elif(choice <= 86): #jump
                self.dna.append(1)
            elif(choice <= 93): #move left
                self.dna.append(2)
            elif(choice <= 100): #move right
                self.dna.append(3)

    def act(self):
        #print(str(time.time_ns()))
        if self.currentAllele<200:
            if self.next_act < time.time_ns():
                if self.dna[self.currentAllele] == 1:
                    self.player.jump()
                elif self.dna[self.currentAllele] == 2:
                    self.player.mvl()
                elif self.dna[self.currentAllele] == 3:
                    self.player.mvr()
                self.next_act = time.time_ns() + self.delay
                self.currentAllele += 1
                self.x = self.player.x
                self.y = self.player.y
        return self.player.act()

    def draw(self, screen):
        self.player.draw(screen)
    def reset(self):
        self.player.x = 400
        self.player.y = 400
        self.player.velocity=0
        self.player.x_velocity=0
        self.x = self.player.x
        self.y = self.player.y
        self.currentAllele=0
        self.coins=[]

    def set_map(self, map):
        self.player.set_map(map)
    def randomChange(self):
        for i in range(200):
            choice = random.randint(1, 120)
            if choice==1:
                self.dna[i]=0
            if choice==2:
                self.dna[i]=1
            if choice==3:
                self.dna[i]=2
            if choice==4:
                self.dna[i]=3
            if choice==5:
                del self.dna[i]
                choice2 = random.randint(1, 4)
                if choice2 == 1:
                    self.dna.append(0)
                if choice2 == 2:
                    self.dna.append(1)
                if choice2 == 3:
                    self.dna.append(2)
                if choice2 == 4:
                    self.dna.append(3)
            if choice == 6:
                del self.dna[199]
                choice2 = random.randint(1, 4)
                if choice2 == 1:
                    self.dna.insert(i,0)
                if choice2 == 2:
                    self.dna.insert(i,1)
                if choice2 == 3:
                    self.dna.insert(i,2)
                if choice2 == 4:
                    self.dna.insert(i,3)
    def handle_key_presses(self):
        return None