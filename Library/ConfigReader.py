import configparser
import os

config = configparser.ConfigParser()
current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(os.path.dirname(current_file_path))
full_path = ""


def Read_ConfigFile(section, key):
    full_path = parent_directory + "\ConfigrationFiles\config.cfg"
    config.read(full_path)
    return config.get(section, key)


def Read_Elements(section, key):
    full_path = parent_directory + "\ConfigrationFiles\Elements.cfg"
    config.read(full_path)
    #config.read("../../ConfigrationFiles/Elements.cfg")
    return config.get(section, key)


'''
import os

configfile_name = "config.ini"

# Check if there is already a configurtion file
if not os.path.isfile(configfile_name):
    # Create the configuration file as it doesn't exist yet
    cfgfile = open(configfile_name, "w")

    # Add content to the file
    Config = ConfigParser.ConfigParser()
    Config.add_section("mysql")
    Config.set("mysql", "host", "localhost")
    Config.set("mysql", "user", "root")
    Config.set("mysql", "passwd", "my secret password")
    Config.set("mysql", "db", "write-math")
    Config.add_section("other")
    Config.set(
        "other",
        "preprocessing_queue",
        [
            "preprocessing.scale_and_center",
            "preprocessing.dot_reduction",
            "preprocessing.connect_lines",
        ],
    )
    Config.set("other", "use_anonymous", True)
    Config.write(cfgfile)
    cfgfile.close()

'''