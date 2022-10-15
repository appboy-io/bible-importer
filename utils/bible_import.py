from utils.constants import APP_CONSTANT
from utils.error_constants import ERROR_CONSTANTS, SystemCheckException
from pathlib import Path
import subprocess
import json
import re
from utils.bible_books import BOOKS
from models import BibleVerse


class BibleImporter():
    def download_bible():
        print('Downlading bibles from repo')
        git_exist = subprocess.run(["git", "clone", APP_CONSTANT['REPO']])
        if git_exist.returncode != 0:
            raise SystemCheckException(ERROR_CONSTANTS['GITHUB_REPO_NOT_FOUND'])
    
    def import_bible():
        print('Importing bibles to DB')
        p = Path('./' + APP_CONSTANT['BIBLE-FILE-NAME'])
        language_dir_list = [f for f in p.iterdir() if f.is_dir()]
        bible_verses = []
        for language in language_dir_list:
            if language.name == ".git":
                continue;

            print("Importing: ", language)
            file = open(str(language) + "/bible.json", encoding="utf8")
            data = json.load(file)

            
            for book in data['Book']:
                for chapter in book['Chapter']:
                    for verse in chapter['Verse']:
                        print(verse['Verseid'])
                        result = re.search(r"(\d{0,2}).(\d{0,2}).(\d{0,3})", verse['Verseid'])
                        bible_book_int = int(result.group(1)) + 1
                        chapter_int = int(result.group(2)) + 1
                        verse_int = int(result.group(3)) + 1
                        bible_verse = BibleVerse.create(
                            book = BOOKS[bible_book_int],
                            chapter = chapter_int,
                            verse = verse_int,
                            text = verse['Verse'],
                            language = language.name
                        )
                        bible_verses.append(bible_verse)

        for verse in bible_verses:
            verse.save()

    def delete_bible_repo():
        remove_bible_directory = subprocess.run(["rm", "-rf", APP_CONSTANT['BIBLE-FILE-NAME']])
        if remove_bible_directory.returncode != 0:
            raise SystemCheckException(ERROR_CONSTANTS['GITHUB_DIR_DELETE_ERR'])

def bible_setup():
    [BibleVerse.drop_table(), BibleVerse.create_table(), BibleImporter.download_bible(), BibleImporter.import_bible()]