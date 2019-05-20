
import logging
import os

import pytest

from datadog_http_handler import DatadogHttpHandler

@pytest.fixture
def datadog_logger():
    '''Make sure you have set the environment variable
    DATADOG_API_KEY (export DATADOG_API_KEY=<your_key>).'''
    
    return DatadogHttpHandler(
        api_key=os.getenv('DATADOG_API_KEY', ''),
        raise_exception=True,
        service='test',
        host='your_hostname',
        logger_name='example',
        tags={'env': 'test', 'user': 'Tim the Enchanter'}
    ).logger

@pytest.fixture
def bad_datadog_logger():
    '''Give a fake api_key to DatadogHttpHandler.'''
    
    return DatadogHttpHandler(
        api_key='bad_key',
        raise_exception=True,
        service='test',
        host='your_hostname',
        logger_name='example',
        tags={'env': 'test', 'user': 'Tim the Enchanter'}
    ).logger

def test_logger_has_handler(datadog_logger):
    '''Check if the logger has any handler added.'''

    assert(datadog_logger.hasHandlers()) is True
    
def test_good_datadog_logging_response(datadog_logger):
    '''Check if sending datadog response throws an exception, if not then message is
    assumed received in datadog logs since it received a 200 response.'''

    datadog_logger.info('Hello World')

@pytest.mark.xfail
def test_bad_datadog_logging_response(bad_datadog_logger):
    '''Check if sending datadog response throws an exception, if not then message is
    assumed received in datadog logs since it received a 200 response.'''

    bad_datadog_logger.info('Hello World')