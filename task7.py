class Media:
    def play(self):
        pass

class Song(Media):
    def play(self):
        print("Qoshiq ijro etilmoqda ")

class Movie(Media):
    def play(self):
        print("Film korsatilmoqda ")

class Podcast(Media):
    def play(self):
        print("Podkast eshittirilmoqda ")

song = Song()
movie = Movie()
podcast = Podcast()

song.play()
movie.play()
podcast.play()



