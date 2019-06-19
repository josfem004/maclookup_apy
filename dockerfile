FROM python:2.7

ADD api.py /

CMD [ "python", "-u", "./api.py"]
