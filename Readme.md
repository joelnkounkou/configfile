# ConfigurationFile

ConfigurationFile is a Python library that wraps unstructured "configuration files" into a neat and easy python object.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install configfile
```

## Usage

```python
from configfile import configfile

# returns Singleton instance with attributes as keys from the file
config = configfile().load('path/to/config.json')

# Reads from a filestream
stream = #fetch from source
config = configfile().read(stream, 'json')

# returns value from `api_key`
config.api_key

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)