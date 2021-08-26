from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window

Window.size = (300, 500)

from requests import post


class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)


class RegisterScreen(Screen):
    email = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    password_rep = ObjectProperty(None)
    dialog = None
    password_checked = None

    def post_user(self):

        if self.password.text == self.password_rep.text:
            self.password_checked = self.password

            print("rabotaet")
            post('http://localhost:5000/post_user',
                 data={'username': f'{self.username.text}', 'email': f'{self.email.text}',
                       'password': f'{self.password_checked.text}'})  # .json()

        else:
            self.dialog = MDDialog(title='Username check', text='Password must be the same',
                                   size_hint=(0.5, 1),
                                   buttons=[
                                       MDFlatButton(text='OK', on_release=lambda _: self.dialog.dismiss())
                                   ])
            self.dialog.open()



class HomeScreen(Screen):
    def navigation_draw(self):
        print("somth")


class WorkersApp(MDApp):
    def build(self):
        self.kv = Builder.load_file('workers.kv')

    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name


if __name__ == "__main__":
    WorkersApp().run()
