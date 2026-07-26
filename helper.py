import logging
import logging.config
import traceback
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import time
# logger = logging.getLogger(__name__)
# # logger.propagate = False
# # logger.info("Hello from logger")
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler("file.log")
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)
# formater = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
# stream_h.setFormatter(formater)
# file_h.setFormatter(formater)
# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning("This is warning")
# logger.error("This is error")

logging.config.fileConfig("logging.conf")

logger = logging.getLogger("simpleExample")
logger.debug("this is a debug message")


try:
    a = [1, 2, 3]
    val = a[4]
except:
    logging.error("The error is %s", traceback.format_exc())


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
handler = TimedRotatingFileHandler("timed_log", when="s", interval=1, backupCount=5)

logger.addHandler(handler)

# for _ in range(1000):
#     logger.info("Hi there")

for _ in range(3):
    logger.info("Hi there")
    time.sleep(3)
