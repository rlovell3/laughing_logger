import os
import logging
import laughing_logger
import sys

"""
Import notes:
# import os              // only required for os.path.basename(__file__) in example below.
# import logging        //only required for logging.{DEBUG, INFO, WARNING, ERROR, CRITICAL} in example below.
#                        You can pass integer values instead of logging.{DEBUG, INFO, WARNING, ERROR, CRITICAL} if you prefer.  
#                        Check the logging module for details.
import laughing_logger //only required to set up logging in ONE LINE OF CODE.  HA HA HA HA !!!!....
import sys             //only required for sys.exit('HA HA HA!!!...') in example below.
"""

if __name__=="__main__":
    # Logging in ONE LINE OF CODE.   HA HA HA HA !!!!....
    console_logger, file_logger = laughing_logger.set_up_my_logging(os.path.basename(__file__), logging.DEBUG, logging.ERROR, "test.log")

    """ 
    Above sets up tuple of 2 loggers: (console_logger, file_logger)
    console_logger will currently log to console  at DEBUG level because of 'logging.DEBUG' argument
    file_logger    will currently log to test.log at ERROR level because of 'logging.ERROR' argument
    You can set each logger's level to any of the generic logging levels:DEBUG, INFO, WARNING, ERROR, CRITICAL

    Arguments:  
    script_name:         name of script calling the laughing_logger module
                         This example uses os.path.basename(__file__) to get the name of the script for you, you lazy bum.
    console_log_level:   logging.{DEBUG, INFO, WARNING, ERROR, CRITICAL}
    file_log_level:      logging.{DEBUG, INFO, WARNING, ERROR, CRITICAL}
    logfile_name:        name of log file to write to.  If file does not exist, it will be created (assuming you have write permission).

    Returns:  tuple[console_logger, file_logger]

    Usage:  
    console_logger, file_logger = set_up_my_logging(os.path.basename(__file__), logging.CRITICAL, logging.ERROR, "test.log")
    console_logger.critical("Something terrible happened in my code")
    file_logger.critical("Something terrible happened in my code")
    sys.exit('HAHAHA')  # exits with return code HAHAHA.
    
    """


    # Example log messages in your code 
    console_logger.debug("This debug msg will appear on the console.")
    console_logger.info("This info msg will appear on the console.")
    console_logger.warning("This warning msg will appear on the console.")
    console_logger.error("This error msg will appear on the console.")
    console_logger.critical("This critical msg will appear on the console.")

    file_logger.debug("This debug msg will appear in the log file.")
    file_logger.info("This info msg will appear in the log file.")
    file_logger.warning("This warning msg will appear in the log file.")
    file_logger.error("This error msg will appear in the log file.")
    file_logger.critical("This critical msg will appear in the log file.")

    """
    Actual console output from above example log messages:
    2023-09-08 16:44 - test_logging.py - DEBUG - This debug msg will appear on the console.
    2023-09-08 16:44 - test_logging.py - INFO - This info msg will appear on the console.
    2023-09-08 16:44 - test_logging.py - WARNING - This warning msg will appear on the console.
    2023-09-08 16:44 - test_logging.py - ERROR - This error msg will appear on the console.
    2023-09-08 16:44 - test_logging.py - CRITICAL - This critical msg will appear on the console.


    cat test.log   # logger set to ERROR, so only ERROR and higher will be logged to file.
    2023-09-08 16:44 - test_logging.py - ERROR - This error msg will appear in the log file.
    2023-09-08 16:44 - test_logging.py - CRITICAL - This critical msg will appear in the log file.

    """


"""                                                                 
This Logging Level:         will print all log messages with its level and all higher levels
DEBUG                       PRINTS DEBUG, INFO, WARNING, ERROR, CRITICAL
INFO                        PRINTS        INFO, WARNING, ERROR, CRITICAL
WARNING                     PRINTS              WARNING, ERROR, CRITICAL
ERROR                       PRINTS                       ERROR, CRITICAL
CRITICAL                    PRINTS                              CRITICAL
"""
print("\U0001F602  \U0001F602 \U0001F602")  # Do you know what this does?  Better ask before you run this script.
sys.exit('\U0001F602')


