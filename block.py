import pygame as pg
from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.surf = pg.Surface((TILE_SIZE,TILE_SIZE))
        self.rect = self.surf.get_rect(center=(x,y))

class BlockTypes:
    def __init__(self,x,y,len,pos,coord,col,count):
        self.x = x
        self.y = y
        self.len = len
        self.pos = pos
        self.coord = coord
        self.col = col
        self.piece = self.create_blocks()
        self.speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
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
            if pg.sprite.collide_rect(b,block):
                return True
        return False
    def get_landscape(self,group):
        ls = [HEIGHT] * GRID_WIDTH
        for block in group:
            col = block.rect.left//TILE_SIZE
            ls[col] = min(ls[col],block.rect.top)
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
    def rotate(self,group,clockwise):
        for i in range(self.len):
            if self.pos == i:
                x = self.piece[i].rect.centerx-self.coord[i][i][0]*TILE_SIZE
                y = self.piece[i].rect.centery+self.coord[i][i][1]*TILE_SIZE
                if clockwise:
                    new_pos = (i+1)%self.len
                else:
                    new_pos = (i-1)%self.len
                new_coord = list(set(self.coord[new_pos]).difference(self.coord[i]))
                for new_x,new_y in new_coord:
                    print(new_y)
                    if self.colliding(Block(x+new_x*TILE_SIZE,y-new_y*TILE_SIZE),group):
                        print('collides')
                        return
                self.x = x
                self.y = y
                self.pos = new_pos
                self.adjust_blocks()
                return
