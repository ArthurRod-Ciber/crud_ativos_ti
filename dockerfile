FROM python:3.14-slim

LABEL maintainer="Arthur Rodrigues Carvalho"
LABEL project="CRUD gerenciamento de ativos"
LABEL version="1.0"

WORKDIR /app

COPY . .

CMD ["tail", "-f", "/dev/null" ]

