from PageObjects.HomePage import HomePage
from PageObjects.AddContacterPage import AddContactPage
import time


class AddContactAction(object):
    @staticmethod
    def addContact(driver, contactPersonName, contactPersonMail, isStarContact, contactPersonPhone,
                   contactPersonComment):
        hp = HomePage(driver)
        hp.homePageObj().click()
        ac = AddContactPage(driver)
        ac.addContactBtn().click()
        ac.contactPersonName().send_keys(contactPersonName)
        ac.contactPersonMail().send_keys(contactPersonMail)
        if isStarContact == "是":
            ac.starContact().click()
        ac.contactPersonPhone().send_keys(contactPersonPhone)
        ac.contactPersonComment().send_keys(contactPersonComment)
        ac.saveContactPeron().click()