from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (325, 580)

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

class CourseScreen(Screen):
   pass
    
class CourseScreenQuest1(Screen):
   pass
class CourseScreenQuest2(Screen):
   pass
class CourseScreenQuest3(Screen):
   pass
class CourseScreenQuest4(Screen):
   pass
class CourseScreenQuest5(Screen):
   pass
class ButtonCard(MDCard, ButtonBehavior):
   pass

class ProtegeMaisApp(MDApp):

  def build(self):
    kv = Builder.load_file("telas.kv")
    screen = kv
    return screen

ProtegeMaisApp().run()