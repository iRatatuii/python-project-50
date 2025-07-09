import os
from typing import LiteralString

from gendiff.scripts.gendiff import parse_file


def test_parse_json():
    path = os.path.join('tests', 'fixtures', 'file1')
    print(path)
    result = parse_file(path, 'json')
    
    assert result == {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
    }
    
    
def test_parse_yaml():
    path: LiteralString = os.path.join('tests', 'fixtures', 'file2')
    result = parse_file(path, 'yaml')
    assert result == {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}