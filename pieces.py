from block import Block
from settings import *
import pygame as pg
import random

def create_blocks(coord,len,x,y,col):
    lob = list()
    for i in range(len):
        lob.append(Block(x+coord[i][0]*TILE_SIZE, y-coord[i][1]*TILE_SIZE))
        lob[i].surf.fill(col)
    return lob

def adjust_blocks(piece,coord,len,x,y):
    for i in range(len):
        piece[i].rect.center = (x+coord[i][0]*TILE_SIZE, y-coord[i][1]*TILE_SIZE)

def get_landscape(group):
    ls = [HEIGHT] * GRID_WIDTH
    for block in group:
        for i in range(block.len):
            col = block.piece[i].rect.left//TILE_SIZE
            ls[col] = min(ls[col],block.piece[i].rect.top)
    return ls

def colliding(b,group):
    # print('bottom')
    # print(b.rect.bottom)
    # print('left')
    # print(b.rect.left)
    # print('right')
    # print(b.rect.right)
    if b.rect.bottom > HEIGHT:
        return True
    if b.rect.left < 0:
        # print('left out')
        return True
    if b.rect.right > WIDTH:
        # print('right out')
        return True
    for block in group:
        for i in range(block.len):
            if pg.sprite.collide_rect(b,block.piece[i]):
                return True
    return False

class IBlock:
    def __init__(self,count):
        self.x = (random.randint(0,GRID_WIDTH-4)+0.5)*TILE_SIZE # centre x
        self.y = 0 # centre y
        self.len = 4
        self.pos = 0
        self.coord = (((0,2),(1,2),(2,2),(3,2)),\
                        ((2,3),(2,2),(2,1),(2,0)),\
                            ((0,1),(1,1),(2,1),(3,1)),\
                                ((1,3),(1,2),(1,1),(1,0)))
        self.piece = create_blocks(self.coord[self.pos],self.len,self.x,self.y,CYAN)
        self.speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
    def update(self,group):
        for i in range(self.len):
            self.piece[i].rect.move_ip(0,self.speed)
            # if colliding(self.piece[i],group):
            #     print('collides')
        if self.piece[3].rect.bottom > HEIGHT:
            diff = self.piece[3].rect.bottom - HEIGHT 
            for i in range(self.len):
                self.piece[i].rect.move_ip(0,-diff)
            return True
        landscape = get_landscape(group)
        for i in range(self.len):
            for j in range(GRID_WIDTH):
                if self.piece[i].rect.left == j * TILE_SIZE and \
                    self.piece[i].rect.bottom > landscape[j]:
                    diff = self.piece[i].rect.bottom - landscape[j]
                    for k in range(self.len):
                        self.piece[k].rect.move_ip(0,-diff)
                    return True
        return False
    def move_left(self,group):
        moved = list()
        for i in range(self.len):
            moved.append(self.piece[i].move_left(group))
        if not all(moved):
            for i in range(self.len):
                if moved[i]:
                    self.piece[i].rect.move_ip(TILE_SIZE,0)
    def move_right(self,group):
        moved = list()
        for i in range(self.len):
            moved.append(self.piece[i].move_right(group))
        if not all(moved):
            for i in range(self.len):
                if moved[i]:
                    self.piece[i].rect.move_ip(-TILE_SIZE,0)
    def update_coord(self,group):
        if self.pos == 0:
            x = self.piece[0].rect.centerx
            y = self.piece[0].rect.centery + 2*TILE_SIZE
            if not colliding(Block(x+2*TILE_SIZE,y),group):
                self.x = x
                self.y = y
                return True
        elif self.pos == 1:
            x = self.piece[3].rect.centerx - 2*TILE_SIZE
            y = self.piece[3].rect.centery
            if not colliding(Block(x,y-TILE_SIZE),group) and \
                not colliding(Block(x+3*TILE_SIZE,y-TILE_SIZE),group):
                self.x = x
                self.y = y
                return True
        elif self.pos == 2:
            x = self.piece[0].rect.centerx
            y = self.piece[0].rect.centery + TILE_SIZE
            if not colliding(Block(x+TILE_SIZE,y),group):
                self.x = x
                self.y = y
                return True
        elif self.pos == 3:
            x = self.piece[3].rect.centerx - TILE_SIZE
            y = self.piece[3].rect.centery
            if not colliding(Block(x,y-2*TILE_SIZE),group) and \
                not colliding(Block(x+3*TILE_SIZE,y-2*TILE_SIZE),group):
                self.x = x
                self.y = y
                return True
        return False
    def adjust_blocks(self,coord):
        for i in range(self.len):
            self.piece[i].rect.center = (self.x+coord[i][0]*TILE_SIZE, self.y-coord[i][1]*TILE_SIZE)    
    def rotate(self,group,clockwise):
        can_rotate = self.update_coord(group)
        if can_rotate:
            if clockwise:
                self.pos = (self.pos + 1) % self.len
            else:
                self.pos = (self.pos - 1) % self.len
            adjust_blocks(self.piece,self.coord[self.pos],self.len,self.x,self.y)