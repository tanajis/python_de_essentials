import logging
import other # other model
import sys
# Create terminal Logger object
# This will print logs on the terminal. 
logger = logging.getLogger(__name__)
logging.basicConfig(
    force=True,  # Forces reconfiguration, clears existing handlers
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),      #  File output
        logging.StreamHandler(sys.stdout)    #  Terminal output
    ]
)

# logging.basicConfig(level=logging.INFO)  # Confirms things are working as expected.
# logging.basicConfig(level=logging.ERROR)  # A serious problem that prevents a function from running.
# logging.basicConfig(level=logging.WARNING) #Indicates unexpected issues or potential future problems.
# logging.basicConfig(level=logging.DEBUG)  #Detailed information for diagnosing problems
# logging.basicConfig(level=logging.CRITICAL) #A severe error that may stop the program from running.
# FIXED: Added force=True to override any existing config + moved before logger calls

# Info shows all messages except debug
# Error shows errors and criticals
# warning shows warnings, errors and criticals.
# debug shows all - debug warnings, errors and criticals.
# criticals shows only critical



if __name__ == "__main__":

    # print log on the terminal
    logger.info("This is an info message")
    logger.error("This is an error message")
    logger.warning("This is an warning message")
    logger.debug("This is an debug message")
    logger.critical("This is an critical message")

    # Logs from other module
    res = other.dummy_func()

# Why Not Use print() Statements?
# While print() can help in simple scripts, it is not reliable for complex programs. Python's built-in logging module is more flexible:

# Records which part of the code runs.
# Logs errors and warnings.
# Can store logs in files or output streams.
# Supports different log levels to filter messages.
