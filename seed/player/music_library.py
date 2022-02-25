class MusicLibrary:

    def __init__(self):
        self.song_library = []

    def add(self, trackdetails):
        # function to add trackdetails to the song_library
        self.song_library.append(trackdetails)

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
# have made trackdetails = Track(info on title, artist, file type)
trackdetails = Track("The Boys of Summer", "DJ Sammy", "summer.mp3")
print(trackdetails.title)

# music_library = MusicLibrary() with all the ufnctions within 
music_library = MusicLibrary()
# have made trackdetails = Track(info on title, artist, file type)
trackdetails = Track("The Boys of Summer", "DJ Sammy", "summer.mp3")
# music_library now adds the details of the track. title to the music_library.
music_library.add(trackdetails.title)
music_library.add(trackdetails.artist)
music_library.add(trackdetails.file)



# prints all details in music-library. Now that I've added details 
# about the song it prints the array with title, artist and file type
print(music_library.all())

   
    
    
