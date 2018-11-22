from commandlib import CommandError, Command
from hitchrun import DIR, expected


@expected(CommandError)
def helloworld():
    """
    Say hello world.
    """
    DIR.gen.joinpath("hello.txt").write_text("Hello world")
    Command("cat", "hello.txt").in_dir(DIR.gen).run()
