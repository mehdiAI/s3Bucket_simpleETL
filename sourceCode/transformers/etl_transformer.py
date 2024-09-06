"""
   ETL component 
"""
import logging
from typing import NamedTuple

from sourceCode.common.s3 import S3BucketConnector


class EtlSourceConfig(NamedTuple):
    pass

class SourceConfig(NamedTuple):
    """
    Class for source configuration data

    src_first_extract_date: determines the date for extracting the source
    #src_columns: source column names
    src_col_date: column name for date in source
    src_col_isin: column name for isin in source
    src_col_time: column name for time in source

    """
    src_first_extract_date: str
    #src_columns: list
    src_col_date: str
    src_col_isin: str
    src_col_time: str



class TargetConfig(NamedTuple):
    """
    Class for target configuration data

    trg_col_isin: column name for isin in target
    trg_col_date: column name for date in target
    trg_key: basic key of target file
    trg_key_date_format: date format of target file key
    trg_format: file format of the target file
    """
    trg_col_isin: str
    trg_col_date: str
    trg_key: str
    trg_key_date_format: str
    trg_format: str

class ETL():
    """
    Reads the data, transforms and writes the transformed to target
    """

    def __init__(self, s3_bucket_src: S3BucketConnector,
                 s3_bucket_trg: S3BucketConnector, meta_key: str,
                 src_args: SourceConfig, trg_args: TargetConfig):
        """
        Constructor for XetraTransformer

        :param s3_bucket_src: connection to source S3 bucket
        :param s3_bucket_trg: connection to target S3 bucket
        :param meta_key: used as self.meta_key -> key of meta file
        :param src_args: NamedTouple class with source configuration data
        :param trg_args: NamedTouple class with target configuration data
        """
        self._logger = logging.getLogger(__name__) 
        self.s3_bucket_src = s3_bucket_src
        self.s3_bucket_trg = s3_bucket_trg
        self.meta_key = meta_key
        self.src_args = src_args
        self.trg_args = trg_args
        self.extract_date =
        self.extract_date_list =
        self.meta_update_list = 
    
    def extract(self):
        pass

    def transform_report1(self):
        pass
    
    def load(self):
        pass
    
    def etl_report1(self):
        pass