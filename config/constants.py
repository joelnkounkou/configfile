from enum import Enum as Enum


class FileTypes(Enum):
    ENV: str = 'env'
    JSON: str = 'json'
    TXT: str = 'txt'
    ACCEPTED_EXTENSIONS = [ENV, JSON, TXT]


class Messages(Enum):
    INVALID_CONFIG_FILE_PATH: str = 'Invalid or non-existant `config_file_path` provided'
    UNACCEPTED_FILE_EXTENSION: str = 'Unaccepted `file_type` or file extension'


class Constants(Enum):
    PERIOD: str = '.'
    READ: str = 'r'
