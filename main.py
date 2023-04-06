import pygame
import sys
import config
import grid

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT))
        self.grid = grid.Grid(30, 30)

        self.is_playing = False

    def main_loop(self):

        enter_pressed_before = False
        enter_pressed_cur = False

        clock = pygame.time.Clock()
        font = pygame.font.SysFont("arial", 32)

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                if not enter_pressed_before:
                    enter_pressed_cur = True
                else:
                    enter_pressed_cur = False
                enter_pressed_before = True

            else:
                enter_pressed_cur = False
                enter_pressed_before = False

            if enter_pressed_cur:
                self.is_playing = not self.is_playing

            msg = ""
            if self.is_playing:
                self.grid.update(self.screen.get_rect())
                msg = "PLAYING |> (PRESS SPACE)"
            else:
                self.grid.check_mouse_press(self.screen.get_rect())
                msg = "PAUSED || (PRESS SPACE)"

            self.screen.fill((200, 200, 200))

            text = font.render(msg, 32, (255, 255, 255))
            self.grid.draw(self.screen)
            self.screen.blit(text, (200, 10))
            pygame.display.update()


if __name__ == "__main__":
    Game().main_loop()
