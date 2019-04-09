import logging
from .default import DefaultConfig

class ProductionConfig(DefaultConfig):
    APP_ENV = "production"
    LOG_LEVEL = logging.INFO

    # ACCESS KEY and SECRET KEY. This is not a best practice in any production environment to embed the keys
    # and the best practice is to use IAM role.
    ACCESS_KEY = ''
    SECRET_ACCESS_KEY = ''

    S3_BUCKET = '<your-bucket-name-here>'
    S3_KEY = 'flats-etl-processor/raw/{0}/{1}/'
    S3_FILE = ''
    OUTPUT_PATH = 'flats-etl-processor/clean'
