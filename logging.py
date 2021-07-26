from loguru import logger

logger.add("info.log", format="{time} {level} {message}", 
           level="INFO", rotation="100 KB", compression="zip")
logger.add("error.log", format="{time} {level} {message}", 
           level="ERROR", rotation="100 KB", compression="zip")
