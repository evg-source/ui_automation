import logging
from framework.base_page import BasePage
import cfg

logging.basicConfig(level=cfg.debug_level)


class ScalePage(BasePage):
    def reset_scale(self):
        # el_id = "reset"
        # el = self.wd.find_element_by_id(el_id)
        # there is a bug in the code there are 2 elements with "reset" id
        # one is the button the other one is the element between bowls
        el_xpath = "//button[text()='Reset']"
        el = self.wd.find_element_by_xpath(el_xpath)
        el.click()

    def weigh(self):
        el_id = "weigh"
        el = self.wd.find_element_by_id(el_id)
        el.click()

    def weigh_bars(self, left_bowl, right_bowl):
        """
        :param left_bowl: list [0, 1,...8]
        :param right_bowl: list [0, 1,...8]
        :return:
        """
        logging.info("Left: {} Right: {}".format(left_bowl, right_bowl))
        self.reset_scale()

        for i in range(len(left_bowl)):
            el = self.wd.find_element_by_id("left_" + str(i))
            el.send_keys(str(left_bowl[i]))

        for i in range(len(right_bowl)):
            el = self.wd.find_element_by_id("right_" + str(i))
            el.send_keys(str(right_bowl[i]))

        self.weigh()

    def get_last_weighing(self):
        xpath = "//div[@class='game-info']/ol/li"
        els = self.wd.find_elements_by_xpath(xpath)
        logging.info(els[-1].text)
        return els[-1].text

    def click_on_bar(self, bar_num=0):
        """
        :param bar_num: int 0 to 8
        :return:
        """
        if bar_num not in range(9):
            raise ValueError("Expected bar number from 0 to 8")
        el_id = "coin_" + str(bar_num)
        el = self.wd.find_element_by_id(el_id)
        el.click()


