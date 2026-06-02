import sys

print(sys.path)
from app.core.log import logger


def build():
    logger.info("Building meta knowledge...")


if __name__ == '__main__':
    build()
