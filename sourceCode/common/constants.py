"""
    File to store constants.
"""

from enum import Enum

class S3FileTypes(Enum):
    """
        supported file types for S3BucketConnector.

    Args:
        Enum (_type_): _description_
    """
    CSV = 'csv'
    PARQUET = 'parquet'
    
class MetaProcessFormat(Enum):
    """
        Formation for MetaProcess class.
    """
    META_DATA_FORMAT = '%Y-%m-%d'
    META_PROCESS_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    META_PROCESSED_DATE_FILE_COL = 'processed_date_file'
    META_OBJECT_NAME_COL = 'object_name'
    META_INSERTING_DATE_COL = 'inserting_date'
    META_FILE_FORMAT = 'csv'