import pytest
import sys


from lookfor.lookfor import find_dir, find_ext_all, find_ext_in_dir, find_file, search_file, repstr


@pytest.mark.parametrize('test_input, expected', [
    ('test_dir', './test_dir'),  
    ('photos', None),
    ('test_dir_two', './test_dir/test_dir_two')
])
def test_find_dir(test_input, expected):
    assert find_dir(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ('.c', 'found 0 .c files'),  
    ('.txt', 'found 4 .txt files')
])
def test_find_ext_all(test_input, expected):
    assert find_ext_all(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ('.c', 'found 0 .c files'),
    ('.txt', 'found 2 .txt files')
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
    ('hello', 'txt_test_one.txt', {'string': 'hello', 'count': 2, 'found on lines': '[1, 5]'}),
    ('goodbye', 'txt_test_one.txt', {'string': 'goodbye', 'count': 1, 'found on lines': '[9]'}),
    ('lookfor', 'txt_test_one.txt', 'Not Found'),
    ('hello', 'nonexistent_file.txt', 'Error opening file')
])
def test_search_file(test_input, test_input2, expected):
    assert search_file(test_input, test_input2) == expected


@pytest.mark.parametrize('test_input, test_input2, test_input3, expected', [
    ('test_repstr.txt', 'world', 'planet', 0),
    ('test_repstr.txt', 'coffee', 'tea', 0),
    ('txt_test_sdsd.txt', 'coffee', 'tea', 1)
])
def test_repstr(test_input, test_input2, test_input3, expected):
    assert repstr(test_input, test_input2, test_input3) == expected