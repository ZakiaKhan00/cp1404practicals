"""
Programming Languages
Estimate: 30 mins
Actual:40 mins
"""

class ProgrammingLanguage:
    def __init__(self,name = "", typing = "", reflection = "", year = 0):
        """Initialise programming language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return true if programming language typing is Dynamic"""
        return self.typing == "Dynamic"