from tests.base_test import BaseTest


class ScaleTests(BaseTest):
    """
    Base class for the Scale Tests
    Contains code shared among the tests
    """

    def get_lighter_bars(self, weighing):
        if ">" in weighing:
            lighter_bars = weighing.split(">")
            return eval(lighter_bars[-1].strip())

        if "<" in weighing:
            lighter_bars = weighing.split("<")
            return eval(lighter_bars[0].strip())
