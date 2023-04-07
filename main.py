import pygame
import sys
import config
import grid

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT))
        self.grid = grid.Grid(50, 50)

        self.is_playing = False

    def main_loop(self):

        space_pressed_before = False
        space_pressed_cur = False

        clock = pygame.time.Clock()
        font = pygame.font.SysFont("arial", 32)

        background_image = None
        grid_surface = None

        try:
            background_image = pygame.image.load("background.jpg")
            background_image = pygame.transform.scale(background_image, (config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT))
            grid_surface = pygame.surface.Surface((config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT)).convert_alpha()

        except:
            grid_surface = pygame.surface.Surface((config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT))

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                if not space_pressed_before:
                    space_pressed_cur = True
                else:
                    space_pressed_cur = False
                space_pressed_before = True
            elif pygame.key.get_pressed()[pygame.K_RETURN]:
                self.grid.clear()
            else:
                space_pressed_cur = False
                space_pressed_before = False

            if space_pressed_cur:
                self.is_playing = not self.is_playing

            msg = ""
            if self.is_playing:
                self.grid.update(self.screen.get_rect())
                msg = "PLAYING |> (PRESS SPACE)"
            else:
                self.grid.check_mouse_press(self.screen.get_rect())
                msg = "PAUSED || (PRESS SPACE)"

            self.screen.fill((200, 200, 200))
            grid_surface.fill((0, 0, 0, 255))

            text = font.render(msg, 32, (255, 255, 255))
            if background_image:
                self.screen.blit(background_image, (0, 0))

            self.grid.draw(grid_surface)
            self.screen.blit(grid_surface, (0, 0))
            self.screen.blit(text, (200, 10))
            pygame.display.update()


if __name__ == "__main__":
    Game().main_loop()
