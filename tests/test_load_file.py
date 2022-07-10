import unittest
import json

from config import load_file as lf
from config.constants import FileTypes as ft
from tests.resources import TestResources as tr


class TestLoadFile(unittest.TestCase):

    def setUp(self) -> None:
        pass

    
    def test_loading_unsupported_file_type(self) -> None:
        data = lf.load(tr.UNACCEPTED_FILE_PATH.value, tr.UNACCEPTED_FILE_EXTENSION.value)
        self.assertEqual(data, {})
        

    def test_loading_json_file(self) -> None:
        expected = self._load_json()
        data = lf.load(tr.JSON.value, ft.JSON.value)
        self.assertEqual(data.get('key1'), expected.get('key1'))
        self.assertEqual(data.get('key2'), expected.get('key2'))
        self.assertEqual(data.get('key3'), expected.get('key3'))
        self.assertEqual(data.get('key4'), expected.get('key4'))
        self.assertEqual(data.get('key5'), expected.get('key5'))
    

    def test_loading_txt_file(self) -> None:
        pass


    def test_loading_env_file(self) -> None:
        pass
    

    def tearDown(self) -> None:
        pass


    def _load_json(self) -> dict:
        with open(tr.JSON.value, "r") as content:
            data = json.load(content)
        return data



if __name__ == "__main__":
    unittest.main()