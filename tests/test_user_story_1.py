import pytest
from lib.user_story_1 import * 

def test_takes_100_returns_correct():
    assert reading_time_estimator("Software engineering is the disciplined application of engineering principles \n " \
    "to the design, development, testing, and maintenance of software systems. It combines technical expertise \n " \
    "with structured methodologies to create reliable, efficient, and scalable solutions. Key aspects include \n " \
    "requirements analysis, system design, coding, quality assurance, and project management. Software engineers \n " \
    "often work collaboratively, using tools like version control and agile practices to ensure adaptability and efficiency. \n " \
    "The field evolves rapidly, integrating emerging technologies such as artificial intelligence, cloud computing, and \n " \
    "cybersecurity. Ultimately, software engineering aims to deliver high-quality software that meets user needs, functions \n" \
    " correctly, and remains maintainable over time chocolate pony.") == "30 seconds"

def test_takes_100_returns_false():
    assert reading_time_estimator(100) == "Text string must be provided."

def test_returns_string_from_no_args():
    assert reading_time_estimator(None) == "no word count given"