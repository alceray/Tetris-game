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
        super().__init__(x,0,4,0,coord,CYAN,count)
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
        super().__init__(x,0,4,0,coord,YELLOW,count)
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

class RBlock(BlockTypes):
    def __init__(self,count):
        x = (random.randint(0,GRID_WIDTH-3)+0.5)*TILE_SIZE
        coord = (((0,2),(0,1),(1,1),(2,1)),\
                        ((1,0),(1,1),(1,2),(2,2)),\
                            ((0,1),(1,1),(2,1),(2,0)),\
                                ((0,0),(1,0),(1,1),(1,2)))
        super().__init__(x,0,4,0,coord,BLUE,count)
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

class LBlock(BlockTypes):
    def __init__(self,count):
        x = (random.randint(0,GRID_WIDTH-3)+0.5)*TILE_SIZE
        coord = (((0,1),(1,1),(2,1),(2,2)),\
                        ((1,0),(1,1),(1,2),(2,0)),\
                            ((0,0),(0,1),(1,1),(2,1)),\
                                ((1,0),(1,1),(1,2),(0,2)))
        super().__init__(x,0,4,0,coord,ORANGE,count)
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
        super().__init__(x,0,4,0,coord,GREEN,count)
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
        super().__init__(x,0,4,0,coord,PURPLE,count)
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
        super().__init__(x,0,4,0,coord,RED,count)
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