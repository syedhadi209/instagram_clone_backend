FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir /instagram_clone
WORKDIR /instagram_clone
COPY . /instagram_clone/
RUN pip install -r requirements.txt
EXPOSE 8000

CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]
