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
      filenames:
      - hitch/hitchreqs.in
      - hitch/key.py
      - hitch/engine.py
      - hitch/mystory.story
      - hitch/selectors.yml
  - initial hk
  - hk:
      args: bdd
      will output: |-
        RUNNING My first story in /path/to/hitch/mystory.story ... SUCCESS in n.n seconds.
