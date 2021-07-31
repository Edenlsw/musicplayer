import unittest

from player.music_library import MusicLibrary


class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        MusicLibrary()
