from block import *
from settings import *
import pygame as pg
import random

class IBlock(BlockTypes):
    def __init__(self,count):
        x = (random.randint(0,GRID_WIDTH-4)+0.5)*TILE_SIZE
        coord = (((0,2),(1,2),(2,2),(3,2)),\
                        ((2,3),(2,2),(2,1),(2,0)),\
                            ((0,1),(1,1),(2,1),(3,1)),\
                                ((1,3),(1,2),(1,1),(1,0)))
        speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
        super().__init__(x,0,4,0,coord,CYAN,speed)
    def update(self,group):
        return super().update(group)
    def move_left(self,group):
        super().move_left(group)
    def move_right(self,group):
        super().move_right(group)
    def drop(self,group):
        super().drop(group)
    def update_coord(self,group):
        if self.pos == 0:
            x = self.piece[0].rect.centerx
            y = self.piece[0].rect.centery + 2*TILE_SIZE
            if not super().colliding(Block(x+2*TILE_SIZE,y),group):
                self.x = x
                self.y = y
                return True
        elif self.pos == 1:
            x = self.piece[3].rect.centerx - 2*TILE_SIZE
            y = self.piece[3].rect.centery
            if not super().colliding(Block(x,y-TILE_SIZE),group) and \
                not super().colliding(Block(x+3*TILE_SIZE,y-TILE_SIZE),group):
                self.x = x
                self.y = y
                return True
        elif self.pos == 2:
            x = self.piece[0].rect.centerx
            y = self.piece[0].rect.centery + TILE_SIZE
            if not super().colliding(Block(x+TILE_SIZE,y),group):
                self.x = x
                self.y = y
                return True
        elif self.pos == 3:
            x = self.piece[3].rect.centerx - TILE_SIZE
            y = self.piece[3].rect.centery
            if not super().colliding(Block(x,y-2*TILE_SIZE),group) and \
                not super().colliding(Block(x+3*TILE_SIZE,y-2*TILE_SIZE),group):
                self.x = x
                self.y = y
                return True
        return False
    def rotate(self,group,clockwise):
        can_rotate = self.update_coord(group)
        if can_rotate:
            if clockwise:
                self.pos = (self.pos + 1) % self.len
            else:
                self.pos = (self.pos - 1) % self.len
            super().adjust_blocks()