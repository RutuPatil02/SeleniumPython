import configparser


def Read_ConfigFile(section, key):
    config = configparser.ConfigParser()
    config.read("../ConfigrationFiles/config.cfg")
    return config.get(section, key)


def Read_Elements(section, key):
    config = configparser.ConfigParser()
    config.read("../ConfigrationFiles/Elements.cfg")
    return config.get(section, key)
