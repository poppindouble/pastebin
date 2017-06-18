## Setup
### 1. Install virtualenv via pip (if you don't have virtualenv):
```sh
$ pip install virtualenv
```
### 2. Activate virtualenv
```sh
$ source pastebin/bin/activate
```
### 3. Install requirements
```sh
$ pip install -r requirements.txt
```

## Run

```sh
$ export FLASK_APP=app/app.py
$ flask run
```

## Stop
```
ctrl+c
$ deactivate
```