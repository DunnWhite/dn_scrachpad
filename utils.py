"""Utility functions for common tasks."""

import os
import json
import hashlib
from typing import Any, Dict, List, Optional
from datetime import datetime


def get_file_hash(filepath: str, algorithm: str = 'sha256') -> str:
    """Calculate hash of a file.

    Args:
        filepath: Path to the file.
        algorithm: Hash algorithm (default: sha256).

    Returns:
        Hex digest of file hash.

    Raises:
        FileNotFoundError: If file does not exist.
    """
    hash_func = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def read_json(filepath: str) -> Any:
    """Read JSON file.

    Args:
        filepath: Path to JSON file.

    Returns:
        Parsed JSON data.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(data: Any, filepath: str, indent: int = 2) -> None:
    """Write data to JSON file.

    Args:
        data: Data to serialize.
        filepath: Path to output file.
        indent: Indentation level (default: 2).
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def format_timestamp(timestamp: Optional[float] = None,
                     fmt: str = '%Y-%m-%d %H:%M:%S') -> str:
    """Format timestamp to readable string.

    Args:
        timestamp: Unix timestamp (default: current time).
        fmt: Datetime format string.

    Returns:
        Formatted datetime string.
    """
    if timestamp is None:
        dt = datetime.now()
    else:
        dt = datetime.fromtimestamp(timestamp)
    return dt.strftime(fmt)


def human_readable_size(size_bytes: int) -> str:
    """Convert bytes to human readable size.

    Args:
        size_bytes: Size in bytes.

    Returns:
        Human readable size string (e.g., '1.2 MB').
    """
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(size_bytes)
    for unit in units:
        if size < 1024.0 or unit == units[-1]:
            return f'{size:.2f} {unit}'
        size /= 1024.0
    return f'{size_bytes} B'


def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten a nested dictionary.

    Args:
        d: Dictionary to flatten.
        parent_key: Base key for nested keys.
        sep: Separator for nested keys.

    Returns:
        Flattened dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def find_files_by_extension(directory: str, extension: str) -> List[str]:
    """Find all files with given extension in directory.

    Args:
        directory: Directory to search.
        extension: File extension (e.g., '.txt').

    Returns:
        List of file paths.
    """
    matches = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                matches.append(os.path.join(root, file))
    return matches


if __name__ == '__main__':
    # Demo usage
    print('Utility functions demo:')
    print(f'Current time: {format_timestamp()}')
    print(f'Human readable size: {human_readable_size(123456789)}')

    # Example dictionary flattening
    sample_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
    print(f'Original dict: {sample_dict}')
    print(f'Flattened dict: {flatten_dict(sample_dict)}')

    print('All utilities are ready to use!')