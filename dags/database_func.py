import psycopg2
import psycopg2.extras
from datetime import datetime
import pandas as pd

PG_USER = 'postgres'
PG_PASSWORD = 'banlaso1'
PG_HOST = 'localhost'
PG_PORT = '5432'
PG_DATABASE = 'news'


def insert_news(news_list):
    conn = psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        user=PG_USER,
        password=PG_PASSWORD,
        dbname=PG_DATABASE
    )
    cur = conn.cursor()

    delete_query = 'DELETE FROM news_data'
    cur.execute(delete_query)

    insert_query = '''
    INSERT INTO news_data (title, url, like_count, time)
    VALUES %s
    '''

    records = [
        (news['Title'], news['Url'], news['Like'], datetime.strptime(news['Time'], '%Y-%m-%d %H:%M:%S'))
        for news in news_list
    ]

    psycopg2.extras.execute_values(cur, insert_query, records)
    conn.commit()
    conn.close()


def fetch_news_data():
    conn = psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        user=PG_USER,
        password=PG_PASSWORD,
        dbname=PG_DATABASE
    )
    cur = conn.cursor()

    query = 'SELECT title, url, like_count, time FROM news_data'
    df = pd.read_sql(query, conn)

    conn.close()

    return df

