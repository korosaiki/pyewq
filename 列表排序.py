from random import randint

# 随机生成10个数字并排序
list = []
i=0
while i < 10:
    list.append(randint(1,1000))
    i += 1
print(list)
# 默认为按小到大排序
list.sort()
print(list)
# 使用形参reverse逆转排序
list.sort(reverse=True)
print(list)
list.append(999)
# 逆序
list.reverse()
print(list)