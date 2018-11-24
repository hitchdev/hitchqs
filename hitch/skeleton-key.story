Skeleton key.py:
  about: |
    Create simple hitch folder with a key.py and
    hitchreqs.in that does the bare minimum.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: skeleton key
      will output: Quickstart run successfully!
  - files appear:
      filenames:
      - hitch/hitchreqs.in
      - hitch/key.py
  - initial hk
  - hk:
      args: helloworld
      will output: Hello world
