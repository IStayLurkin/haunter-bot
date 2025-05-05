# logger_setup.py
import logging
import sys
import re
from colorama import Fore, Style

def init_logger():
    class ColorFormatter(logging.Formatter):
        def __init__(self):
            super().__init__(datefmt="%Y-%m-%d %H:%M:%S")
        def format(self, record):
            ts   = self.formatTime(record)
            lvl  = f"{Fore.BLUE}{record.levelname:<7}{Style.RESET_ALL}"
            name = f"{Fore.MAGENTA}{record.name}{Style.RESET_ALL}"
            msg  = re.sub(r"DINGU \d+\s*", "", record.getMessage())
            return f"[{ts}] {lvl} {name}: {msg}"

    for h in logging.root.handlers[:]:
        logging.root.removeHandler(h)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(ColorFormatter())
    logging.basicConfig(level=logging.DEBUG, handlers=[handler])

    for name in logging.root.manager.loggerDict:
        logger = logging.getLogger(name)
        logger.handlers = [handler]
        logger.propagate = False
