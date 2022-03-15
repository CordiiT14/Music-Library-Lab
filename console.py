from models.artist import Artist
from models.album import Album

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


artist_1 = Artist('P!nk')
artist_2 = Artist('Elton John')

artist_repository.save(artist_1)
# artist_repository.save(artist_2)

album_1 = Album('Funhouse', artist_1, 'pop-rock')

album_repository.save(album_1)

artists = artist_repository.select_all()

for artist in artists:
    print(artist.__dict__)