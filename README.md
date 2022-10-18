**Bible Importer**
-----------------
This is a simple project that accomplishes three things:
* Creates database with bible verses. The schema is simply language, book, chapter, verse.
* API to support searching of verses and verse ranges. (In progress)

*How to run*
-----------
Containerization is provided for the project in the form of a docker compose. On initial run you can use:
```bash
docker-compose up --build
```
After initial build, you can stick to
```bash
docker-compose up
```

If you don't want to run in a containerized space, you can run (preferably using venv):
```bash
python main.py
```
You will have to set up some environment variables for the database connection. The specific name of those variables are specificed in models.py