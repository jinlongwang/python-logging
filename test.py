# coding=utf-8
import logconfig

__author__ = 'jinlong'

loggers = {
    'loggers':{
        'test': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
logconfig.initialize_logging("test", "test", loggers)

import logging
logger = logging.getLogger('test')

logger.info("hehehe")
