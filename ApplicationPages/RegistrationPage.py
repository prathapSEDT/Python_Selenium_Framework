from allure_commons.types import AttachmentType

from GenricMethods.WebLibrary import Utils
from ApplicationOR.RegistrationPageOR import RegistrationPage_OR
from ReadTestData.ReadJsonTestData import GetTestData
import allure


class Registration(Utils,GetTestData):

    @allure.step("Filling data to register a new user")
    def fillRegistrationForm(self):
        # pageName, elementName, xpath, data
        print(Utils.currentTestCase)

        gender=GetTestData.getData(self,Utils.currentTestCase,"Gender")
        firstname = GetTestData.getData(self,Utils.currentTestCase, "FirstName")
        lastName = GetTestData.getData(self,Utils.currentTestCase, "LastName")
        day = GetTestData.getData(self,Utils.currentTestCase, "Day")
        month=GetTestData.getData(self,Utils.currentTestCase, "Month")
        year = GetTestData.getData(self,Utils.currentTestCase, "Year")
        email = GetTestData.getData(self,Utils.currentTestCase, "Email")
        password = GetTestData.getData(self,Utils.currentTestCase, "Password")
        cnfpassword = GetTestData.getData(self,Utils.currentTestCase, "ConfirmPassword")

        if str(gender).lower()=='male':

            Utils.clickElement(self,"Registartion", "Gender_Male", RegistrationPage_OR.rdo_Gender_Male)
        else:
            Utils.clickElement(self, "Registartion", "Gender_Female", RegistrationPage_OR.rdo_Gender_Female)

        Utils.sendData(self,"Registartion", "First Name", RegistrationPage_OR.edi_FirstName, firstname)
        Utils.sendData(self,"Registartion", "Last Name", RegistrationPage_OR.edi_LastName, lastName)
        Utils.selectDropDownByText(self,"Registartion", "Day", RegistrationPage_OR.drp_Day, day)
        Utils.selectDropDownByText(self,"Registartion", "Month", RegistrationPage_OR.drp_Month, month)
        Utils.selectDropDownByText(self,"Registartion", "Year", RegistrationPage_OR.drp_Year, year)
        Utils.sendData(self,"Registartion", "Email", RegistrationPage_OR.edi_Email, email)
        Utils.sendData(self,"Registartion", "Password", RegistrationPage_OR.edi_Password, password)
        Utils.sendData(self,"Registartion", "Confirm Password", RegistrationPage_OR.edi_cnfPassword, cnfpassword)
        self.getScreenShot()

