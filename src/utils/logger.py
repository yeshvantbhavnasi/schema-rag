import logging


def setup_logger(config):
    logging.basicConfig(
        level=config['logging']['level'],
        filename=config['logging']['file']
    )
    return logging.getLogger(__name__)
