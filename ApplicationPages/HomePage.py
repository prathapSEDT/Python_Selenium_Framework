from allure_commons.types import AttachmentType

from GenricMethods.WebLibrary import Utils
from ApplicationOR.HomePageOR import HomePage_OR
import allure

class HomePage(Utils, HomePage_OR):

    @allure.step("Navigate To Registration Page")
    def naviagateToRegistrationPage(self):

        status=Utils.clickElement(self,"Home Page", "Register", HomePage_OR.lnk_Register)
        self.getScreenShot()
        assert status,"Verification Registration page navigation"
