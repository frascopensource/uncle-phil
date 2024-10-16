"""
Utils package initialization.

This module loads environment variables from the `.env` file and sets up global variables
for use across the package. It also provides a function to reload environment variables.
"""
from dotenv import load_dotenv
import os


def load_environment_variables():
    """
    Load environment variables from the .env file and set global variables.
    """
    load_dotenv(override=True)

    global VAR
    VAR = os.getenv('VAR')


# Initial load of environment variables
load_environment_variables()
