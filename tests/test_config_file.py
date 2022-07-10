import unittest

from config import load_file as lf
from config import exceptions as exc
from config import config_file as config
from tests.resources import TestResources as tr


class TestConfig(unittest.TestCase):

    def setUp(self) -> None:
        self.json_config_model = config.Config().load(tr.JSON.value)
        self.json_config_expected_data = lf._load_json(tr.JSON.value)
        

    def test_with_invalid_json_path(self) -> None:
        with self.assertRaises(exc.InvalidConfigFilePath):
            config.Config().load(file_path=tr.NON_EXISTANT_FILE_PATH.value)
    

    def test_with_invalid_file_extension(self) -> None:
        with self.assertRaises(exc.UnacceptedFileType):
            config.Config().load(file_path=tr.UNACCEPTED_FILE_PATH.value)
    

    def test_non_existant_attribute(self) -> None:
        self.assertEqual(self.json_config_model.key_123, None)
    

    def test_config_model_attr_from_json(self) -> None:
        self.assertEqual(self.json_config_model.file_path, tr.JSON.value)
        self.assertEqual(self.json_config_model.file_type, 'json')
        self.assertEqual(self.json_config_model.key1, self.json_config_expected_data.get('key1'))
        self.assertEqual(self.json_config_model.key2, self.json_config_expected_data.get('key2'))
        self.assertEqual(self.json_config_model.key3, self.json_config_expected_data.get('key3'))
        self.assertEqual(self.json_config_model.key4, self.json_config_expected_data.get('key4'))
        self.assertEqual(self.json_config_model.key5, self.json_config_expected_data.get('key5'))
    

    def test_config_model_instance(self) -> None:
        model_a = config.Config().load(tr.JSON.value)
        model_b = config.Config().load(tr.TXT.value)
        self.assertTrue(model_a == model_b)
    

    def test_config_model_to_dict(self) -> None:
        data = self.json_config_model.to_dict()
        self.assertIsInstance(data, dict)
        self.assertEqual(data.get('key1'), self.json_config_expected_data.get('key1'))
        self.assertEqual(data.get('key2'), self.json_config_expected_data.get('key2'))
        self.assertEqual(data.get('key3'), self.json_config_expected_data.get('key3'))
        self.assertEqual(data.get('key4'), self.json_config_expected_data.get('key4'))
        self.assertEqual(data.get('key5'), self.json_config_expected_data.get('key5'))
    

    def tearDown(self) -> None:
        pass



if __name__ == "__main__":
    unittest.main()