import os
import pytest

from search import (
    search_dir, search_file
)


def test_search_dir():
    dir = os.path.abspath('test_dir')
    results = search_dir(dir, text='lorem ipsum')

    assert results


def test_search_file():
    file = os.path.abspath('test_dir/test')
    results = search_file(file, text='tempus urna')

    assert results

