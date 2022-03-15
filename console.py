
from models.artist import Artist
from models.album import Album

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


# artist_1 = Artist('P!nk')
# artist_2 = Artist('Elton John')

# artist_repository.save(artist_1)
# artist_repository.save(artist_2)

# album_1 = Album('Funhouse', artist_1, 'pop-rock')
# album_2 = Album('Diamonds', artist_2, 'pop-rock')

# album_repository.save(album_1)
# album_repository.save(album_2)

# albums = album_repository.select_all()

# for album in albums:
#     print(album.__dict__)

# artists = artist_repository.select_all()

# for artist in artists:
#     print(artist.__dict__)

# artist_1 = Artist('Bjork')
# album_3 = Album('Vespertine', artist_1, 'Bjrock')
# artist_repository.save(artist_1)
# album_repository.save(album_3)

# vespertine = album_repository.select(album_3.id)
# print(vespertine.title)
# album_repository.delete_all()
# artist_repository.delete_all()