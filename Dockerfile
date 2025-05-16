FROM python:3.9-alpine AS builder
RUN apk add --no-cache gcc musl-dev
COPY . .
RUN pip install -r requirements.txt

FROM python:3.9-alpine
COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY . .
CMD ["python", "main.py"]
