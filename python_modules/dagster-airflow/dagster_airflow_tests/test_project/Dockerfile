FROM python:3.7

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

ENTRYPOINT [ "dagit" ]

CMD [ "--help" ]

EXPOSE 3000
