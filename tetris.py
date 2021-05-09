import pygame as pg
import random
from settings import *
from block import *

class Tetris:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(KEY_DELAY,KEY_INTERVAL)
        self.count = 0
    def draw_grid(self):
        for x in range(0,WIDTH,TILE_SIZE):
            pg.draw.line(self.screen,DARK_GREY,(x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,TILE_SIZE):
            pg.draw.line(self.screen,DARK_GREY,(0,y),(WIDTH,y))
    def run(self):
        self.all_sprites = pg.sprite.Group()
        self.type = random.choice(list(GAME_PIECES.keys()))
        self.block = Piece(self.count, self.type)
        self.running = True
        # if only the first option is used delete self.left to self.down
        self.left = False
        self.right = False
        self.up_z = False
        self.up_up = False
        self.down = False
        # if only the second option is used delete self.Time to self.rotate_interval
        self.Time = INITIAL_TIME
        self.lastTime = INITIAL_TIME
        self.interval = MOVE_TIME
        self.rotate_interval = ROTATE_TIME
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def events(self):
        pressed = pg.key.get_pressed()
        if (pg.time.get_ticks() > self.lastTime + self.interval) and \
            (pg.time.get_ticks() > self.Time + self.rotate_interval):
            self.lastTime = pg.time.get_ticks()
            self.Time = pg.time.get_ticks()
            if pressed[pg.K_LEFT] and pressed[pg.K_UP]:
                self.block.move_left(self.all_sprites)
                self.block.rotate(self.all_sprites,clockwise=True)
            if pressed[pg.K_RIGHT] and pressed[pg.K_UP]:
                self.block.move_right(self.all_sprites)
                self.block.rotate(self.all_sprites,clockwise=True)
            if pressed[pg.K_LEFT] and pressed[pg.K_z]:
                self.block.move_left(self.all_sprites)
                self.block.rotate(self.all_sprites,clockwise=False)
            if pressed[pg.K_RIGHT] and pressed[pg.K_z]:
                self.block.move_right(self.all_sprites)
                self.block.rotate(self.all_sprites,clockwise=False)
        if (pg.time.get_ticks() > self.lastTime + self.interval):
            self.lastTime = pg.time.get_ticks()
            if pressed[pg.K_ESCAPE]:
                self.running = False 
            if pressed[pg.K_LEFT]:
                self.block.move_left(self.all_sprites)
            if pressed[pg.K_RIGHT]:
                self.block.move_right(self.all_sprites)
        if (pg.time.get_ticks() > self.Time + self.rotate_interval):
            self.Time = pg.time.get_ticks()
            if pressed[pg.K_SPACE]:
                self.block.drop(self.all_sprites)
            if pressed[pg.K_UP]:
                self.block.rotate(self.all_sprites,clockwise=True)
            if pressed[pg.K_z]:
                self.block.rotate(self.all_sprites,clockwise=False)
        pg.event.pump()
    # if this option is upcommented, remember to uncomment the clock ticks in 
    # block.py Piece Class movement functions, note it has not been added for
    # the rotate function
    """def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                if event.key == pg.K_LEFT:
                    self.left = True
                if event.key == pg.K_RIGHT:
                    self.right = True
                if event.key == pg.K_SPACE:
                    self.down = True
                if event.key == pg.K_UP:
                    self.up_up = True
                if event.key == pg.K_z:
                    self.up_z = True
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.left = False
                if event.key == pg.K_RIGHT:
                    self.right = False
                if event.key == pg.K_SPACE:
                    self.down = False
                if event.key == pg.K_UP:
                    self.up_up = False
                if event.key == pg.K_z:
                    self.up_z = False
        if self.left:
            self.block.move_left(self.all_sprites)
        if self.right:
            self.block.move_right(self.all_sprites)
        if self.down:
            self.block.drop(self.all_sprites)
        if self.up_z:
            self.block.rotate(self.all_sprites,clockwise=False)
        if self.up_up:
            self.block.rotate(self.all_sprites,clockwise=True)"""
    def update(self):
        add_block = self.block.update(self.all_sprites)
        self.line_clear()
        if add_block:
            for block in self.block.piece:
                self.all_sprites.add(block)
            self.reach_top()
            self.count += 1
            self.type = random.choice(list(GAME_PIECES.keys()))
            self.block = Piece(self.count, self.type)
    def draw(self):
        self.screen.fill(BG_COLOUR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.surf,sprite.rect)
        self.draw_block()
        pg.display.update()
    def draw_block(self):
        for i in range(self.block.len):
            self.screen.blit(self.block.piece[i].surf,self.block.piece[i].rect)
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
    def reach_top(self):
        for sprite in self.all_sprites:
            if sprite.rect.top == 0:
                self.running = False
                break

t = Tetris()
t.run()
pg.quit()
