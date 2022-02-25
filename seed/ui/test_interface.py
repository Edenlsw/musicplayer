import unittest
from ui.interface import Interface
from ui.mocks import PrintLine, InputLine, TestingConsoleIO


class TestConsoleRunner(unittest.TestCase):
    OPTIONS = [
        PrintLine("Enter:"),
        PrintLine("  a: to add a track"),
        PrintLine("  d: to delete a track"),
        PrintLine("  l: to list your tracks"),
        PrintLine("  q: to quit"),
    ]

    INTRO = [PrintLine("Welcome to your music library!"), *OPTIONS]

    QUIT = [*OPTIONS, InputLine("What do you pick? ", "q")]

    def test_adds_tracks(self):
        testing_console_io = TestingConsoleIO(
            *self.INTRO,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "Major's Titling Victory"),
            InputLine("What's the artist? ", "The Cribs"),
            InputLine("What's the file? ", "file1.mp3"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "l"),
            PrintLine("1. Major's Titling Victory by The Cribs @ file1.mp3"),
            *self.QUIT,
        )
        interface = Interface(testing_console_io)
        interface.run()
        self.assertTrue(testing_console_io.is_done())

    def test_deletes_tracks(self):
        testing_console_io = TestingConsoleIO(
            *self.INTRO,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "Major's Titling Victory"),
            InputLine("What's the artist? ", "The Cribs"),
            InputLine("What's the file? ", "file1.mp3"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "a"),
            InputLine("What's the title? ", "Be Safe (feat. Lee Ranaldo)"),
            InputLine("What's the artist? ", "The Cribs"),
            InputLine("What's the file? ", "file2.mp3"),
            PrintLine("Added successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "d"),
            PrintLine("1. Major's Titling Victory by The Cribs @ file1.mp3"),
            PrintLine("2. Be Safe (feat. Lee Ranaldo) by The Cribs @ file2.mp3"),
            InputLine("Which do you want to delete? ", "1"),
            PrintLine("Deleted successfully."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "d"),
            PrintLine("1. Be Safe (feat. Lee Ranaldo) by The Cribs @ file2.mp3"),
            InputLine("Which do you want to delete? ", "2"),
            PrintLine("No such track."),
            *self.OPTIONS,
            InputLine("What do you pick? ", "l"),
            PrintLine("1. Be Safe (feat. Lee Ranaldo) by The Cribs @ file2.mp3"),
            *self.QUIT,
        )
        interface = Interface(testing_console_io)
        interface.run()
        self.assertTrue(testing_console_io.is_done())

    def test_cycles_on_wrong_choice(self):
        testing_console_io = TestingConsoleIO(
            *self.INTRO,
            InputLine("What do you pick? ", "z"),
            PrintLine("No such command! Try again."),
            *self.QUIT,
        )
        interface = Interface(testing_console_io)
        interface.run()
        self.assertTrue(testing_console_io.is_done())
