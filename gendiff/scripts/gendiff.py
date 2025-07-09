import argparse
import json


def parse_file(path, format):
    path = f"{path}.{format}"
    with open(path, "r") as file:
        return json.load(file)
    
    
def generate_diff(file1, file2):
    all_item = file1 | file2
    result = []

    for key in sorted(all_item):
        value1 = file1.get(key)
        value2 = file2.get(key)

        if value1 == value2:
            result.append(f"    {key}: {str(value1).lower()}")
        elif key not in file1:
            result.append(f"  + {key}: {str(value2).lower()}")
        elif key not in file2:
            result.append(f"  - {key}: {str(value1).lower()}")
        else:
            result.append(f"  - {key}: {str(file1[key]).lower()}")
            result.append(f"  + {key}: {str(file2[key]).lower()}")
    diff_output = "{\n" + "\n".join(result) + "\n}"
    return diff_output


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        usage="%(prog)s [-h] [-f FORMAT] first_file second_file",
        description="Compares two configuration files and shows a difference.",
    )

    parser.add_argument("first_file", nargs="+")
    parser.add_argument("second_file", nargs="+")

    parser.add_argument(
        "-f", "--format", nargs="?", help="set format of output"
    )
    args = parser.parse_args()
    
    file1 = args.first_file[0]
    file2 = args.second_file[0]

    data1 = parse_file(file1, args.format)
    data2 = parse_file(file2, args.format)

    result = generate_diff(data1, data2)
    print(result)
