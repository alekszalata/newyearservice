FROM python:latest

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver","--noreload", "0.0.0.0:8000"]
