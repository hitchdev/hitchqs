Hitchstory Tutorial:
  about: |
    Create simple hitch folder with a key.py and
    hitchreqs in with hitchstory which has a bunch of
    tests which show off the features of hitchstory.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: tutorial hitchstory
      will output: Quickstart run successfully!
  - files appear:
      hitch/hitchreqs.in: |
        hitchstory
        pathquery
        hitchrun
        # add package names here, save and just rerun "hk command" and they will be installed
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
        from hitchstory import BaseEngine, GivenDefinition, GivenProperty
        from strictyaml import Str


        class Engine(BaseEngine):
            given_definition = GivenDefinition(
                website=GivenProperty(Str()),
            )

            def __init__(self, paths):
                self.path = paths

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
      hitch/mystory.story: |
        Logged in:
          given:
            website: /login  # preconditions
          steps:
          - Form filled:
              username: AzureDiamond
              password: hunter2
          - Clicked: login


        Email sent:
          about: |
            The most basic email with no subject, cc or bcc
            set.
          based on: logged in             # inherits from and continues from story above
          steps:
          - Clicked: new email
          - Form filled:
              to: Cthon98@aol.com
              contents: |                # long form text
                Hey guys,

                I think I got hacked!
          - Clicked: send email
          - Email was sent

  - initial hk
  - hk:
      args: bdd email
      will output: |-
        RUNNING Email sent in /home/colm/hitch/tempqs/hitch/mystory.story ... set up
        /login
        password: hunter2
        username: AzureDiamond
        login
        new email
        contents: Hey guys,

        I think I got hacked!

        to: Cthon98@aol.com
        send email
        email was sent
        success
        SUCCESS in 0.0 seconds.
        tear down run
