
#!/bin/sh

export FLASK_APP=./Restful_API/main.py

source $(pipenv --venv)/bin/activate

flask run -h 0.0.0.0