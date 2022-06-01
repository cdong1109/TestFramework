from Util.ParseConfigFile import ParseConfigFile
from Util.ObjectMap import *


class AddContactPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.cf = ParseConfigFile()
        self.addContactOption = self.cf.getItemsSection("126mail_addContactsPage")

    def addContactBtn(self):
        try:
            locateType, locatorExpression = self.addContactOption["addContactsPage.createContactBtn".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonName(self):
        try:
            locateType, locatorExpression = self.addContactOption["addContactsPage.contactPersonName".lower()].split(
                ">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonMail(self):
        try:
            locateType, locatorExpression = self.addContactOption["addContactsPage.contactPersonMail".lower()].split(
                ">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def starContact(self):
        try:
            locateType, locatorExpression = self.addContactOption["addContactsPage.starContact".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonPhone(self):
        try:
            locateType, locatorExpression = self.addContactOption["addContactsPage.contactPersonPhone".lower()].split(
                ">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def contactPersonComment(self):
        try:
            locateType, locatorExpression = self.addContactOption["addContactsPage.contactPersonComment".lower()].split(
                ">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def saveContactPeron(self):
        try:
            locateType, locatorExpression = self.addContactOption["addContactsPage.saveContactPeron".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e