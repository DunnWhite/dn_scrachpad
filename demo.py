#!/usr/bin/env python3
"""Demo script showing usage of utilities."""

import os
import sys
import tempfile
import json

# Add current directory to path to import utils
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import utils

def demo_file_hash():
    """Demo file hash calculation."""
    print("=== File Hash Demo ===")
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write("Hello, World!\nThis is a test file.")
        temp_path = f.name

    try:
        hash_value = utils.get_file_hash(temp_path, 'sha256')
        print(f"File: {temp_path}")
        print(f"SHA256 hash: {hash_value}")
    finally:
        os.unlink(temp_path)
    print()

def demo_json_operations():
    """Demo JSON read/write."""
    print("=== JSON Operations Demo ===")
    data = {
        "name": "Test Project",
        "version": "1.0.0",
        "author": "Developer",
        "dependencies": ["utils", "json"],
        "metadata": {
            "created": "2024-01-01",
            "updated": "2024-03-14"
        }
    }

    # Write JSON
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json_file = f.name

    try:
        utils.write_json(data, json_file)
        print(f"Written JSON to: {json_file}")

        # Read back
        loaded = utils.read_json(json_file)
        print(f"Read JSON data keys: {list(loaded.keys())}")

        # Flatten nested dict
        flattened = utils.flatten_dict(loaded)
        print(f"Flattened keys: {list(flattened.keys())}")
    finally:
        os.unlink(json_file)
    print()

def demo_formatting():
    """Demo timestamp and size formatting."""
    print("=== Formatting Demo ===")

    # Timestamp
    timestamp = utils.format_timestamp()
    print(f"Current time: {timestamp}")

    # Human readable size
    sizes = [1024, 1024*1024, 1024*1024*1024, 123456789]
    for size in sizes:
        readable = utils.human_readable_size(size)
        print(f"{size} bytes = {readable}")
    print()

def demo_file_search():
    """Demo file search by extension."""
    print("=== File Search Demo ===")

    # Create temporary directory with test files
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create some test files
        extensions = ['.txt', '.json', '.py']
        for ext in extensions:
            for i in range(2):
                path = os.path.join(tmpdir, f'test{i}{ext}')
                with open(path, 'w') as f:
                    f.write(f'Test content for {path}')

        # Search for .txt files
        txt_files = utils.find_files_by_extension(tmpdir, '.txt')
        print(f"Found {len(txt_files)} .txt files in {tmpdir}")
        for f in txt_files:
            print(f"  - {os.path.basename(f)}")
    print()

def main():
    """Run all demos."""
    print("Utility Functions Demo")
    print("=" * 50)

    demos = [
        demo_file_hash,
        demo_json_operations,
        demo_formatting,
        demo_file_search,
    ]

    for demo in demos:
        try:
            demo()
        except Exception as e:
            print(f"Demo failed: {e}")
            print()

    print("=" * 50)
    print("All demos completed successfully!")

if __name__ == '__main__':
    main()