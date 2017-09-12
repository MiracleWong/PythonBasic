from email.mime.text import MIMEText
from subprocess import Popen, PIPE
import commands

## 读取TXT的数据
def readHtml():
    file_object = open('/home/wangr/python/PythonFiles/demo1.html')
    try:
        html = file_object.read()
        return html
    finally:
        file_object.close()


def send_mail(sender, recevier, subject, html_content):
    msg = MIMEText(html_content, 'html', 'utf-8')
    msg["From"] = sender
    msg["To"] = recevier
    msg["Subject"] = subject
    p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)  d
    p.communicate(msg.as_string())  
def main():
    html = readHtml()
    # send_mail("report@51iwifi.com","cfwr1991@126.com","Mail From Python", "<a href='http://www.cnblogs.com/miraclewong/'>Miracle Wong</a>")
    # send_mail("report@51iwifi.com","cfwr1991@126.com","Mail From Python", "Hello World")
    send_mail("report@51iwifi.com","cfwr1991@126.com","Mail From Python", html)

if __name__ == '__main__':
    main()
