import unittest
from GenricMethods.WebLibrary import Utils
from ApplicationPages.HomePage import HomePage
from ApplicationPages.RegistrationPage import Registration
import pytest
from allure import severity, severity_level
import time


class test_Registartion(unittest.TestCase, Utils):
    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures('preAndPostActivities')
    @severity(severity_level.CRITICAL)
    def test_validateNewUserRegistration(self):
        Utils.currentTestCase = "Tc_01"
        homePage = HomePage()
        homePage.naviagateToRegistrationPage()

        regPage = Registration()
        regPage.fillRegistrationForm()
