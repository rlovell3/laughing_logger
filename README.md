# Laughing Logger &#x1F602;
## Set up Python logging in one friggin line of code  &#x1F923;;

### BREAKING CHANGES
This code was initially released on 2023-09-08.  The set_up function was changed later that night
to handle setting the logging levels without needing to import the logging module.  This is a breaking change.
If you have been using the code from 2023-09-08, you will need to update the language of your arguments to the set_up function.
See **test_logging.py** for complete details.

### You need a few imports to really get your logging config down to one line.  Here they are:
```python
import laughing-logger
import os
```
You can remove os depending on how you deal with passing the name of your calling script to the setup function.  See **test_logging.py** for complete details.

### Usage
After your imports, simply enter this one-liner to set up your entire logging framework:
<br>
<br>
```python
console_logger, file_logger = laughing_logger.set_up_my_logging(os.path.basename(__file__), laughing_logger.LaughingLogLevel.DEBUG, laughing_logger.LaughingLogLevel.ERROR, "test.log")

```
<br>
You can use integers instad of laughing_logger.LaughingLogLevel.{DEBUG, INFO, WARNING, ERROR, CRITICAL}
The integers are defined in the logging module as DEBUG=10, INFO=20, WARNING=30, ERROR=40, CRITICAL=50.
<br>
That one-line setup gives you two loggers:
- one for logging to the console
- one for logging to a file

Adjustable Logging levels (in order of detail):
- logging.DEBUG     Max detail
- logging.INFO      a bit less detail
- logging.WARNING   even less detail
- logging.ERROR     You probably won't ever need this one
- logging.CRITICAL  For when something breaks and you need to capture any details you can.

Set each logger in the one-line setup command to the levels you want to deal with for debugging.
Later, once you code is ready for production, bump up the logging levels
to capture only the detail you need.  

You only need to change the one-line setup to adjust the levels of all your logging output.

<br>
Output is formatted to include the name of the running program and a timestamp (without microseconds).  It is a format that I just ccouldn't find in any of the examples.
<br>
Formatting is set by this attribute:
<br>

```python
('%(asctime)s - %(script_name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M'))
```

<br>
See test_logging.py for a complete example of importing, setting up, and using.




