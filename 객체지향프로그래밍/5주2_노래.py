class Song:
    def __init__(self, title, artist):
        self.__title = title
        self.__artist = artist

    @property
    def title(self):
        return self.__title
    @property
    def artist(self):
        return self.__artist

    def __str__(self):
        return f'{self.__title} by {self.__artist}'

    @classmethod
    def create_songs(cls, slist):
        songs = []

        for artist, title in slist:
            songs.append(cls(title, artist)) #cls 는 class이름인 Song을 의미

        return songs

def main():
    songs = [('바다의 왕자', '레몬나인틴'), ('On the Ground', 'Rose')] #튜플들로 구성된 리스트
    song_instance = Song.create_songs(songs) #Song 객체에서 클래스메쏘드인 create_songs 기능을 사용한다.

    for song in song_instance:
        print(song)


main()

