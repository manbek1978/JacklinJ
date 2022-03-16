from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from datetime import datetime
from datetime import date


class JJ(App):
    def build(self):
        # returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        # image widget
        self.window.add_widget(Image(source="rm.png"))
        # label widget
        self.greeting = Label(
            text="Введите данные!",
            font_size=24,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting)
        # text input widget
        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            font_size=22,
            size_hint=(1, 0.5)
        )

        self.window.add_widget(self.user)
        # button widget
        self.button = Button(
            text="Вперёд >",
            size_hint=(1, 0.5),
            font_size=22,
            bold=True,
            background_color='#00FFCE',
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window


    def callback(self, instance):
        # change label text to "vvod + user text!"
        self.greeting.text = "Введено данные == " + self.user.text
        with open('inform.csv', 'r+', encoding='utf-8') as f:
            myDataList = f.readline()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(self.user.text)
                if self.user not in nameList:
                    now = datetime.now()
                    dt_string = now.strftime('  %H:%M  %d/%m/%Y')
                    f.writelines(f'\n{self.user.text}')
                    f.writelines(f'\n{dt_string}')
                    f.seek(0)
                    
 
if __name__ == "__main__":
    current_time = date.today()
    date_obj = date(2022, 12, 28)
    if current_time < date_obj:
        JJ().run()
 