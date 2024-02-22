FROM python:3.11.2-buster
# Install necessary system packages
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev-compat \
    pkg-config
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000