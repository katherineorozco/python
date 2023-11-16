import pytest
from television import Television

class Test:
    def test_init(self):
        assert Television()._Television__status is False
        assert Television()._Television__muted is False
        assert Television()._Television__volume == Television.MIN_VOLUME
        assert Television()._Television__channel == Television.MIN_CHANNEL
        assert str(Television()) == Television().__str__()
