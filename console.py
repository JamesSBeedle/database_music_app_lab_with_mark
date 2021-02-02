import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# album_1 = Album("How to make Friends and Influence People", "Rock", "Terrorvision")
# album_repository.save(album_1)

artist_1 = Artist("Mark")
artist_repository.save(artist_1)