import logging
import os


def browser_log():
    """Создание логгера для браузера"""

    try:
        os.stat('logs')
    except FileNotFoundError:
        os.mkdir('logs')

    log = logging.getLogger('browser')
    log.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    filehandler_info = logging.FileHandler(filename='logs/info.log', mode='a')
    filehandler_info.setLevel(level=logging.INFO)
    filehandler_info.setFormatter(formatter)

    filehandler_critical = logging.FileHandler(filename='logs/warning.log', mode='a')
    filehandler_critical.setLevel(level=logging.INFO)
    filehandler_critical.setFormatter(formatter)

    filehandler_error = logging.FileHandler(filename='logs/error.log', mode='a')
    filehandler_error.setLevel(level=logging.INFO)
    filehandler_error.setFormatter(formatter)

    consolehandler_info = logging.StreamHandler()
    consolehandler_info.setLevel(level=logging.INFO)
    consolehandler_info.setFormatter(formatter)

    log.addHandler(filehandler_info)
    log.addHandler(filehandler_critical)
    log.addHandler(filehandler_error)

    log.addHandler(consolehandler_info)

    return log
