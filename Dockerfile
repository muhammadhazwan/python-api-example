FROM python:3.9

WORKDIR /app

COPY ./ /app/

RUN pip install pip --upgrade && pip install --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 8000:8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]