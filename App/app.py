# Applicaion  base
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
from kivyir import *

# Theme Manager
from kivymd.theming import ThemeManager

# UI/UX components
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager, MDScreenManager
from kivymd.uix.button import MDButton
from kivymd.uix.label import MDLabel


class App(MDApp):
    def build(self):

        # Register the custom font
        LabelBase.register(
            name="nasalization",
            fn_regular="assets/fonts/nasalization.otf",
        )

        self.theme_cls.font_styles["nasalization"] = {
            "large": {
                "line-height": 1.64,
                "font-name": "nasalization",
            },
        }
        
        global sm
        sm = MDScreenManager()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Lightcyan"

        self.titlebar_widget = False
        Window.minimum_height = 667
        Window.minimum_width = 375
        self.title = "SSTREAM"
        sm.add_widget(Builder.load_file(f'templates/home_mobile.kv'))
        sm.add_widget(Builder.load_file(f'templates/search_mobile.kv'))
        sm.add_widget(Builder.load_file(f'templates/account_mobile.kv'))
        return sm
        
    # Load Screen function
    def load_screen(self, screen, td):
            sm.transition.direction = td
            sm.current = screen

    # Switch theme dark/light
    def switch_theme(self):
        custom_sheet = None

        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
        self.theme_cls.primary_palette = (
            "Lightcyan" if self.theme_cls.primary_palette == "Darkgoldenrod" else "Darkgoldenrod"
        )


if __name__ == "__main__":
    App().run()