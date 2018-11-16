from hitchstory import StoryCollection, BaseEngine, exceptions, validate, no_stacktrace_for
from hitchstory import GivenDefinition, GivenProperty, InfoDefinition, InfoProperty
from templex import Templex
from strictyaml import Optional, Str, Map, Int, Bool, Enum, load
import hitchpylibrarytoolkit
from templex import Templex
from hitchrunpy import (
    ExamplePythonCode,
    HitchRunPyException,
    ExpectedExceptionMessageWasDifferent,
)



CODE_TYPE = Map({"in python 2": Str(), "in python 3": Str()}) | Str()


class Engine(BaseEngine):
    """Python engine for running tests."""

    given_definition = GivenDefinition(
        python_version=GivenProperty(Str()),
    )

    info_definition = InfoDefinition(
        status=InfoProperty(schema=Enum(["experimental", "stable"])),
        docs=InfoProperty(schema=Str()),
        fails_on_python_2=InfoProperty(schema=Bool()),
        description=InfoProperty(schema=Str()),
        experimental=InfoProperty(schema=Bool()),
    )

    def __init__(self, keypath, rewrite=False):
        self.path = keypath
        self._rewrite = rewrite

    def set_up(self):
        """Set up your applications and the test environment."""
        self.path.state = self.path.gen.joinpath("state")
        if self.path.state.exists():
            self.path.state.rmtree(ignore_errors=True)
        self.path.state.mkdir()

        self.path.profile = self.path.gen.joinpath("profile")

        if not self.path.profile.exists():
            self.path.profile.mkdir()

        self.qs = hitchpylibrarytoolkit.project_build(
            "hitchqs",
            self.path,
            self.given["python version"],
        ).bin.quickstart


    def quickstart(self, args, will_output=None):
        import shlex
        self.qs(*shlex.split(args)).in_dir(self.path.state).run()

    @no_stacktrace_for(FileNotFoundError)
    def files_appear(self, **files):
        for filename, expected_content in files.items():
            actual_content = self.path.state.joinpath(filename).text()
            try:
                Templex(actual_content).assert_match(expected_content)
            except AssertionError:
                if self._rewrite:
                    self.current_step.update(**{filename: actual_content})
                else:
                    raise

    def pause(self, message="Pause"):
        import IPython

        IPython.embed()
