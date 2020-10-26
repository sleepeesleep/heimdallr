from moduls.delta import Delta
from moduls.dump import Dump
import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('/root/heimdallr/setting.ini')
    directory = config['main']['path_directory_logs']
    file = open(config['main']['file_for_log'], 'w')
    file.write(str(Delta().check(directory)) + str(config['main']['hostname']) + '\n')
    file.write(str(Dump().check(directory)) + str(config['main']['hostname']) + '\n')
    file.close()
