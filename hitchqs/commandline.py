from path import Path
import dirtemplate
import os
import sys


TEMPLATE_DIR = Path(__file__).realpath().abspath().dirname() / "templates"


def run():
    arguments = sys.argv[1:]
    assert len(arguments) == 1
    template = arguments[0]
    assert template in ["simplekey", "explainkey", "hitchstory"]
    if Path("hitch").exists():
        print((
            "Directory '{}' already exists here, "
            "remove it to run quickstart again."
        ).format("hitch"))
        sys.exit(1)
    cwd = Path(os.getcwd()).abspath()
    dirtemplate.DirTemplate(
        name="hitch", src=TEMPLATE_DIR / template, dest=cwd
    ).ensure_built()
    Path("builddb.sqlite").remove()
    print("Quickstart run successfully!")
