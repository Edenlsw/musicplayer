from dataclasses import dataclass


@dataclass
class PrintLine:
    message: str


@dataclass
class InputLine:
    message: str
    send: str

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return self.message == other.message


class TestingConsoleIO:
    def __init__(self, *expected):
        self.expected = list(expected)
        self.log = []

    def print(self, message):
        actual_line = PrintLine(message)
        if self.expected == []:
            self._raise_end_of_dialogue(actual_line)
        expected_line = self.expected.pop(0)
        if expected_line != actual_line:
            self._raise_unexpected_line(expected_line, actual_line)
        self.log.append(expected_line)

    def input(self, prompt=None):
        actual_line = InputLine(prompt, None)
        if self.expected == []:
            self._raise_end_of_dialogue(actual_line)
        expected_line = self.expected.pop(0)
        if expected_line != actual_line:
            self._raise_unexpected_line(expected_line, actual_line)
        self.log.append(expected_line)
        return expected_line.send

    def _raise_end_of_dialogue(self, actual_line):
        raise Exception(
            "Expected end of dialogue, got: "
            + repr(actual_line)
            + "\nFull Log:\n"
            + self._format_log(actual_line)
        )

    def _raise_unexpected_line(self, expected_line, actual_line):
        raise Exception(
            "Expected "
            + repr(expected_line)
            + ", got "
            + repr(actual_line)
            + "\nFull Log:\n"
            + self._format_log(actual_line, expected_line)
        )

    def _format_log(self, actual=None, expected=None):
        formatted = []
        formatted.extend([f"GOOD: {line}" for line in self.log])
        if expected is None:
            formatted.append(f"UNEXPECTED: {actual}")
        else:
            formatted.append(f"WRONG: GOT {actual}, EXPECTED: {expected}")
        formatted.extend([f"UNMET: {line}" for line in self.expected])
        return "\n".join(formatted)

    def is_done(self):
        return self.expected == []


class MockSubprocess:
    def __init__(self):
        self.called = False
        self.args = None

    def call(self, args):
        self.called = True
        self.args = args
