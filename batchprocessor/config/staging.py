import logging

from .default import DefaultConfig

class StagingConfig(DefaultConfig):
    APP_ENV = "staging"
    LOG_LEVEL = logging.INFO
    ACCESS_KEY = ''
    SECRET_ACCESS_KEY = ''

    S3_BUCKET = '<your-bucket-name-here>'
    S3_KEY = 'flats-etl-processor/raw/{0}/{1}/'
    S3_FILE = ''
    OUTPUT_PATH = 'flats-etl-processor/clean'