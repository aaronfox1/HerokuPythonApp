import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestCase(unittest.TestCase):

    def test(self):
        #Setting up chromedriver
        chromedriver = "chromedriver"
        driver = webdriver.Chrome(chromedriver)
        
        path = "https://demo-app-circleci.herokuapp.com/"
        
        driver.get(path)
        
        element = driver.find_element_by_xpath("//h1[text() = 'CircleCI Demo App]").text

        assert element == 'CircleCI Demo App'
        print('Test has been been a success')
        
        driver.close()

if __name__ == "__main__":
    unittest.main()

/html/body/div/div/h1