from db.run_sql import run_sql

from models.artist import Artist
import repositories.artist_repository as artist_rep


def save(artist):
    sql = "INSERT INTO artists (name, user_id) VALUES ( %s )RETURNING id"
    values = [artist.name, artist.id]
    results = run_sql(sql, values)
    id = results[0]["id]"]
    artist.id = id
    return artist


def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM artists WHERE id =%s"
    values = [id]
    run_sql(sql, values)


def select(id):
    this_artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not none:
        this_artist = Artist(result["name"], result["id"])
    return this_artist


def select_all():
    all_artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row["name"], row["id"])
        all_artists.append(artist)
    return all_artists


def list_by_artist():
    pass


def update(artist):
    sql = "UPDATE artists SET (name) VALUES (%s) WHERE ID =%s"
    values = [artist.name, artist.id]
    run_sql(sql, values)