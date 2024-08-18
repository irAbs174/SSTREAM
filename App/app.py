import os
from kaki.app import App as KakiApp
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.screen import MDScreen


class MainScreen(MDScreen):
    pass


class LoginScreen(MDScreen):
    pass


class MyApp(KakiApp, MDApp):
    KV_FILES = [
        os.path.join(os.getcwd(), 'App/templates/main.kv'),
        os.path.join(os.getcwd(), 'App/templates/user/login.kv'),
    ]

    CLASSES = {
        "MainScreen": "main",
        "LoginScreen": "login",
    }

    AUTORELOADER_PATHS = [(os.getcwd(), {"recursive": True})]

    def build_app(self):
        self.theme_cls.primary_palette = "Green"
        Window.size = [350, 560]
        sm = ScreenManager()
        sm.add_widget(Factory.MainScreen())
        sm.add_widget(Factory.LoginScreen())
        return sm


if __name__ == "__main__":
    MyApp().run()
