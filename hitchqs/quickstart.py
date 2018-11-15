from path import Path
import dirtemplate
import os


TEMPLATE_DIR = Path(__file__).realpath().abspath().dirname() / "templates"


def run():
    cwd = Path(os.getcwd()).abspath()
    dirtemplate.DirTemplate(
        name="hitch", src=TEMPLATE_DIR / "simple", dest=cwd
    ).ensure_built()
