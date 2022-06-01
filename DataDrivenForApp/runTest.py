from TestScripts.SearchApp import searchApp
from TestScripts.AppRank import appRank
from Util.ParseLoadTestConfig import *

if __name__ == '__main__':
    moduleNames = parseLoadTestConfig()

    for module in moduleNames:
        eval(module + "()")
