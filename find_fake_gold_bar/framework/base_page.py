from framework.web_driver import WebDriver


class BasePage(WebDriver):

    def dismiss_alert(self):
        alert = self.wd.switch_to.alert
        alert.accept()

    def get_alert_text(self):
        alert = self.wd.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text
