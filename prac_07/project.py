"""
Project class for Project Class Program
Estimate: 30 mins
Actual: 38 mins
"""
from datetime import datetime

FULL_COMPLETION = 100

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Create a new Project instance."""
        self.name = name
        self.start_date = start_date  # stored as string in dd/mm/yyyy format
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __lt__(self, other):
        """Enable sorting projects by priority."""
        return self.priority < other.priority

    def compare_start_date(self, other):
        """Return True if this project's start date is earlier than another's."""
        self_date = datetime.strptime(self.start_date, "%d/%m/%Y").date()
        other_date = datetime.strptime(other.start_date, "%d/%m/%Y").date()
        return self_date < other_date

    def is_complete(self):
        """Check if the project is finished (100% complete)."""
        return self.completion_percentage >= FULL_COMPLETION

    def __str__(self):
        """Return a nicely formatted summary of the project."""
        return (f"{self.name}, start: {self.start_date}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")