import pytest

from search import (
    search_dir, search_file
)


def pytest_runtest_teardown(item):
    """Clean up tmpdir data after test"""
    if item.rep_call.passed:
        if 'tmpdir' in item.funcargs:
            tmpdir = item.funcargs['tmpdir']
            if tmpdir.check():
                tmpdir.remove()


def generate_example(tmpdir, depth=5):
    """
    Generate a directory structure containing a text file at the specified
    depth
    """
    dir = tmpdir.mkdir('test_dir')
    for i in range(depth):
        dir = dir.mkdir(f'test_dir{i}')

    p = dir.join('test_file.txt')
    p.write('Lorem Ipsum')
    return p


@pytest.mark.parametrize('depth', [(0), (1), (2), (3), (4), (5)])
def test_search_dir_tmpdir(tmpdir, depth):
    generate_example(tmpdir, depth)
    results = search_dir(tmpdir, text='lorem ipsum')
    assert 'MATCH' in str(next(results))


@pytest.mark.parametrize('depth', [(0), (1), (2), (3), (4), (5)])
def test_search_file_tmpdir(tmpdir, depth):
    file = generate_example(tmpdir, depth)
    results = search_file(file, 'lorem ipsum')
    assert 'MATCH' in str(next(results))
