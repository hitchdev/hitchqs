from hitchstory import GivenDefinition, GivenProperty, InfoDefinition, InfoProperty
from hitchstory import BaseEngine, validate, no_stacktrace_for
from strictyaml import CommaSeparated, Str, Int


class Engine(BaseEngine):
    # https://hitchdev.com/hitchstory/using/alpha/given
    given_definition = GivenDefinition(
        example_precondition=GivenProperty(Str())
    )

    # https://hitchdev.com/hitchstory/using/alpha/metadata
    info_definition = InfoDefinition(
        jiras=InfoProperty(schema=CommaSeparated(Str())),
    )

    def __init__(self, paths):
        self.path = paths

    def set_up(self):
        pass

    # https://hitchdev.com/hitchstory/using/alpha/expected-exceptions
    @no_stacktrace_for(AssertionError)
    @validate(with_number=Int())
    def do_something(self, with_number=1):
        # https://hitchdev.com/hitchstory/using/alpha/steps-and-step-arguments
        assert with_number == 1

    def tear_down(self):
        pass
