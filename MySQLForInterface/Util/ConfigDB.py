import configparser
from Config.VarConfig import configPath


def dbConfigParse():
    cf = configparser.ConfigParser()
    cf.read(configPath)
    host = cf.get("mysqlconf", "host")
    port = cf.get("mysqlconf", "port")
    db = cf.get("mysqlconf", "db_name")
    user = cf.get("mysqlconf", "user")
    password = cf.get("mysqlconf", "password")
    return {"host": host, "port": int(port), "db": db, "user": user, "password": password}