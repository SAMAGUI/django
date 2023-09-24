FROM python:3.11.2

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8000/ || exit 1

CMD [ "python", "manage.py","runserver","0.0.0.0:8000" ]