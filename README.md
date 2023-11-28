# Laughing Logger &#x1F602;
## Set up Python logging in one friggin line of code  &#x1F923;;

You need a few imports to really get your logging config down to one line.  Here they are:
```python
import laughing-logger
import os
```
You can remove "__import os__" depending on how you deal with passing the name of your calling script to the setup function.  See __test_logging.py__ for complete details.  


## Usage
After your imports, simply enter this one-liner to set up your entire logging framework:  
```python
console_logger, file_logger = laughing_logger.set_up_my_logging(os.path.basename(__file__), laughing_logger.LaughingLogLevel.DEBUG, laughing_logger.LaughingLogLevel.ERROR, "test.log")

```

The one-liner gives you two loggers:  
- "console_logger" for logging to the console
- "file_logger" for logging to a file

## The Levels
Adjustable Logging levels (in order of detail):
- "DEBUG"     Max detail
- "INFO"      a bit less detail
- "WARNING"   even less detail
- "ERROR"  You probably won't ever need this one  (HA HA HAHAAAAAA.....)
- "CRITICAL"  The most quiet setting.  You really don't like feedback, do you?  

Set the two loggers in the one-line instantiation to the detail levels you want while coding.  I use DEBUG initially. Later, once code is ready for production, bump up the logging levels to capture only the detail you need, like "__INFO__" or "__CRITICAL__".  

You only need to change the one-line setup to adjust all your logging output. Think of the one-liner as a logging filter.  

## Down in the code...
Throughout your code, you will add logging statements.  If you normally use a print statement to debug, use a logging statement instead, and set its logging level to debug.  

For screen and file output that you want whether you are in debug mode or full production, choose a logging level for each statement that is aligned with your needs. The higher the level, the less filtered it becomes.  

For example, let's examine these three logging statements buried somewhere in your code:  
`console_logger.debug(f"debug me: {infile}")`  
`console_logger.error(f"some error: {infile}")`  
`console_logger.critical(f"mission critical: {issue}")`  
Up top, in your instantiation, while your console_logger is set to DEBUG, all three statements will print to console.  

But once you change the level up in the instantiation call to, let's say, ERROR, only the second and third statements will print.  If you change the instantiation call to CRITICAL, only the third statement will print.  

This is the essence of hierarchical logging. All your buried logging statements get set up as you write code.  You filter them out simply by changing the logging levels up in your instantiation of the function.


## Output
Output is formatted to include the name of the running program and a timestamp (without microseconds).  It is a format that I just couldn't find in any of the examples online. Plus, I didn't like having to do it all every time I started a new project.  

#### Actual console output from above example log messages with console_logger set to DEBUG level:  
    2023-09-09 15:10 - test_logging.py - DEBUG - debug me: some_filename  
    2023-09-09 15:10 - test_logging.py - ERROR - some error: help me  
    2023-09-09 15:10 - test_logging.py - CRITICAL - mission critical: lunch break  

## Installation
You don't need to pip install this or anything else for that matter.  You actually don't need to run pip for anything at all, if you are really close to the metal, and use virtual environments a lot.  

Simply create a directory somewhere convenient, and add it to your PYTHONPATH environment variable.  
Then, when you drop this project into it, it will be available throughout your system, whether you are using a virtual environment or your basic system.  

I recommend putting all your own tools and code libraries in there.  

Example: create a directory named "pythonpath_stuff".  
`mkdir /path/to/pythonpath_stuff`  

Add it to your path variable:  
`export PYTHONPATH=$PYTHONPATH:/path/to/pythonpath_stuff`  

## Persistence
You need the PYTHONPATH to persist, so either add the export statement to your "__~/.bashrc__" or similar file, or for absolute supreme persistence and availability, add it to the "__/etc/environment__" file.  

See __sample_logging.py__ for a complete example of importing, setting up, and using.  

## Additional Notes  
For the record, I don't code my logging statement on one line.  I prefer to format it like this:  
```python
console_logger, file_logger = laughing_logger.set_up_my_logging(os.path.basename(__file__),  
        laughing_logger.LaughingLogLevel.DEBUG,  
        laughing_logger.LaughingLogLevel.ERROR,  
        "test.log"  
        )

```

Kudos to you for coding.  Most people never try.  

HA HA HA HAHAAAAAA...  
