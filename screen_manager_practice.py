from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import sqlite3 as sql

#this app allows users to input events, store, delete, and display their plans, events, or daily routines

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        con = sql.connect('planner_app.db')  # connects to sqlite, creating a db
        cur = con.cursor()  # creates a cursor object using the cursor method

        # creates the table for data
        cur.execute(""" CREATE TABLE IF NOT EXISTS planner(
                        day text,
                        title text,
                        time text)
                        """)
        con.commit()
        con.close()

        self.main_app_grid = GridLayout(rows=2, cols=4)

        self.sunday = Button(text="Sunday", font_size=30)
        self.sunday.bind(on_press=self.sunday_screen)
        self.main_app_grid.add_widget(self.sunday)

        self.monday = Button(text="Monday", font_size=30)
        self.monday.bind(on_press=self.monday_screen)
        self.main_app_grid.add_widget(self.monday)

        self.tuesday = Button(text="Tuesday", font_size=30)
        self.tuesday.bind(on_press=self.tuesday_screen)
        self.main_app_grid.add_widget(self.tuesday)

        self.wednesday = Button(text="Wednesday", font_size=30)
        self.wednesday.bind(on_press=self.wednesday_screen)
        self.main_app_grid.add_widget(self.wednesday)

        self.thursday = Button(text="Thursday", font_size=30)
        self.thursday.bind(on_press=self.thursday_screen)
        self.main_app_grid.add_widget(self.thursday)

        self.friday = Button(text="Friday", font_size=30)
        self.friday.bind(on_press=self.friday_screen)
        self.main_app_grid.add_widget(self.friday)

        self.saturday = Button(text="Saturday", font_size=30)
        self.saturday.bind(on_press=self.saturday_screen)
        self.main_app_grid.add_widget(self.saturday)

        self.planner_app = Label(text="Planner App", font_size=30)
        self.main_app_grid.add_widget(self.planner_app)

        self.add_widget(self.main_app_grid)


    def sunday_screen(self, instance):
        main_app.root.current = "sunday"
        main_app.root.transition.direction = "left"

    def monday_screen(self, instance):
        main_app.root.current = "monday"
        main_app.root.transition.direction = "left"

    def tuesday_screen(self, instance):
        main_app.root.current = "tuesday"
        main_app.root.transition.direction = "left"

    def wednesday_screen(self, instance):
        main_app.root.current = "wednesday"
        main_app.root.transition.direction = "left"

    def thursday_screen(self, instance):
        main_app.root.current = "thursday"
        main_app.root.transition.direction = "left"

    def friday_screen(self, instance):
        main_app.root.current = "friday"
        main_app.root.transition.direction = "left"

    def saturday_screen(self, instance):
        main_app.root.current = "saturday"
        main_app.root.transition.direction = "left"


class DeletePage(Screen):
# page will delete an event from planner by typing in the title, then pushing delete button
    title = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DeletePage, self).__init__(**kwargs)
        self.delete_page = FloatLayout()
        self.mygrid = GridLayout(cols=2, height=200)

#layout for the buttons on top of the screen
        self.delete_grid = GridLayout(rows=2, cols=4, height=Window.size[1] * 0.1, size_hint_y=None)

        self.main_menu = Button(text="Main Menu", font_size=10)
        self.main_menu.bind(on_press=self.return_main)
        self.delete_grid.add_widget(self.main_menu)

        self.sunday = Button(text="Sunday", font_size=10)
        self.sunday.bind(on_press=self.sunday_btn)
        self.delete_grid.add_widget(self.sunday)

        self.monday = Button(text="Monday", font_size=10)
        self.monday.bind(on_press=self.monday_btn)
        self.delete_grid.add_widget(self.monday)

        self.tuesday = Button(text="Tuesday", font_size=10)
        self.tuesday.bind(on_press=self.tuesday_btn)
        self.delete_grid.add_widget(self.tuesday)

        self.wednesday = Button(text="Wednesday", font_size=10)
        self.wednesday.bind(on_press=self.wednesday_btn)
        self.delete_grid.add_widget(self.wednesday)

        self.thursday = Button(text="Thursday", font_size=10)
        self.thursday.bind(on_press=self.thursday_btn)
        self.delete_grid.add_widget(self.thursday)

        self.friday = Button(text="Friday", font_size=10)
        self.friday.bind(on_press=self.friday_btn)
        self.delete_grid.add_widget(self.friday)

        self.saturday = Button(text="Saturday", font_size=10)
        self.saturday.bind(on_press=self.saturday_btn)
        self.delete_grid.add_widget(self.saturday)

        self.delete_grid.pos_hint = {"top": 1}
        self.delete_page.add_widget(self.delete_grid)


#bottom row consisting of main menu button, a text input, and delete button
        self.bottom_row = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)

        self.left_col = GridLayout(rows=2)

        self.title_del_row = GridLayout(cols=3)
        self.title_label = Label(text="Title")
        self.title_del_row.add_widget(self.title_label)

        self.input_title = TextInput(width=Window.size[0]*0.6, size_hint_x=None)
        self.title_del_row.add_widget(self.input_title)

        self.left_col.add_widget(self.title_del_row)

        self.time_del_row = GridLayout(cols=3)
        self.time_label = Label(text="Time")
        self.time_del_row.add_widget(self.time_label)

        self.input_time = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.time_del_row.add_widget(self.input_time)
        self.left_col.add_widget(self.time_del_row)

        self.del_button = Button(text="Delete", width=Window.size[0] * 0.2, size_hint_x=None)
        self.del_button.bind(on_press=self.del_data)  # the del_button is binded to do an event

        self.bottom_row.add_widget(self.left_col)
        self.bottom_row.add_widget(self.del_button)
        self.delete_page.add_widget(self.bottom_row)

        self.add_widget(self.delete_page)


    def del_data(self, instance):
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        del_time_word = self.input_time.text
        del_title_word = self.input_title.text  # the title that is to be removed is saved to var
        cur.execute("""DELETE FROM planner WHERE title = ? AND time = ?""", (del_title_word, del_time_word,))
        con.commit()
        con.close()
        #self.input.text = ""

    def return_main(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

    def sunday_btn(self, instance):
        self.delete_page.clear_widgets()

        self.delete_page = FloatLayout()
        self.mygrid = GridLayout(cols=2, height=300)

        # layout for the buttons on top of the screen
        self.delete_grid = GridLayout(rows=2, cols=4, height=Window.size[1] * 0.1, size_hint_y=None)

        self.main_menu = Button(text="Main Menu", font_size=10)
        self.main_menu.bind(on_press=self.return_main)
        self.delete_grid.add_widget(self.main_menu)

        self.sunday = Button(text="Sunday", font_size=10)
        self.sunday.bind(on_press=self.sunday_btn)
        self.delete_grid.add_widget(self.sunday)

        self.monday = Button(text="Monday", font_size=10)
        self.monday.bind(on_press=self.monday_btn)
        self.delete_grid.add_widget(self.monday)

        self.tuesday = Button(text="Tuesday", font_size=10)
        self.tuesday.bind(on_press=self.tuesday_btn)
        self.delete_grid.add_widget(self.tuesday)

        self.wednesday = Button(text="Wednesday", font_size=10)
        self.wednesday.bind(on_press=self.wednesday_btn)
        self.delete_grid.add_widget(self.wednesday)

        self.thursday = Button(text="Thursday", font_size=10)
        self.thursday.bind(on_press=self.thursday_btn)
        self.delete_grid.add_widget(self.thursday)

        self.friday = Button(text="Friday", font_size=10)
        self.friday.bind(on_press=self.friday_btn)
        self.delete_grid.add_widget(self.friday)

        self.saturday = Button(text="Saturday", font_size=10)
        self.saturday.bind(on_press=self.saturday_btn)
        self.delete_grid.add_widget(self.saturday)

        self.delete_grid.pos_hint = {"top": 1}
        self.delete_page.add_widget(self.delete_grid)

        self.mygrid.pos_hint = {"top": 0.9}
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Sunday' """)
        row = cur.fetchall()
        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.mygrid.add_widget(self.row)
            self.mygrid.add_widget(self.another_row)

        self.delete_page.add_widget(self.mygrid)
        con.commit()
        con.close()

        self.bottom_row = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)

        self.left_col = GridLayout(rows=2)

        self.title_del_row = GridLayout(cols=3)
        self.title_label = Label(text="Title")
        self.title_del_row.add_widget(self.title_label)

        self.input_title = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.title_del_row.add_widget(self.input_title)

        self.left_col.add_widget(self.title_del_row)

        self.time_del_row = GridLayout(cols=3)
        self.time_label = Label(text="Time")
        self.time_del_row.add_widget(self.time_label)

        self.input_time = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.time_del_row.add_widget(self.input_time)
        self.left_col.add_widget(self.time_del_row)

        self.del_button = Button(text="Delete", width=Window.size[0] * 0.2, size_hint_x=None)
        self.del_button.bind(on_press=self.del_data)  # the del_button is binded to do an event

        self.bottom_row.add_widget(self.left_col)
        self.bottom_row.add_widget(self.del_button)
        self.delete_page.add_widget(self.bottom_row)

        self.add_widget(self.delete_page)

    def monday_btn(self, instance):
        self.delete_page.clear_widgets()

        self.delete_page = FloatLayout()
        self.mygrid = GridLayout(cols=2, height=300)

        # layout for the buttons on top of the screen
        self.delete_grid = GridLayout(rows=2, cols=4, height=Window.size[1] * 0.1, size_hint_y=None)

        self.main_menu = Button(text="Main Menu", font_size=10)
        self.main_menu.bind(on_press=self.return_main)
        self.delete_grid.add_widget(self.main_menu)

        self.sunday = Button(text="Sunday", font_size=10)
        self.sunday.bind(on_press=self.sunday_btn)
        self.delete_grid.add_widget(self.sunday)

        self.monday = Button(text="Monday", font_size=10)
        self.monday.bind(on_press=self.monday_btn)
        self.delete_grid.add_widget(self.monday)

        self.tuesday = Button(text="Tuesday", font_size=10)
        self.tuesday.bind(on_press=self.tuesday_btn)
        self.delete_grid.add_widget(self.tuesday)

        self.wednesday = Button(text="Wednesday", font_size=10)
        self.wednesday.bind(on_press=self.wednesday_btn)
        self.delete_grid.add_widget(self.wednesday)

        self.thursday = Button(text="Thursday", font_size=10)
        self.thursday.bind(on_press=self.thursday_btn)
        self.delete_grid.add_widget(self.thursday)

        self.friday = Button(text="Friday", font_size=10)
        self.friday.bind(on_press=self.friday_btn)
        self.delete_grid.add_widget(self.friday)

        self.saturday = Button(text="Saturday", font_size=10)
        self.saturday.bind(on_press=self.saturday_btn)
        self.delete_grid.add_widget(self.saturday)

        self.delete_grid.pos_hint = {"top": 1}
        self.delete_page.add_widget(self.delete_grid)

        self.mygrid.pos_hint = {"top": 0.9}
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Monday' """)
        row = cur.fetchall()
        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.mygrid.add_widget(self.row)
            self.mygrid.add_widget(self.another_row)
        self.delete_page.add_widget(self.mygrid)
        con.commit()
        con.close()

        self.bottom_row = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)

        self.left_col = GridLayout(rows=2)

        self.title_del_row = GridLayout(cols=3)
        self.title_label = Label(text="Title")
        self.title_del_row.add_widget(self.title_label)

        self.input_title = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.title_del_row.add_widget(self.input_title)

        self.left_col.add_widget(self.title_del_row)

        self.time_del_row = GridLayout(cols=3)
        self.time_label = Label(text="Time")
        self.time_del_row.add_widget(self.time_label)

        self.input_time = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.time_del_row.add_widget(self.input_time)
        self.left_col.add_widget(self.time_del_row)

        self.del_button = Button(text="Delete", width=Window.size[0] * 0.2, size_hint_x=None)
        self.del_button.bind(on_press=self.del_data)  # the del_button is binded to do an event

        self.bottom_row.add_widget(self.left_col)
        self.bottom_row.add_widget(self.del_button)
        self.delete_page.add_widget(self.bottom_row)

        self.add_widget(self.delete_page)

    def tuesday_btn(self, instance):
        self.delete_page.clear_widgets()

        self.delete_page = FloatLayout()
        self.mygrid = GridLayout(cols=2, height=300)

        # layout for the buttons on top of the screen
        self.delete_grid = GridLayout(rows=2, cols=4, height=Window.size[1] * 0.1, size_hint_y=None)

        self.main_menu = Button(text="Main Menu", font_size=10)
        self.main_menu.bind(on_press=self.return_main)
        self.delete_grid.add_widget(self.main_menu)

        self.sunday = Button(text="Sunday", font_size=10)
        self.sunday.bind(on_press=self.sunday_btn)
        self.delete_grid.add_widget(self.sunday)

        self.monday = Button(text="Monday", font_size=10)
        self.monday.bind(on_press=self.monday_btn)
        self.delete_grid.add_widget(self.monday)

        self.tuesday = Button(text="Tuesday", font_size=10)
        self.tuesday.bind(on_press=self.tuesday_btn)
        self.delete_grid.add_widget(self.tuesday)

        self.wednesday = Button(text="Wednesday", font_size=10)
        self.wednesday.bind(on_press=self.wednesday_btn)
        self.delete_grid.add_widget(self.wednesday)

        self.thursday = Button(text="Thursday", font_size=10)
        self.thursday.bind(on_press=self.thursday_btn)
        self.delete_grid.add_widget(self.thursday)

        self.friday = Button(text="Friday", font_size=10)
        self.friday.bind(on_press=self.friday_btn)
        self.delete_grid.add_widget(self.friday)

        self.saturday = Button(text="Saturday", font_size=10)
        self.saturday.bind(on_press=self.saturday_btn)
        self.delete_grid.add_widget(self.saturday)

        self.delete_grid.pos_hint = {"top": 1}
        self.delete_page.add_widget(self.delete_grid)

        self.mygrid.pos_hint = {"top": 0.9}
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Tuesday' """)
        row = cur.fetchall()
        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.mygrid.add_widget(self.row)
            self.mygrid.add_widget(self.another_row)
        self.delete_page.add_widget(self.mygrid)
        con.commit()
        con.close()

        self.bottom_row = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)

        self.left_col = GridLayout(rows=2)

        self.title_del_row = GridLayout(cols=3)
        self.title_label = Label(text="Title")
        self.title_del_row.add_widget(self.title_label)

        self.input_title = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.title_del_row.add_widget(self.input_title)

        self.left_col.add_widget(self.title_del_row)

        self.time_del_row = GridLayout(cols=3)
        self.time_label = Label(text="Time")
        self.time_del_row.add_widget(self.time_label)

        self.input_time = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.time_del_row.add_widget(self.input_time)
        self.left_col.add_widget(self.time_del_row)

        self.del_button = Button(text="Delete", width=Window.size[0] * 0.2, size_hint_x=None)
        self.del_button.bind(on_press=self.del_data)  # the del_button is binded to do an event

        self.bottom_row.add_widget(self.left_col)
        self.bottom_row.add_widget(self.del_button)
        self.delete_page.add_widget(self.bottom_row)

        self.add_widget(self.delete_page)

    def wednesday_btn(self, instance):
        self.delete_page.clear_widgets()

        self.delete_page = FloatLayout()
        self.mygrid = GridLayout(cols=2, height=300)

        # layout for the buttons on top of the screen
        self.delete_grid = GridLayout(rows=2, cols=4, height=Window.size[1] * 0.1, size_hint_y=None)

        self.main_menu = Button(text="Main Menu", font_size=10)
        self.main_menu.bind(on_press=self.return_main)
        self.delete_grid.add_widget(self.main_menu)

        self.sunday = Button(text="Sunday", font_size=10)
        self.sunday.bind(on_press=self.sunday_btn)
        self.delete_grid.add_widget(self.sunday)

        self.monday = Button(text="Monday", font_size=10)
        self.monday.bind(on_press=self.monday_btn)
        self.delete_grid.add_widget(self.monday)

        self.tuesday = Button(text="Tuesday", font_size=10)
        self.tuesday.bind(on_press=self.tuesday_btn)
        self.delete_grid.add_widget(self.tuesday)

        self.wednesday = Button(text="Wednesday", font_size=10)
        self.wednesday.bind(on_press=self.wednesday_btn)
        self.delete_grid.add_widget(self.wednesday)

        self.thursday = Button(text="Thursday", font_size=10)
        self.thursday.bind(on_press=self.thursday_btn)
        self.delete_grid.add_widget(self.thursday)

        self.friday = Button(text="Friday", font_size=10)
        self.friday.bind(on_press=self.friday_btn)
        self.delete_grid.add_widget(self.friday)

        self.saturday = Button(text="Saturday", font_size=10)
        self.saturday.bind(on_press=self.saturday_btn)
        self.delete_grid.add_widget(self.saturday)

        self.delete_grid.pos_hint = {"top": 1}
        self.delete_page.add_widget(self.delete_grid)

        self.mygrid.pos_hint = {"top": 0.9}
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Wednesday' """)
        row = cur.fetchall()
        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.mygrid.add_widget(self.row)
            self.mygrid.add_widget(self.another_row)
        self.delete_page.add_widget(self.mygrid)
        con.commit()
        con.close()

        self.bottom_row = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)

        self.left_col = GridLayout(rows=2)

        self.title_del_row = GridLayout(cols=3)
        self.title_label = Label(text="Title")
        self.title_del_row.add_widget(self.title_label)

        self.input_title = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.title_del_row.add_widget(self.input_title)

        self.left_col.add_widget(self.title_del_row)

        self.time_del_row = GridLayout(cols=3)
        self.time_label = Label(text="Time")
        self.time_del_row.add_widget(self.time_label)

        self.input_time = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.time_del_row.add_widget(self.input_time)
        self.left_col.add_widget(self.time_del_row)

        self.del_button = Button(text="Delete", width=Window.size[0] * 0.2, size_hint_x=None)
        self.del_button.bind(on_press=self.del_data)  # the del_button is binded to do an event

        self.bottom_row.add_widget(self.left_col)
        self.bottom_row.add_widget(self.del_button)
        self.delete_page.add_widget(self.bottom_row)

        self.add_widget(self.delete_page)

    def thursday_btn(self, instance):
        self.delete_page.clear_widgets()

        self.delete_page = FloatLayout()
        self.mygrid = GridLayout(cols=2, height=300)

        # layout for the buttons on top of the screen
        self.delete_grid = GridLayout(rows=2, cols=4, height=Window.size[1] * 0.1, size_hint_y=None)

        self.main_menu = Button(text="Main Menu", font_size=10)
        self.main_menu.bind(on_press=self.return_main)
        self.delete_grid.add_widget(self.main_menu)

        self.sunday = Button(text="Sunday", font_size=10)
        self.sunday.bind(on_press=self.sunday_btn)
        self.delete_grid.add_widget(self.sunday)

        self.monday = Button(text="Monday", font_size=10)
        self.monday.bind(on_press=self.monday_btn)
        self.delete_grid.add_widget(self.monday)

        self.tuesday = Button(text="Tuesday", font_size=10)
        self.tuesday.bind(on_press=self.tuesday_btn)
        self.delete_grid.add_widget(self.tuesday)

        self.wednesday = Button(text="Wednesday", font_size=10)
        self.wednesday.bind(on_press=self.wednesday_btn)
        self.delete_grid.add_widget(self.wednesday)

        self.thursday = Button(text="Thursday", font_size=10)
        self.thursday.bind(on_press=self.thursday_btn)
        self.delete_grid.add_widget(self.thursday)

        self.friday = Button(text="Friday", font_size=10)
        self.friday.bind(on_press=self.friday_btn)
        self.delete_grid.add_widget(self.friday)

        self.saturday = Button(text="Saturday", font_size=10)
        self.saturday.bind(on_press=self.saturday_btn)
        self.delete_grid.add_widget(self.saturday)

        self.delete_grid.pos_hint = {"top": 1}
        self.delete_page.add_widget(self.delete_grid)

        self.mygrid.pos_hint = {"top": 0.9}
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Thursday' """)
        row = cur.fetchall()
        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.mygrid.add_widget(self.row)
            self.mygrid.add_widget(self.another_row)
        self.delete_page.add_widget(self.mygrid)
        con.commit()
        con.close()

        self.bottom_row = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)

        self.left_col = GridLayout(rows=2)

        self.title_del_row = GridLayout(cols=3)
        self.title_label = Label(text="Title")
        self.title_del_row.add_widget(self.title_label)

        self.input_title = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.title_del_row.add_widget(self.input_title)

        self.left_col.add_widget(self.title_del_row)

        self.time_del_row = GridLayout(cols=3)
        self.time_label = Label(text="Time")
        self.time_del_row.add_widget(self.time_label)

        self.input_time = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.time_del_row.add_widget(self.input_time)
        self.left_col.add_widget(self.time_del_row)

        self.del_button = Button(text="Delete", width=Window.size[0] * 0.2, size_hint_x=None)
        self.del_button.bind(on_press=self.del_data)  # the del_button is binded to do an event

        self.bottom_row.add_widget(self.left_col)
        self.bottom_row.add_widget(self.del_button)
        self.delete_page.add_widget(self.bottom_row)

        self.add_widget(self.delete_page)

    def friday_btn(self, instance):
        self.delete_page.clear_widgets()

        self.delete_page = FloatLayout()
        self.mygrid = GridLayout(cols=2, height=300)

        # layout for the buttons on top of the screen
        self.delete_grid = GridLayout(rows=2, cols=4, height=Window.size[1] * 0.1, size_hint_y=None)

        self.main_menu = Button(text="Main Menu", font_size=10)
        self.main_menu.bind(on_press=self.return_main)
        self.delete_grid.add_widget(self.main_menu)

        self.sunday = Button(text="Sunday", font_size=10)
        self.sunday.bind(on_press=self.sunday_btn)
        self.delete_grid.add_widget(self.sunday)

        self.monday = Button(text="Monday", font_size=10)
        self.monday.bind(on_press=self.monday_btn)
        self.delete_grid.add_widget(self.monday)

        self.tuesday = Button(text="Tuesday", font_size=10)
        self.tuesday.bind(on_press=self.tuesday_btn)
        self.delete_grid.add_widget(self.tuesday)

        self.wednesday = Button(text="Wednesday", font_size=10)
        self.wednesday.bind(on_press=self.wednesday_btn)
        self.delete_grid.add_widget(self.wednesday)

        self.thursday = Button(text="Thursday", font_size=10)
        self.thursday.bind(on_press=self.thursday_btn)
        self.delete_grid.add_widget(self.thursday)

        self.friday = Button(text="Friday", font_size=10)
        self.friday.bind(on_press=self.friday_btn)
        self.delete_grid.add_widget(self.friday)

        self.saturday = Button(text="Saturday", font_size=10)
        self.saturday.bind(on_press=self.saturday_btn)
        self.delete_grid.add_widget(self.saturday)

        self.delete_grid.pos_hint = {"top": 1}
        self.delete_page.add_widget(self.delete_grid)

        self.mygrid.pos_hint = {"top": 0.9}
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Friday' """)
        row = cur.fetchall()
        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.mygrid.add_widget(self.row)
            self.mygrid.add_widget(self.another_row)
        self.delete_page.add_widget(self.mygrid)
        con.commit()
        con.close()

        self.bottom_row = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)

        self.left_col = GridLayout(rows=2)

        self.title_del_row = GridLayout(cols=3)
        self.title_label = Label(text="Title")
        self.title_del_row.add_widget(self.title_label)

        self.input_title = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.title_del_row.add_widget(self.input_title)

        self.left_col.add_widget(self.title_del_row)

        self.time_del_row = GridLayout(cols=3)
        self.time_label = Label(text="Time")
        self.time_del_row.add_widget(self.time_label)

        self.input_time = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.time_del_row.add_widget(self.input_time)
        self.left_col.add_widget(self.time_del_row)

        self.del_button = Button(text="Delete", width=Window.size[0] * 0.2, size_hint_x=None)
        self.del_button.bind(on_press=self.del_data)  # the del_button is binded to do an event

        self.bottom_row.add_widget(self.left_col)
        self.bottom_row.add_widget(self.del_button)
        self.delete_page.add_widget(self.bottom_row)

        self.add_widget(self.delete_page)

    def saturday_btn(self, instance):
        self.delete_page.clear_widgets()

        self.delete_page = FloatLayout()
        self.mygrid = GridLayout(cols=2, height=300)

        # layout for the buttons on top of the screen
        self.delete_grid = GridLayout(rows=2, cols=4, height=Window.size[1] * 0.1, size_hint_y=None)

        self.main_menu = Button(text="Main Menu", font_size=10)
        self.main_menu.bind(on_press=self.return_main)
        self.delete_grid.add_widget(self.main_menu)

        self.sunday = Button(text="Sunday", font_size=10)
        self.sunday.bind(on_press=self.sunday_btn)
        self.delete_grid.add_widget(self.sunday)

        self.monday = Button(text="Monday", font_size=10)
        self.monday.bind(on_press=self.monday_btn)
        self.delete_grid.add_widget(self.monday)

        self.tuesday = Button(text="Tuesday", font_size=10)
        self.tuesday.bind(on_press=self.tuesday_btn)
        self.delete_grid.add_widget(self.tuesday)

        self.wednesday = Button(text="Wednesday", font_size=10)
        self.wednesday.bind(on_press=self.wednesday_btn)
        self.delete_grid.add_widget(self.wednesday)

        self.thursday = Button(text="Thursday", font_size=10)
        self.thursday.bind(on_press=self.thursday_btn)
        self.delete_grid.add_widget(self.thursday)

        self.friday = Button(text="Friday", font_size=10)
        self.friday.bind(on_press=self.friday_btn)
        self.delete_grid.add_widget(self.friday)

        self.saturday = Button(text="Saturday", font_size=10)
        self.saturday.bind(on_press=self.saturday_btn)
        self.delete_grid.add_widget(self.saturday)

        self.delete_grid.pos_hint = {"top": 1}
        self.delete_page.add_widget(self.delete_grid)

        self.mygrid.pos_hint = {"top": 0.9}
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Saturday' """)
        row = cur.fetchall()
        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.mygrid.add_widget(self.row)
            self.mygrid.add_widget(self.another_row)
        self.delete_page.add_widget(self.mygrid)
        con.commit()
        con.close()

        self.bottom_row = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)

        self.left_col = GridLayout(rows=2)

        self.title_del_row = GridLayout(cols=3)
        self.title_label = Label(text="Title")
        self.title_del_row.add_widget(self.title_label)

        self.input_title = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.title_del_row.add_widget(self.input_title)

        self.left_col.add_widget(self.title_del_row)

        self.time_del_row = GridLayout(cols=3)
        self.time_label = Label(text="Time")
        self.time_del_row.add_widget(self.time_label)

        self.input_time = TextInput(width=Window.size[0] * 0.6, size_hint_x=None)
        self.time_del_row.add_widget(self.input_time)
        self.left_col.add_widget(self.time_del_row)

        self.del_button = Button(text="Delete", width=Window.size[0] * 0.2, size_hint_x=None)
        self.del_button.bind(on_press=self.del_data)  # the del_button is binded to do an event

        self.bottom_row.add_widget(self.left_col)
        self.bottom_row.add_widget(self.del_button)
        self.delete_page.add_widget(self.bottom_row)

        self.add_widget(self.delete_page)

class Day(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_float = FloatLayout()

        self.bottom_grid = GridLayout(cols=3, height=Window.size[0] * 0.1, size_hint_y=None)

        self.button = Button(text="Go Back")
        self.button.bind(on_press=self.main_menu_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Delete Event")
        self.button.bind(on_press=self.del_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Add Event")
        self.button.bind(on_press=self.add_event_button)
        self.bottom_grid.add_widget(self.button)

        self.main_float.add_widget(self.bottom_grid)

        self.add_widget(self.main_float)


class Sunday(Day):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)

        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Sunday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

# moved refresh_title_grid to the top of the page
        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)

        self.connect_data()

    def connect_data(self):
        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Sunday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def refresh_data(self, instance):
        # Had trouble trying to be cute by deleting the widget with the data and calling the connect_data method but
        # but program would not run because of a problem I didn't know how to fix
        # so I ended up copying and pasting code from this class

        self.main_float.clear_widgets()

        self.main_float = FloatLayout()

        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Sunday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)

        self.bottom_grid = GridLayout(cols=3, height=Window.size[0] * 0.1, size_hint_y=None)
        # alter code so buttons alter size along with the window

        self.button = Button(text="Go Back")
        self.button.bind(on_press=self.main_menu_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Delete Event")
        self.button.bind(on_press=self.del_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Add Event")
        self.button.bind(on_press=self.add_event_button)
        self.bottom_grid.add_widget(self.button)
        self.main_float.add_widget(self.bottom_grid)


        self.add_widget(self.main_float)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Sunday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        print("Refreshed")
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def main_menu_button(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

    def del_button(self, instance):
        main_app.root.current = "delete_page"
        main_app.root.transition.direction = "left"

    def add_event_button(self, instance):
        main_app.root.current = "schedule"



class SundaySchedule(Screen):
    day = "Sunday"
    title = ObjectProperty(None)
    time = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mygrid = GridLayout(rows=2)

#gridlayout for whole page
        self.title_time_grid = GridLayout(rows=2, cols=2, height=Window.size[1]*0.9, size_hint_y=None)

#gridlayout for the title and time sections
        self.title = Label(text="Title", font_size=30)
        self.title_time_grid.add_widget(self.title)
        self.title_input = TextInput()
        self.title_time_grid.add_widget(self.title_input)

        self.time = Label(text="Time", font_size=30)
        self.title_time_grid.add_widget(self.time)
        self.time_input = TextInput()
        self.title_time_grid.add_widget(self.time_input)

        self.mygrid.add_widget(self.title_time_grid)

#gridlayout for the back and submit buttons
        self.bottom_row = GridLayout(rows=1, cols=2)

        self.back_button = Button(text="Back")
        self.back_button.bind(on_press=self.return_main)
        self.bottom_row.add_widget(self.back_button)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.add_data)
        self.bottom_row.add_widget(self.submit)

        self.mygrid.add_widget(self.bottom_row)

        self.add_widget(self.mygrid)

    def display_data(self, title, time):
        title = self.title_input.text
        time = self.time_input.text

        print(f"{title}:{time}")

    def add_data(self, instance):
        title = self.title_input.text
        time = self.time_input.text

        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" INSERT INTO planner (day,title,time) VALUES(?,?,?)""",
                    (self.day, title, time)
                    )

        con.commit()
        con.close()

        self.display_data(title, time)
        self.time_input.text = ""
        self.title_input.text = ""

    def return_main(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

        # create an if else statement with boolean after pressing the submit button
        # if pressed, a screen of confirmation will appear


class Monday(Day):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Monday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.connect_data()

    def connect_data(self):
        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Monday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def refresh_data(self, instance):
        # Had trouble trying to be cute by deleting the widget with the data and calling the connect_data method but
        # but program would not run because of a problem I didn't know how to fix
        # so I ended up copying and pasting code from this class

        self.main_float.clear_widgets()

        self.main_float = FloatLayout()

        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Monday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)

        self.bottom_grid = GridLayout(cols=3, height=Window.size[0] * 0.1, size_hint_y=None)
        # alter code so buttons alter size along with the window

        self.button = Button(text="Go Back")
        self.button.bind(on_press=self.main_menu_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Delete Event")
        self.button.bind(on_press=self.del_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Add Event")
        self.button.bind(on_press=self.add_event_button)
        self.bottom_grid.add_widget(self.button)
        self.main_float.add_widget(self.bottom_grid)

        self.add_widget(self.main_float)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Monday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        print("Refreshed")
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def main_menu_button(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

    def del_button(self, instance):
        main_app.root.current = "delete_page"
        main_app.root.transition.direction = "left"

    def add_event_button(self, instance):
        main_app.root.current = "monday_schedule"


class MondaySchedule(Screen):
    monday = "Monday"
    title = ObjectProperty(None)
    time = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mygrid = GridLayout(rows=2)

        # gridlayout for whole page
        self.title_time_grid = GridLayout(rows=2, cols=2, height=Window.size[1] * 0.9, size_hint_y=None)

        # gridlayout for the title and time sections
        self.title = Label(text="Title", font_size=30)
        self.title_time_grid.add_widget(self.title)
        self.title_input = TextInput()
        self.title_time_grid.add_widget(self.title_input)

        self.time = Label(text="Time", font_size=30)
        self.title_time_grid.add_widget(self.time)
        self.time_input = TextInput()
        self.title_time_grid.add_widget(self.time_input)

        self.mygrid.add_widget(self.title_time_grid)

        # gridlayout for the back and submit buttons
        self.bottom_row = GridLayout(rows=1, cols=2)

        self.back_button = Button(text="Back")
        self.back_button.bind(on_press=self.return_main)
        self.bottom_row.add_widget(self.back_button)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.monday_add_data)
        self.bottom_row.add_widget(self.submit)

        self.mygrid.add_widget(self.bottom_row)

        self.add_widget(self.mygrid)

    def display_data(self, title, time):
        title = self.title_input.text
        time = self.time_input.text


        print(f"{title}:{time}")

    def monday_add_data(self, instance):
        title = self.title_input.text
        time = self.time_input.text


        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" INSERT INTO planner (day,title,time) VALUES(?,?,?)""",
                    (self.monday, title, time,)
                    )

        con.commit()
        con.close()

        self.display_data(title, time)
        self.time_input.text = ""
        self.title_input.text = ""

    def return_main(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

        # create an if else statement with boolean after pressing the submit button
        # if pressed, a screen of confirmation will appear


class Tuesday(Day):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Tuesday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.connect_data()

    def connect_data(self):
        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Tuesday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def refresh_data(self, instance):
        # Had trouble trying to be cute by deleting the widget with the data and calling the connect_data method but
        # but program would not run because of a problem I didn't know how to fix
        # so I ended up copying and pasting code from this class

        self.main_float.clear_widgets()

        self.main_float = FloatLayout()

        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Tuesday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)

        self.bottom_grid = GridLayout(cols=3, height=Window.size[0] * 0.1, size_hint_y=None)
        # alter code so buttons alter size along with the window

        self.button = Button(text="Go Back")
        self.button.bind(on_press=self.main_menu_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Delete Event")
        self.button.bind(on_press=self.del_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Add Event")
        self.button.bind(on_press=self.add_event_button)
        self.bottom_grid.add_widget(self.button)
        self.main_float.add_widget(self.bottom_grid)

        self.add_widget(self.main_float)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Tuesday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        print("Refreshed")
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def main_menu_button(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

    def del_button(self, instance):
        main_app.root.current = "delete_page"
        main_app.root.transition.direction = "left"

    def add_event_button(self, instance):
        main_app.root.current = "tuesday_schedule"


class TuesdaySchedule(Screen):
    day = "Tuesday"
    title = ObjectProperty(None)
    time = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mygrid = GridLayout(rows=2)

        # gridlayout for whole page
        self.title_time_grid = GridLayout(rows=2, cols=2, height=Window.size[1] * 0.9, size_hint_y=None)

        # gridlayout for the title and time sections
        self.title = Label(text="Title", font_size=30)
        self.title_time_grid.add_widget(self.title)
        self.title_input = TextInput()
        self.title_time_grid.add_widget(self.title_input)

        self.time = Label(text="Time", font_size=30)
        self.title_time_grid.add_widget(self.time)
        self.time_input = TextInput()
        self.title_time_grid.add_widget(self.time_input)

        self.mygrid.add_widget(self.title_time_grid)

        # gridlayout for the back and submit buttons
        self.bottom_row = GridLayout(rows=1, cols=2)

        self.back_button = Button(text="Back")
        self.back_button.bind(on_press=self.return_main)
        self.bottom_row.add_widget(self.back_button)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.add_data)
        self.bottom_row.add_widget(self.submit)

        self.mygrid.add_widget(self.bottom_row)

        self.add_widget(self.mygrid)

    def display_data(self, title, time):
        title = self.title_input.text
        time = self.time_input.text

        print(f"{title}:{time}")

    def add_data(self, instance):
        title = self.title_input.text
        time = self.time_input.text

        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" INSERT INTO planner (day,title,time) VALUES(?,?,?)""",
                    (self.day, title, time)
                    )

        con.commit()
        con.close()

        self.display_data(title, time)
        self.time_input.text = ""
        self.title_input.text = ""

    def return_main(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

        # create an if else statement with boolean after pressing the submit button
        # if pressed, a screen of confirmation will appear


class Wednesday(Day):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Wednesday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.connect_data()

    def connect_data(self):
        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Wednesday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def refresh_data(self, instance):
        # Had trouble trying to be cute by deleting the widget with the data and calling the connect_data method but
        # but program would not run because of a problem I didn't know how to fix
        # so I ended up copying and pasting code from this class

        self.main_float.clear_widgets()

        self.main_float = FloatLayout()

        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Wednesday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)

        self.bottom_grid = GridLayout(cols=3, height=Window.size[0] * 0.1, size_hint_y=None)
        # alter code so buttons alter size along with the window

        self.button = Button(text="Go Back")
        self.button.bind(on_press=self.main_menu_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Delete Event")
        self.button.bind(on_press=self.del_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Add Event")
        self.button.bind(on_press=self.add_event_button)
        self.bottom_grid.add_widget(self.button)
        self.main_float.add_widget(self.bottom_grid)

        self.add_widget(self.main_float)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Wednesday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        print("Refreshed")
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def main_menu_button(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

    def del_button(self, instance):
        main_app.root.current = "delete_page"
        main_app.root.transition.direction = "left"

    def add_event_button(self, instance):
        main_app.root.current = "wednesday_schedule"


class WednesdaySchedule(Screen):
    day = "Wednesday"
    title = ObjectProperty(None)
    time = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mygrid = GridLayout(rows=2)

        # gridlayout for whole page
        self.title_time_grid = GridLayout(rows=2, cols=2, height=Window.size[1] * 0.9, size_hint_y=None)

        # gridlayout for the title and time sections
        self.title = Label(text="Title", font_size=30)
        self.title_time_grid.add_widget(self.title)
        self.title_input = TextInput()
        self.title_time_grid.add_widget(self.title_input)

        self.time = Label(text="Time", font_size=30)
        self.title_time_grid.add_widget(self.time)
        self.time_input = TextInput()
        self.title_time_grid.add_widget(self.time_input)

        self.mygrid.add_widget(self.title_time_grid)

        # gridlayout for the back and submit buttons
        self.bottom_row = GridLayout(rows=1, cols=2)

        self.back_button = Button(text="Back")
        self.back_button.bind(on_press=self.return_main)
        self.bottom_row.add_widget(self.back_button)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.add_data)
        self.bottom_row.add_widget(self.submit)

        self.mygrid.add_widget(self.bottom_row)

        self.add_widget(self.mygrid)

    def display_data(self, title, time):
        title = self.title_input.text
        time = self.time_input.text

        print(f"{title}:{time}")

    def add_data(self, instance):
        title = self.title_input.text
        time = self.time_input.text

        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" INSERT INTO planner (day,title,time) VALUES(?,?,?)""",
                    (self.day, title, time)
                    )

        con.commit()
        con.close()

        self.display_data(title, time)
        self.time_input.text = ""
        self.title_input.text = ""

    def return_main(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

        # create an if else statement with boolean after pressing the submit button
        # if pressed, a screen of confirmation will appear


class Thursday(Day):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Thursday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.connect_data()

    def connect_data(self):
        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Thursday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def refresh_data(self, instance):
        # Had trouble trying to be cute by deleting the widget with the data and calling the connect_data method but
        # but program would not run because of a problem I didn't know how to fix
        # so I ended up copying and pasting code from this class

        self.main_float.clear_widgets()

        self.main_float = FloatLayout()

        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Thursday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)

        self.bottom_grid = GridLayout(cols=3, height=Window.size[0] * 0.1, size_hint_y=None)
        # alter code so buttons alter size along with the window

        self.button = Button(text="Go Back")
        self.button.bind(on_press=self.main_menu_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Delete Event")
        self.button.bind(on_press=self.del_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Add Event")
        self.button.bind(on_press=self.add_event_button)
        self.bottom_grid.add_widget(self.button)
        self.main_float.add_widget(self.bottom_grid)

        self.add_widget(self.main_float)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Thursday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        print("Refreshed")
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def main_menu_button(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

    def del_button(self, instance):
        main_app.root.current = "delete_page"
        main_app.root.transition.direction = "left"

    def add_event_button(self, instance):
        main_app.root.current = "thursday_schedule"


class ThursdaySchedule(Screen):
    day = "Thursday"
    title = ObjectProperty(None)
    time = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mygrid = GridLayout(rows=2)

        # gridlayout for whole page
        self.title_time_grid = GridLayout(rows=2, cols=2, height=Window.size[1] * 0.9, size_hint_y=None)

        # gridlayout for the title and time sections
        self.title = Label(text="Title", font_size=30)
        self.title_time_grid.add_widget(self.title)
        self.title_input = TextInput()
        self.title_time_grid.add_widget(self.title_input)

        self.time = Label(text="Time", font_size=30)
        self.title_time_grid.add_widget(self.time)
        self.time_input = TextInput()
        self.title_time_grid.add_widget(self.time_input)

        self.mygrid.add_widget(self.title_time_grid)

        # gridlayout for the back and submit buttons
        self.bottom_row = GridLayout(rows=1, cols=2)

        self.back_button = Button(text="Back")
        self.back_button.bind(on_press=self.return_main)
        self.bottom_row.add_widget(self.back_button)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.add_data)
        self.bottom_row.add_widget(self.submit)

        self.mygrid.add_widget(self.bottom_row)

        self.add_widget(self.mygrid)

    def display_data(self, title, time):
        title = self.title_input.text
        time = self.time_input.text

        print(f"{title}:{time}")

    def add_data(self, instance):
        title = self.title_input.text
        time = self.time_input.text

        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" INSERT INTO planner (day,title,time) VALUES(?,?,?)""",
                    (self.day, title, time)
                    )

        con.commit()
        con.close()

        self.display_data(title, time)
        self.time_input.text = ""
        self.title_input.text = ""

    def return_main(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

        # create an if else statement with boolean after pressing the submit button
        # if pressed, a screen of confirmation will appear


class Friday(Day):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Friday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.connect_data()

    def connect_data(self):
        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Friday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def refresh_data(self, instance):
        # Had trouble trying to be cute by deleting the widget with the data and calling the connect_data method but
        # but program would not run because of a problem I didn't know how to fix
        # so I ended up copying and pasting code from this class

        self.main_float.clear_widgets()

        self.main_float = FloatLayout()

        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Friday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)

        self.bottom_grid = GridLayout(cols=3, height=Window.size[0] * 0.1, size_hint_y=None)
        # alter code so buttons alter size along with the window

        self.button = Button(text="Go Back")
        self.button.bind(on_press=self.main_menu_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Delete Event")
        self.button.bind(on_press=self.del_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Add Event")
        self.button.bind(on_press=self.add_event_button)
        self.bottom_grid.add_widget(self.button)
        self.main_float.add_widget(self.bottom_grid)

        self.add_widget(self.main_float)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Friday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        print("Refreshed")
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def main_menu_button(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

    def del_button(self, instance):
        main_app.root.current = "delete_page"
        main_app.root.transition.direction = "left"

    def add_event_button(self, instance):
        main_app.root.current = "friday_schedule"


class FridaySchedule(Screen):
    day = "Friday"
    title = ObjectProperty(None)
    time = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mygrid = GridLayout(rows=2)

        # gridlayout for whole page
        self.title_time_grid = GridLayout(rows=2, cols=2, height=Window.size[1] * 0.9, size_hint_y=None)

        # gridlayout for the title and time sections
        self.title = Label(text="Title", font_size=30)
        self.title_time_grid.add_widget(self.title)
        self.title_input = TextInput()
        self.title_time_grid.add_widget(self.title_input)

        self.time = Label(text="Time", font_size=30)
        self.title_time_grid.add_widget(self.time)
        self.time_input = TextInput()
        self.title_time_grid.add_widget(self.time_input)

        self.mygrid.add_widget(self.title_time_grid)

        # gridlayout for the back and submit buttons
        self.bottom_row = GridLayout(rows=1, cols=2)

        self.back_button = Button(text="Back")
        self.back_button.bind(on_press=self.return_main)
        self.bottom_row.add_widget(self.back_button)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.add_data)
        self.bottom_row.add_widget(self.submit)

        self.mygrid.add_widget(self.bottom_row)

        self.add_widget(self.mygrid)

    def display_data(self, title, time):
        title = self.title_input.text
        time = self.time_input.text

        print(f"{title}:{time}")

    def add_data(self, instance):
        title = self.title_input.text
        time = self.time_input.text

        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" INSERT INTO planner (day,title,time) VALUES(?,?,?)""",
                    (self.day, title, time)
                    )

        con.commit()
        con.close()

        self.display_data(title, time)
        self.time_input.text = ""
        self.title_input.text = ""

    def return_main(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

        # create an if else statement with boolean after pressing the submit button
        # if pressed, a screen of confirmation will appear


class Saturday(Day):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Saturday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.connect_data()

    def connect_data(self):
        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Saturday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def refresh_data(self, instance):
        # Had trouble trying to be cute by deleting the widget with the data and calling the connect_data method but
        # but program would not run because of a problem I didn't know how to fix
        # so I ended up copying and pasting code from this class

        self.main_float.clear_widgets()

        self.main_float = FloatLayout()

        self.refresh_title_grid = GridLayout(cols=2, height=Window.size[0] * 0.1, size_hint_y=None)
        self.refresh = Button(text="Refresh", size_hint_x=None, width=80)
        self.refresh.bind(on_press=self.refresh_data)
        self.refresh_title_grid.add_widget(self.refresh)

        self.title = Label(text="Saturday", font_size=40)
        self.refresh_title_grid.add_widget(self.title)

        self.refresh_title_grid.pos_hint = {'top': 1}
        self.main_float.add_widget(self.refresh_title_grid)

        self.mygrid = GridLayout(cols=2, height=Window.size[1] * 0.87, size_hint_y=None)
        self.list_of_events_grid = GridLayout(cols=2, height=Window.size[1] * 0.77, size_hint_y=None)

        self.bottom_grid = GridLayout(cols=3, height=Window.size[0] * 0.1, size_hint_y=None)
        # alter code so buttons alter size along with the window

        self.button = Button(text="Go Back")
        self.button.bind(on_press=self.main_menu_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Delete Event")
        self.button.bind(on_press=self.del_button)
        self.bottom_grid.add_widget(self.button)

        self.button = Button(text="Add Event")
        self.button.bind(on_press=self.add_event_button)
        self.bottom_grid.add_widget(self.button)
        self.main_float.add_widget(self.bottom_grid)

        self.add_widget(self.main_float)
        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" SELECT title, time FROM planner WHERE day = 'Saturday' """)
        row = cur.fetchall()

        for title, time in row:
            self.row = Label(text=str(time), font_size=20, size_hint_y=None, height=70)
            self.another_row = Label(text=str(title), font_size=20, size_hint_y=None, height=70)
            self.list_of_events_grid.add_widget(self.row)
            self.list_of_events_grid.add_widget(self.another_row)
        print("Refreshed")
        self.mygrid.add_widget(self.list_of_events_grid)
        self.main_float.add_widget(self.mygrid)
        con.commit()
        con.close()

    def main_menu_button(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

    def del_button(self, instance):
        main_app.root.current = "delete_page"
        main_app.root.transition.direction = "left"

    def add_event_button(self, instance):
        main_app.root.current = "saturday_schedule"


class SaturdaySchedule(Screen):
    day = "Saturday"
    title = ObjectProperty(None)
    time = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mygrid = GridLayout(rows=2)

        # gridlayout for whole page
        self.title_time_grid = GridLayout(rows=2, cols=2, height=Window.size[1] * 0.9, size_hint_y=None)

        # gridlayout for the title and time sections
        self.title = Label(text="Title", font_size=30)
        self.title_time_grid.add_widget(self.title)
        self.title_input = TextInput()
        self.title_time_grid.add_widget(self.title_input)

        self.time = Label(text="Time", font_size=30)
        self.title_time_grid.add_widget(self.time)
        self.time_input = TextInput()
        self.title_time_grid.add_widget(self.time_input)

        self.mygrid.add_widget(self.title_time_grid)

        # gridlayout for the back and submit buttons
        self.bottom_row = GridLayout(rows=1, cols=2)

        self.back_button = Button(text="Back")
        self.back_button.bind(on_press=self.return_main)
        self.bottom_row.add_widget(self.back_button)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.add_data)
        self.bottom_row.add_widget(self.submit)

        self.mygrid.add_widget(self.bottom_row)

        self.add_widget(self.mygrid)

    def display_data(self, title, time):
        title = self.title_input.text
        time = self.time_input.text

        print(f"{title}:{time}")

    def add_data(self, instance):
        title = self.title_input.text
        time = self.time_input.text

        con = sql.connect('planner_app.db')
        cur = con.cursor()
        # must define the variable as self.day
        cur.execute(""" INSERT INTO planner (day,title,time) VALUES(?,?,?)""",
                    (self.day, title, time)
                    )

        con.commit()
        con.close()

        self.display_data(title, time)
        self.time_input.text = ""
        self.title_input.text = ""

    def return_main(self, instance):
        main_app.root.current = "main"
        main_app.root.transition.direction = "right"

        # create an if else statement with boolean after pressing the submit button
        # if pressed, a screen of confirmation will appear


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("planner.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    main_app = MyMainApp()
    main_app.run()

