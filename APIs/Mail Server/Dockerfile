FROM python:3-alpine3.12
WORKDIR /app
COPY . .
RUN apk add --update --no-cache --virtual .build-deps \
g++ \
libxml2 \
libxml2-dev && \
apk add libxslt-dev && \
pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 105