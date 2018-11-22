Selenium Director:
  about: |
    Create simple hitch folder with a key.py and
    hitchreqs in with hitchstory which has a bunch of
    tests which show off the features of hitchstory.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: tutorial seleniumdirector
      will output: Quickstart run successfully!
  - files appear:
      hitch/hitchreqs.in: |
        hitchstory
        seleniumdirector
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
        from hitchstory import BaseEngine, no_stacktrace_for
        from seleniumdirector import WebDirector, SeleniumDirectorException
        from selenium import webdriver, WebDriverException


        class Engine(BaseEngine):
            def __init__(self, dirs):
                self.dirs = dirs

            def set_up(self):
                self._webdriver = webdriver.Chrome()
                self._director = WebDirector(
                    self.driver,
                    self.dirs.key / "selectors.yml",
                    default_timeout=5
                )

            @no_stacktrace_for(SeleniumDirectorException)
            def visit(self, url):
                self._director.visit("http://localhost:8000/{}".format(url))

            @no_stacktrace_for(SeleniumDirectorException)
            def expect_page(self, name):
                self._director.wait_for_page(name)

            @no_stacktrace_for(SeleniumDirectorException)
            def fill_form(self, **textboxes):
                for name, text in textboxes.items():
                    self._director.the(name).element.clear()
                    self._director.the(name).send_keys(text)

            @no_stacktrace_for(SeleniumDirectorException)
            def click(self, item):
                self._director.the(item).click()

            @no_stacktrace_for(WebDriverException)
            def refresh_page(self):
                self._webdriver.refresh()

            def tear_down(self):
                if hasattr(self, '_webdriver'):
                    self._webdriver.quit()
      hitch/mystory.story: |
        My first story:
          steps:
          - Do something
