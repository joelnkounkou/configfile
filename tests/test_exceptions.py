import unittest

from config import exceptions as exc
from config.constants import Messages as mes
from tests.resources import TestResources as tr


class TestExceptions(unittest.TestCase):

    def setUp(self) -> None:
        pass
        

    def test_invalid_config_path_exception(self) -> None:
        with self.assertRaises(exc.InvalidConfigFilePath) as context:
            self._invalid_file_path()

        expected_message = f'{mes.INVALID_CONFIG_FILE_PATH.value}: <{tr.NON_EXISTANT_FILE_PATH.value}>'
        self.assertEqual(context.exception.message, expected_message)
    

    def test_invalid_file_types(self) -> None:
        with self.assertRaises(exc.UnacceptedFileType) as context:
            self._invalid_file_ext()
        
        expected_message = f'{mes.UNACCEPTED_FILE_EXTENSION.value}: <{tr.UNACCEPTED_FILE_EXTENSION.value}>'
        self.assertEqual(context.exception.message, expected_message)


    def tearDown(self) -> None:
        pass


    def _invalid_file_path(self) -> None:
        raise exc.InvalidConfigFilePath(tr.NON_EXISTANT_FILE_PATH.value)
    

    def _invalid_file_ext(self) -> None:
        raise exc.UnacceptedFileType(tr.UNACCEPTED_FILE_EXTENSION.value)


if __name__ == "__main__":
    unittest.main()