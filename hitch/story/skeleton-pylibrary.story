Skeleton hitch pylibrary:
  about: |
    Create a skeleton python library with all of the
    hitch tools laid out.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: skeleton hitchpylibrary
      will output: Quickstart run successfully!
  - files appear:
      filenames:
      - pylibrary/hitch/hitchreqs.in
      - pylibrary/hitch/debugrequirements.txt
      - pylibrary/hitch/story/example.story
      - pylibrary/hitch/key.py
      - pylibrary/hitch/build.py
      - pylibrary/hitch/engine.py
      - pylibrary/setup.py
      - pylibrary/.gitignore
      - pylibrary/README.md
      - pylibrary/VERSION
      - pylibrary/MANIFEST.in
      - pylibrary/pylibrary/__init__.py
      - pylibrary/docs/index.md
