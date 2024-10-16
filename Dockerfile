
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/streamlit/streamlit-example.git .

RUN pip3 install -r requirements.txt

EXPOSE 8690

HEALTHCHECK CMD curl --fail http://localhost:8690/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8690", "--server.address=0.0.0.0"]
