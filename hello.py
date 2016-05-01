import kivy
kivy.require('1.9.1') # can be neglected but is a good practise

# Starting point of any application in kivy
from kivy.app import App # Imports App from kivy
from kivy.uix.button import Label # Imports Label

class HelloApp(App):
	def build(self):
		return Label(text='Hello World')

if __name__ ==  "__main__": # Reduces Complexity
	HelloApp().run() # Function call

# Run by --> python <script_name.py> --size=100x100 -< optional
# On mac kivy instead of python