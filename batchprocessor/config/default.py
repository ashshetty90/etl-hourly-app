import logging

class DefaultConfig():
    AWS_REGION_NAME = 'ap-southeast-1'
    LOG_LEVEL = logging.DEBUG
    
   

    # ACCESS KEY and SECRET KEY. This is not a best practice in any production environment to embed the keys
    # and the best practice is to use IAM role.
    ACCESS_KEY = ''
    SECRET_ACCESS_KEY = ''  

    S3_FILE = ''
    OUTPUT_PATH = ''
