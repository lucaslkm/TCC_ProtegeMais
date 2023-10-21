from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.clock import Clock
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyA7zRJyibj48iQtYfjEoSoUdG8FXvE_Kz8",
    "authDomain": "protegemais-a5c9c.firebaseapp.com",
    "databaseURL": "https://protegemais-a5c9c-default-rtdb.firebaseio.com",
    "projectId": "protegemais-a5c9c",
    "storageBucket": "protegemais-a5c9c.appspot.com",
    "messagingSenderId": "710472061009",
    "appId": "1:710472061009:web:9e2e52044d30f851e1a870",
    "measurementId": "G-3JVS7HDZMK"
        }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


Window.size = (325, 580)

screen = ScreenManager()

class SplashScreen(Screen):
    pass


class LoginScreen(MDScreen):
    def callback_dash(self, *args):
        MDApp.get_running_app().root.current = "dashboard"

    def login(self):
      email = self.ids.email.text
      password = self.ids.senha.text
      if auth.sign_in_with_email_and_password(email,password):
         Clock.schedule_once(self.callback_dash, 3)

class RegisterScreen(MDScreen): 
      def callback(self, *args):
        MDApp.get_running_app().root.current = "login"

      def cadastro(self):
        email = self.ids.email_registro.text
        password = self.ids.senha_registro.text
        password_confirm = self.ids.confirma_senha.text
        if password == password_confirm and "@" in email and ".com" in email and len(password) >= 6:
            if auth.create_user_with_email_and_password(email,password):
               Clock.schedule_once(self.callback, 3)
         
class ForgetSenhaScreen(MDScreen):
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