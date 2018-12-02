from hitchstory import BaseEngine, GivenDefinition, GivenProperty
from hitchstory import no_stacktrace_for
from hitchrunpy import ExamplePythonCode, HitchRunPyException
from strictyaml import Str
import hitchbuildpy


class Engine(BaseEngine):
    given_definition = GivenDefinition(my_string=GivenProperty(Str()))

    def __init__(self, paths):
        self.path = paths

    def set_up(self):
        virtualenv = (
            hitchbuildpy.VirtualenvBuild(
                hitchbuildpy.PyenvBuild("3.7.0").with_build_path(self.path.share),
                name="venv",
            )
            .with_requirementstxt("requirements.txt")
            .with_build_path(self.path.gen)
        )
        virtualenv.ensure_built()

        self.example_py_code = (
            ExamplePythonCode(virtualenv.bin.python, self.path.gen)
            .with_setup_code(self.given.get("setup", ""))
            .with_terminal_size(160, 100)
            .with_long_strings(my_string=self.given.get("my_string"))
        )

    @no_stacktrace_for(HitchRunPyException)
    def run(self, code, will_output=None):
        pass
