class MusicLibrary:

    def __init__(self):
        self.song_library = []

    def add(self, track):
        # self.song = track
        # self.song_library.append(self.song)
        self.song_library.append(track)

    def remove(self, track):
        self.track = track 
        if self.track < len(self.song_library):
            del self.song_library[self.track] 
            return True
        else:
            return False

    def all(self):
        return self.song_library
# =======================================
class Track:
    
    def __init__(self, song_title, song_artist, song_file):
        self.title = song_title
        self.artist = song_artist
        self.file = song_file
        
# ==================================

trackdetails = Track("The Boys of Summer", "DJ Sammy", "summer.mp3")
print(trackdetails.title)

music_library = MusicLibrary()
trackdetails = Track("The Boys of Summer", "DJ Sammy", "summer.mp3")
music_library.add(trackdetails.title)

print(music_library.all())

   
    
    
