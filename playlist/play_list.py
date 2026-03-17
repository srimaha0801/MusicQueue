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
    
    def play_song(self,song):
        temp = self.head
        while temp:
            if temp.song == song:
                return song
            temp = temp.next
        return "Not found"
    
    def show_playlist(self):
        temp = self.head
        songs = []

        while temp:
            songs.append(temp.song)
            temp = temp.next

        return songs
    
    def next_song(self, current_song):
        temp = self.head
        while temp:
            if temp.song == current_song:
                if temp.next:
                    return temp.next.song
            temp = temp.next
        return "No Next song"
    
    def prev_song(self, current_song):
        temp = self.head
        while temp:
            if temp.song == current_song:
                if temp.prev:
                    return temp.prev.song
            temp = temp.next
        return "No Previous song"
    
    def delete_song(self, current_song):
        temp = self.head
        print("Trying to delete:", current_song)
        print("Playlist before delete:", self.show_playlist())
        while temp:
            if temp.song == current_song:
                if temp == self.head:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None

                elif temp == self.tail:
                    self.tail = temp.prev
                    if self.tail:
                        self.tail.next = None
                
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                print("Deleted:", temp.song)
                print("Playlist after delete:", self.show_playlist())
                
                return "Song deleted"
            temp = temp.next
        print("song not found")
        return "Song not found"