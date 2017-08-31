# -*- coding: utf-8 -*-
# filename: utf-8

from poplib import POP3_SSL

client = POP3_SSL("pop.qq.com")

# 填写自己的账号
client.user("shiyanlou@qq.com")

# 对于 qq 邮箱而言，在第三方客户端登陆时，都需填写授权码，此处更换为自己的授权码，不要填写密码
client.pass_("shiyanlou")

all_num,all_sz = client.stat()

print "总的邮件数量为:", all_num
print "总邮件字节数为:", all_sz

print client.list()

# 获取编号号为 2 的邮件，如果你的 qq 邮箱中的邮件为空，此处会出错
msg_2 = client.retr(2)

# 打印邮件
print "this is a email: \r\n"
for i in msg_2[1]:
    print i

# 退出
print "\r\n", client.quit()