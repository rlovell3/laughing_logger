# laughing_logger.py - A Python script to set up logging for your own python scripts.
# Depends on the logging module.  

# Copyright 2023 by Ross Lovell.  All Rights Reserved.
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Ross Lovell
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# ROSS LOVELL DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# ROSS LOVELL BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
# ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.



# The laughing_logger.py depends upon the logging module.  
# The logging module is part of the standard library.
# The logging module's license must be honored if you use this code.

# copy of logging module's license:
# Copyright 2001-2019 by Vinay Sajip. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Vinay Sajip
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# VINAY SAJIP DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# VINAY SAJIP BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
# ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
    

# Let's get into it, shall we?   Ha Ha Ha!!!!
import logging
from enum import Enum


class LaughingLogLevel(Enum):
    """
    Simple enumeration of logging levels.  
    LaughingLogLevel.{DEBUG, INFO, WARNING, ERROR, CRITICAL} 
    are equivalent to logging.{DEBUG, INFO, WARNING, ERROR, CRITICAL}
    """
    DEBUG = 10
    INFO = 20 
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
    
    def __int__(self):
        return self.value


class ScriptNameFilter(logging.Filter):
    """Class to inject script_name into log records"""
    def __init__(self, script_name):
        self.script_name = script_name

    def filter(self, record):
        record.script_name = self.script_name
        return True

# Function to set up logging
def set_up_my_logging(script_name: str, console_log_level: int, file_log_level: int, logfile: str) -> tuple[logging.Logger, logging.Logger]:
    """Function to set up logging
    Arguments:  script_name, console_log_level, file_log_level, logfile
    LOGGING choices: logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL
    Returns:  console_logger, file_logger
    Usage:  console_logger, file_logger = set_up_my_logging(os.path.basename(__file__), logging.DEBUG, logging.INFO, "test.log")
    """
    
    # convert console_log_level and file_log_level to int
    console_log_level = int(console_log_level)
    file_log_level = int(file_log_level)


    # Initialize logging filters
    script_name_filter = ScriptNameFilter(script_name)
    # Create and configure console logger
    console_logger = logging.getLogger("console_logger")
    console_logger.setLevel(console_log_level)
    console_handler = logging.StreamHandler()
    console_handler.addFilter(script_name_filter)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(script_name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M'))
    console_logger.addHandler(console_handler)
    
    # Create and configure file logger
    file_logger = logging.getLogger("file_logger")
    file_logger.setLevel(file_log_level)
    file_handler = logging.FileHandler(logfile)
    file_handler.addFilter(script_name_filter)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(script_name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M'))
    file_logger.addHandler(file_handler)

    return console_logger, file_logger

if __name__ == '__main__':
    """ call the logging function.  
    Arguments:  calling script name, console_log_level, file_log_level, logfile
    Log_level choices: logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL"""
    
    #add the following line to your program.
    console_logger, file_logger = set_up_my_logging("laughing_logger.py", LaughingLogLevel.DEBUG, LaughingLogLevel.INFO, "test.log")

    # Example loggers to use in your code
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
    
