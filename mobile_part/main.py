from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)


class RegisterScreen(Screen):
    email = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    password_rep = ObjectProperty(None)
    dialog = None

    def print_password(self):
        print(self.password.text)

    def check_password(self):

        if self.password.text == self.password_rep.text:
            return self.password.text
        else:
            self.dialog = MDDialog(title='Username check', text='Password must be the same',
                                   size_hint=(0.5, 1),
                                   buttons=[
                                       MDFlatButton(text='OK', on_release=lambda _: self.dialog.dismiss())
                                           ])
            self.dialog.open()



class WindowManager(ScreenManager):
    pass


class MyGrid(Widget):
    pass


class WorkersApp(MDApp):
    def build(self):
        self.kv = Builder.load_file('workers.kv')


if __name__ == "__main__":
    WorkersApp().run()
