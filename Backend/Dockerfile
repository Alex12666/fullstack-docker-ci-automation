FROM python:3.9-slim

WORKDIR /app

# Adicione o .txt aqui na linha 7
COPY requirements.txt .

# Adicione o .txt aqui na linha 9 também
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]