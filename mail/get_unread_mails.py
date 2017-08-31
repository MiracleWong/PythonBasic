# -*- coding: utf-8 -*-

from imaplib import IMAP4_SSL
import email

from email.header import decode_header
client = IMAP4_SSL("imap.qq.com")

# 修改相应的账号
client.login('shiyanlou@qq.com', 'shiyanlou')

# 选择文件夹（默认为“收件箱”）
client.select()

# 获取到收件箱未读邮件的消息号
resp, data = client.search(None, "UNSEEN")


# 解析邮件的函数
def parse_msg(msg):
    # subject
    subject_info = msg.get("Subject")
    subject = decode_header(subject_info)[0][0]
    print "Subject:", subject

    # From
    from_info = email.utils.parseaddr(msg.get("From"))
    if len(from_info) == 2:
        user = email.header.decode_header(from_info[0])[0][0]
        from_addr = user + "<" + from_info[1] + ">"
    else:
        from_addr = from_info
    print "From:", from_addr

    # Date
    date = msg.get("Date")
    print "Date:", date

    # body
    for i in msg.walk():
        content_type = i.get_content_type()
        # 是有效的信息
        if not i.is_multipart():
            # 在这里我们只打印文本信息
            if content_type == "text/plain":
                content = i.get_payload(decode=True)
                print "\r\n", "Content:", content


# data 的内容格式为 ['19 20']
for num in data[0].split():
    typ, data = client.fetch(int(num), "(RFC822)")
    msg = data[0][1]
    msg = email.message_from_string(msg)
    print "*" * 30, "\r\n"
    parse_msg(msg)