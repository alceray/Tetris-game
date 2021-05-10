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
    def draw_grid(self):
        for x in range(SIDE_WIDTH,WIDTH,TILE_SIZE):
            pg.draw.line(self.screen,DARK_GREY,(x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,TILE_SIZE):
            pg.draw.line(self.screen,DARK_GREY,(SIDE_WIDTH,y),(WIDTH,y))
    def run(self):
        self.count = 0
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.type = random.choice(list(GAME_PIECES.keys()))
        self.block = BlockTypes(self.count, self.type)
        self.hard_drop = False
        self.add_block = False
        self.running = True
        self.left = False
        self.right = False
        self.z = False
        self.up = False
        self.drop = False
        self.down = False
        self.cooldown = 0
        self.rotate_cd = 0
        self.add_block_cd = 10*COOLDOWN_TIME
        self.font = pg.font.SysFont("Times New Roman",FONT_SIZE)
        self.pause_time = 0
        while self.running:
            self.clock.tick(FPS)
            self.draw_grid()
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.end_game(self.score, self.font)
                if event.key == pg.K_LEFT:
                    self.left = True
                if event.key == pg.K_RIGHT:
                    self.right = True
                if event.key == pg.K_SPACE:
                    self.drop = True
                if event.key == pg.K_UP:
                    self.up = True
                if event.key == pg.K_z:
                    self.z = True
                if event.key == pg.K_RSHIFT:
                    self.pause(self.font)
                if event.key == pg.K_LSHIFT:
                    self.pause(self.font)
                if event.key == pg.K_DOWN:
                    self.down = True
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.left = False
                if event.key == pg.K_RIGHT:
                    self.right = False
                if event.key == pg.K_SPACE:
                    self.drop = False
                if event.key == pg.K_UP:
                    self.up = False
                if event.key == pg.K_z:
                    self.z = False
                if event.key == pg.K_DOWN:
                    self.down = False
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
            if self.drop:
                self.block.drop(self.all_sprites)
                self.cooldown += 5*COOLDOWN_TIME
                self.hard_drop = True
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
            if self.down:
                self.block.soft_drop(self.all_sprites,SOFT_DROP_SPEED)
                if self.add_block:
                    self.cooldown += 5*COOLDOWN_TIME
        else:
            self.cooldown -= FPS
    def holding_key(self):
        return self.left or self.right or self.up or self.z or self.down
    def update(self):
        self.add_block = self.block.update(self.all_sprites,self.block.speed)
        self.line_clear()
        #print(self.add_block_cd)
        if self.hard_drop or (self.add_block and self.add_block_cd < 0 and self.holding_key())\
            or (self.add_block and self.add_block_cd == 0):
            for block in self.block.piece:
                self.all_sprites.add(block)
            self.reach_top()
            self.count += 1
            self.type = random.choice(list(GAME_PIECES.keys()))
            self.block = BlockTypes(self.count, self.type)
            self.hard_drop = False
            self.add_block_cd = 10*COOLDOWN_TIME
        elif self.add_block and self.add_block_cd < 0:
            self.add_block_cd += 10
        elif self.add_block and self.add_block_cd > 0:
            self.add_block_cd -= FPS
    def draw(self):
        self.screen.fill(BG_COLOUR)
        score_text_pos = (SIDE_WIDTH / 2, 4 * TILE_SIZE)
        score_val_pos = (SIDE_WIDTH / 2, 5.1 * TILE_SIZE)
        self.print_score(self.screen, self.score, self.font, score_text_pos, score_val_pos)
        time_text_pos = (SIDE_WIDTH / 2, 6.5 * TILE_SIZE)
        time_val_pos = (SIDE_WIDTH / 2, 7.6 * TILE_SIZE)
        self.print_time(self.screen, self.pause_time, self.font, time_text_pos, time_val_pos)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.surf,sprite.rect)
        if not self.add_block:
            self.draw_block_shadow()
        self.draw_grid()
        self.draw_block()
        pg.display.update()
    def draw_block(self):
        for block in self.block.piece:
            self.screen.blit(block.surf,block.rect)
    def draw_block_shadow(self):
        min_dist = 2*HEIGHT
        for block in self.block.piece:
            min_dist = min(HEIGHT-block.rect.bottom,min_dist)
            for sprite in self.all_sprites:
                diff = sprite.rect.top - block.rect.bottom
                if block.rect.x == sprite.rect.x and diff >= 0:
                    min_dist = min(min_dist,diff)
        for block in self.block.piece:
            shadow = pg.Surface((TILE_SIZE,TILE_SIZE))
            shadow_rect = shadow.get_rect(\
                center=(block.rect.centerx,block.rect.centery+min_dist))
            shadow.set_alpha(127)
            shadow.fill(self.block.col)
            self.screen.blit(shadow,shadow_rect)
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
                    self.score += 1
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
    def pause(self, font):
        initial_time = pg.time.get_ticks()
        final_time = pg.time.get_ticks()
        paused = True
        self.screen.fill(BLACK)
        text = font.render("Press Shift to continue",True,WHITE)
        self.screen.blit(text,(100,(HEIGHT-FONT_SIZE)/2))
        while paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    final_time = pg.time.get_ticks()
                    paused = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RSHIFT or event.key == pg.K_LSHIFT \
                        or event.key == pg.K_ESCAPE:
                        final_time = pg.time.get_ticks()
                        paused = False
            self.pause_time += (final_time - initial_time)
            pg.display.update()
    def print_score(self, screen, score, font, text_pos, val_pos):
        text = font.render("Score:",True,WHITE)
        textRect = text.get_rect()
        textRect.center = text_pos
        screen.blit(text,textRect)
        val = font.render(str(score),True,WHITE)
        valRect = val.get_rect()
        valRect.center = val_pos
        screen.blit(val,valRect)
    def print_time(self, screen, pause, font, text_pos, val_pos):
        time = (pg.time.get_ticks() - pause) // 100
        decisec = time % 10
        sec = (time // 10) % 100
        minute = sec // 60
        sec = sec % 60
        text = font.render("Time:",True,WHITE)
        textRect = text.get_rect()
        textRect.center = text_pos
        screen.blit(text,textRect)
        val_output = "{:02d}:{:02d}:{}"
        val = font.render(val_output.format(minute, sec, decisec),True,WHITE)
        valRect = val.get_rect()
        valRect.center = val_pos
        screen.blit(val,valRect)
    def end_game(self, score, font):
        the_end = True
        self.screen.fill(BLACK)
        text = font.render("THE END",True,RED)
        textRect = text.get_rect()
        textRect.x = WIDTH / 2
        textRect.y = 1.5 * TILE_SIZE
        textRect.center = (textRect.x, textRect.y)
        self.screen.blit(text,textRect)
        results = font.render("Results:", True, WHITE)
        resultRect = text.get_rect()
        resultRect.center = (textRect.x, 100)
        self.screen.blit(results,resultRect)
        score_text_pos = (WIDTH / 2, 4.5 * TILE_SIZE)
        score_val_pos = (WIDTH / 2, 5.5 * TILE_SIZE)
        self.print_score(self.screen, score, font, score_text_pos, score_val_pos)
        time_text_pos = (WIDTH / 2, 7 * TILE_SIZE)
        time_val_pos = (WIDTH / 2, 8 * TILE_SIZE)
        self.print_time(self.screen, score, font, time_text_pos, time_val_pos)
        quit_x = 8.5 * TILE_SIZE
        quit_y = 13 * TILE_SIZE
        button_width = 4.5 * TILE_SIZE
        button_height = 1.5 * TILE_SIZE
        restart_x = 1.5 * TILE_SIZE
        restart_y = quit_y
        quit_text = font.render("QUIT",True,BLACK)
        quitRect = quit_text.get_rect()
        quitRect.x = quit_x + (button_width / 2)
        quitRect.y = quit_y + (button_height / 2)
        quitRect.center = (quitRect.x, quitRect.y)
        restart_text = font.render("RESTART",True,BLACK)
        restartRect = restart_text.get_rect()
        restartRect.x = restart_x + (button_width / 2)
        restartRect.y = restart_y + (button_height / 2)
        restartRect.center = (restartRect.x, restartRect.y)
        while self.running:
            mouse = pg.mouse.get_pos()
            will_quit = quit_x <= mouse[0] <= quit_x + button_width and \
                quit_y <= mouse[1] <= quit_y + button_height
            will_restart = restart_x <= mouse[0] <= restart_x + button_width and \
                restart_y <= mouse[1] <= restart_y + button_height
            if will_quit:
                pg.draw.rect(self.screen, DARK_GREY, \
                    [quit_x, quit_y, button_width, button_height])
            else:
                pg.draw.rect(self.screen, WHITE, \
                    [quit_x, quit_y, button_width, button_height])
            self.screen.blit(quit_text,quitRect)
            if will_restart:
                pg.draw.rect(self.screen, DARK_GREY, \
                    [restart_x, restart_y, button_width, button_height])
            else:
                pg.draw.rect(self.screen, WHITE, \
                    [restart_x, restart_y, button_width, button_height])
            self.screen.blit(restart_text,restartRect)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if will_restart:
                        self.running = False
                        pg.quit()
                        t = Tetris()
                        t.run()
                    if will_quit:
                        self.running = False
            pg.display.update()


t = Tetris()
t.run()
pg.quit()
