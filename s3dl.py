import json
import os
from datetime import datetime

import boto3


class S3FileDownloader:
    def __init__(self):
        super().__init__()
        self.rootdir = os.path.join(
            os.getcwd(), datetime.now().strftime('%Y%m%d_%H%M%S'))

        settings = json.load(
            open('setting\s3dl.json', 'r', encoding='utf-8'))

        self.__s3rs = boto3.resource(
            's3',
            aws_access_key_id=settings['accessKeyId'],
            aws_secret_access_key=settings['secretAccessKey'],
        )

    def download(self, bucket_name: str, s3_directory_names: list) -> str:
        dlrootdir = self.__mkdir(self.rootdir, bucket_name)
        bucket = self.__s3rs.Bucket(bucket_name)

        for s3dirname in s3_directory_names:
            subdir = self.__mkdir(dlrootdir, s3dirname)
            for s3obj in bucket.objects.filter(Prefix=s3dirname):
                print(f'download {s3obj.key}')
                bucket.download_file(
                    s3obj.key, os.path.join(dlrootdir, s3obj.key))

        return dlrootdir

    def __mkdir(self, root: str, dir_name: str) -> str:
        d = os.path.join(root, dir_name)
        if not os.path.exists(d):
            os.makedirs(d)
        return d
