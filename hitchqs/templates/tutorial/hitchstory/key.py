from hitchstory import exceptions, StoryCollection
from pathquery import pathquery
from engine import Engine
from hitchrun import DIR, expected


@expected(exceptions.HitchStoryException)
def bdd(*keywords):
    """
    Run story with name containing keywords.
    """
    StoryCollection(pathquery(DIR.key).ext("story"), Engine(DIR)).shortcut(*keywords).play()


@expected(exceptions.HitchStoryException)
def regression():
    """
    Run all stories
    """
    StoryCollection(pathquery(DIR.key).ext("story"), Engine(DIR)).ordered_by_name().play()
