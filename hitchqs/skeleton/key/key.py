from commandlib import CommandError, Command, python, python_bin
from hitchrun import DIR, expected

# Usable path.py objects -- https://pathpy.readthedocs.io/en/stable/api.html

# DIR.gen -- build directory (~/.hitch/xxxxxx, where the symlink 'gen' links to)
# DIR.project -- the directory containng the "hitch" folder.
# DIR.key -- the directory this file - key.py is in.
# DIR.share -- ~/.hitch/share - build folder shared build artefacts.
# DIR.cur -- the directory "hk" was run in.


# If "expected" is used, no stacktrace will be displayed for that exception
@expected(CommandError)
def hello(argument):
    """
    Try running "hk hello world".
    """
    # https://pathpy.readthedocs.io/en/stable/api.html
    DIR.gen.joinpath("hello.txt").write_text(argument)

    # https://hitchdev.com/commandlib/
    Command("cat", "hello.txt").in_dir(DIR.gen).run()


@expected(CommandError)
def runcommand():
    """
    Run python 3 code with the hk virtualenv.
    """
    python("pythoncode.py").run()             # run python code using this project's virtualenv
    python_bin.python("pythoncode.py").run()  # equivalent
