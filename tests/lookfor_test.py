import pytest
import sys

sys.path.append("../lookfor")
from lookfor import find_dir


@pytest.mark.parametrize('test_input, expected', [
    ('test_dir', './test_dir'),  
    ('photos', None),
    ('test_dir_two', './test_dir/test_dir_two')])
def test_find_dir(test_input, expected):
    assert find_dir(test_input) == expected
