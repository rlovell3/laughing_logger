# Laughing Logger &#x1F602;
## Set up Python logging in one friggin line of code  &#x1F923;;

You need a few imports to really get your logging config down to one line.  Here they are:
```python
import laughing-logger
import os
```
You can remove __import os__ depending on how you deal with passing the name of your calling script to the setup function.  See **test_logging.py** for complete details.  

### Usage
After your imports, simply enter this one-liner to set up your entire logging framework:   
```python
console_logger, file_logger = laughing_logger.set_up_my_logging(os.path.basename(__file__), laughing_logger.LaughingLogLevel.DEBUG, laughing_logger.LaughingLogLevel.ERROR, "test.log")

```

The one-liner gives you two loggers:  
- console_logger for logging to the console
- file_logger for logging to a file

Adjustable Logging levels (in order of detail):
- logging.DEBUG     Max detail
- logging.INFO      a bit less detail
- logging.WARNING   even less detail
- logging.ERROR     You probably won't ever need this one  (HA HA HAHAAAAAA.....)
- logging.CRITICAL  The most quiet setting.  You really don't like feedback, do you?  

Set each logger in the one-line setup command to the detail levels you want while coding.  I use DEBUG initially. Later, once you code is ready for production, bump up the logging levels to capture only the detail you need.  

You only need to change the one-line setup to adjust the all your logging output.  

Output is formatted to include the name of the running program and a timestamp (without microseconds).  It is a format that I just couldn't find in any of the examples online. Plus, I didn't like having to do it all every time I started a new project.  

Formatting, if you care, is set by this attribute:  


```python
('%(asctime)s - %(script_name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M'))
```


See **sample_logging.py** for a complete example of importing, setting up, and using.  
HA HA HA HAHAAAAAA...




