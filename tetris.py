import pygame as pg
import random
from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self,count):
        pg.sprite.Sprite.__init__(self)
        self.surf = pg.Surface((TILE_SIZE,TILE_SIZE))
        self.surf.fill(random.choice(BLOCK_COLOURS))
        self.rect = self.surf.get_rect(
            center=(random.randint(0,9)*TILE_SIZE+TILE_SIZE/2,0))
        self.speed = B_START_SPEED + (count//B_SPEED_INCREMENT) * B_SPEED_UP
    def update(self):
        self.rect.move_ip(0,self.speed)
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            return True
        return False

class Tetris:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(200,100)
        self.count = 0
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
                    self.block.rect.move_ip(-TILE_SIZE,0)
                if event.key == pg.K_RIGHT:
                    self.block.rect.move_ip(TILE_SIZE,0)
    def update(self):
        add_block = self.block.update()
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

t = Tetris()
t.run()
pg.quit()