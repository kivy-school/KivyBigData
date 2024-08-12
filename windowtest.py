from kivy.app import runTouchApp
from kivy.lang import Builder
from kivy.core.window import Window

#this is to make the Kivy window always on top
Window.always_on_top = True
#set the window title
Window.set_title('Welcome to Kivy School!')

#kv language setting the main widget to be a button
kvString = '''
Button:
    text: "Hello world!"
'''

#run Kivy app
runTouchApp(Builder.load_string(kvString))