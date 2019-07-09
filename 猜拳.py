while user =  int(input("请输入 石头0，剪刀1，布2："))
from random import randint
robot = randint(0,2)
print("电脑输入%d"%robot)
if user > robot:
    print("你赢了")
elif user < robot:\
    print("你输了")
else:
    print("平手")
    print(robot)