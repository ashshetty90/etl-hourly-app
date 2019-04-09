"""
Main app for hourly etl  app

Usage:
    app.py --env=<env>
    app.py (-h | --help)
    app.py ( --version | -v )

Options:
  -h --help     Show this screen.
  --version     Show version.
  --env=ENV     The environment name [default: dev].

"""
from docopt import docopt, DocoptExit
from batchprocessor import VERSION
import os
import signal
from functools import partial
import sys
import boto3


DEFAULT_APP_ENV = "development"
        
if __name__ == "__main__":
        try:
            arguments = docopt(__doc__, version="hourly-etl-app %s" % VERSION)
            os.environ["APP_ENV"] = arguments.get("--env", DEFAULT_APP_ENV)
        except DocoptExit:
            print("something wrong")


from batchprocessor.log import getLogger
from batchprocessor.processor import Processor 
from batchprocessor.config import Config

LOG = getLogger("batchprocessor")
boto3.setup_default_session(region_name=Config.AWS_REGION_NAME)

def start():
    LOG.info("Starting in %s", Config.APP_ENV)
    try:
        processor = Processor(Config.S3_BUCKET,Config.S3_KEY, output_path=Config.OUTPUT_PATH)
        processor.process()
    except Exception:
        LOG.warning("Unable to process (%s, %s):",
                            Config.S3_BUCKET,Config.S3_KEY, exc_info=True)    
    except Exception:
        LOG.exception("Shutting down due to an unhandled exception:")
    
if __name__ == "__main__":
    print("Starting the app..")
    start()