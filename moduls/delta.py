import os
import re
import time, datetime
from telegram import Telegram
from email import Email
import configparser
config = configparser.ConfigParser()
config.read("/root/heimdallr/setting.ini")

class Delta():
    def check(self, directory):
        files = os.listdir(directory)
        list_names = []
        for file in files:
            name = re.findall(r'delta\-\d+\-\d+\-\d+T\d+:\d+:\d+', str(file))
            if name:
                list_names.append(str(name))
        list_names.sort()
        last_file = list_names[len(list_names) - 1]
        result = re.search(r'\d+\-\d+\-\d+T\d+:\d+:\d+', str(last_file))
        a = str(result.group(0))
        timestamp_last_file = time.mktime(datetime.datetime.strptime(a, "%Y-%m-%dT%H:%M:%S").timetuple())
        if (time.time() - timestamp_last_file) > int(config['delta']['time_for_alerting_delta']):
            Telegram().sendMessage("Last delta file in %s ALARM" % (a))
            Email().sendMessage("Last delta file in %s ALARM" % (a))
            return "Last delta file in %s this ALARM" % (a)
        else:
            return "Last delta file in %s this OK" % (a)
