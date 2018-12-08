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


About demo templates:
  about: |
    Output a list of available of usable demo
    templates.
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: demo
      exit code: 0
      will output: |-
        seleniumdirector
        pythonapi
        key
        hitchstory
