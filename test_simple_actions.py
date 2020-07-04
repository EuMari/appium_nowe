import os
import unittest
from appium import webdriver
from time import sleep


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
        desired_caps['udid'] = 'localhost:41769' #do uzupelnienia z gmsaas instances list -q | xargs -n1 gmsaas instances adbconnect
        desired_caps['appPackage'] = 'io.appium.android.apis'   #http://www.automationtestinghub.com/apppackage-and-appactivity-name/
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        # connect to Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_simple_actions(self):
        self.driver.is_app_installed('io.appium.android.apis')
        self.driver.find_element_by_accessibility_id('Graphics').click()
        self.driver.find_element_by_accessibility_id('Arcs').click()


        #headerElement = self.driver.find_element_by_id('android:id/action_bar')
        #headerText = headerElement.text
        #self.assertIsNotNone(headerElement)
        #print(headerText)

        headerElement = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Graphics/Arcs")')
        headerText = headerElement.text
        self.assertIsNotNone(headerElement)
        print(headerText)

        self.driver.back()
        self.driver.back()

        #all_names = self.driver.find_elements_by_class_name(android.widget.TextView)
        element = self.driver.find_element_by_accessibility_id('App')
        sleep(1)
        self.assertIsNotNone(element)
        print(element.text)

        find_category_elements = self.driver.find_elements_by_id('android:id/text1')
        # elements = self.driver.find_elements_by_android_uiautomator('new UiSelector().enabled(true)')
        total_categories = len(find_category_elements)
        print(total_categories)

        if self.assertGreater(total_categories,10):
            print('Zakladek jest wiecej niz 10')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingApp)
    unittest.TextTestRunner(verbosity=2).run(suite)


#Kroki:
#1. Wejdź do „Graphics”
#2. Wejdź do „Arcs”
#3. Sprawdź czy nagłówek istnieje
#4. Sprawdź jaka jest jego treść

#Oczekiwane rezultaty:
#Prawidłowe wyświetlenie treści nagłówka.

#5. Wróć do okna głównego
#6. Wejdź do „Graphic”
#7. Sprawdź czy istnieje „App”
#8. Sprawdź ile jest zakładek
#9. Sprawdź czy zakładek jest powyżej 10

#Oczekiwane rezultaty:
#Prawidłowe zliczenie ilości zakładek.