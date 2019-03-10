from configparser import ConfigParser
from Config.VarConfig import pageElementLocatorPath


class ParseConfigFile(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemsSection(self, sectionName):
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionVaule(self, sectionName, optionName):
        optionValue = self.cf.get(sectionName, optionName)
        return optionValue
