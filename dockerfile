FROM python:3.9.11

COPY . .
EXPOSE 8000
CMD ["python","server.py"]