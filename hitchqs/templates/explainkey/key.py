from hitchrun import DIR
from commandlib import Command


def helloworld():
    """
    hk helloworld -> "hello world"
    """
    print("hello world")


def runcommand():
    """
    hk runcommand -> "ls -l"
    """
    # See https://hitchdev.com/commandlib/
    # -- for more details on how to use commandlib
    Command("ls", "-l").in_dir(DIR.key).run()

    # N.B. DIR.key is the folder this file - key.py - is in


def twoargs(arg1, arg2):
    """
    twoargs arg1 arg1 -> "arg1 arg2"
    """
    print(arg1)
    print(arg2)


def manyargs(*args):
    """
    manyargs arg1 arg2 arg2 -> "arg1 arg2 arg3"
    """
    for arg in args:
        print(arg)


def build():
    """
    Put file in gen folder and read it back.

    The gen folder is a folder like "~/.hitch/fdsfds". There is
    a symlink to is in the same folder as key.py.
    """
    example_file = DIR.gen / "example.txt"
    # See https://pathpy.readthedocs.io/en/latest/api.html
    # -- for more details on how to use path.py objects

    example_file.write_text("hello")
    print(example_file.abspath())  # Print filename
    print(example_file.text())  # Print contents


def directories():
    """
    Show all usable special directories.
    """
    print(DIR.cwd)  # Directory hk was run in
    print(DIR.share)  # ~/.hitch/share - for shared build artefacts (e.g. base pythons)
    print(DIR.key)  # Directory this key.py file is in (usually 'hitch')
    print(
        DIR.project
    )  # Directory *above* key.py directory (the folder the 'hitch' directory is in)
    print(DIR.gen)  # ~/.hitch/jonafd -- build directory. 'gen' symlinks here.


def ipython():
    """
    Use IPython.embed() to experiment in the python environment.
    """
    import IPython

    IPython.embed()
