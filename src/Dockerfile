FROM python:3.11-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

# Install dependencies
RUN apt-get update && apt-get install -y \
  git \
  wait-for-it

# Install python requirements
RUN pip install -r /usr/src/app/requirements.txt

ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]
