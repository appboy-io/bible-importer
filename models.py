import peewee
import os

database = peewee.PostgresqlDatabase(
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_TYPE')
    )

class BibleVerse(peewee.Model):
    """
    Model for verses
    """
    id = peewee.IdentityField()
    book = peewee.CharField()
    chapter = peewee.IntegerField()
    verse = peewee.IntegerField()
    text = peewee.TextField()
    language = peewee.TextField()
    created_at = peewee.TimestampField()

    class Meta:
        database = database

if __name__ == "__main__":
    try:
        BibleVerse.create_table()
    except peewee.OperationalError:
        print("BibleVerse created already")