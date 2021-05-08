from block import *
from settings import *
import pygame as pg
import random

class Piece(BlockTypes):
    def __init__(self,count,block_type):
        len = GAME_PIECES[block_type]["Width"]
        x = (random.randint(0,GRID_WIDTH-len)+0.5)*TILE_SIZE
        coord = GAME_PIECES[block_type]["Coord"]
        col = GAME_PIECES[block_type]["Col"]
        super().__init__(x,0,4,0,coord,col,count)        
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
