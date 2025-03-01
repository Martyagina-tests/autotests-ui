import pytest
import random

@pytest.mark.flaky(reruns=3, reruns_delay=2 )
def test_reruns():
    assert  random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_rerun_1(self):
        ...

    def test_rerun_2(self):
        ...