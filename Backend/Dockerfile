# 1. Correção da tag do Python
FROM python:3.9-slim

WORKDIR /app

# 2. Ajustado para o nome real do seu arquivo (sem o .txt se ele for apenas 'requirements')
COPY requirements .

RUN pip install --no-cache-dir -r requirements

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]