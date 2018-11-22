from sys import argv, exit
from path import Path
import dirtemplate
import os


TEMPLATE_DIR = Path(__file__).realpath().abspath().dirname() / "templates"


def run():
    arguments = argv[1:]
    assert len(arguments) == 2
    template_type = arguments[0]
    assert template_type in ["tutorial", "skeleton", ]
    available_templates = [
        str(path.basename()) for path in TEMPLATE_DIR.joinpath(template_type).listdir()
    ]
    template = arguments[1]
    if template not in available_templates:
        print("{} '{}' does not exist.".format(template_type, template))
        exit(1)
    assert template in available_templates
    if Path("hitch").exists():
        print((
            "Directory '{}' already exists here, "
            "remove it to run quickstart again."
        ).format("hitch"))
        exit(1)
    cwd = Path(os.getcwd()).abspath()
    dirtemplate.DirTemplate(
        name="hitch", src=TEMPLATE_DIR / template_type / template, dest=cwd
    ).ensure_built()
    Path("builddb.sqlite").remove()
    print("Quickstart run successfully!")
