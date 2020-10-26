import smtplib
import configparser
import re
config = configparser.ConfigParser()
config.read("/root/heimdallr/setting.ini")


class Email():
    def sendMessage(self, body):
        gmail_user = config['email']['gmail_user']
        gmail_password = config['email']['gmail_password']
        to_sends = re.split(r',', config['email']['to'])
        sender = gmail_user
        subject = "Alarm"
        to = []
        for to_se in to_sends:
                to.append(str(to_se))
        for recipient in to:
            smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            smtp_server.login(gmail_user, gmail_password)
            message = "Subject: {}\n\n{}".format(subject, body)
            smtp_server.sendmail(sender, recipient, message)
            smtp_server.close()
