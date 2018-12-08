from hitchstory import exceptions, StoryCollection
from pathquery import pathquery
from engine import Engine
from hitchrun import DIR, expected


def _stories(engine):
    return StoryCollection(pathquery(DIR.project / "story").ext("story"), engine)


@expected(exceptions.HitchStoryException)
def bdd(*keywords):
    """
    Run story with name containing keywords.
    """
    _stories(Engine(DIR)).shortcut(*keywords).play()


@expected(exceptions.HitchStoryException)
def rbdd(*keywords):
    """
    Run story with name containing keywords and rewrite.
    """
    _stories(Engine(DIR, rewrite=True)).shortcut(*keywords).play()


@expected(exceptions.HitchStoryException)
def regression():
    """
    Run all stories.
    """
    _stories(Engine(DIR)).ordered_by_name().play()
