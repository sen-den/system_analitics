# IAS for educational ratings

## Prerequisites 
1. Python3+
1. pyenv

## Initial setup
1. Checkout source code
1. Navigate to the project root dir
1. Create virtualenv `pyenv virtualenv system-analitics`
1. Activate virtualenv `pyenv activate system-analitics`
1. Install recruitments `pip install -r recruitments.txt`
1. Run database migrations `python ./manage.py migrate`
1. Create superuser `python ./manage.py createsuperuser`

## On model update
1. Create migration `python ./manage.py makemigrations`
