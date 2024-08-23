"""Connector and methods accessing s3
"""
import boto3 # type: ignore

import os



class S3BucketConnector():
    """ 
        Class for interacting with S3 Buckets.
    """
    
    def __init__(self, access_key:str, secret_key:str, enfpoint_url:str, bucket:str) -> None:
        """
            Constructor for S3BucketConnector
            
            var1 access_key: access key for connecting to s3 bucket in the provider.
            var2 secret_key: secret key for connecting to s3 bucket in the provider.
            var3 enfpoint_url: enfpoint_url for connecting to s3 bucket in the provider.
            var4 bucket: bucket is a name of bucket for connecting to s3 in the provider.
        """    
        self.access_key = access_key
        self.secret_key = secret_key
        self.enfpoint_url = enfpoint_url
        self.bucket = bucket
        self.session = boto3.Session(aws_access_key_id=access_key,
                                     aws_secret_access_key=secret_key)
        self._s3 = self.session.resource(service_name='s3',enfpoint_url=enfpoint_url)
        self._bucket = self._s3.Bucket(bucket)
        
    def retrieveObjectFromS3Bucket(self):
        pass
        
    def list_s3bucketObjects_in_prefix(self):
        pass
    
    def read_csv_to_df(self):
        pass
    
    def read_parquet_to_df(self):
        pass
    
    def write_df_to_parquetObjS3(self):
        pass
    
    def write_df_to_csvObjS3(self):
        pass