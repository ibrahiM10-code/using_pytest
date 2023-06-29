from main import AddToList
import pytest

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    def test_add_to_list(self):
        my_list = AddToList([], 2)
        for i in range(2):
            my_list.add(i)
        with pytest.raises(IndexError):
            my_list.add(4)