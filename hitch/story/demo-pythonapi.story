Demo Python API:
  about: |
    Demo showing off how to develop, test and autodocument
    python code API projects using the combination of

    * hitchkey -- https://hitchdev.com/hitchkey
    * hitchstory -- https://hitchdev.com/hitchstory
    * hitchbuildpy -- https://hitchdev.com/hitchbuildpy
    * hitchrunpy -- https://hitchdev.com/hitchrunpy

  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: demo pythonapi
      will output: Quickstart run successfully!
  - files appear:
      filenames:
      - pythonapi/state.py
      - pythonapi/game.py
      - pythonapi/hitch/hitchreqs.in
      - pythonapi/hitch/key.py
      - pythonapi/hitch/engine.py
      - pythonapi/story/glider.story
      - pythonapi/requirements.txt
  - initial hk:
      args: bdd glider
      in dir: pythonapi/
  - hk:
      args: bdd glider
      will output: |-
        RUNNING Glider in /path/to/pythonapi/story/glider.story ... SUCCESS in n.n seconds.
      in dir: pythonapi/
