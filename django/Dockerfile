FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /todo/django
ADD requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5894