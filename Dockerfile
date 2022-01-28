FROM python:3.10-slim-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Setup app
RUN mkdir -p /app
WORKDIR /app
COPY models /app/models
COPY routes /app/routes
COPY index.py /app
COPY db.py /app
COPY .env /app

CMD ["python", "index.py"]