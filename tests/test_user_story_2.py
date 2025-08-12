from lib.user_story_2 import *
import pytest

# grammar_checker("Hello my name is Ben.") => "String grammar is correct."

def test_grammar_checker():
    assert grammar_checker("Hello my name is Ben.") == "String grammar is correct."


# grammar_checker("hello i am ben.") => "Missing starting capital letter."

def test_takes_a_lower_case_string_returns_error_string():
    assert grammar_checker("hello i am ben.") == "Missing starting capital letter."


# grammar_checker("Hello my name is ben") => "Missing ending punctuation mark."

def test_for_missing_punctuation_mark():
    assert grammar_checker("Hello my name is ben") == "Missing ending punctuation mark."


