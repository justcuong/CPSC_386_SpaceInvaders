import pygame.font


class Button:

    def __init__(self, ai_settings, screen, msg, text1, text2, text3, text4, menu):
        """Initialize button attributes"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self.prep_msg(msg)
        self.prep_text1(text1)
        self.prep_text2(text2)
        self.prep_text3(text3)
        self.prep_text4(text4)
        self.prep_menu(menu)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def prep_menu(self, menu):
        self.menu_image = self.font.render(menu, True, self.text_color, self.button_color)
        self.menu_image_rect = self.menu_image.get_rect()
        self.menu_image_rect.center = (650, 450)

    def prep_text1(self, text1):
        self.text1_image = self.font.render(text1, True, self.text_color, self.button_color)
        self.text1_image_rect = self.text1_image.get_rect()
        self.text1_image_rect.center = (350, 500)

    def prep_text2(self, text2):
        self.text2_image = self.font.render(text2, True, self.text_color, self.button_color)
        self.text2_image_rect = self.text2_image.get_rect()
        self.text2_image_rect.center = (350, 550)

    def prep_text3(self, text3):
        self.text3_image = self.font.render(text3, True, self.text_color, self.button_color)
        self.text3_image_rect = self.text3_image.get_rect()
        self.text3_image_rect.center = (350, 600)

    def prep_text4(self, text4):
        self.text4_image = self.font.render(text4, True, self.text_color, self.button_color)
        self.text4_image_rect = self.text4_image.get_rect()
        self.text4_image_rect.center = (350, 650)

    def draw_button(self):
        # Draw the blank button then the message
        self.screen.fill(self.button_color)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.menu_image, self.menu_image_rect)
        self.screen.blit(self.text1_image, self.text1_image_rect)
        self.screen.blit(self.text2_image, self.text2_image_rect)
        self.screen.blit(self.text3_image, self.text3_image_rect)
        self.screen.blit(self.text4_image, self.text4_image_rect)
