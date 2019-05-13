# datadog-http-handler

Python logging module allowing you to log directly to Datadog via https.
urrently support only for python 3.6+.

## Installation

Install [python 3.7.2+](https://www.python.org/downloads/)

Install [pip](https://pip.pypa.io/en/stable/installing/)
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

Install datadog-http-handler
```bash
pip install git+https://github.com/nrccua/datadog-http-handler.git
```

## Usage

The typical usage of this library to output to datadog

```bash
from pylogs import DatadogHttpHandler

logger = DatadogHttpHandler(api_key='<DATADOG_API_KEY>', service='test', host='your_hostname',
                            logger_name='example', tags={'env': 'test', 'user': 'Tim the Enchanter'})
logger.info('Hello World')
```

## AUTHORS

* **Tim Reichard**

See also the list of [contributors](https://github.com/nrccua/pylogs/contributors) who participated in this project.

## ACKNOWLEDGEMENTS

* **Bryan Cusatis** - NRCCUA Architecture Team Lead
