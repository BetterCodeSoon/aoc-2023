import pytest
import src.utils.file_helper as file_helper


@pytest.fixture
def testfile_path():
    return file_helper.PROJECT_ROOT / "resources" / "tests" / "testfile1.txt"

@pytest.fixture
def testfile_content():
    return ['1abc2:12\n', 'pqr3stu8vwx:38\n', 'a1b2c3d4e5f:15\n', 'treb7uchet:77']