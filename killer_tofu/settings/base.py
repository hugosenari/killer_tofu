LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'killer_tofu/.log/debug.log',
            'maxBytes': 50 * 1024 * 1024,
            'backupCount': 10
        },
    },
    'loggers': {
        '': {
            'handlers': ['logfile'],
            'level': 'DEBUG'
        },
        'project': {
            'level': 'INFO',
            'propagate': True,
        },
    }
}