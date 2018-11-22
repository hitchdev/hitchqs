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
      hitch/hitchreqs.in: |
        hitchrun
      hitch/key.py: |
        from hitchrun import DIR


        def helloworld():
            """
            Print all of the available directories.
            """
            print(DIR.gen)
            print(DIR.key)
            print(DIR.project)
            print(DIR.share)
            print(DIR.cur)
