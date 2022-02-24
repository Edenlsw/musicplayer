# from dbm.ndbm import library


class MusicLibrary:



    def __init__(self):
        self.song_library = []


    def add(self, track):
        self.track = track
        self.song_library.append(self.track)

    def remove(self, track):
        self.track = track 
        if self.track < len(self.song_library):
            del self.song_library[self.track] 
            return True
        else:
            return False
            

        

    def all(self):
        return self.song_library

    # def remove(self, track):
    #     self.track = track - 1
    #     del self.song_library[self.track]       

        


# music_library = MusicLibrary()