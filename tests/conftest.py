import pytest
import src.utils.file_helper as file_helper
from aoc2.bag import Bag


@pytest.fixture
def testfile1_path():
    return file_helper.PROJECT_ROOT / "resources" / "testing" / "file_helper_testfile1.txt"


@pytest.fixture
def file_helper_testfile1_content_lines():
    return ['1abc2:12', 'pqr3stu8vwx:38', 'a1b2c3d4e5f:15', 'treb7uchet:77']


@pytest.fixture()
def testfile1_delimiter():
    return ":"


@pytest.fixture
def testfile1_dict():
    return {"1abc2": "12", "pqr3stu8vwx": "38", "a1b2c3d4e5f": "15", "treb7uchet": "77"}


@pytest.fixture
def testfile1_tuple_list():
    return [("1abc2", "12"), ("pqr3stu8vwx", "38"), ("a1b2c3d4e5f", "15"), ("treb7uchet", "77")]


@pytest.fixture
def aoc2_bag():
    return Bag(12, 13, 14)
