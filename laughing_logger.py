# laughing_logger.py - A Python script to set up logging for your own python scripts.
# laughing_logger.py
# Python script to easily set up logging with a console logger and file logger.
# Includes custom log levels and formatting.
# Depends on the logging module and the enum module.  

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


# Let's get into it, shall we?   Ha Ha Ha!!!!
import logging
from enum import Enum
from pathlib import Path


class LaughingLogLevel(Enum):
    """
    Simple enumeration of logging levels.  
    LaughingLogLevel.{DEBUG, INFO, WARNING, ERROR, CRITICAL} 
    are equivalent to logging.{DEBUG, INFO, WARNING, ERROR, CRITICAL}
    """
    DEBUG    = 10
    INFO     = 20 
    WARNING  = 30
    ERROR    = 40
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
    if not isinstance(console_log_level, int):
        console_log_level = int(console_log_level)
    
    if not isinstance(file_log_level, int):
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
    """ 
    Call laughing_logger.set_up_my_logging(parameters) from within your script.  
    Arguments:  calling script name: str
                console log level: LaughingLogLevel.{DEBUG, INFO, WARNING, ERROR, CRITICAL}
                file log level: LaughingLogLevel.{DEBUG, INFO, WARNING, ERROR, CRITICAL}
                logfile: str
    
    Calling Script Name:  This should be the name of the script you are writing.  It will be used in the log file to help trace where the log message came from.
    Console log level:  This is the log level for the console logger.  The console logger is the logger that prints to the console.  
                        The console logger will print to the console regardless of the log level set for the file logger.
    File log level:  This is the log level for the file logger.  The file logger will print to the file regardless of the log level set for the console logger.
    Logfile:  This is the name of the log file.  The file logger will write to the file if the path is writable by the user.  If the path is not writable, the file logger will not write to the file.
    Log_level choices:  Each of your two loggers has its reporting detail set in the instantiation of the loggers:
    
    This Logging Level:         will print all log messages with its level and all higher levels
    DEBUG                       PRINTS DEBUG, INFO, WARNING, ERROR, CRITICAL
    INFO                        PRINTS        INFO, WARNING, ERROR, CRITICAL
    WARNING                     PRINTS              WARNING, ERROR, CRITICAL
    ERROR                       PRINTS                       ERROR, CRITICAL
    CRITICAL                    PRINTS                              CRITICAL
                 
    # Examples:
    console_logger, file_logger = laughing_logger.set_up_my_logging("your_script_name.py", LaughingLogLevel.DEBUG, LaughingLogLevel.INFO, "my_logfile.txt")
    
    or use the os module to report the calling script name for you.
    console_logger, file_logger = laughing_logger.set_up_my_logging(os.path.basename(__file__), LaughingLogLevel.ERROR, LaughingLogLevel.CRITICAL, "my_logfile.txt")
    """

    logfile = Path("hahahahaha.log")
    console_logger, file_logger = set_up_my_logging("laughing_logger.py", LaughingLogLevel.DEBUG, LaughingLogLevel.INFO, logfile)

    # Example logging statements to use in your code:
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


    
