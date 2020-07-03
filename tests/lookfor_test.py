import pytest
import sys

sys.path.append("../lookfor")
from lookfor import find_dir, find_ext_all, find_ext_in_dir, find_file, search_file


@pytest.mark.parametrize('test_input, expected', [
    ('test_dir', './test_dir'),  
    ('photos', None),
    ('test_dir_two', './test_dir/test_dir_two')
])
def test_find_dir(test_input, expected):
    assert find_dir(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ('.c', 'found 0 .c files'),  
    ('.txt', 'found 3 .txt files')
])
def test_find_ext_all(test_input, expected):
    assert find_ext_all(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ('.c', 'found 0 .c files'),
    ('.txt', 'found 1 .txt files')
])
def test_find_ext_in_dir(test_input, expected):
    assert find_ext_in_dir(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ('txt_test_one.txt', './txt_test_one.txt'),
    ('txt_test_two.txt', './test_dir/txt_test_two.txt'),
    ('txt_test_three.txt', './test_dir/test_dir_two/txt_test_three.txt'),
    ('helloworld.c', None)
])
def test_find_file(test_input, expected):
    assert find_file(test_input) == expected


@pytest.mark.parametrize('test_input, test_input2, expected',[
    ('hello', 'txt_test_one.txt', {'string': str, 'found': True, 'count': 2, 'found on lines': [1, 5]}),
    ('goodbye', 'txt_test_one.txt', {'string': str, 'found': True, 'count': 1, 'found on lines': [9]}),
    ('lookfor', 'txt_test_one.txt', 'Not Found')
])
def test_search_file(test_input, test_input2, expected):
    assert search_file(test_input, test_input2) == expected