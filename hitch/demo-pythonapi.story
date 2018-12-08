Demo Python API:
  about: |
    Short demo showing off how hitchstory, hitchbuildpy
    and hitchrunpy work together to test and document
    python API code.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: demo pythonapi
      will output: Quickstart run successfully!
  - files appear:
      filenames:
      - codeapi/example.py
      - codeapi/hitch/hitchreqs.in
      - codeapi/hitch/key.py
      - codeapi/hitch/engine.py
      - codeapi/hitch/mystory.story
      - codeapi/requirements.txt
  - initial hk:
      args: bdd print
      in dir: codeapi/
  - hk:
      args: bdd print
      will output: |-
        RUNNING Print the addition of two numbers in /path/to/codeapi/hitch/mystory.story ... SUCCESS in 0.1 seconds.
      in dir: codeapi/
