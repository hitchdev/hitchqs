Demo key.py:
  about: |
    Create simple hitch folder with a key.py that has
    various commands that explain various hitchkey
    features.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: demo key
      will output: Quickstart run successfully!
  - files appear:
      filenames:
      - hitch/hitchreqs.in
      - hitch/key.py
