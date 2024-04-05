import pytest
import tempfile
import os
from function import filter_text
@pytest.fixture
def temp_files():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as input_file:
        input_file.write("apple\nbanana\norange\n")
    yield input_file.name, "filtered.txt"
    os.unlink(input_file.name)

# Параметризація тестів
@pytest.mark.parametrize("keyword, expected_output", [
    ("apple", "apple\n"),
    ("banana", "banana\n"),
    ("orange", "orange\n"),
    ("grape", ""),
])
def test_filter_text(temp_files, keyword, expected_output):
    input_file, output_file = temp_files
    filter_text(input_file, output_file, keyword)
    with open(output_file, 'r') as f:
        assert f.read() == expected_output