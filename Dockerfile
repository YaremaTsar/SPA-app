FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
ADD . /SPA-app
RUN pip install -r SPA-app/requirements.txt