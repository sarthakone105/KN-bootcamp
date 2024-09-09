import logging


# logging settings

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger("ArthmethicApp")

def add(a, b):
    result = a + b
    logger.debug(f"Adding started : {a} + {b}, result: {result}")
    return result

def substract(a, b):
    result = a - b
    logger.debug(f"Minus started : {a} - {b}, result: {result}")
    return result


def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplication started : {a} * {b}, result: {result}")
    return result


def divide(a, b):
    try:
        result = a/b
        logger.debug(f"Division started : {a} / {b} : result: {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by Zero Error")
        return None
    
    
add(10, 5)
substract(10, 5)
multiply(10, 5)
divide(10, 0)
