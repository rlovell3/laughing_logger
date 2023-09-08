# Laughing Logger &#x1F602;
## Set up Python logging in one friggin line of code  &#x1F923;;
    
### You need a few imports to really get your logging config down to one line.  Here they are:
```python
import logging
import laughing-logger
import os
```
You can cut that list down depending on how you deal with a few things in the one-liner.  See **test_logging.py** for complete details.

### Usage
After your imports, simply enter this one-liner to set up your entire logging framework:
<br>
<br>
```python
console_logger, file_logger = laughing_logger.set_up_my_logging(os.path.basename(__file__), logging.DEBUG, logging.ERROR, "test.log")
```

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




