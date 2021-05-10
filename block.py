import pygame as pg
from settings import *
import random

class Block(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.surf = pg.Surface((TILE_SIZE,TILE_SIZE))
        self.rect = self.surf.get_rect(center=(x,y))

class BlockTypes:
    def __init__(self,count,block_type):
        length = GAME_PIECES[block_type]["Length"]
        self.x = (random.randint(INFO_WIDTH,GRID_WIDTH-length)+0.5)*TILE_SIZE
        self.y = 0
        self.size = GAME_PIECES[block_type]["Size"]
        self.pos = 0
        self.coord = GAME_PIECES[block_type]["Coord"]
        self.col = GAME_PIECES[block_type]["Col"]
        self.piece = self.create_blocks()
        self.speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
    def create_blocks(self):
        blocks = list()
        for i in range(self.size):
            blocks.append(Block(self.x+self.coord[self.pos][i][0]*TILE_SIZE, \
                self.y-self.coord[self.pos][i][1]*TILE_SIZE))
            blocks[i].surf.fill(self.col)
        return blocks
    def adjust_blocks(self):
        for i in range(self.size):
            self.piece[i].rect.center = (self.x+self.coord[self.pos][i][0]*TILE_SIZE, \
                self.y-self.coord[self.pos][i][1]*TILE_SIZE)
    def colliding(self,b,group):
        if b.rect.left < SIDE_WIDTH:
            return True
        if b.rect.right > WIDTH:
            return True
        for block in group:
            if pg.sprite.collide_rect(b,block):
                return True
        return False
    def update(self,group,speed):
        self.move_down(speed)
        for block in self.piece:
            if block.rect.bottom > HEIGHT:
                diff = block.rect.bottom - HEIGHT 
                for b in self.piece:
                    b.rect.move_ip(0,-diff)
                return True
        for block in self.piece:
            for sprite in group:
                if pg.sprite.collide_rect(block,sprite):
                    diff = block.rect.bottom - sprite.rect.top
                    for b in self.piece:
                        b.rect.move_ip(0,-diff)
                    return True
        return False
    def move_down(self,speed):
        for block in self.piece:
            block.rect.move_ip(0,speed)
    def move_left(self,group):
        moved = list()
        for block in self.piece:
            block.rect.move_ip(-TILE_SIZE,0)
            moved.append(not self.colliding(block,group))
        if not all(moved):
            for block in self.piece:
                block.rect.move_ip(TILE_SIZE,0)
    def move_right(self,group):
        moved = list()
        for block in self.piece:
            block.rect.move_ip(TILE_SIZE,0)
            moved.append(not self.colliding(block,group))
        if not all(moved):
            for block in self.piece:
                block.rect.move_ip(-TILE_SIZE,0)
    def drop(self,group):
        min_dist = HEIGHT
        for block in self.piece:
            min_dist = min(HEIGHT - block.rect.bottom, min_dist)
            for sprite in group:
                if block.rect.x == sprite.rect.x and \
                    block.rect.bottom < sprite.rect.top:
                    new_dist = sprite.rect.top - block.rect.bottom
                    min_dist = min(min_dist,new_dist)
        for block in self.piece:
            block.rect.bottom += min_dist
    def rotate(self,group,clockwise):
        for i in range(self.size):
            if self.pos == i:
                x = self.piece[i].rect.centerx-self.coord[i][i][0]*TILE_SIZE
                y = self.piece[i].rect.centery+self.coord[i][i][1]*TILE_SIZE
                if clockwise:
                    new_pos = (i+1)%self.size
                else:
                    new_pos = (i-1)%self.size
                new_coord = list(set(self.coord[new_pos]).difference(self.coord[i]))
                for new_x,new_y in new_coord:
                    if self.colliding(Block(x+new_x*TILE_SIZE,y-new_y*TILE_SIZE),group):
                        return
                self.x = x
                self.y = y
                self.pos = new_pos
                self.adjust_blocks()
                return
    def soft_drop(self,group,speed):
        self.update(group,speed)
            
