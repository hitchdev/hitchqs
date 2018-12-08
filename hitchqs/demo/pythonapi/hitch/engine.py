from hitchstory import BaseEngine, GivenDefinition, GivenProperty
from hitchstory import no_stacktrace_for
from hitchrunpy import ExamplePythonCode, HitchRunPyException
from templex import Templex
from strictyaml import Str
import hitchbuildpy


class Engine(BaseEngine):
    given_definition = GivenDefinition(
        setup=GivenProperty(Str()),
        state=GivenProperty(Str()),
    )

    def __init__(self, paths, rewrite=False):
        self.path = paths
        self._rewrite = rewrite

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
            .with_strings(state=self.given['state'])
            .with_modules("game.py", "state.py")
        )

    @no_stacktrace_for(HitchRunPyException)
    def run(self, code, will_output=None):
        result = self.example_py_code.with_code(code).run()

        if will_output is not None:
            try:
                Templex(will_output).assert_match(result.output)
            except AssertionError:
                if self._rewrite:
                    self.current_step.update(**{"will output": result.output})
                else:
                    raise
