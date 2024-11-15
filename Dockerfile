FROM python:3.9 AS builder
RUN apt-get update && apt-get install -y gcc
COPY . .
RUN pip install -r requirements.txt

FROM python:3.9-slim
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . .
CMD ["python", "main.py"]
