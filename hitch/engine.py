from hitchstory import StoryCollection, BaseEngine, exceptions, validate, no_stacktrace_for
from hitchstory import GivenDefinition, GivenProperty, InfoDefinition, InfoProperty
from strictyaml import MapPattern, Seq, Str, Map, Int, Bool, Enum, load
from hitchrunpy import ExamplePythonCode, HitchRunPyException
import hitchpylibrarytoolkit
from templex import Templex
from commandlib import Command
from pathquery import pathquery
import shlex
import re


CODE_TYPE = Map({"in python 2": Str(), "in python 3": Str()}) | Str()


class Engine(BaseEngine):
    """Python engine for running tests."""

    given_definition = GivenDefinition(
        python_version=GivenProperty(Str()),
        files=GivenProperty(MapPattern(Str(), Str())),
    )

    info_definition = InfoDefinition(
        status=InfoProperty(schema=Enum(["experimental", "stable"])),
        docs=InfoProperty(schema=Str()),
        fails_on_python_2=InfoProperty(schema=Bool()),
        description=InfoProperty(schema=Str()),
        experimental=InfoProperty(schema=Bool()),
    )

    def __init__(self, keypath, rewrite=False, build=False):
        self.path = keypath
        self._rewrite = rewrite
        self._build = hitchpylibrarytoolkit.PyLibraryBuild(
            "hitchqs",
            self.path,
        )

    def set_up(self):
        """Set up your applications and the test environment."""  
        self._build.ensure_built()
        
        self.path.state = self.path.project.parent / "tempqs"
        if self.path.state.exists():
            self.path.state.rmtree(ignore_errors=True)
        self.path.state.mkdir()

        for filename, contents in self.given.get("files", {}).items():
            filepath = self.path.state.joinpath(filename)
            if not filepath.dirname().exists():
                filepath.dirname().makedirs()
            filepath.write_text(contents)

        self.path.profile = self.path.gen.joinpath("profile")

        if not self.path.profile.exists():
            self.path.profile.mkdir()

        self.qs = self._build.bin.quickstart

    def _run(self, command, args, will_output=None, exit_code=0, timeout=5):
        process = command(*shlex.split(args)).interact().screensize(160, 80).run()
        process.wait_for_finish()

        actual_output = process.stripshot()\
                               .replace(self.path.state, "/path/to")

        # Replace 35.1 SECONDS with n.n SECONDS
        actual_output = re.sub("[0-9]+\.[0-9]", "n.n", actual_output)

        if will_output is not None:
            try:
                Templex(will_output).assert_match(actual_output)
            except AssertionError:
                if self._rewrite:
                    self.current_step.update(**{"will output": actual_output})
                else:
                    raise

        assert process.exit_code == exit_code, "Exit code should be {} was {}, output:\n{}".format(
            exit_code,
            process.exit_code,
            actual_output,
        )

    @validate(timeout=Int(), exit_code=Int())
    def quickstart(self, args, will_output=None, exit_code=0, timeout=5):
        self._run(self.qs.in_dir(self.path.state), args, will_output, exit_code, timeout=timeout)

    def hk(self, args, will_output=None, exit_code=0, timeout=5, in_dir=""):
        if self._build:
            self._run(Command("hk").in_dir(self.path.state / in_dir), args, will_output, exit_code, timeout=timeout)

    def initial_hk(self, args="", in_dir=""):
        if self._build:
            Command("hk", *shlex.split(args)).in_dir(self.path.state / in_dir).run()

    @validate(filenames=Seq(Str()))
    def files_appear(self, filenames):
        appeared = set()
        should_appear = set(filenames)
        for existing_file in pathquery(self.path.state):
            if "__pycache__" not in existing_file and not existing_file.isdir():
                appeared.add(str(existing_file.relpath(self.path.state)))

        diff = should_appear.symmetric_difference(appeared)

        assert diff == set(), \
            "Difference in files that appeared:\n{}".format('\n'.join(diff))

    def pause(self, message="Pause"):
        import IPython

        IPython.embed()


    def tear_down(self):
        if self._build:
            if self.path.state.exists():
                Command("hk", "--clean").ignore_errors().in_dir(self.path.state).run()
