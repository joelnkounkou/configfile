import os
import argparse


def run_all_unit_tests(test_directory, regex):
    [_run_tests_in(x[0], regex) for x in os.walk(test_directory)]


def clear_pyc_files():
    _execute_command("find . -name '*.pyc' -delete")
    _execute_command("""find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf""")


def _parse_arguments(dir='tests', regex='test_*.py'):
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir', '--dir', dest='test_directory', default=dir, type=str, help="The path of the test folder.")
    parser.add_argument('-regex', '--regex', dest='regex', default=regex, type=str, help="The regex expression to locate test files.")
    args = parser.parse_args()
    return args.test_directory, args.regex


def _run_tests_in(directory, regex):
    _execute_command(f"python -m unittest discover -s {directory} -p '{regex}'")


def _execute_command(command):
    os.system(command)


if __name__ == '__main__':
    test_directory, regex = _parse_arguments()
    run_all_unit_tests(test_directory, regex)
    clear_pyc_files()