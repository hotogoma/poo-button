import os
import json
import urllib.request
import psycopg2


EVENT_TYPE = 'poo'


def save_to_db():
    dsn = os.environ.get('DATABASE_URL')
    with psycopg2.connect(dsn) as conn:
        with conn.cursor() as cur:
            query = 'INSERT INTO data.baby_events (type) VALUES (%s)'
            cur.execute(query, (EVENT_TYPE,))
        conn.commit()


def post_to_slack():
    data = {
        'text': 'うんち！',
        'username': 'うんちメモリーズ',
        'icon_emoji': ':poop:',
    }

    url = os.environ.get('SLACK_INCOMING_WEBHOOK_URL')
    data = json.dumps(data).encode('ascii')
    req = urllib.request.Request(url, data)
    urllib.request.urlopen(req)


def post_to_pixela():
    url = '{}/decrement'.format(os.environ.get('PIXELA_GRAPH_URL'))
    headers = {
        'Content-Length': 0,
        'X-User-Token': os.environ.get('PIXELA_API_TOKEN'),
    }
    req = urllib.request.Request(url, None, headers, method='put')
    urllib.request.urlopen(req)


def handler(event, context):
    save_to_db()
    post_to_slack()
    post_to_pixela()
