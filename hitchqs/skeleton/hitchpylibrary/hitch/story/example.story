Example:
  given:
    pyenv_version: 3.7.0
    setup: |
      import pylibrary
  steps:
  - run: |
      print(pylibrary.hello())
