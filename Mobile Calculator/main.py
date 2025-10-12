from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ListProperty

# Optional: for testing on PC
Window.size = (360, 600)

class CalculatorLayout(BoxLayout):
    history_list = ListProperty([])

    def button_press(self, value):
        self.ids.input_box.text += str(value)

    def clear(self):
        self.ids.input_box.text = ""

    def backspace(self):
        self.ids.input_box.text = self.ids.input_box.text[:-1]

    def calculate(self):
        try:
            expression = self.ids.input_box.text
            # Handle % button
            if "%" in expression:
                expression = expression.replace("%", "/100")
            result = str(eval(expression))
            self.history_list.append(f"{expression} = {result}")
            self.ids.input_box.text = result
            self.update_history()
        except:
            self.ids.input_box.text = "Error"

    def update_history(self):
        self.ids.history_box.text = "\n".join(self.history_list[::-1])  # latest first

    def delete_history(self):
        self.history_list = []
        self.ids.history_box.text = ""
   

