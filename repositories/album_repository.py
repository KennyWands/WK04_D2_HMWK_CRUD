from db.run_sql import run_sql

from models.album import Album
import repositories.album_repository as album_rep


def save():
    pass


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM albums WHERE id =%s"
    values = [id]
    run_sql(sql, values)


def select():
    pass


def select_all():
    pass


def list_by_artist():
    pass


def update():
    pass
