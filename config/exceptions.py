import os
from config.constants import Messages as Messages


class InvalidConfigFilePath(Exception):
    
    def __init__(self, file_path: os.path) -> None:
        self.file_path = file_path
        self.message = f'{Messages.INVALID_CONFIG_FILE_PATH.value}: <{self.file_path}>'
        super().__init__(self.message)


class UnacceptedFileType(Exception):
    
    def __init__(self, extension: str) -> None:
        self.extension = extension
        self.message = f'{Messages.UNACCEPTED_FILE_EXTENSION.value}: <{self.extension}>'
        super().__init__(self.message)