# Don't edit this file until you're told to.
# If you do, the rest of the module won't work!

from player.music_library import MusicLibrary, Track


class Interface:
    def __init__(self, console):
        self.console = console
        self.music_library = MusicLibrary()

    def run(self):
        self.console.print("Welcome to your music library!")
        while True:
            choice = self._prompt()
            if choice == "a":
                self._add_track()
            elif choice == "d":
                self._remove_track()
            elif choice == "l":
                self._list_tracks()
            elif choice == "q":
                return
            else:
                self.console.print("No such command! Try again.")

    def _prompt(self):
        self.console.print("Enter:")
        self.console.print("  a: to add a track")
        self.console.print("  d: to delete a track")
        self.console.print("  l: to list your tracks")
        self.console.print("  q: to quit")
        return self.console.input("What do you pick? ")

    def _add_track(self):
        title = self.console.input("What's the title? ")
        artist = self.console.input("What's the artist? ")
        file = self.console.input("What's the file? ")
        self.music_library.add(Track(title, artist, file))  # We pass the Track in.
        self.console.print("Added successfully.")

    def _list_tracks(self):
        for idx, track in enumerate(self.music_library.all()):
            self.console.print(
                f"{idx + 1}. {track.title} by {track.artist} @ {track.file}"
            )

    def _remove_track(self):
        self._list_tracks()
        track_id = int(self.console.input("Which do you want to delete? "))
        if self.music_library.remove(track_id - 1):
            self.console.print("Deleted successfully.")
        else:
            self.console.print("No such track.")


class ConsoleIO:
    def print(self, message):
        print(message)

    def input(self, prompt=None):
        if prompt is None:
            return input()
        return input(prompt)
