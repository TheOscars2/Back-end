# Simple Flask Server for APPetite

Some helpful commands:
## If you're checking out a clean repo.
```
python3 -m venv venv;
. venv/bin/activate;
pip install -r requirements.txt;
```
- Git clean makes sure you don't have any extra files living in your directory.

## Before getting started
Make sure to `cd` into the appropriate file directory.  All subsequent commands
assume this has happened.
```
. venv/bin/activate;
```

# Adding a dependency
Suppose you just `pip install`'d something and want it to stick!  From the root
of the repository:
```
pip freeze > requirements.txt;
```

and after pulling elsewhere:
```
pip install -r requirements.txt;
```

# To use locally
```
FLASK_APP=app.py flask run --port 4000;
```
