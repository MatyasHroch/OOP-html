import logging

# Could be set in a config file
LOG_ON = True

# ANSI escape codes for colored output
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Set the logging level and format
logging.basicConfig(
    level=logging.WARNING,
    # we need to know the module, function, and line number
    format=f"{YELLOW}%(levelname)s:{RESET} %(message)s ",
)


def log_warning(message):
    """Logs a warning message with a yellow color.
    Mostly used for warnings because of missing required attributes.
    """
    if not LOG_ON:
        return
    colored_message = f"{YELLOW}{message}{RESET}"
    logging.warning(colored_message)
