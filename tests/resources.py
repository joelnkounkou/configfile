import os
from enum import Enum as Enum
from config.constants import FileTypes as ft


class TestResources(Enum):
    #Directories and names
    TEST_DIR: str = 'tests'
    FOLDER: str = 'test_files'
    PREFIX: str = 'example_'

    #Test files
    ENV: os.path = os.path.join(TEST_DIR, FOLDER, f'{PREFIX}{ft.ENV.value}.{ft.ENV.value}')
    JSON: os.path = os.path.join(TEST_DIR, FOLDER, f'{PREFIX}{ft.JSON.value}.{ft.JSON.value}')
    TXT: os.path = os.path.join(TEST_DIR, FOLDER, f'{PREFIX}{ft.TXT.value}.{ft.TXT.value}')

    #For test cases
    NON_EXISTANT_FILE_PATH: os.path = os.path.join(TEST_DIR, FOLDER, f'invalid.{ft.JSON.value}')
    UNACCEPTED_FILE_EXTENSION: str = 'xyz'
    UNACCEPTED_FILE_PATH: os.path = os.path.join(TEST_DIR, FOLDER, f'{PREFIX}xyz.xyz')