import pytest

import src
import data

FILE = "data/day_1.txt"
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    @pytest
    def read_raw_data(self):
        with open(FILE) as f:
            lines = f.readlines()
            print(lines)
        return
