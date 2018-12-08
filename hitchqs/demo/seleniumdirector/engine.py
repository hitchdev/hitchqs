from hitchstory import BaseEngine, no_stacktrace_for
from seleniumdirector import WebDirector, SeleniumDirectorException
from selenium.common.exceptions import WebDriverException
from selenium import webdriver


class Engine(BaseEngine):
    def __init__(self, dirs):
        self.dirs = dirs

    def set_up(self):
        self._webdriver = webdriver.Chrome()
        self._director = WebDirector(
            self._webdriver, self.dirs.key / "selectors.yml", default_timeout=5
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
        if hasattr(self, "_webdriver"):
            self._webdriver.quit()
