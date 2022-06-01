from Util.ParseConfigFile import ParseConfigFile
from Util.ObjectMap import *


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.cf = ParseConfigFile()
        self.loginOption = self.cf.getItemsSection("126mail_login")

    def framObj(self):
        try:
            locateType, locatorExpression = self.loginOption["loginPage.frame".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()

    def usernameObj(self):
        try:
            locateType, locatorExpression = self.loginOption["loginPage.userName".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            locateType, locatorExpression = self.loginOption["loginPage.passWord".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def loginBtnObj(self):
        try:
            locateType, locatorExpression = self.loginOption["loginPage.loginButton".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
