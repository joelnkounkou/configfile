import os
import json

from config import constants as constants


def load(file_path: os.path, file_extension: str) -> dict:
    load_by = {
        constants.FileTypes.JSON.value: _load_json
    }
    return load_by[file_extension](file_path) if file_extension in load_by else {}


def _load_json(file_path: os.path) -> dict:
    with open(file_path, constants.Constants.READ.value) as f:
        data = json.load(f)
    return data