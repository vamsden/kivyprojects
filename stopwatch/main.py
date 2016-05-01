# File: main.py
import kivy

from kivy.app import App
from kivy.core.text import LabelBase

from kivy.core.window import Window # background color
from kivy.utils import get_color_from_hex

from kivy.clock import Clock
from time import strftime


class ClockApp(App):
	def update_time(self, nap):
		self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

	def on_start(self):
		Clock.schedule_interval(self.update_time, 1)

if __name__ == "__main__":
	Window.clearcolor = get_color_from_hex('#e21826')
	LabelBase.register(name='Roboto',
		fn_regular='Roboto-Thin.ttf',
		fn_bold='Roboto-Medium.ttf')
	ClockApp().run()