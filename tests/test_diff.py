from gendiff.scripts.gendiff import parse_file, generate_diff
import os


def test_generate_diff():
    path1 = os.path.join('tests', 'fixtures', 'file1')
    path2 = os.path.join('tests', 'fixtures', 'file2')
    
    data1 = parse_file(path1, 'json')
    data2 = parse_file(path2, 'json')
    
    result = generate_diff(data1, data2)
    # file1 = {
    # "host": "hexlet.io",
    # "timeout": 50,
    # "proxy": "123.234.53.22",
    # "follow": False
    # }

    # file2 = {
    # "timeout": 20,
    # "verbose": True,
    # "host": "hexlet.io"
    # }
    
    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

    assert result == expected
    
