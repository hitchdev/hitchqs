from strictyaml import load
from sys import argv, exit
from path import Path
import dirtemplate
import os


THIS_DIR = Path(__file__).realpath().abspath().dirname()


def run():
    arguments = argv[1:]
    assert len(arguments) == 1 or len(arguments) == 2
    template_type = arguments[0]
    assert template_type in ["demo", "skeleton"]
    available_templates = [
        str(path.basename()) for path in THIS_DIR.joinpath(template_type).listdir()
    ]

    if len(arguments) == 1:
        print("\n".join(available_templates))
        exit(0)

    template = arguments[1]
    if template not in available_templates:
        print("{} '{}' does not exist.".format(template_type, template))
        exit(1)

    assert template in available_templates

    template_path = THIS_DIR / template_type / template

    hitchqs_settings = load(template_path.joinpath("hitchqs.yml").text()).data

    project_path_name = hitchqs_settings["path"]

    if Path(project_path_name).exists():
        print(
            (
                "Directory '{}' already exists here, "
                "remove it to run quickstart again."
            ).format(project_path_name)
        )
        exit(1)
    cwd = Path(os.getcwd()).abspath()
    dirtemplate.DirTemplate(
        name=project_path_name, src=template_path, dest=cwd
    ).ignore_files("hitchqs.yml").ensure_built()
    Path("builddb.sqlite").remove()
    print("Quickstart run successfully!")
