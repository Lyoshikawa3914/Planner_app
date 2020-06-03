import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class MainWindow(GridLayout):
    #calls on gridlayout to make whatever is needed to show visuals
    #pass

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.rows = 7
        self.cols = 4

        #make seperate pages for each day, that user can click to
        self.sunday = Button(text="Sunday", font_size=20)
        self.add_widget(self.sunday)

        self.sunday.bind(on_press=self.sunday_button)

        self.monday = Button(text="Monday", font_size=20)
        #self.monday.bind(on_press=self.pressed)
        self.add_widget(self.monday)

        self.tuesday = Button(text="Tuesday", font_size=20)
        #self.tuesday.bind(on_press=self.pressed)
        self.add_widget(self.tuesday)

        self.wednesday = Button(text="Wednesday", font_size=20)
        #self.wednesday.bind(on_press=self.pressed)
        self.add_widget(self.wednesday)

        self.thursday = Button(text="Thursday", font_size=20)
        #self.thursday.bind(on_press=self.pressed)
        self.add_widget(self.thursday)

        self.friday = Button(text="Friday", font_size=20)
        #self.friday.bind(on_press=self.pressed)
        self.add_widget(self.friday)

        self.saturday = Button(text="Saturday", font_size=20)
        #self.saturday.bind(on_press=self.pressed)
        self.add_widget(self.saturday)

        self.logo = Label(text="Planner App", font_size=20)
        self.add_widget(self.logo)

    def sunday_button(self, instance):
        self.sunday_screen = Sunday()
        screen = Screen(name="sunday")
        screen.add_widget(self.sunday_screen)
        self.sunday_screen.add_widget(screen)
        main_app.screen_manager.current = "sunday"

class Sunday(GridLayout):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(text="Hello world")
        self.add_widget(self.message)


#planner = Builder.load_file("planner.kv")

class main(App):
    # calls on App to make the framework
    def build(self):
        #return MainWindow()
        self.screen_manager = ScreenManager()

        self.main_window = MainWindow()
        screen = Screen(name="main")
        screen.add_widget(self.main_window)
        self.screen_manager.add_widget(screen)





        return self.screen_manager



if __name__ == "__main__":
    main_app = main()
    main_app.run()