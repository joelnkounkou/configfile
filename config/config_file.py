import os

from config import exceptions as exc
from config import constants as constants
from config import load_file as load_file


class Config:

    _instance = None

    def __init__(self) -> None:
        self.file_path: os.path = None
        self.file_type: str = None
        self._data: dict = {}
    

    def load(self, file_path):
        self._does_file_exist(file_path)
        extension = self._get_file_extension(file_path)
        self._digest_file(file_path, extension)
        self.file_path = file_path
        self.file_type = extension
        return self
    

    def to_dict(self) -> dict:
        return self._data


    def _does_file_exist(self, file_path: os.path) -> None:
        if not os.path.exists(file_path): raise exc.InvalidConfigFilePath(file_path)
    

    def _get_file_extension(self, file_path: os.path) -> str:
        extension = os.path.splitext(file_path)[-1]
        if constants.Constants.PERIOD.value in extension:
            extension = extension[1:]
        if extension not in constants.FileTypes.ACCEPTED_EXTENSIONS.value: raise exc.UnacceptedFileType(extension)
        return extension


    def _digest_file(self, file_path: os.path, file_type: str) -> None:
        self._data = load_file.load(file_path, file_type)
        [setattr(self, key, self._data.get(key)) for key in self._data]


    def __getattribute__(self, name: str):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            return None
    

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
        return cls._instance
