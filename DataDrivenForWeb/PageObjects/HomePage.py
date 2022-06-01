from Util.ParseConfigFile import ParseConfigFile
from Util.ObjectMap import *


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.cf = ParseConfigFile()
        self.homePageOption = self.cf.getItemsSection("126mail_homepage")

    def homePageObj(self):
        try:
            locateType, locatorExpression = self.homePageOption["homePage.addressBook".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
