from Utilities.excel_utilities import ExcelUtilities
from pages.Loginpage import LoginPage
import pytest
import config



class Test_Case02:

    def test_invalid_credentials(self,driver):
        row=ExcelUtilities.max_row(config.testdata,"data")

        for r in range(2,row+1):
            username=ExcelUtilities.read_excel(config.testdata,"data",r,1)
            password=ExcelUtilities.read_excel(config.testdata,"data",r,2)

            login_page=LoginPage(driver)
            login_page.login(username,password)
            assert "Epic sadface" in login_page.error_message()




