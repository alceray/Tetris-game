import pygame as pg
from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.surf = pg.Surface((TILE_SIZE,TILE_SIZE))
        self.rect = self.surf.get_rect(center=(x,y))
    #     self.speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
    # def update(self,group):
    #     self.rect.move_ip(0,self.speed)
    #     if self.rect.bottom > HEIGHT:
    #         self.rect.bottom = HEIGHT
    #         return True
    #     for block in group:
    #         for i in range(block.len):
    #             if pg.sprite.collide_rect(self,block.piece[i]):
    #                 self.rect.bottom = block.piece[i].rect.top
    #                 return True
    #     return False
    def move_left(self,group):
        self.rect.move_ip(-TILE_SIZE,0)
        if self.rect.left < 0:
            self.rect.move_ip(TILE_SIZE,0)
            return False
        for block in group:
            for i in range(block.len):
                if pg.sprite.collide_rect(self,block.piece[i]):
                    self.rect.move_ip(TILE_SIZE,0)
                    return False
        return True
    def move_right(self,group):
        self.rect.move_ip(TILE_SIZE,0)
        if self.rect.right > WIDTH:
            self.rect.move_ip(-TILE_SIZE,0)
            return False
        for block in group:
            for i in range(block.len):
                if pg.sprite.collide_rect(self,block.piece[i]):
                    self.rect.move_ip(-TILE_SIZE,0)
                    return False
        return True
    def drop(self,group):
        max_height = HEIGHT
        for sprite in group:
            if sprite.rect.x == self.rect.x and sprite.rect.top < max_height:
                max_height = sprite.rect.top
        self.rect.bottom = max_height
