import pytest

from src.utils.input.counter import Counter


class TestCounter:

    @pytest.mark.parametrize("count", [1, 0, -3])
    def test_initialization(self, count):
        if count >= 0:
            assert Counter(count).count == count
        else:
            with pytest.raises(ValueError):
                Counter(count)
