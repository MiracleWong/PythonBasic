# -*- coding: utf-8 -*-
# filename: utf-8

from poplib import POP3_SSL

client = POP3_SSL("pop.qq.com")

# 填写自己的账号
client.user("shiyanlou@qq.com")

# 对于 qq 邮箱而言，在第三方客户端登陆时，都需填写授权码，此处更换为自己的授权码，不要填写密码
client.pass_("shiyanlou")
IFS=","
msg = client.retr(client.stat()[0])
for i in msg:
    print i

print "\r\n", client.quit()