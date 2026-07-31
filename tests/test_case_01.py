import pytest
import config
from pages.Loginpage import LoginPage

class Test_case01:
    @pytest.mark.parametrize("username", ["standard_user",
                                          "problem_user",
                                          "performance_glitch_user",
                                          "error_user","visual_user"])
    def test_login_with_valid_credentials(self,driver,username):
        loginpage=LoginPage(driver)
        loginpage.login(username,config.PASSWORD)
        assert "inventory" in loginpage.geturl()

