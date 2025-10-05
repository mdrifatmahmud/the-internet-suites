import pytest
from helpers.utils import load_config

@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]
