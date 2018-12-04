from commandlib import CommandError, Command, python, python_bin
from hitchrun import DIR, expected


# If "expected" is used, no stacktrace will be displayed for that exception
@expected(CommandError)
def hello(argument):
    """
    Try running "hk hello world".
    """
    DIR.gen.joinpath("hello.txt").write_text(argument)
    Command("cat", "hello.txt").in_dir(DIR.gen).run()


## path.py objects -- 

# DIR.gen -- build directory (~/.hitch/xxxxxx, where the symlink 'gen' links to)
# DIR.project -- the directory containng the "hitch" folder.
# DIR.key -- the directory this file - key.py is in.
# DIR.share -- ~/.hitch/share - build folder shared build artefacts.
# DIR.cur -- the directory "hk" was run in.

## Command objects -- 

# Command("cat").run() -- runs cat
# python("pythoncode.py").run() -- run python code using this project's virtualenv
# python_bin.python("pythoncode.py").run() -- equivalent to above. Easily run CLI commands this way.
