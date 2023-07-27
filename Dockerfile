FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
COPY manage.py /app/
COPY tests /app/tests
COPY templates /app/templates
COPY static /app/static
COPY quitter /app/quitter
CMD ["gunicorn", "--bind=0.0.0.0:8000", "quitter.wsgi:application"]
