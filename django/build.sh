#!/bin/bash
rm -rf */migrations
python manage.py makemigrations user
python manage.py makemigrations todolist
python manage.py migrate