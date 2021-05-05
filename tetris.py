import pygame as pg

BLACK = (0,0,0)
DARKGREY = (45,45,45)
FPS = 60
TILE_SIZE = 32
GRID_WIDTH = 10
GRID_HEIGHT = 20
WIDTH = TILE_SIZE * GRID_WIDTH
HEIGHT = TILE_SIZE * GRID_HEIGHT
SCREEN_SIZE = (WIDTH,HEIGHT)
BG_COLOUR = BLACK

class Block(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)


class Tetris:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
    def draw_grid(self):
        for x in range(0,WIDTH,TILE_SIZE):
            pg.draw.line(self.screen,DARKGREY,(x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,TILE_SIZE):
            pg.draw.line(self.screen,DARKGREY,(0,y),(WIDTH,y))
    def run(self):
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
                elif event.key == pg.K_UP:
                    self.running = True
    def update(self):
        pass
    def draw(self):
        self.screen.fill(BG_COLOUR)
        self.draw_grid()
        pg.display.update()

t = Tetris()
t.run()
pg.quit()