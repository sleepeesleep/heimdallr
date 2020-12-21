import smtplib
import configparser
import re
import os

config = configparser.ConfigParser()
config.read("/root/heimdallr/setting.ini")


class Email():
    def sendMessage(self, body):
        to_sends = config['email']['to']
        os.system("echo \"%s\" | mail -s \"Alarm\" %s " % (body, to_sends))
