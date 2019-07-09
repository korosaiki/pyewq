mail = "133@foxmail.com"
print(mail[0:4])
# lens = len(mail)
print(mail[3:0:-1])
print(mail[:12:2])
dizhi = mail.find("@")
if dizhi == 0:
    print("地址不合法")
else:
    print("合法",dizhi)
#
# qiepian = mail.split()333333333
