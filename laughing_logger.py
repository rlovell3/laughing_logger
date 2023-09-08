
import os
import logging


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
    
    #add the following lines to your program.
    console_logger, file_logger = set_up_my_logging(os.path.basename(__file__), logging.DEBUG, logging.INFO, "test.log")

    # Test loggers
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
    
