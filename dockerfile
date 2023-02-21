FROM python:3.9.11
WORKDIR /app
COPY . .
EXPOSE 8000
RUN pip install -r requirements.txt
CMD ["python","./server.py"]