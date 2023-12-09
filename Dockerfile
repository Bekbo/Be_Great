FROM python:3.10-alpine


RUN mkdir Be_Great
WORKDIR Be_Great
ADD . /Be_Great/


RUN pip install -r requirements.txt
CMD python manage.py migrate

#CMD gunicorn BeGreat.wsgi:application -b 0.0.0.0:8000
