About skeleton templates:
  about: |
    Output a list of available of usable skeleton
    templates.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: skeleton
      exit code: 0
      will output: |-
        key
        hitchstory


About tutorial templates:
  about: |
    Output a list of available of usable tutorialss
    templates.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: tutorial
      exit code: 0
      will output: |-
        seleniumdirector
        key
        hitchstory
