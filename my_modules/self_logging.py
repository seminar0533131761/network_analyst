import logging


class MyLogger:
    def __init__(self, log_level=logging.INFO, log_format='%(asctime)s - %(levelname)s - %(message)s'):
        self.log_level = log_level
        self.log_format = log_format
        self.logger = self.setup_logger()

    def setup_logger(self):
        my_logger = logging.getLogger(__name__)
        my_logger.setLevel(self.log_level)

        formatter = logging.Formatter(self.log_format)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.log_level)
        console_handler.setFormatter(formatter)

        my_logger.addHandler(console_handler)

        return my_logger

    def get_logger(self):
        return self.logger


# Usage example:
if __name__ == "__main__":
    my_logger = MyLogger(log_level=logging.INFO)
    logger = my_logger.get_logger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
