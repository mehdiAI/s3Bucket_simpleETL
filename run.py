"""
Running the ETL application
"""
import logging
import logging.config

import yaml

import os

def main():
    """
        Entry point to run the etl job.
    """
    cwd = os.getcwd()
    # Parsing TAML file
    config_path=cwd+'\\configs\\etl_report_config.yml'
    config = yaml.safe_load(open(config_path))
    # Configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    #logger.info('this is a info test log!')
    
if __name__=='__main__':
    main()