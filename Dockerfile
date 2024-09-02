FROM apache/airflow:2.10.0
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  chromium \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install --no-cache-dir \
  selenium==4.24.0 \
  psycopg2==2.9.9 \
  pandas==2.2.2\
