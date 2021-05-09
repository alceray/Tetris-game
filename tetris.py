import pygame as pg
import random
from settings import *
from block import *

class Tetris:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        # pg.key.set_repeat(KEY_DELAY,KEY_INTERVAL)
        self.count = 0
    def draw_grid(self):
        for x in range(0,WIDTH,TILE_SIZE):
            pg.draw.line(self.screen,DARK_GREY,(x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,TILE_SIZE):
            pg.draw.line(self.screen,DARK_GREY,(0,y),(WIDTH,y))
    def run(self):
        self.all_sprites = pg.sprite.Group()
        self.type = random.choice(list(GAME_PIECES.keys()))
        self.block = BlockTypes(self.count, self.type)
        self.running = True
        self.left = False
        self.right = False
        self.z = False
        self.up = False
        self.down = False
        self.cooldown = 0
        self.rotate_cd = 0
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
                    self.left = True
                if event.key == pg.K_RIGHT:
                    self.right = True
                if event.key == pg.K_SPACE:
                    self.down = True
                if event.key == pg.K_UP:
                    self.up = True
                if event.key == pg.K_z:
                    self.z = True
                if event.key == pg.K_RSHIFT:
                    self.pause()
                if event.key == pg.K_LSHIFT:
                    self.pause()
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.left = False
                if event.key == pg.K_RIGHT:
                    self.right = False
                if event.key == pg.K_SPACE:
                    self.down = False
                if event.key == pg.K_UP:
                    self.up = False
                if event.key == pg.K_z:
                    self.z = False
        self.key_count = 0 
        if self.cooldown < 0:
            if self.left:
                self.block.move_left(self.all_sprites)
                self.cooldown += COOLDOWN_TIME
                self.key_count += 1
            if self.right:
                self.block.move_right(self.all_sprites)
                self.cooldown += COOLDOWN_TIME
                self.key_count += 1
            if self.down:
                self.block.drop(self.all_sprites)
                self.cooldown += 5*COOLDOWN_TIME
            if self.z:
                if self.key_count == 0 and self.rotate_cd <= 0:
                    self.block.rotate(self.all_sprites,clockwise=False)
                    self.cooldown += 2*COOLDOWN_TIME
                    self.rotate_cd += 0.8*COOLDOWN_TIME
                elif self.key_count > 0 and self.rotate_cd <= 0:
                    self.block.rotate(self.all_sprites,clockwise=False)
                    self.rotate_cd += 2*COOLDOWN_TIME
                elif self.key_count > 0:
                    self.rotate_cd -= 2*FPS
                else:
                    self.rotate_cd -= FPS
            if self.up:
                # rotate without moving left/right
                if self.key_count == 0 and self.rotate_cd <= 0:
                    self.block.rotate(self.all_sprites,clockwise=True)
                    self.cooldown += 2*COOLDOWN_TIME
                    self.rotate_cd += 0.8*COOLDOWN_TIME
                # rotate while moving left/right
                elif self.key_count > 0 and self.rotate_cd <= 0:
                    self.block.rotate(self.all_sprites,clockwise=True)
                    self.rotate_cd += 2*COOLDOWN_TIME
                # lower more cd when moving left/right
                elif self.key_count > 0:
                    self.rotate_cd -= 2*FPS
                else:
                    self.rotate_cd -= FPS
        else:
            self.cooldown -= FPS
    def update(self):
        add_block = self.block.update(self.all_sprites)
        self.line_clear()
        if add_block:
            for block in self.block.piece:
                self.all_sprites.add(block)
            self.reach_top()
            self.count += 1
            self.type = random.choice(list(GAME_PIECES.keys()))
            self.block = BlockTypes(self.count, self.type)
    def draw(self):
        self.screen.fill(BG_COLOUR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.surf,sprite.rect)
        self.draw_block()
        pg.display.update()
    def draw_block(self):
        for i in range(self.block.size):
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
    def pause(self):
        loop = True
        self.screen.fill(BLACK)
        self.font = pg.font.SysFont("Times New Roman",FONT_SIZE)
        self.text = self.font.render("Press Shift to continue",True,WHITE)
        self.screen.blit(self.text,(25,(HEIGHT-FONT_SIZE)/2))
        while loop:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    loop = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RSHIFT:
                        loop = False
                    elif event.key == pg.K_LSHIFT:
                        loop = False
                    elif event.key == pg.K_ESCAPE:
                        loop = False
            pg.display.update()

t = Tetris()
t.run()
pg.quit()
