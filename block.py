import pygame as pg
from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.surf = pg.Surface((TILE_SIZE,TILE_SIZE))
        self.rect = self.surf.get_rect(center=(x,y))

class BlockTypes:
    def __init__(self,x,y,len,pos,coord,col,speed):
        self.x = x
        self.y = y
        self.len = len
        self.pos = pos
        self.coord = coord
        self.col = col
        self.piece = self.create_blocks()
        self.speed = speed
    def create_blocks(self):
        blocks = list()
        for i in range(self.len):
            blocks.append(Block(self.x+self.coord[self.pos][i][0]*TILE_SIZE, \
                self.y-self.coord[self.pos][i][1]*TILE_SIZE))
            blocks[i].surf.fill(self.col)
        return blocks
    def adjust_blocks(self):
        for i in range(self.len):
            self.piece[i].rect.center = (self.x+self.coord[self.pos][i][0]*TILE_SIZE, \
                self.y-self.coord[self.pos][i][1]*TILE_SIZE)
    def colliding(self,b,group):
        if b.rect.bottom > HEIGHT:
            return True
        if b.rect.left < 0:
            return True
        if b.rect.right > WIDTH:
            return True
        for block in group:
            for i in range(block.len):
                if pg.sprite.collide_rect(b,block.piece[i]):
                    return True
        return False
    def get_landscape(self,group):
        ls = [HEIGHT] * GRID_WIDTH
        for block in group:
            for i in range(block.len):
                col = block.piece[i].rect.left//TILE_SIZE
                ls[col] = min(ls[col],block.piece[i].rect.top)
        return ls
    def update(self,group):
        for i in range(self.len):
            self.piece[i].rect.move_ip(0,self.speed)
        for i in range(self.len):
            if self.piece[i].rect.bottom > HEIGHT:
                diff = self.piece[i].rect.bottom - HEIGHT 
                for j in range(self.len):
                    self.piece[j].rect.move_ip(0,-diff)
                return True
        landscape = self.get_landscape(group)
        for i in range(self.len):
            for j in range(GRID_WIDTH):
                if self.piece[i].rect.x == j * TILE_SIZE and \
                    self.piece[i].rect.bottom > landscape[j]:
                    diff = self.piece[i].rect.bottom - landscape[j]
                    for k in range(self.len):
                        self.piece[k].rect.move_ip(0,-diff)
                    return True
        return False
    def move_left(self,group):
        moved = list()
        for i in range(self.len):
            self.piece[i].rect.move_ip(-TILE_SIZE,0)
            moved.append(not self.colliding(self.piece[i],group))
        if not all(moved):
            for i in range(self.len):
                self.piece[i].rect.move_ip(TILE_SIZE,0)
    def move_right(self,group):
        moved = list()
        for i in range(self.len):
            self.piece[i].rect.move_ip(TILE_SIZE,0)
            moved.append(not self.colliding(self.piece[i],group))
        if not all(moved):
            for i in range(self.len):
                self.piece[i].rect.move_ip(-TILE_SIZE,0)
    def drop(self,group):
        landscape = self.get_landscape(group)
        min_dist = HEIGHT
        for i in range(self.len):
            for j in range(GRID_WIDTH):
                if self.piece[i].rect.x == j * TILE_SIZE:
                    min_dist = min(min_dist,landscape[j]-self.piece[i].rect.bottom)
        for i in range(self.len):
            self.piece[i].rect.bottom += min_dist