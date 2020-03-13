user = input("请输入用户名：")
移除前后空格
add = user.strip()
print(add)
if add.isalnum():
注意：isalnum = isnum+isalpha
    print("注册成功")
else:
    print("注册失败")
