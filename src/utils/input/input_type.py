from dataclasses import dataclass


@dataclass(frozen=True)
class InputType:
    TYPE_PUZZLE: str = "puzzle"
    TYPE_TESTCASE: str = "testcase"

    VALID_TYPES = [TYPE_PUZZLE, TYPE_TESTCASE]
