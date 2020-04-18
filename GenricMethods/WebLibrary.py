from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from ReadTestData.ReadJsonTestData import GetTestData
import os

import pytest
import allure


class Utils(GetTestData):

    currentTestCase=""


    def __init__(self):
        print("Loading WebLib")

    @pytest.fixture(scope='session')
    def preAndPostActivities(self):
        self.createResultsFolder()
        GetTestData.loadTestData(self)
        self.launchBrowser()
        yield
        self.closeBrowser()

    @allure.step("Launching Browser")
    def launchBrowser(self):
        status = True
        try:
            print("Launching the browser")
            driverPath = "../Drivers/chromedriver.exe"
            global driver
            driver = webdriver.Chrome(executable_path=driverPath)
            driver.get("https://demo.nopcommerce.com/")
            driver.maximize_window()

        except Exception as e:
            status = False;
            print(e)
        return driver


    @allure.step("Click the element {1} on the page {0}")
    def clickElement(self, pageName, elementName, xpath):

        status = True

        try:
            action = ActionChains(driver)
            element = driver.find_element_by_xpath(xpath)
            action.move_to_element(element).click(element).perform()
            print("Clicked the Element {0} on the Page {1} sucessfully ".format(elementName, pageName))
        except Exception as e:
            print(e)
            print("Unable to click the element :" + elementName + " on the page " + pageName)
            status = False
        return status

    @allure.step("Enter the data {3} for the  element {1} on the page {0}")
    def sendData(self, pageName, elementName, xpath, data):

        status = True

        try:
            action = ActionChains(driver)
            element = driver.find_element_by_xpath(xpath)
            action.move_to_element(element).click(element).perform()
            element.clear()
            element.send_keys(data)


            print("Data Entered for the element  {0} on the Page {1} sucessfully with data as : {2}".format(elementName,
                                                                                                            pageName,
                                                                                                            data))
        except Exception as e:
            print(e)
            print("Unable to enter the  data into the element :" + elementName + " on the page " + pageName)
            status = False
        return status

    @allure.step("select the dropdown {1} on the page {0} with the values {3}")
    def selectDropDownByText(self, pageName, elementName, xpath, data):

        status = True

        try:
            select=Select(driver.find_element_by_xpath(xpath))
            select.select_by_visible_text(data)

            print("DropDown  {0} is selected with the option {1} on the Page {2} sucessfully ".format(elementName,data,pageName))
        except Exception as e:
            print(e)
            print("Unable to select the  option for the dropdown :" + elementName + " on the page " + pageName)
            status = False
        return status

    @allure.step("select the dropdown {1} on the page {0} with the values {3}")
    def selectDropDownByValue(self, pageName, elementName, xpath, data):

        status = True

        try:
            select=Select(driver.find_element_by_xpath(xpath))
            select.select_by_value(data)

            print("DropDown  {0} is selected with the option {1} on the Page {2} sucessfully ".format(elementName,data,pageName))
        except Exception as e:
            print(e)
            print("Unable to select the  option for the dropdown :" + elementName + " on the page " + pageName)
            status = False
        return status

    @allure.step("select the dropdown {1} on the page {0} with the values {3}")
    def selectDropDownByIndex(self, pageName, elementName, xpath, data):

        status = True

        try:
            select=Select(driver.find_element_by_xpath(xpath))
            select.select_by_index(data)

            print("DropDown  {0} is selected with the option {1} on the Page {2} sucessfully ".format(elementName,data,pageName))
        except Exception as e:
            print(e)
            print("Unable to select the  option for the dropdown :" + elementName + " on the page " + pageName)
            status = False
        return status

    @allure.step("closing the browser")
    def closeBrowser(self):
        driver.close()


    def getScreenShot(self):
        allure.attach(driver.get_screenshot_as_png(),name="Screen Shot",attachment_type=AttachmentType.PNG)

    def createResultsFolder(self):

        os.makedirs( os.getcwd()[0:os.getcwd().rfind("\\")]+"\\Reports")



