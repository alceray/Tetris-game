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
        pos = random.randint(0,3)
        super().__init__(x,0,4,pos,coord,CYAN,speed)
    def update(self,group):
        return super().update(group)
    def move_left(self,group):
        super().move_left(group)
    def move_right(self,group):
        super().move_right(group)
    def drop(self,group):
        super().drop(group)
    def rotate(self,group,clockwise):
        super().rotate(group, clockwise)

class Square(BlockTypes):
    def __init__(self,count):
        x = (random.randint(0,GRID_WIDTH-2)+0.5)*TILE_SIZE
        coord = (((0,0),(1,0),(0,1),(1,1)),)
        speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
        super().__init__(x,0,4,0,coord,YELLOW,speed)
    def update(self,group):
        return super().update(group)
    def move_left(self,group):
        super().move_left(group)
    def move_right(self,group):
        super().move_right(group)
    def drop(self,group):
        super().drop(group)
    def rotate(self, group, clockwise):
        return

class LBlock(BlockTypes):
    def __init__(self,count):
        x = (random.randint(0,GRID_WIDTH-3)+0.5)*TILE_SIZE
        coord = (((0,2),(0,1),(1,1),(2,1)),\
                        ((1,0),(1,1),(1,2),(2,2)),\
                            ((0,1),(1,1),(2,1),(2,0)),\
                                ((0,0),(1,0),(1,1),(1,2)))
        speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
        pos = random.randint(0,3)
        super().__init__(x,0,4,pos,coord,ORANGE,speed)
    def update(self,group):
        return super().update(group)
    def move_left(self,group):
        super().move_left(group)
    def move_right(self,group):
        super().move_right(group)
    def drop(self,group):
        super().drop(group)
    def rotate(self,group,clockwise):
        super().rotate(group, clockwise)

class RBlock(BlockTypes):
    def __init__(self,count):
        x = (random.randint(0,GRID_WIDTH-3)+0.5)*TILE_SIZE
        coord = (((0,0),(0,1),(1,1),(2,1)),\
                        ((1,0),(1,1),(1,2),(0,2)),\
                            ((0,1),(1,1),(2,1),(2,2)),\
                                ((1,0),(1,1),(1,2),(2,0)))
        speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
        pos = random.randint(0,3)
        super().__init__(x,0,4,pos,coord,BLUE,speed)
    def update(self,group):
        return super().update(group)
    def move_left(self,group):
        super().move_left(group)
    def move_right(self,group):
        super().move_right(group)
    def drop(self,group):
        super().drop(group)
    def rotate(self,group,clockwise):
        super().rotate(group, clockwise)

class SBlock(BlockTypes):
    def __init__(self,count):
        x = (random.randint(0,GRID_WIDTH-3)+0.5)*TILE_SIZE
        coord = (((0,1),(1,1),(1,2),(2,2)),\
                        ((1,1),(1,2),(2,0),(2,1)),\
                            ((0,0),(1,0),(1,1),(2,1)),\
                                ((0,2),(0,1),(1,1),(1,0)))
        speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
        pos = random.randint(0,3)
        super().__init__(x,0,4,pos,coord,GREEN,speed)
    def update(self,group):
        return super().update(group)
    def move_left(self,group):
        super().move_left(group)
    def move_right(self,group):
        super().move_right(group)
    def drop(self,group):
        super().drop(group)
    def rotate(self,group,clockwise):
        super().rotate(group, clockwise)

class TBlock(BlockTypes):
    def __init__(self,count):
        x = (random.randint(0,GRID_WIDTH-3)+0.5)*TILE_SIZE
        coord = (((0,0),(1,0),(2,0),(1,1)),\
                        ((0,0),(0,1),(0,2),(1,1)),\
                            ((0,2),(1,2),(2,2),(1,1)),\
                                ((2,0),(2,1),(2,2),(1,1)))
        speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
        self.pos = random.randint(0,3)
        super().__init__(x,0,4,0,coord,PURPLE,speed)
    def update(self,group):
        return super().update(group)
    def move_left(self,group):
        super().move_left(group)
    def move_right(self,group):
        super().move_right(group)
    def drop(self,group):
        super().drop(group)
    def rotate(self,group,clockwise):
        super().rotate(group, clockwise)

class ZBlock(BlockTypes):
    def __init__(self,count):
        x = (random.randint(0,GRID_WIDTH-3)+0.5)*TILE_SIZE
        coord = (((0,2),(1,1),(1,2),(2,1)),\
                        ((1,1),(1,0),(2,2),(2,1)),\
                            ((0,1),(1,0),(1,1),(2,0)),\
                                ((0,0),(0,1),(1,1),(1,2)))
        speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
        pos = random.randint(0,3)
        super().__init__(x,0,4,pos,coord,RED,speed)
    def update(self,group):
        return super().update(group)
    def move_left(self,group):
        super().move_left(group)
    def move_right(self,group):
        super().move_right(group)
    def drop(self,group):
        super().drop(group)
    def rotate(self,group,clockwise):
        super().rotate(group, clockwise)