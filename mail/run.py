# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from tkMessageBox import showinfo

from mail import get_mail
from imaplib import IMAP4_SSL
from smtplib import SMTP_SSL
from email.mime.text import MIMEText


class window:
    def __init__(self, top, user=None, password=None):

        self.user = user
        self.password = password

        # 发送邮件
        send = ttk.LabelFrame(top, text="发送邮件")
        send.grid(row=0, column=0, padx=8, pady=8)

        # 收件人
        recv_label = tk.Label(send, text="收件人： ")
        recv_label.grid(row=0, column=0, sticky=tk.W, padx=20, pady=10)
        self.recv_enter = tk.Entry(send, width=30)
        self.recv_enter.grid(row=0, column=1, sticky=tk.W, padx=20)

        # 主题
        sub_label = tk.Label(send, text="主题： ")
        sub_label.grid(row=1, column=0, sticky=tk.W, padx=20, pady=10)
        self.sub_enter = tk.Entry(send, width=30)
        self.sub_enter.grid(row=1, column=1, sticky=tk.W, padx=20)

        # 内容
        content_label = tk.Label(send, text="邮件内容： ")
        content_label.grid(row=2, sticky=tk.W, padx=20, pady=5)
        self.content_text = tk.Text(send, width=40, height=10)
        self.content_text.grid(row=3, columnspan=2, sticky=tk.W, padx=20, pady=5)

        # buttoon
        list_button = tk.Button(send, text="查看", width=10, command=self.read)
        list_button.grid(row=4, column=0, padx=20, pady=10)
        send_button = tk.Button(send, text="发送", width=10, command=self.send)
        send_button.grid(row=4, column=1)

        # 收取邮件
        recv = tk.LabelFrame(top, text="收件箱")
        recv.grid(row=1, column=0, padx=8, pady=8, sticky=tk.W)

        self.list_box = tk.Listbox(recv, width=40, height=10)
        self.list_box.bind("<Double-1>", self.get_one_mail)
        self.list_box.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=tk.W, padx=20, pady=10)
        print "run"

        self.msg = None

    def read(self):
        self.msg = MIMEText(self.content_text.get(1.0, tk.END))
        self.msg['From'] = user
        self.msg['To'] = self.recv_enter.get()
        self.msg['Subject'] = self.sub_enter.get()
        showinfo("info", self.msg.as_string())

    def send(self):
        if not self.msg:

            self.msg = MIMEText(self.content_text.get(1.0, tk.END))
            self.msg['From'] = user
            self.msg['To'] = self.recv_enter.get()
            self.msg['Subject'] = self.sub_enter.get()
        try:
            smtp_client = SMTP_SSL("smtp.qq.com")
            smtp_client.login(user=self.user, password=self.password)
            smtp_client.sendmail(from_addr=user, to_addrs=self.recv_enter.get(), msg=self.msg.as_string())
            showinfo("info", "suscess")
        except Exception as e:
            showinfo("info", e)

    def insert(self):
        self.lst = get_mail(imap_client)
        for i in self.lst:
            self.list_box.insert(tk.END, i.get("Subject"))

    def get_one_mail(self, ev=None):
        index = self.list_box.curselection()[0]
        mail = self.lst[index]
        text = """
        From: %s
        Subject: %s
        Date: %s

        Conetnt: 
        %s""" % (mail.get("From"), mail.get("Subject"), mail.get("Date"), mail.get("Content"))
        showinfo("info", text)

if __name__ == "__main__":
    user = "shiyanlou@qq.com"
    password = "shiyanlou"

    imap_client = IMAP4_SSL("imap.qq.com")
    imap_client.login(user=user, password=password)
    imap_client.select()

    top = tk.Tk()
    top.title("客户端")
    test = window(top, user=user, password=password)
    test.insert()
    top.mainloop()