import os

from gendiff.parser import parse_file
from gendiff.scripts.gendiff import generate_diff


def load_fixture(name):
    path = os.path.join('tests', 'fixtures', name)
    with open(path, 'r') as f:
        return f.read().strip() 
    
    
def test_generate_diff_json():
    pass


def test_generate_diff():
    path1 = os.path.join("tests", "fixtures", "recursive1.json")
    path2 = os.path.join("tests", "fixtures", "recursive2.json")

    data1 = parse_file(path1)
    data2 = parse_file(path2)

    result = generate_diff(data1, data2, formatter="stylish")
    expected = load_fixture("expected_stylish.txt")
  
    assert result == expected


def test_generate_diff_yaml():
    file1 = "tests/fixtures/recursive1.yaml"
    file2 = "tests/fixtures/recursive2.yaml"
    
    data1 = parse_file(file1)
    data2 = parse_file(file2)

    result = generate_diff(data1, data2, formatter="stylish")
    expected = load_fixture("expected_stylish.txt")
    assert result == expected