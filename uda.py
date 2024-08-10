from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.clock import Clock

class MyWidget(BoxLayout):
    # Define a NumericProperty
    counter = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Create a button and bind its text property to the counter
        self.button = Button(text=str(self.counter))
        self.add_widget(self.button)
        
        # Bind the NumericProperty to update the button text
        self.bind(counter=self.update_button_text)
        
        # Schedule a function to update the counter property
        Clock.schedule_interval(self.increment_counter, 1)  # Update every 1 second

    def update_button_text(self, instance, value):
        # Update the button text when the counter property changes
        self.button.text = str(value)
        
    def increment_counter(self, dt):
        # Increment the counter
        self.counter += 1

class MyKivyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyKivyApp().run()
