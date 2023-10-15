FROM python:3.8-slim
WORKDIR /app
COPY requeriments*.txt ./
RUN pip install --upgrade -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
