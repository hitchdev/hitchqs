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
        from commandlib import CommandError, Command
        from hitchrun import DIR, expected


        @expected(CommandError)
        def helloworld():
            """
            Say hello world.
            """
            DIR.gen.joinpath("hello.txt").write_text("Hello world")
            Command("cat", "hello.txt").in_dir(DIR.gen).run()

  - initial hk
  - hk:
      args: helloworld
      will output: Hello world
