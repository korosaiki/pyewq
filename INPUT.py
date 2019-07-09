# # print("*" *  50)
# # gsname = input('公司名称：')
# # print('公司名称：%f' % gsname)
# #
# # print('========================')
#
# a=input('请输入第一个数字：')
# b=input('请输入第二个数字:')
# int_a = int(a)DNS获取方式
# int_b = int(b)
# int_c = int_a+int_b
# print('%d + %d等于%d'%(int_a,int_b,int_c))
# ==========
tis = input("请输入用户名：")
# tiss = 'admin'
if not tis == "admin":
    print("欢迎你%s"%(tis))
else:
    print('你好，%s不是正确的用户名'%(tis))