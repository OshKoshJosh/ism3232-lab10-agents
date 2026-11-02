
# AI Assistance — Lab 10

I used ChatGPT to help generate, understand, and debug class definitions for this assignment.

## Class 1: GuitarLookup (my_tool.py)

### AI-Generated Code

```python
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
```

### My Line-by-Line Explanations

Write an explanation for each line of the class above, including why it is needed.

Things to explain:
- What `class GuitarLookup:` creates
- Why `__init__` accepts `guitars`
- Why `self.guitars = guitars` saves the catalog
- How the `for` loop searches through guitar names
- Why `.lower()` makes matching case-insensitive
- Why `return None` handles an unsuccessful search
- How `.get(guitar)` retrieves guitar details

Also explain what each docstring describes.
