from hitchstory import HitchStoryException
from hitchrun import expected
from hitchrun import DIR
from engine import Engine
import hitchpylibrarytoolkit


toolkit = hitchpylibrarytoolkit.ProjectToolkit(
    "pylibrary",
    DIR,
    Engine,
)


@expected(HitchStoryException)
def bdd(*keywords):
    """Run single story."""
    toolkit.bdd(Engine(DIR), keywords)


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


def docgen():
    """
    Build documentation.
    """
    toolkit.docgen()


def readmegen():
    """
    Build README.md and CHANGELOG.md.
    """
    toolkit.readmegen()

