from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def get_formatter(format_name):
    match format_name:
        case 'stylish':
            return format_stylish
        case 'plain':
            return format_plain
        case _:
            raise ValueError(f"Unsupported format: {format_name}")
