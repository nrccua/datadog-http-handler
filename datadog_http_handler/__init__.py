
from datetime import datetime
import logging
from logging import StreamHandler

import requests

def define_logger(logger_name, msg_fmt, level):
    '''Setup logger with msg formatting and logging level.'''

    if msg_fmt is None:
        msg_fmt = '%(asctime)s.%(msecs)03d %(levelname)s - %(message)s'
    if level is None:
        level = logging.INFO

    return logging.getLogger(logger_name), msg_fmt, level

class DatadogHttpHandler:

    def __init__(self, api_key, service, host='', source='', tags={},
                 logger_name=None, msg_fmt=None, level=None, raise_exception=False):

        self.logger, msg_fmt, level = define_logger(logger_name, msg_fmt, level)
        tags = ','.join([f"{k}:{v}" for k, v in tags.items()])
        handler = DataDogHandler(api_key, raise_exception, service, host, tags, source)
        handler.setLevel(level)
        self.logger.setLevel(level)
        self.logger.addHandler(handler)


class DataDogHandler(StreamHandler):
    '''Send log messages to Datadog via http requests.'''

    def __init__(self, api_key, raise_exception, service='', host='', tags='', source=''):
        StreamHandler.__init__(self)
        self.api_key = api_key
        self.service = service
        self.host = host
        self.source = source
        self.tags = tags
        self.raise_exception = raise_exception
        self.headers = {'Content-Type': 'application/json'}
        self.url = f"https://http-intake.logs.datadoghq.com/v1/input/{api_key}"

    def emit(self, record):

        date = datetime.utcfromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        payload = {'message': record.msg, 'level': record.levelname}
        payload['ddtags'] = self.tags + f",datetime:{date}" if self.tags else f"datetime:{date}"
        if self.service:
            payload['service'] = self.service
        if self.host:
            payload['hostname'] = self.host
        if self.source:
            payload['ddsource'] = self.source

        try:
            response = requests.post(self.url, json=payload, headers=self.headers)
            if response.status_code != 200 and self.raise_exception:
                raise Exception('Failed sending logs to Datadog')
        except requests.exceptions.RequestException as err:
            if self.raise_exception:
                raise Exception(err)
