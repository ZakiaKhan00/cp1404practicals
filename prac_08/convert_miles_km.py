"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = "Zakia Khan"

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    """Main app class for converting miles to kilometres."""
    result_text = StringProperty()

    def build(self):
        """Build the Kivy app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Convert the user entered miles to kilometres and update the output label."""
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.handle_update(miles)

    def handle_increment(self, text, change):
        """Handle Up/Down button press to adjust miles by the given change value."""
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.miles_input.text = str(miles)
        self.handle_update(miles)

    def convert_to_number(self, text):
        """Convert text input to a float, return 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0

    def handle_update(self, miles):
        """Update the result label."""
        print("update")
        self.result_text = str(miles * MILES_TO_KM)

MilesToKmApp().run()
