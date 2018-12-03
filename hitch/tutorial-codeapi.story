Tutorial Code API:
  about: |
    Create simple project
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: tutorial codeapi
      will output: Quickstart run successfully!
  - files appear:
      filenames:
      - codeapi/example.py
      - codeapi/hitch/hitchreqs.in
      - codeapi/hitch/key.py
      - codeapi/hitch/engine.py
      - codeapi/hitch/mystory.story
  - initial hk:
      in dir: codeapi/
  - hk:
      args: bdd my story
      will output: passed
      in dir: codeapi/
