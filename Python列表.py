my_list = [[1,2,3],[4,5,6],[7,8,9]]
i= 0
while i < len(my_list):
    j = 0
    while j < len(my_list[i]):
        print(my_list[i][j])
        j += 1
    i += 1
print('*'*30)
# for val in my_list:
#     if val[2]
#     print(val)
for o in my_list:
    for v in o:
        print(v)