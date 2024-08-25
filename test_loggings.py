import logging 
LOGGER = logging.getLogger(__name__)

def test_myloggings():
    LOGGER.warning("Warning logs!")
    LOGGER.info("Info logs!")
    LOGGER.error("Error logs!")
    LOGGER.critical("Critical logs!")
    assert True