import pygame as pg
import sys
from settings import *


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.font_title = pg.font.Font(None, 100)
        self.font_button = pg.font.Font(None, 50)
        self.title_text = self.font_title.render('DOOM STYLE GAME', True, (255, 0, 0))
        self.title_rect = self.title_text.get_rect(center=(HALF_WIDTH, 150))
        
        # Buttons
        self.start_text = self.font_button.render('START', True, (255, 255, 255))
        self.start_rect = self.start_text.get_rect(center=(HALF_WIDTH, HALF_HEIGHT - 50))
        self.start_button_rect = pg.Rect(self.start_rect.x - 50, self.start_rect.y - 25, 300, 80)
        
        self.quit_text = self.font_button.render('QUIT', True, (255, 255, 255))
        self.quit_rect = self.quit_text.get_rect(center=(HALF_WIDTH, HALF_HEIGHT + 100))
        self.quit_button_rect = pg.Rect(self.quit_rect.x - 50, self.quit_rect.y - 25, 300, 80)
        
        self.hovered_button = None

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.start_button_rect.collidepoint(event.pos):
                    return 'start'
                if self.quit_button_rect.collidepoint(event.pos):
                    pg.quit()
                    sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
        return None

    def update(self):
        mouse_pos = pg.mouse.get_pos()
        self.hovered_button = None
        if self.start_button_rect.collidepoint(mouse_pos):
            self.hovered_button = 'start'
        elif self.quit_button_rect.collidepoint(mouse_pos):
            self.hovered_button = 'quit'

    def draw(self):
        self.screen.fill((0, 0, 0))
        
        # Draw title
        self.screen.blit(self.title_text, self.title_rect)
        
        # Draw start button
        start_color = (255, 100, 0) if self.hovered_button == 'start' else (50, 50, 50)
        pg.draw.rect(self.screen, start_color, self.start_button_rect)
        pg.draw.rect(self.screen, (255, 255, 255), self.start_button_rect, 3)
        self.screen.blit(self.start_text, self.start_rect)
        
        # Draw quit button
        quit_color = (255, 100, 0) if self.hovered_button == 'quit' else (50, 50, 50)
        pg.draw.rect(self.screen, quit_color, self.quit_button_rect)
        pg.draw.rect(self.screen, (255, 255, 255), self.quit_button_rect, 3)
        self.screen.blit(self.quit_text, self.quit_rect)
        
        pg.display.flip()

    def run(self):
        pg.mouse.set_visible(True)
        while True:
            action = self.check_events()
            if action == 'start':
                pg.mouse.set_visible(False)
                return
            self.update()
            self.draw()
            self.clock.tick(60)
