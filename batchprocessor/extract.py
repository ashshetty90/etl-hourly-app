import json
import zipfile
import s3fs,boto3

from .log import getLogger
from .config import Config

LOG = getLogger(__name__)

class Extract:
    def __init__(self, s3_bucket_name, s3_key):
        self.s3_bucket_name = s3_bucket_name
        self.s3_key = s3_key

    def load(self):
        payload = []
        s3 = boto3.resource("s3")
        s3_bucket = s3.Bucket(Config.S3_BUCKET)
        for s3_object in s3_bucket.objects.filter(Prefix="flats-etl-processor/raw/2019-04-07/00/"):
            if s3_object.key.endswith('.json.zip'):
                s3_filesystem = s3fs.S3FileSystem(key=Config.ACCESS_KEY,
                                          secret=Config.SECRET_ACCESS_KEY)
                path = "s3://" + self.s3_bucket_name + "/"+ s3_object.key
                LOG.info("Processing file %s",path)
                with s3_filesystem.open(path, "rb") as s3_file:
                    with zipfile.ZipFile(s3_file, "r") as unzipped_file:
                        for filename in unzipped_file.namelist():
                            with unzipped_file.open(filename) as f:
                                for line in f:
                                    payload.append(json.loads(line))
                
           
        # my_bucket = self.s3.bucket(Config.S3_BUCKET).objects(prefix:'flats-etl-processor/raw/2019-04-07/00/', delimiter: '')
                    
        return payload
