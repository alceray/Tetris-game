import pygame as pg
import random
from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self,count):
        pg.sprite.Sprite.__init__(self)
        self.surf = pg.Surface((TILE_SIZE,TILE_SIZE))
        self.surf.fill(random.choice(BLOCK_COLOURS))
        self.rect = self.surf.get_rect(
            center=((0.5+random.randint(0,GRID_WIDTH-1))*TILE_SIZE,0))
        self.speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
    def update(self,group):
        self.rect.move_ip(0,self.speed)
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            return True
        for sprite in group:
            if sprite != self and pg.sprite.collide_rect(self,sprite):
                self.rect.bottom = sprite.rect.top
                return True
        return False
    def move_left(self,group):
        self.rect.move_ip(-TILE_SIZE,0)
        for sprite in group:
            if sprite != self and pg.sprite.collide_rect(self,sprite):
                self.rect.move_ip(TILE_SIZE,0)
                break
    def move_right(self,group):
        self.rect.move_ip(TILE_SIZE,0)
        for sprite in group:
            if sprite != self and pg.sprite.collide_rect(self,sprite):
                self.rect.move_ip(-TILE_SIZE,0)
                break

class Tetris:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(KEY_DELAY,KEY_INTERVAL)
        self.count = 0
        self.lines = [0] * GRID_HEIGHT
    def draw_grid(self):
        for x in range(0,WIDTH,TILE_SIZE):
            pg.draw.line(self.screen,DARK_GREY,(x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,TILE_SIZE):
            pg.draw.line(self.screen,DARK_GREY,(0,y),(WIDTH,y))
    def run(self):
        self.all_sprites = pg.sprite.Group()
        self.block = Block(self.count)
        self.all_sprites.add(self.block)
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                if event.key == pg.K_LEFT:
                    self.block.move_left(self.all_sprites)
                if event.key == pg.K_RIGHT:
                    self.block.move_right(self.all_sprites)
    def update(self):
        add_block = self.block.update(self.all_sprites)
        self.line_clear()
        if add_block:
            self.count += 1
            self.block = Block(self.count)
            self.all_sprites.add(self.block)
    def draw(self):
        self.screen.fill(BG_COLOUR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.surf,sprite.rect)
        pg.display.update()
    def check_line_clear(self):
        self.lines = [0] * GRID_HEIGHT
        for sprite in self.all_sprites:
            row = sprite.rect.top//TILE_SIZE
            self.lines[row] += 1
        if GRID_WIDTH in self.lines:
            return True
        return False
    def line_clear(self):
        if self.check_line_clear():
            for row,num in enumerate(self.lines):
                if num == GRID_WIDTH:
                    self.remove_row(row)
    def remove_row(self,row):
        for sprite in self.all_sprites:
            cur_row = sprite.rect.top//TILE_SIZE
            if cur_row == row: 
                self.all_sprites.remove(sprite)
            elif cur_row < row: 
                sprite.rect.y += TILE_SIZE

t = Tetris()
t.run()
pg.quit()
