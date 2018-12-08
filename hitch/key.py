from hitchstory import HitchStoryException, StoryCollection
from hitchrun import expected
from commandlib import CommandError
from strictyaml import Str, Map, Bool, load
from pathquery import pathquery
from hitchrun import DIR
import dirtemplate
import hitchpylibrarytoolkit
from engine import Engine


PROJECT_NAME = "hitchqs"

"""
----------------------------
Non-runnable utility methods
---------------------------
"""


def _storybook(**kwargs):
    return StoryCollection(pathquery(DIR.key).ext("story"), Engine(DIR, **kwargs))


def _current_version():
    return DIR.project.joinpath("VERSION").bytes().decode("utf8").rstrip()


def _personal_settings():
    settings_file = DIR.key.joinpath("personalsettings.yml")

    if not settings_file.exists():
        settings_file.write_text(
            (
                "engine:\n"
                "  rewrite: no\n"
                "  cprofile: no\n"
                "params:\n"
                "  python version: 3.7.0\n"
            )
        )
    return load(
        settings_file.bytes().decode("utf8"),
        Map(
            {
                "engine": Map({"rewrite": Bool(), "cprofile": Bool()}),
                "params": Map({"python version": Str()}),
            }
        ),
    )


"""
-----------------
RUNNABLE COMMANDS
-----------------
"""


@expected(HitchStoryException)
def bdd(*keywords):
    """Run individual story matching key words."""
    _storybook().only_uninherited().shortcut(*keywords).play()


@expected(HitchStoryException)
def rbdd(*keywords):
    """
    Run story matching keywords and rewrite story if code changed.
    """
    _storybook(rewrite=True).only_uninherited().shortcut(*keywords).play()


@expected(HitchStoryException)
def bbdd(*keywords):
    """Run individual story matching key words and build."""
    _storybook(build=True).only_uninherited().shortcut(*keywords).play()


@expected(HitchStoryException)
def regression():
    """
    Run regression testing - lint and then run all tests.
    """
    lint()
    _storybook().ordered_by_name().play()


def reformat():
    """
    Reformat using black and then relint.
    """
    hitchpylibrarytoolkit.reformat(DIR.project, PROJECT_NAME)


def lint():
    """
    Lint project code and hitch code.
    """
    hitchpylibrarytoolkit.lint(DIR.project, PROJECT_NAME)


def deploy(version):
    """
    Deploy to pypi as specified version.
    """
    hitchpylibrarytoolkit.deploy(DIR.project, PROJECT_NAME, version)


@expected(dirtemplate.exceptions.DirTemplateException)
def docgen():
    """
    Build documentation.
    """
    hitchpylibrarytoolkit.docgen(_storybook({}), DIR.project, DIR.key, DIR.gen)


@expected(dirtemplate.exceptions.DirTemplateException)
def readmegen():
    """
    Build README.md and CHANGELOG.md.
    """
    hitchpylibrarytoolkit.readmegen(
        _storybook({}), DIR.project, DIR.key, DIR.gen, PROJECT_NAME
    )


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
    folder_name = load(backdir.joinpath("hitchqs.yml").text()).data['path']
    assert backdir.exists()
    tempqs = DIR.project.parent / "tempqs" / folder_name
    template_files = pathquery(tempqs).is_not_dir() - \
        pathquery(tempqs).ext("pyc") - \
        pathquery(tempqs).named("hitchreqs.txt")

    for filepath in template_files:
        relpath = filepath.relpath(tempqs)
        print("Copying back {}".format(relpath))
        filepath.copy(backdir / relpath)
