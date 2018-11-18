from hitchstory import BaseEngine, GivenDefinition, GivenProperty
from strictyaml import Str


class Engine(BaseEngine):
    given_definition = GivenDefinition(
        website=GivenProperty(Str()),
    )

    def set_up(self):
        print("set up")
        print(self.given["website"])

    def form_filled(self, **textboxes):
        for name, contents in sorted(textboxes.items()):
            print("{}: {}".format(name, contents))

    def clicked(self, name):
        print(name)

    def email_was_sent(self):
        print("email was sent")

    def on_failure(self, result):
        print("failure")

    def on_success(self):
        print("success")

    def tear_down(self):
        print("tear down run")
