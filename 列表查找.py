list = [10, 20, 30, 40]
# index用于查询，数字不存在即报错
num = 20
new = 666
print(num)
if num in list:
    weizhi = list.index(num)
    print("位置在", weizhi)
    list[weizhi] = new

print(list)

list2 = ["aaa","bbb","ccc"]
# 将list2追加到list的尾部
list.extend(list2)