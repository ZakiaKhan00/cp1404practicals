"""
CP1404/CP5632 Practical
Create a KIVY app that dynamically adds labels based on a predefined list.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

__author__ = "Zakia Khan"

class DynamicLabelsApp(App):
    """Kivy app to dynamically add labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ['Bob', 'Jane', 'John', 'Donald', 'Smith']

    def build(self):
        """Build the KIVY program."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from the sample data."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

DynamicLabelsApp().run()