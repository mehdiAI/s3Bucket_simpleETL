"""Connector and methods accessing s3
"""
import boto3 # type: ignore

import os
import logging


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
        self._logger = logging.getLogger(__name__) 
        self.access_key = access_key
        self.secret_key = secret_key
        self.enfpoint_url = enfpoint_url
        self.bucket = bucket
        self.session = boto3.Session(aws_access_key_id=access_key,
                                     aws_secret_access_key=secret_key)
        self._s3 = self.session.resource(service_name='s3',enfpoint_url=enfpoint_url)
        self._bucket = self._s3.Bucket(bucket)
    
    def preparing_s3Bucket_BucketObj_openDataset(self):
        pass
    
    def preparing_s3Bucket(self):
        pass
    
    def assignDate_s3BucketObj(startDate,date_format,bucketObj_list):
        """ covid19-harmonized-dataset in aws free dataset dont have date in files name then this 
        function create a artificial date for each it object to use them to loading data section based on date.

        Args:
            startDate (str): start of date to assigning to each Object.
            date_format (str): standard of data format.
            bocketObj_list (list): list of s3 bucket objects.

        Returns:
            pandas DataFrame: a table with date and s3 bucket objects columns.
        """
        pass
    
    def retrieveObjectFromS3Bucket(self):
        """
            Retrieve list all objects on the s3 bucket.
            
            return: none and just print it in the output.
        """
        for obj in self._bucket.objects.all():
            print(f"object_name: {obj.key} , last_modified: {obj.last_modified}") 
        
    def list_s3bucketObjects_in_prefix(self,key_prefix:str):
        """
            Retrieve list all objects with prefix filter on the s3 bucket.
            this filter involve om the s3 bucket keys.
            arg1: key_prefix is a string to use filtering.
            return: a list of the s3 bucket objects.
        """
        files = [obj.key for obj in self._bucket.objects.filter(Prefix=key_prefix)]
        return files
    
    def read_csv_to_df(self):
        pass
    
    def read_parquet_to_df(self):
        pass
    
    def write_df_to_parquetObjS3(self):
        pass
    
    def write_df_to_csvObjS3(self):
        pass