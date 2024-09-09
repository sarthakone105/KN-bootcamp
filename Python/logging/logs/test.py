from logger import logging


def add(a, b):
    logging.debug("this addition operation is taking place")
    return a+b


logging.debug("Addtion function is called")
add(5,8)