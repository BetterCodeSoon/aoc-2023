import time
import pytest
import src.utils.benchmark_helper as benchmark_helper


class TestBenchmarkHelper:

    @staticmethod
    def _short_sleep_returns123() -> int:
        time.sleep(0.1)
        return 123

    @staticmethod
    def _short_sleep_returns_sum(value1: int = 1, value2: int = 2) -> int:
        time.sleep(0.1)
        return value1 + value2

    def test_benchmark(self, capsys):
        result = benchmark_helper.benchmark(self._short_sleep_returns123)
        output = capsys.readouterr().out
        assert result == 123
        assert 0.1 <= float(output.split()[-2]) < 0.2

    @pytest.mark.parametrize("value1, value2, expected", [(2, 3, 5)])
    def test_benchmark(self, capsys, value1, value2, expected):
        result = benchmark_helper.benchmark(self._short_sleep_returns_sum, value1, value2)
        output = capsys.readouterr().out
        assert result == expected
        assert 0.1 <= float(output.split()[-2]) < 0.2
