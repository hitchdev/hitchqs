Demo Python API:
  about: |
    Short demo showing off how to develop, test and autodocument
    python code API projects. This code demonstrates how

    * hitchstory
    * hitchbuildpy
    * hitchrunpy

    All work together.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: demo pythonapi
      will output: Quickstart run successfully!
  - files appear:
      filenames:
      - pythonapi/example.py
      - pythonapi/hitch/hitchreqs.in
      - pythonapi/hitch/key.py
      - pythonapi/hitch/engine.py
      - pythonapi/hitch/mystory.story
      - pythonapi/requirements.txt
  - initial hk:
      args: bdd print
      in dir: pythonapi/
  - hk:
      args: bdd print
      will output: |-
        RUNNING Print the addition of two numbers in /path/to/pythonapi/hitch/mystory.story ... SUCCESS in n.n seconds.
      in dir: pythonapi/
