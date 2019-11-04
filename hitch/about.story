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
        hk --skeleton hitchstory  # hk skeleton with hitchstory installed
        hk --skeleton key         # basic hitchkey skeleton


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
        hk --demo hitchstory        # demo of hitchstory
        hk --demo key               # demo of hitchkey's capabilities
        hk --demo pythonapi         # Example API test.
        hk --demo seleniumdirector  # Example selenium demo.
