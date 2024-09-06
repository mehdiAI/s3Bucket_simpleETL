"""
    Test s3 bucket connector methods
"""
import os
import unittest

import boto3
from moto import mock_s3

from sourceCode.common.s3 import S3BucketConnector

class TestS3BucketConnectorMethods(unittest.TestCase):
    """ 
        Testing the S3BucketConnector class
 
    """

    def setUp(self):
        """
            Setting up the enviroment
        """
        # mocking s3 connection start
        self.mock_s3 = mock_s3()
        self.mock_s3.start()
        # Defining the class arguments
        self.s3_access_key = 'SRC_ACCESS_KEY_ID'
        self.s3_secret_key = 'SRC_SECRET_KEY_ID'
        self.s3_endPoint_url = 'https://s3.test.com'
        self.s3_bucket_name = 'test_bucket'
        # creating s3 keys as environment variables
        os.environ[self.s3_access_key] = 'key1'
        os.environ[self.s3_secret_key] = 'key2'
        

    def tearDown(self):
        """
            Executing after unittests.
        """
        self.mock_s3.stop()
        # mocking s3 connection stop
        

    def test_list_s3bucketObjects_in_prefix_ok(self):
        """
            Tests the list_s3bucketObjects_in_prefix method for getting 2 file keys
            as list on the mocked s3 bucket
        """

    def test_list_s3bucketObjects_in_prefix_wrong_prefix(self):
        """
            Tests the list_s3bucketObjects_in_prefix method in case of a
            wrong or not existing prefix
        """


if __name__=="__main__":
    unittest.main()
