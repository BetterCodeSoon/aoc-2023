import pytest
import src.utils.file_helper as file_helper


@pytest.fixture
def testfile_path():
    return file_helper.PROJECT_ROOT / "resources" / "tests" / "testfile1.txt"
