# my_tool.py
# Author: Joshua Reddish


class GuitarLookup:
    """A tool that looks up guitars in a small shop catalog."""

    def __init__(self, guitars):
        """Save the guitar catalog for future lookups."""
        self.guitars = guitars

    def find_guitar(self, text):
        """Find a guitar model mentioned in a customer's message."""
        for guitar in self.guitars:
            if guitar.lower() in text.lower():
                return guitar
        return None

    def get_details(self, guitar):
        """Return the guitar's details, or None if it is unknown."""
        return self.guitars.get(guitar)
