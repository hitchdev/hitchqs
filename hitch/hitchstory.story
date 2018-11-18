Hitchstory:
  about: |
    Create simple hitch folder with a key.py and
    hitchreqs in with hitchstory which runs a simple
    test that does nothing.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: hitchstory
      will output: Quickstart run successfully!
  - files appear:
      hitch/hitchreqs.in: |
        hitchstory
        pathquery
        hitchrun
      hitch/key.py: |
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
      hitch/engine.py: |
        from hitchstory import BaseEngine


        class Engine(BaseEngine):
            def __init__(self, paths):
                self.path = paths

            def set_up(self):
                pass

            def do_something(self):
                pass
      hitch/mystory.story: |
        My first story:
          steps:
          - Do something
