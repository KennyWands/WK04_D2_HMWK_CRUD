import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_rep
import repositories.album_repository as album_rep


for artist in result:
    print(artist.__dict__)

pdb.set_trace()