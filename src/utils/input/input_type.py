from dataclasses import dataclass


@dataclass(frozen=True)
class InputType:
    TYPE_PUZZLE: str = "puzzle"
    TYPE_TESTCASE: str = "testcase"
