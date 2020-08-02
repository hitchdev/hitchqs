from hitchstory import HitchStoryException
from hitchrun import expected
from commandlib import CommandError
from strictyaml import load
from pathquery import pathquery
from hitchrun import DIR
import dirtemplate
import hitchpylibrarytoolkit
from engine import Engine

PROJECT_NAME = "hitchqs"

toolkit = hitchpylibrarytoolkit.ProjectToolkit(
    "hitchqs",
    DIR,
    Engine,
)


@expected(HitchStoryException)
def bdd(*keywords):
    """Run single story."""
    toolkit.bdd(Engine(DIR), keywords)


@expected(HitchStoryException)
def rbdd(*keywords):
    """
    Run story matching keywords and rewrite story if code changed.
    """
    toolkit.bdd(Engine(DIR, rewrite=True), keywords)


@expected(HitchStoryException)
def bbdd(*keywords):
    """Run individual story matching key words and build."""
    toolkit.bdd(Engine(DIR, build=True), keywords)


@expected(HitchStoryException)
def regression():
    """
    Run regression testing - lint and then run all tests.
    """
    toolkit.regression(Engine(DIR))


def reformat():
    """
    Reformat using black and then relint.
    """
    toolkit.reformat()


def lint():
    """
    Lint project code and hitch code.
    """
    toolkit.lint()


def deploy(version):
    """
    Deploy to pypi as specified version.
    """
    toolkit.deploy(version)


@expected(dirtemplate.exceptions.DirTemplateException)
def docgen():
    """
    Build documentation.
    """
    toolkit.docgen()


@expected(dirtemplate.exceptions.DirTemplateException)
def readmegen():
    """
    Build README.md and CHANGELOG.md.
    """
    toolkit.readmegen()


@expected(CommandError)
def doctests():
    """
    Run doctests in utils.py in python 2 and 3.
    """
    for python_version in ["2.7.14", "3.7.0"]:
        pylibrary = hitchpylibrarytoolkit.project_build(
            PROJECT_NAME, DIR, python_version
        )
        pylibrary.bin.python(
            "-m", "doctest", "-v", DIR.project.joinpath(PROJECT_NAME, "utils.py")
        ).in_dir(DIR.project.joinpath(PROJECT_NAME)).run()


@expected(CommandError)
def rerun(version="3.7.0"):
    """
    Rerun last example code block with specified version of python.
    """
    from commandlib import Command

    Command(DIR.gen.joinpath("py{0}".format(version), "bin", "python"))(
        DIR.gen.joinpath("state", "examplepythoncode.py")
    ).in_dir(DIR.gen.joinpath("state")).run()


@expected(CommandError)
@expected(AssertionError)
def copyback(template_type, name):
    """
    After debugging a template, copy it back to the main repo.
    """
    assert template_type in ["demo", "skeleton"]
    backdir = DIR.project / "hitchqs" / template_type / name
    folder_name = load(backdir.joinpath("hitchqs.yml").text()).data["path"]
    assert backdir.exists()
    tempqs = DIR.project.parent / "tempqs" / folder_name
    template_files = (
        pathquery(tempqs).is_not_dir()
        - pathquery(tempqs).ext("pyc")
        - pathquery(tempqs).named("hitchreqs.txt")
    )

    for filepath in template_files:
        relpath = filepath.relpath(tempqs)
        print("Copying back {}".format(relpath))
        filepath.copy(backdir / relpath)
