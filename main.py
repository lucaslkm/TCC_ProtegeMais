from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from helpers import username_helper
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (350, 580)

screen = ScreenManager()

class SplashScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class RegisterScreen(Screen):  
    pass

class ForgetSenhaScreen(Screen):
 pass

class DashboardScreen(Screen):
   pass
class ProtegeMaisApp(MDApp):

  def build(self):
    kv = Builder.load_file("telas.kv")
    screen = kv
    return screen

ProtegeMaisApp().run()