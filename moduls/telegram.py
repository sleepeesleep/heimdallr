import os
import configparser
import re
config = configparser.ConfigParser()
config.read("/root/heimdallr/setting.ini")

class Telegram():
    def sendMessage(self, message):
        ids = re.split(r',', config['telegram']['ids'])
        for id in ids:
            url = "https://api.telegram.org/bot%s/sendMessage" % (config['telegram']['token'])
            os.system("curl -s -X POST %s -d chat_id=%s -d text='%s'" % (url, id, message))
