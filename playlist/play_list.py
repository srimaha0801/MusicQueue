class SongNode:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_song(self, song):
        new_song = SongNode(song)

        if self.head is None:
            self.head = new_song
            self.tail = new_song
            return

        self.tail.next = new_song
        new_song.prev = self.tail
        self.tail = new_song

    def show_playlist(self):
        temp = self.head
        songs = []

        while temp:
            songs.append(temp.song)
            temp = temp.next

        return songs