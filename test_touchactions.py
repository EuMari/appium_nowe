# C4 - akcje dotykowe (TOUCHACTIONS)
#
# Kroki:
# 1. Wejdź do „Views”
# 2. Wejdź do „Expandable list”
# 3. Wejdź do „Custom Adapter”
# 4. Długo przytrzymaj na „People names”
# 5. Kliknij na „Sample action”
#
# Oczekiwane rezultaty:
# Poprawne wybranie pola „Sample action”.

import os
import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class TestingApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'Genymotion Cloud'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['udid'] = 'localhost:44121' #do uzupelnienia z gmsaas instances list -q | xargs -n1 gmsaas instances adbconnect
        desired_caps['appPackage'] = 'io.appium.android.apis'   #http://www.automationtestinghub.com/apppackage-and-appactivity-name/
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        # connect to Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_touch_actions(self):
        self.driver.is_app_installed('io.appium.android.apis')
        # self.driver.find_element_by_accessibility_id('Views').click()
        # self.driver.find_element_by_accessibility_id('Expandable list').click()
        # self.driver.find_element_by_accessibility_id('Custom Adapter').click()

        el = self.driver.find_element_by_accessibility_id('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()
        sleep(1)

        self.driver.find_element_by_accessibility_id('Expandable Lists').click()
        self.driver.find_element_by_accessibility_id('1. Custom Adapter').click()

        el1 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='People Names']")
        el1.click()
        action.long_press(el1).perform()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Sample action']").click()
        sleep(3)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
