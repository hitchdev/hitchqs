Demo Tutorial:
  about: |
    Create simple hitch folder with a key.py and
    hitchreqs in with hitchstory which has a bunch of
    tests which show off the features of hitchstory.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: demo hitchstory
      will output: Quickstart run successfully!
  - files appear:
      filenames:
      - hitch/hitchreqs.in
      - hitch/key.py
      - hitch/engine.py
      - hitch/mystory.story

  - initial hk
  - hk:
      args: bdd email
      will output: |-
        RUNNING Email sent in /path/to/hitch/mystory.story ... set up
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
        SUCCESS in n.n seconds.
        tear down run
