mail = "1@foxmail.com"
sp_mail = mail.split("@")
print(sp_mail)
print("邮箱前缀是",sp_mail[0])
print("邮箱后缀是",sp_mail[1])
qianzhui = mail.count(sp_mail[0])
print(qianzhui)
if qianzhui <2:
    print("邮箱不合法")