import unittest

from player.music_library import MusicLibrary


class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        MusicLibrary()

    def test_addsongs(self):
        music_library = MusicLibrary()
        music_library.add("Rolling Blackouts by The Go! Team")
        music_library.add("Oh Yeah by Locust")
        music_library.add("Sleep on the Wing by Bibio")
        self.assertEqual(music_library.song_library, ["Rolling Blackouts by The Go! Team", "Oh Yeah by Locust", "Sleep on the Wing by Bibio"])

    


    def test_remove_song(self):
        music_library = MusicLibrary()
        music_library.add("Rolling Blackouts by The Go! Team")
        music_library.add("Oh Yeah by Locust")
        music_library.add("Sleep on the Wing by Bibio")
        music_library.remove(1)
        self.assertEqual(music_library.song_library, ["Rolling Blackouts by The Go! Team", "Sleep on the Wing by Bibio"])
    


    def test_view_all_songs(self):
        music_library = MusicLibrary()
        music_library.add("Rolling Blackouts by The Go! Team")
        music_library.add("Sleep on the Wing by Bibio")
        self.assertEqual(music_library.all(), ["Rolling Blackouts by The Go! Team", "Sleep on the Wing by Bibio"])
        


    def test_returns_false_if_removing_song_not_in_list(self):
        music_library = MusicLibrary()
        self.assertFalse(music_library.remove(20))
  



