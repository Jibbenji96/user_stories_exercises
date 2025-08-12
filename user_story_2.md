
## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def grammar_checker(text):
    """
    Checks an inputted string to check that it starts with a capital letter and ends with suitable sentence-ending punctuation mark which returns a string to describe what is missing.

    Parameters: (list all parameters and their types)
        Text: a string 

    Returns: (state the return value and its type)
        A string to describe what is missing.

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
Given a text with no starting capital letter
It returns a string saying it does not start with a capital letter.
"""
grammar_checker("hello i am ben.") => "Missing starting capital letter."

def test_takes_a_lower_case_string_returns_error_string():
    assert grammar_checker("hello i am ben.") == "Missing starting capital letter."

"""
Given a string without a finishing punctuation mark
It returns a string that explains that the inputted string is missing a punctuation mark.
"""
grammar_checker("Hello my name is ben") => "Missing ending punctuation mark."

def test_for_missing_punctuation_mark():
    assert grammar_checker("Hello my name is ben") == "Missing ending punctuation mark."


"""
Given a string with capital letter and punctuation mark.
"""
grammar_checker("Hello my name is Ben.") => "String grammar is correct."

def test_grammar_checker():
    assert grammar_checker("Hello my name is Ben.") == "String grammar is correct."

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
