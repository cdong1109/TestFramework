from PageObjects.LoginPage import LoginPage


class LoginAction(object):
    @staticmethod
    def login(driver, username, password):
        try:
            login = LoginPage(driver)
            driver.switch_to.frame(login.framObj())
            login.usernameObj().send_keys(username)
            login.passwordObj().send_keys(password)
            login.loginBtnObj().click()
            login.switchToDefaultContent()
        except Exception as e:
            raise e
