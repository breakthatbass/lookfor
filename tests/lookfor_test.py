import pytest
import sys

sys.path.append("../lookfor")
from lookfor import find_dir, find_ext_all


@pytest.mark.parametrize('test_input, expected', [
    ('test_dir', './test_dir'),  
    ('photos', None),
    ('test_dir_two', './test_dir/test_dir_two')])
def test_find_dir(test_input, expected):
    assert find_dir(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ('.c', 'found 0 .c files'),  
    ('.txt', 'found 3 .txt files')])
def test_find_ext_all(test_input, expected):
    assert find_ext_all(test_input) == expected