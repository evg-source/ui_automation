import unittest
import logging
from framework.web_driver import WebDriver
from framework.scale_page import ScalePage
from scale_tests import ScaleTests
import cfg

logging.basicConfig(level=cfg.debug_level)


class FindFakeBarTests(ScaleTests):
    """
    Tests to Find Fake Gold Bar
    There are 2 tests
    Generic test which can accept more or less then 9 bars
    9 Bar test which works only with 9 bars
    In case of 9 bars minimum number of weighing is 1, max number 3
    """

    def setUp(self):
        wd = WebDriver.initiate_web_driver()
        wd.get(cfg.scale_page_url)

    def tearDown(self):
        WebDriver.wd.quit()

    def test_generic_algorithm(self):
        """
        Generic algorithm which can handle variable number of bars
        :return:
        """
        bars_n = 9
        scale_page = ScalePage()
        l_bowl = [i for i in range(bars_n // 2)]
        r_bowl = [i for i in range(bars_n // 2, bars_n - 1)]
        last_bar = None
        if bars_n % 2 > 0:
            last_bar = bars_n - 1

        scale_page.weigh_bars(l_bowl, r_bowl)
        scale_result = scale_page.get_last_weighing()

        if "=" in scale_result:
            if last_bar is not None:
                logging.info("Fake bar: {}".format(last_bar))
                scale_page.click_on_bar(last_bar)
                msg = scale_page.get_alert_text()
                self.assertEqual(msg, "Yay! You find it!")
            else:
                self.assertTrue(False, "Expected odd number of bars, but got {}".format(bars_n))

        else:
            while bars_n > 1:
                bars = self.get_lighter_bars(scale_result)
                bars_n = len(bars)
                if len(bars) > 1:
                    l_bowl = bars[:bars_n // 2]
                    r_bowl = bars[bars_n // 2:]
                    scale_page.weigh_bars(l_bowl, r_bowl)
                    scale_result = scale_page.get_last_weighing()

                else:
                    logging.info("Fake bar: {}".format(bars[0]))
                    scale_page.click_on_bar(bars[0])
                    msg = scale_page.get_alert_text()
                    self.assertEqual(msg, "Yay! You find it!")

    def test_9_bars_algorithm(self):
        """
        9 bars algorithm
        :return:
        """
        scale_page = ScalePage()
        l_bowl = [i for i in range(4)]
        r_bowl = [i for i in range(4, 8)]

        # 1st weighing
        scale_page.weigh_bars(l_bowl, r_bowl)
        scale_result = scale_page.get_last_weighing()

        if "=" in scale_result:
            logging.info("Fake bar: {}".format(8))
            scale_page.click_on_bar(8)
            msg = scale_page.get_alert_text()
            self.assertEqual(msg, "Yay! You find it!")

        else:
            bars = self.get_lighter_bars(scale_result)
            l_bowl = bars[:2]
            r_bowl = bars[2:]
            # 2nd weighing
            scale_page.weigh_bars(l_bowl, r_bowl)
            scale_result = scale_page.get_last_weighing()

            bars = self.get_lighter_bars(scale_result)
            l_bowl = bars[:1]
            r_bowl = bars[1:]
            # 3rd weighing
            scale_page.weigh_bars(l_bowl, r_bowl)
            scale_result = scale_page.get_last_weighing()

            bars = self.get_lighter_bars(scale_result)
            logging.info("Fake bar: {}".format(bars[0]))
            scale_page.click_on_bar(bars[0])
            msg = scale_page.get_alert_text()
            self.assertEqual(msg, "Yay! You find it!")


if __name__ == '__main__':
    unittest.main()
