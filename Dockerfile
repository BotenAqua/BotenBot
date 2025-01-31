FROM python:3.9.21-slim AS builder
RUN apt-get update && apt-get install -y gcc
COPY . .
RUN pip install -r requirements.txt

FROM python:3.9.21-slim
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . .
CMD ["python", "main.py"]

