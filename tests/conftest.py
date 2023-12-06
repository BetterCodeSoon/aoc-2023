import pytest
import src.utils.file_helper as file_helper


@pytest.fixture
def testfile1_path():
    return file_helper.PROJECT_ROOT / "resources" / "testing" / "testfile1.txt"


@pytest.fixture
def testfile1_content_lines():
    return ['1abc2:12\n', 'pqr3stu8vwx:38\n', 'a1b2c3d4e5f:15\n', 'treb7uchet:77']


@pytest.fixture()
def testfile1_delimiter():
    return ":"


@pytest.fixture
def testfile1_dict():
    return {"1abc2": "12", "pqr3stu8vwx": "38", "a1b2c3d4e5f": "15", "treb7uchet": "77"}
