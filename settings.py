# colours 
BLACK = (0,0,0)
WHITE = (255,255,255)
DARK_GREY = (45,45,45)
BLUE = (0,0,255)
CYAN = (0,255,255)
YELLOW = (255,255,0)
PURPLE = (128,0,128)
GREEN = (0,255,0)
RED = (255,0,0)
ORANGE = (255,127,0)
BG_COLOUR = BLACK
BLOCK_COLOURS = [CYAN,YELLOW,PURPLE,GREEN,RED,BLUE,ORANGE]

# DO NOT change these
FPS = 60
COOLDOWN_TIME = 200

# speed values
B_START_SPEED = 1.5
B_SPEED_UP = 0.1
B_SPEED_INCREMENT = 20
SOFT_DROP_SPEED = 15

# game dimensions
TILE_SIZE = 32
GRID_WIDTH = 10
INFO_WIDTH = 4
SIDE_WIDTH = TILE_SIZE * INFO_WIDTH
TOTAL_WIDTH = INFO_WIDTH + GRID_WIDTH
GRID_HEIGHT = 20
WIDTH = TILE_SIZE * TOTAL_WIDTH # 480
HEIGHT = TILE_SIZE * GRID_HEIGHT # 640
SCREEN_SIZE = (WIDTH,HEIGHT) # (480,640)
FONT_SIZE = 30

# Game pieces
GAME_PIECES = {
    "IBlock": {
        "Col" : CYAN, 
        "Length" : 4, 
        "Size" : 4,
        "Coord" : (((0,2),(1,2),(2,2),(3,2)),\
                        ((2,3),(2,2),(2,1),(2,0)),\
                            ((0,1),(1,1),(2,1),(3,1)),\
                                ((1,3),(1,2),(1,1),(1,0)))
    },
    "OBlock": {
        "Col" : YELLOW, 
        "Length" : 2, 
        "Size" : 4,
        "Coord" : (((0,0),(1,0),(0,1),(1,1)),\
                        ((0,0),(1,0),(0,1),(1,1)),\
                            ((0,0),(1,0),(0,1),(1,1)),\
                                ((0,0),(1,0),(0,1),(1,1)))
    }, 
    "JBlock": {
        "Col" : BLUE, 
        "Length" : 3,
        "Size" : 4,
        "Coord" : (((0,2),(0,1),(1,1),(2,1)),\
                        ((1,0),(1,1),(1,2),(2,2)),\
                            ((0,1),(1,1),(2,1),(2,0)),\
                                ((0,0),(1,0),(1,1),(1,2)))
    },
    "LBlock": { 
        "Col" : ORANGE, 
        "Length" : 3, 
        "Size" : 4,
        "Coord" : (((0,1),(1,1),(2,1),(2,2)),\
                        ((1,0),(1,1),(1,2),(2,0)),\
                            ((0,0),(0,1),(1,1),(2,1)),\
                                ((1,0),(1,1),(1,2),(0,2)))
    },
    "SBlock": {
        "Col" : GREEN, 
        "Length" : 3, 
        "Size" : 4,
        "Coord" : (((0,1),(1,1),(1,2),(2,2)),\
                        ((1,1),(1,2),(2,0),(2,1)),\
                            ((0,0),(1,0),(1,1),(2,1)),\
                                ((0,2),(0,1),(1,1),(1,0)))
    },
    "TBlock": {
        "Col" : PURPLE, 
        "Length" : 3, 
        "Size" : 4,
        "Coord" : (((0,1),(1,1),(2,1),(1,2)),\
                        ((1,0),(1,1),(1,2),(2,1)),\
                            ((0,1),(1,1),(2,1),(1,0)),\
                                ((1,0),(1,1),(1,2),(0,1)))
    },
    "ZBlock": {
        "Col" : RED, 
        "Length" : 3,
        "Size" : 4,
        "Coord" : (((0,2),(1,1),(1,2),(2,1)),\
                        ((1,1),(1,0),(2,2),(2,1)),\
                            ((0,1),(1,0),(1,1),(2,0)),\
                                ((0,0),(0,1),(1,1),(1,2)))
    }
}