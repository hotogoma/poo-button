import os
import json
import urllib.request


def handler(event, context):
    data = {
        'text': 'うんち！',
        'username': 'うんちメモリーズ',
        'icon_emoji': ':poop:',
    }

    url = os.environ.get('SLACK_INCOMING_WEBHOOK_URL')
    data = json.dumps(data).encode('ascii')
    req = urllib.request.Request(url, data)
    urllib.request.urlopen(req)
