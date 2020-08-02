Skeleton Hitchstory:
  about: |
    Create simple hitch folder with a key.py and
    hitchreqs in with hitchstory which runs a simple
    test that does nothing.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: skeleton hitchstory
      will output: Quickstart run successfully!
  - files appear:
      filenames:
      - hitch/hitchreqs.in
      - hitch/key.py
      - hitch/engine.py
      - hitch/mystory.story
  - initial hk
  - hk:
      args: bdd my story
      will output: x
