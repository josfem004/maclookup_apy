FROM python:latest

WORKDIR ~/maclookup_apy

COPY api.py .

CMD ["api.py"]