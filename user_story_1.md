
## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def reading_time_estimator(text):
    """
    Converts text string into an integer representing the word count.
    Takes the rate of 200 words a minute, and applies it to the total word count of text 
    to calculate how much time it would take to read

    Parameters: (list all parameters and their types)
        Text: a string 

    Returns: (state the return value and its type)
        an estimated amount of time it would take to read a piece of text (e.g. 1 hour 23 minutes)

    Side effects: (state any side effects)
        No side effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given 350 words
It returns a number representing the time in hours and minutes, to read 
the text of that size
"""
reading_time_estimator("350 WORD TEXT") => "1 hour 45 minutes"

def test_takes_350_returns_correct():
    assert reading_time_estimator("INSERT 350 WORD TEXT") == "1 hour 45 minutes"

"""
Given 100 words
It returns a number representing the time in hours and minutes, to read 
the text of that size
"""
reading_time_estimator("100 WORD TEXT") => [30 minutes]

def test_takes_100_returns_correct():
    assert reading_time_estimator("INSERT 100 WORD TEXT") == "30 minutes"


"""
Given no arguments
It returns a string saying "no word count given"
"""
reading_time_estimator() => "no word count given"

def test_returns_string_from_no_args():
    assert reading_time_estimator() == "no word count given"

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
