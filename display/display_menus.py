from display.display_buttons import DisplayButtons
from settings.general_settings import GENERAL
from sprites.camera_sprites import BUTTON_Q_CAMERA_IMAGE, BUTTON_E_CAMERA_IMAGE, \
    BUTTON_W_CAMERA_IMAGE, BUTTON_S_CAMERA_IMAGE, MOUSE_L_CAMERA_IMAGE, BUTTON_A_CAMERA_IMAGE, \
    BUTTON_D_CAMERA_IMAGE, MOUSE_R_CAMERA_IMAGE

from fonts.fonts import *

from settings.menu_settings import DISPLAY

from utilities.general import get_leaderboard_scores

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


class DisplayMenus:
    def __init__(self, screen, player):
        # Screen
        self.screen = screen

        # Characters
        self.player = player

        # Backgrounds
        self.menu_background = pygame.image.load(GENERAL["menu_background_path"]).convert_alpha()
        # Clock
        self.clock = pygame.time.Clock()
        # Fonts
        self.tiny_font = TINY_FONT
        self.small_font = SMALL_FONT
        self.medium_font = MEDIUM_FONT
        self.large_font = LARGE_FONT
        self.font_color = FONT_COLOR
        # Buttons
        self.first_menu_button_x = 0.62 * GENERAL["width"]
        self.first_menu_button_y = 0.144 * GENERAL["width"]

        self.play_button_image = pygame.image.load(DISPLAY["play_btn_img"]).convert_alpha()
        self.play_button = DisplayButtons(x=self.first_menu_button_x,
                                          y=self.first_menu_button_y,
                                          image=self.play_button_image,
                                          scale=1,
                                          name="play")

        self.settings_button_image = pygame.image.load(DISPLAY["settings_btn_img"]).convert_alpha()
        self.settings_button = DisplayButtons(x=self.first_menu_button_x,
                                              y=self.first_menu_button_y + 90,
                                              image=self.settings_button_image,
                                              scale=1,
                                              name="settings")

        self.leaderboard_button_image = pygame.image.load(
            DISPLAY["leaderboard_btn_img"]).convert_alpha()
        self.leaderboard_button = DisplayButtons(x=self.first_menu_button_x,
                                                 y=self.first_menu_button_y + 180,
                                                 image=self.leaderboard_button_image,
                                                 scale=1,
                                                 name="leaderboard")

        self.credits_button_image = pygame.image.load(
            DISPLAY["credits_btn_img"]).convert_alpha()
        self.credits_button = DisplayButtons(x=self.first_menu_button_x,
                                             y=self.first_menu_button_y + 270,
                                             image=self.credits_button_image,
                                             scale=1,
                                             name="credits")

        self.sounds_on_button_image = pygame.image.load(
            DISPLAY["sounds_on_btn_img"]).convert_alpha()
        self.sounds_on_button = DisplayButtons(x=self.first_menu_button_x,
                                               y=self.first_menu_button_y + 360,
                                               image=self.sounds_on_button_image,
                                               scale=1,
                                               name="sounds_on")

        self.sounds_off_button_image = pygame.image.load(
            DISPLAY["sounds_off_btn_img"]).convert_alpha()
        self.sounds_off_button = DisplayButtons(x=self.first_menu_button_x,
                                                y=self.first_menu_button_y + 360,
                                                image=self.sounds_off_button_image,
                                                scale=1,
                                                name="sounds_off")

        self.main_menu_button_image = pygame.image.load(
            DISPLAY["main_menu_btn_img"]).convert_alpha()
        self.main_menu_button = DisplayButtons(x=self.first_menu_button_x,
                                               y=self.first_menu_button_y + 360,
                                               image=self.main_menu_button_image,
                                               scale=1,
                                               name="main")

        self.continue_button_image = pygame.image.load(
            DISPLAY["continue_btn_img"]).convert_alpha()
        self.continue_button = DisplayButtons(x=self.first_menu_button_x,
                                              y=self.first_menu_button_y,
                                              image=self.continue_button_image,
                                              scale=1,
                                              name="continue")

        self.restart_button_image = pygame.image.load(
            DISPLAY["restart_btn_img"]).convert_alpha()
        self.restart_button = DisplayButtons(x=self.first_menu_button_x,
                                             y=self.first_menu_button_y + 180,
                                             image=self.restart_button_image,
                                             scale=1,
                                             name="restart")

        self.back_button_image = pygame.image.load(
            DISPLAY["back_btn_img"]).convert_alpha()
        self.back_button = DisplayButtons(x=self.first_menu_button_x,
                                          y=self.first_menu_button_y + 360,
                                          image=self.back_button_image,
                                          scale=1,
                                          name="back")

        self.back_button_lb_image = pygame.image.load(
            DISPLAY["back_btn_img"]).convert_alpha()
        self.back_button_lb = DisplayButtons(x=700,
                                             y=790,
                                             image=self.back_button_image,
                                             scale=1,
                                             name="back")

        # Settings button images
        self.btn_q = BUTTON_Q_CAMERA_IMAGE
        self.btn_w = BUTTON_W_CAMERA_IMAGE
        self.btn_e = BUTTON_E_CAMERA_IMAGE
        self.btn_a = BUTTON_A_CAMERA_IMAGE
        self.btn_s = BUTTON_S_CAMERA_IMAGE
        self.btn_d = BUTTON_D_CAMERA_IMAGE
        self.mouse_l = MOUSE_L_CAMERA_IMAGE
        self.mouse_r = MOUSE_R_CAMERA_IMAGE

        # Misc
        self.credits = GENERAL["credits"]

    def display_main_menu(self, game_setup):
        """
        Displays main menu on screen.
        """
        self.screen.blit(self.menu_background, (0, 0))

        # Menu buttons
        if self.play_button.draw(self.screen, game_setup.sound_is_on):
            game_setup.reset_player()
            game_setup.turn_off_menus()
            game_setup.main_menu_shown = False
            game_setup.is_playing_game = True

        elif self.settings_button.draw(self.screen, game_setup.sound_is_on):
            game_setup.turn_off_menus()
            game_setup.settings_menu_shown = True
            # game_setup.before_settings_menu = "home"

        elif self.leaderboard_button.draw(self.screen, game_setup.sound_is_on):
            game_setup.turn_off_menus()
            game_setup.leaderboard_menu_shown = True

        elif self.credits_button.draw(self.screen, game_setup.sound_is_on):
            game_setup.turn_off_menus()
            game_setup.credits_menu_shown = True

        if not self.player.sound_is_on:
            if self.sounds_off_button.draw(self.screen, game_setup.sound_is_on):
                game_setup.sound_is_on = True
                self.player.sound_is_on = True

        elif self.player.sound_is_on:
            if self.sounds_on_button.draw(self.screen, game_setup.sound_is_on):
                game_setup.sound_is_on = False
                self.player.sound_is_on = False

    def display_settings_menu(self, game_setup):
        self.screen.blit(self.menu_background, (0, 0))

        buttons = [self.btn_w, self.btn_s, self.btn_a, self.btn_d, self.btn_q, self.btn_q,
                   self.mouse_l, self.mouse_r]
        descriptions = ["forwards", "backwards", "left", "right", "use potion", "use portal",
                        "shot bullet", "throw bomb"]

        for i, (button, description) in enumerate(zip(buttons, descriptions)):
            self.screen.blit(button,
                             (self.first_menu_button_x - 0.02 * GENERAL["width"],
                              self.first_menu_button_y + (i * 45))
                             )
            text = self.small_font.render(description, True, self.font_color)
            self.screen.blit(text,
                             (self.first_menu_button_x - 0.02 * GENERAL["width"] + 75,
                              self.first_menu_button_y + (i * 45 + 10)))

        # Back Button
        if self.back_button.draw(self.screen, game_setup.sound_is_on):
            if game_setup.before_settings_menu == "pause":
                game_setup.turn_off_menus()
                game_setup.pause_menu_shown = True

            elif game_setup.before_settings_menu == "home":
                game_setup.turn_off_menus()
                game_setup.main_menu_shown = True

    def display_leaderboad_menu(self, game_setup):
        self.screen.fill((35, 35, 35))

        # Calculate base position
        base_x = 300
        base_y = 150

        # Get scores
        top_scores = get_leaderboard_scores()

        # Gam over text
        leaderboard_text = self.large_font.render("Leaderboard", True,
                                                  GENERAL["white"])
        self.screen.blit(leaderboard_text, (base_x + 300,
                                            base_y))

        for i, item in enumerate(top_scores):
            name = self.small_font.render(
                f"{item[0]}", True, GENERAL["white"])
            self.screen.blit(name, (base_x + 350,
                                    base_y + 135 + (i * 50)))

            score = self.small_font.render(
                f"{item[1]}", True, GENERAL["white"])
            self.screen.blit(score, (base_x + 650,
                                     base_y + 135 + (i * 50)))

        # Back Button
        if self.back_button_lb.draw(self.screen, game_setup.sound_is_on):
            if game_setup.before_settings_menu == "pause":
                game_setup.turn_off_menus()
                game_setup.pause_menu_shown = True

            elif game_setup.before_settings_menu == "home":
                game_setup.turn_off_menus()
                game_setup.main_menu_shown = True

    def display_credit_menu(self, game_setup):
        """
        Displays credit menu with credits and a Main Menu button.
        """
        self.screen.blit(self.menu_background, (0, 0))
        # Loop over credits and blit them
        for i, credit in enumerate(self.credits):
            text = self.tiny_font.render(credit, True, self.font_color)
            self.screen.blit(text, (
                self.first_menu_button_x - 0.02 * GENERAL["width"],
                self.first_menu_button_y + i * 18))

        # Blit Main Menu button
        if self.back_button.draw(self.screen, game_setup.sound_is_on):
            game_setup.turn_off_menus()
            game_setup.main_menu_shown = True

    def display_pause_menu(self, game_setup):
        """
        Displays pause menu on screen.
        """
        self.screen.blit(self.menu_background, (0, 0))

        # Menu buttons
        if self.continue_button.draw(self.screen, game_setup.sound_is_on):
            game_setup.turn_off_menus()
            game_setup.is_playing_game = True
            game_setup.pause_menu_shown = False

        elif self.settings_button.draw(self.screen, game_setup.sound_is_on):
            game_setup.turn_off_menus()
            game_setup.settings_menu_shown = True
            game_setup.before_settings_menu = "pause"

        elif self.restart_button.draw(self.screen, game_setup.sound_is_on):
            game_setup.reset_game()
            game_setup.turn_off_menus()
            game_setup.main_menu_shown = False
            game_setup.is_playing_game = True

        elif self.main_menu_button.draw(self.screen, game_setup.sound_is_on):
            # game_setup.turn_off_menus()
            # game_setup.main_menu_shown = True
            # game_setup.is_playing_game = False
            game_setup.reset_game()
