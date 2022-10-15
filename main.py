#!/usr/bin/python
from models import BibleVerse
import peewee
import csv
from utils.system_checks import full_system_check
from utils.bible_import import bible_setup, BibleImporter

if __name__ == "__main__":
    try:
        full_system_check()
        bible_setup()
    except Exception as e:
        print(e)
    finally:
        BibleImporter.delete_bible_repo()