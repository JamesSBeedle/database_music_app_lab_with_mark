import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Mark")
artist_repository.save(artist_1)

album_1 = Album("How to make Friends and Influence People", "Rock", artist_1 )
album_repository.save(album_1)

album_1.genre = "Brit-Pop_Rock"
album_repository.update(album_1)



print(album_repository.select(album_1.id))

for album in album_repository.select_all():
    print(album.__dict__)


pdb.set_trace()


