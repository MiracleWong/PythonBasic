from email.mime.text import MIMEText
from subprocess import Popen, PIPE
import commands
def send_mail(sender, recevier, subject, html_content):
    msg = MIMEText(html_content, 'html', 'utf-8')
    msg["From"] = sender
    msg["To"] = recevier
    msg["Subject"] = subject
    p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)  
    p.communicate(msg.as_string())  
def main():
    send_mail("report@51iwifi.com","cfwr1991@126.com","Mail From Python", "Hello World")

if __name__ == '__main__':
    main()
