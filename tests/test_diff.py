from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    file1 = {
        "host": "localhost",
        "timeout": 50,
        "verbose": True
    }

    file2 = {
        "host": "localhost",
        "timeout": 20,
        "debug": True
    }

    expected = '''{
  + debug: true
    host: localhost
  - timeout: 50
  + timeout: 20
  - verbose: true
}'''

    result = generate_diff(file1, file2)
    assert result == expected
    
