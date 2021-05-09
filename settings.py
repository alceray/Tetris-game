# colours 
BLACK = (0,0,0)
DARK_GREY = (45,45,45)
BLUE = (0,0,255)
CYAN = (0,255,255)
YELLOW = (255,255,0)
PURPLE = (128,0,128)
GREEN = (0,255,0)
RED = (255,0,0)
ORANGE = (255,127,0)

# game settings
FPS = 60
INITIAL_TIME = 0
MOVE_TIME = 75
ROTATE_TIME = 400
DROP_TIME = 100
B_START_SPEED = 2
B_SPEED_UP = 0.1
B_SPEED_INCREMENT = 15
KEY_DELAY = 200
KEY_INTERVAL = 100
TILE_SIZE = 32
GRID_WIDTH = 10
GRID_HEIGHT = 20
WIDTH = TILE_SIZE * GRID_WIDTH # 320
HEIGHT = TILE_SIZE * GRID_HEIGHT # 640
SCREEN_SIZE = (WIDTH,HEIGHT) # (320,640)
BG_COLOUR = BLACK
BLOCK_COLOURS = [CYAN,YELLOW,PURPLE,GREEN,RED,BLUE,ORANGE]

# Game pieces
GAME_PIECES = {
    "IBlock": {
        "Col" : CYAN, 
        "Length" : 4, 
        "Coord" : (((0,2),(1,2),(2,2),(3,2)),\
                        ((2,3),(2,2),(2,1),(2,0)),\
                            ((0,1),(1,1),(2,1),(3,1)),\
                                ((1,3),(1,2),(1,1),(1,0)))
    },
    "OBlock": {
        "Col" : YELLOW, 
        "Length" : 2, 
        "Coord" : (((0,0),(1,0),(0,1),(1,1)),\
                        ((0,0),(1,0),(0,1),(1,1)),\
                            ((0,0),(1,0),(0,1),(1,1)),\
                                ((0,0),(1,0),(0,1),(1,1)))
    }, 
    "JBlock": {
        "Col" : BLUE, 
        "Length" : 3,
        "Coord" : (((0,2),(0,1),(1,1),(2,1)),\
                        ((1,0),(1,1),(1,2),(2,2)),\
                            ((0,1),(1,1),(2,1),(2,0)),\
                                ((0,0),(1,0),(1,1),(1,2)))
    },
    "LBlock": { 
        "Col" : ORANGE, 
        "Length" : 3, 
        "Coord" : (((0,1),(1,1),(2,1),(2,2)),\
                        ((1,0),(1,1),(1,2),(2,0)),\
                            ((0,0),(0,1),(1,1),(2,1)),\
                                ((1,0),(1,1),(1,2),(0,2)))
    },
    "SBlock": {
        "Col" : GREEN, 
        "Length" : 3, 
        "Coord" : (((0,1),(1,1),(1,2),(2,2)),\
                        ((1,1),(1,2),(2,0),(2,1)),\
                            ((0,0),(1,0),(1,1),(2,1)),\
                                ((0,2),(0,1),(1,1),(1,0)))
    },
    "TBlock": {
        "Col" : PURPLE, 
        "Length" : 3, 
        "Coord" : (((0,1),(1,1),(2,1),(1,2)),\
                        ((1,0),(1,1),(1,2),(2,1)),\
                            ((0,1),(1,1),(2,1),(1,0)),\
                                ((1,0),(1,1),(1,2),(0,1)))
    },
    "ZBlock": {
        "Col" : RED, 
        "Length" : 3,
        "Coord" : (((0,2),(1,1),(1,2),(2,1)),\
                        ((1,1),(1,0),(2,2),(2,1)),\
                            ((0,1),(1,0),(1,1),(2,0)),\
                                ((0,0),(0,1),(1,1),(1,2)))
    }
}