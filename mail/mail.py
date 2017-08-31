# -*- coding: utf-8 -*-
import email
from email.header import decode_header


# 只读取收件箱中的未读邮件
def get_mail(client):
    mail_list = []
    resp, data = client.search(None, "UNSEEN")
    if data:
        for num in data[0].split():
            typ, data = client.fetch(int(num), "(RFC822)")
            msg = data[0][1]
            msg = email.message_from_string(msg)

            subject_info = msg.get("Subject")
            subject = decode_header(subject_info)[0][0]

            from_info = email.utils.parseaddr(msg.get("From"))
            if len(from_info) == 2:
                user = email.header.decode_header(from_info[0])[0][0]
                from_addr = user + "<" + from_info[1] + ">"
            else:
                from_addr = from_info

            date = msg.get("Date")
            content = None
            for i in msg.walk():
                content_type = i.get_content_type()
                content_charset = i.get_charsets()[0]
                if not i.is_multipart():
                    # 在这里只读取文本信息，可以修改为 content_type == "text/html",即超文本处理
                    if content_type == "text/plain":
                        content = i.get_payload(decode=True)
                        if content_charset:
                            content=content.decode(content_charset)
            mail = {"From":from_addr,
                    "Subject":subject,
                    "Date":date,
                    "Content":content}
            mail_list.append(mail)
    return mail_list