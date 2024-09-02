from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import os
import sys
sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)))
from crawler_func import scrape
from database_func import insert_news
from model_func import ranking_news

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

dag = DAG(
    dag_id='ranking_news',
    default_args=default_args,
    start_date= datetime(2024, 9, 1),
    schedule_interval='@once',
    catchup=False
)

scrape_data = PythonOperator(
    task_id='scrape_data',
    python_callable=scrape,
    dag=dag
)

rank_news = PythonOperator(
    task_id="ranking_news",
    python_callable=ranking_news,
    op_args=[scrape_data.output],
    dag=dag
)

save_data = PythonOperator(
    task_id='save_data',
    python_callable=insert_news,
    op_args=[rank_news.output],
    dag=dag
)

scrape_data >> rank_news >> save_data