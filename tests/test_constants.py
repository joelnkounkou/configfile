import unittest

from config import constants as constants
from tests import resources as resources


class TestConstants(unittest.TestCase):

    def setUp(self) -> None:
        self.json = 'json'
        self.txt = 'txt'
        self.env = 'env'
        

    def test_file_type_constants(self) -> None:
        self.assertEqual(constants.FileTypes.JSON.value, self.json)
        self.assertEqual(constants.FileTypes.TXT.value, self.txt)
        self.assertEqual(constants.FileTypes.ENV.value, self.env)
    

    def test_accepted_file_types(self) -> None:
        accepted = [self.json, self.txt, self.env]
        for file_extension in constants.FileTypes.ACCEPTED_EXTENSIONS.value:
            self.assertTrue(file_extension in accepted)
    

    def test_invalid_config_message(self) -> None:
        message = 'Invalid or non-existant `config_file_path` provided'
        self.assertEqual(constants.Messages.INVALID_CONFIG_FILE_PATH.value, message)
    

    def test_unaccepted_file_type_message(self) -> None:
        message = 'Unaccepted `file_type` or file extension'
        self.assertEqual(constants.Messages.UNACCEPTED_FILE_EXTENSION.value, message)


    def test_constants(self) -> None:
        self.assertEqual(constants.Constants.PERIOD.value, '.')
        self.assertEqual(constants.Constants.READ.value, 'r')

    
    def tearDown(self) -> None:
        pass


class TestResources(unittest.TestCase):

    def setUp(self) -> None:
        pass


    def test_test_files_constants(self) -> None:
        test_dir = 'tests'
        folder = 'test_files'
        prefix = 'example_'
        json_file = f'{test_dir}/{folder}/{prefix}json.json'
        env_file = f'{test_dir}/{folder}/{prefix}env.env'
        txt_file = f'{test_dir}/{folder}/{prefix}txt.txt'
        invalid_file_path = f'{test_dir}/{folder}/invalid.json'
        unaccepted_file_ext = 'xyz'
        xyz_file = f'{test_dir}/{folder}/{prefix}xyz.xyz'

        self.assertEqual(resources.TestResources.NON_EXISTANT_FILE_PATH.value, invalid_file_path)
        self.assertEqual(resources.TestResources.UNACCEPTED_FILE_EXTENSION.value, unaccepted_file_ext)
        self.assertEqual(resources.TestResources.UNACCEPTED_FILE_PATH.value, xyz_file)

        self.assertEqual(resources.TestResources.TEST_DIR.value, test_dir)
        self.assertEqual(resources.TestResources.FOLDER.value, folder)
        self.assertEqual(resources.TestResources.PREFIX.value, prefix)

        self.assertEqual(resources.TestResources.JSON.value, json_file)
        self.assertEqual(resources.TestResources.TXT.value, txt_file)
        self.assertEqual(resources.TestResources.ENV.value, env_file)


    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()